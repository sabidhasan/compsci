from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    """Complete the implementation of index in such a way that it displays an HTML table summarizing, for the user currently logged in,
    which stocks the user owns, the numbers of shares owned, the current price of each stock, and the total value of each holding
    (i.e., shares times price). Also display the user’s current cash balance along with a grand total (i.e., stocks' total value plus cash)."""
    row = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])
    row2 = db.execute(
        "SELECT *, SUM(amountpurchased) FROM purchases WHERE username_users = :username GROUP BY stockname HAVING SUM(amountpurchased) > 0 ORDER BY date DESC", username=session["user_id"])
    
    for item in row2:
        look = lookup(item["stockname"])
        item["stockname"] = item["stockname"].upper()
        item["current_value"] = str(look["price"])
        item["full_name"] = str(look["name"])
        item["total_value"] = "{:,.2f}".format(float(look["price"]) * item["SUM(amountpurchased)"])
        item["Date"] = item["Date"][:10]
        item["profit"] = usd((float(look["price"]) * float(item["SUM(amountpurchased)"])) - (float(item["price"]) * float(item["SUM(amountpurchased)"])))
        
    cash_balance = usd(float(row[0]["cash"]) + sum([float(i["total_value"]) for i in row2]))
    return render_template("index.html", msg=row2, cb=cash_balance, c=usd(float(row[0]["cash"])))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""
    #If post, then condiuct the purchase!    
    if request.method == "POST":
        if request.form.get("number") is None or request.form.get("stock") is None:
            return apology("No value entered for stock or number")
            
        try:
            amount = int(request.form.get("number"))
            stock_name = request.form.get("stock")
        except (ValueError, TypeError):
            return apology("Invalid amount entered: {}".format(request.form.get("number")))
        if amount <= 0:
            return apology("Amount entered must be positive!")
        
        #Try to get stock data
        stock_data = lookup(stock_name)
        if not(stock_data):
            return apology("Invalid stock symbol {}".format(stock_name))

        #do database work
        rows = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])
        cash = float(rows[0]["cash"])
        
        #check if purchase is valid
        if cash < stock_data['price'] * amount:
            return render_template("buy.html", msg="Insufficient cash ({}) for stock {}. \n Required amount {}".format(usd(cash), stock_name, usd(stock_data['price'] * amount)))
        else:
            db.execute("INSERT INTO 'purchases' ('username_users', 'stockname', 'amountpurchased', 'price') VALUES (:id, :stock, :amt, :price)", id=rows[0]["id"], stock=stock_name.lower(), amt=amount, price=stock_data['price'])
            #Subtract the money
            db.execute("UPDATE 'users' SET cash = :newcash WHERE id = :id", newcash=cash-stock_data['price']*amount, id=rows[0]["id"])
            return render_template("buy.html", msg="Successfully purchased {} shares of {}!".format(amount, stock_name))

    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    #!!!!!########!!!!!!!!############
    #!!!!!########!!!!!!!!############
    #!!!!!########!!!!!!!!############
    #!!!!!########!!!!!!!!############
    #!!!!!########!!!!!!!!############
    #!!!!!########!!!!!!!!############
    return apology("TODO")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST" and request.form.get("stock"):
        #obtain the quote
        x = lookup(request.form.get("stock"))
        #if quote was suceesfully found, then
        if x:
            x['price'] = usd(x['price'])
            return render_template("quote.html", quote=x)
        else:
            return render_template("quote.html", quote='Sorry, quote {} was not found'.format(request.form.get("stock")))
    #First time here, or quote entered was invalid
    return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
    if request.method == "POST":
        session.clear()
        
        username = request.form.get("username")
        userpw = request.form.get("password")
        userpw2 = request.form.get("password2")
        
        #no username/pw
        if not username or not userpw or not userpw2:
            return apology("must provide username/password")
        # ensure password was the asme twice
        elif not (userpw == userpw2):
            return apology("passwords must match")
        #IF USERNAME already exists
        if len(db.execute("SELECT * FROM users WHERE username = :username", username=username)) != 0:
            return apology("username already exists")

        #insert into DB
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hashed)", username=username, hashed=pwd_context.hash(userpw))
        #return homepage
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)
        session["user_id"] = rows[0]["id"]

        return redirect(url_for("index"))
        
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    #If post, then condiuct the purchase!    
    if request.method == "POST":
        if request.form.get("number") is None or request.form.get("stock") is None:
            return apology("No value entered for stock or number")
            
        try:
            amount = int(request.form.get("number"))
            stock_name = request.form.get("stock")
        except (ValueError, TypeError):
            return apology("Invalid amount entered: {}".format(request.form.get("number")))

        #Try to get stock data
        stock_data = lookup(stock_name)
        if not(stock_data):
            return apology("Invalid stock symbol {}".format(stock_name))
        
        #See if you own this even
        rows = db.execute("SELECT *, SUM(amountpurchased) FROM 'purchases' WHERE stockname = :stock AND username_users = :user", stock=stock_name.lower(), user=session["user_id"])
        if rows[0]["SUM(amountpurchased)"] is None or rows[0]["SUM(amountpurchased)"] <= 0 or rows[0]["SUM(amountpurchased)"] < amount:
            return apology("Sorry, you don't own (enough) {} stock".format(stock_name))
            
        #Amount valid?
        if amount > int(rows[0]["SUM(amountpurchased)"]) or amount <= 0:
            return apology("Amount entered is either not positive or not valid")
        #Get amount ready for insertion into DB    
        amount = -1*amount
        
        #do DB work
        #cash = float(db.execute("SELECT * FROM 'users' WHERE id = :id", id=session["user_id"])[0]["cash"]) + 
        db.execute("INSERT INTO 'purchases' ('username_users', 'stockname', 'amountpurchased', 'price') VALUES (:id, :stock, :amt, :price)", id=session["user_id"], stock=stock_name.lower(), amt=amount, price=stock_data['price'])
        db.execute("UPDATE 'users' SET cash = cash + :newcash WHERE id = :id", newcash=(float(amount*-1*stock_data['price'])), id=session["user_id"])
        
        return render_template("sell.html", msg="Sold {} shares of stock {} for {}".format(-1*amount, stock_name, usd(stock_data['price'] * -1*amount)))
    else:
        return render_template("sell.html")