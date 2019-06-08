# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
import pylab
import re
import datetime
# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    return [pylab.polyfit(x, y, deg) for deg in degs]

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model
    """
    return 1 - (((y - estimated)**2).sum() / ((y - y.mean())**2).sum())

def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.
    """
    for model in models:
        # Plot x vals
        pylab.plot(x, y, 'bo')
        # Predict y vals for x vals, using model
        model_predicted_y_vals = pylab.poly1d(model)(x)
        # Plot model values
        pylab.plot(x, model_predicted_y_vals, 'r-')
        rsq = r_squared(y, model_predicted_y_vals)
        se = 'Std Err: ' + str(se_over_slope(x, y, model_predicted_y_vals, model)) if len(model) - 1 == 1 else ''
        pylab.title('Year vs. Temperature: Degree {} \n R2 {} \n {}'.format(len(model) - 1, rsq, se))
        pylab.xlabel('Year')
        pylab.ylabel('Temperature (C)')
        pylab.show()
    
def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    ret = []
    for year in years:
        curr_year = []
        for city in multi_cities:
            curr_city_avg = pylab.array(climate.get_yearly_temp(city, year)).mean()
            curr_year.append(curr_city_avg)
        ret.append(sum(curr_year) / len(curr_year))
    return pylab.array(ret)

def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    ret = []
    for i, val in enumerate(y):
        start_idx = max(i - window_length + 1, 0)
        sub_arr = y[start_idx:i + 1]
        ret.append(sum(sub_arr) / len(sub_arr))
    return pylab.array(ret)

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model
    """
    return (((y - estimated)**2).sum()/len(y))**0.5

def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    ret = []
    for year in years:
        # Average temp (across all cities) for each day in year
        curr_yr_daily_temps = []
        for month in range(1, 13):
            for day in range(1, 32):
                try:
                    # Generate temps for all cities on this date, and get average
                    avg_tmps = [climate.get_daily_temp(city, month, day, year) for city in multi_cities]
                    curr_yr_daily_temps.append(pylab.mean(avg_tmps))
                except AssertionError:
                    # This is not a valid day, or its data doesn't exist
                    continue
        ret.append(pylab.std(curr_yr_daily_temps))
    return pylab.array(ret)

def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.
    """
    for model in models:
        # Plot x vals
        pylab.plot(x, y, 'bo')
        # Predict y vals for x vals, using model
        predicted = pylab.poly1d(model)(x)
        # Error
        error = rmse(y, predicted)
        # Plot model values
        pylab.plot(x, predicted, 'r-')
        pylab.xlabel('Year')
        pylab.ylabel('Predicted Temperature (C)')
        pylab.title('Year vs. Temperature: Degree {} \n rmse {}'.format(len(model) - 1, error))
        pylab.show()

if __name__ == '__main__':
    # Part A.4
    climate_model = Climate('data.csv')
    years = pylab.array(TRAINING_INTERVAL)
    test_years = pylab.array(TESTING_INTERVAL)
    ## Part A.4.1
    # jan_10_temps = []
    # for year in years:
    #     jan_10_temps.append(climate_model.get_daily_temp('NEW YORK', 1, 10, year))
    # y = pylab.array(jan_10_temps)
    # evaluate_models_on_training(years, y, generate_models(years, y, [1]))

    ## Part A.4.2
    # yearly_temps = []
    # for year in years:
    #     yearly_avg_temp = pylab.array(climate_model.get_yearly_temp('NEW YORK', year)).mean()
    #     yearly_temps.append(yearly_avg_temp)
    # y = pylab.array(yearly_temps)
    # evaluate_models_on_training(years, y, generate_models(years, y, [1]))

    # Part B
    # y = gen_cities_avg(climate_model, CITIES, years)
    # evaluate_models_on_training(years, y, generate_models(years, y, [1]))    

    # Part C
    # y = moving_average(gen_cities_avg(climate_model, CITIES, years), 5)
    # evaluate_models_on_training(years, y, generate_models(years, y, [1]))    

    # Part D
    ## Part D.2.1
    # moving_avg_y_training = moving_average(gen_cities_avg(climate_model, CITIES, years), 5)
    # models = generate_models(years, moving_avg_y_training, [1, 2, 20])
    # evaluate_models_on_training(years, moving_avg_y_training, models)

    ## Part D.2.2
    # Calculate moving average for 2010-2015
    # moving_avg_y_training = moving_average(gen_cities_avg(climate_model, CITIES, years), 5)
    # moving_avg_y_testing = moving_average(gen_cities_avg(climate_model, CITIES, test_years), 5)
    # models = generate_models(years, moving_avg_y_training, [1, 2, 20])
    # evaluate_models_on_testing(test_years, moving_avg_y_testing, models)
    
    # Part E
    # stdevs = gen_std_devs(climate_model, CITIES, years)
    # avgs = moving_average(stdevs, 5)
    # evaluate_models_on_training(years, avgs, generate_models(years, avgs, [1]))
    pass
