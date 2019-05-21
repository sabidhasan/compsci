# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
import feedparser
import string
import time
import threading
import re
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    
    def is_phrase_in(self, text):
        text = re.sub(r"[!\"#$%&\'()*+,-.\/:;<=>?@\]\[^_`{|}~ ]+", " ", text).lower()
        return re.findall(self.phrase + "$", text) or (self.phrase + " " in text)

# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, news_story):
        return self.is_phrase_in(news_story.title)

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, news_story):
        return self.is_phrase_in(news_story.description)

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, time):
        self.time = datetime.strptime(time, "%d %b %Y %H:%M:%S").replace(tzinfo=pytz.timezone("EST"))

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        return self.time < story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        return self.time > story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, other_trigger):
        self.other_trigger = other_trigger

    def evaluate(self, story):
        return not self.other_trigger.evaluate(story)

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, trigger_1, trigger_2):
        self.trigger_1 = trigger_1
        self.trigger_2 = trigger_2
    
    def evaluate(self, story):
        return self.trigger_1.evaluate(story) and self.trigger_2.evaluate(story)

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, trigger_1, trigger_2):
        self.trigger_1 = trigger_1
        self.trigger_2 = trigger_2
    
    def evaluate(self, story):
        return self.trigger_1.evaluate(story) or self.trigger_2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.
    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    ret = []
    for story in stories:
        if any(trigger.evaluate(story) for trigger in triggerlist): 
            ret.append(story)
    return ret

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file
    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    
    ret = []
    triggers = {}
    for line in lines:
        line = line.split(',')
        if len(line) < 3:
            raise SyntaxError
        if line[0] == 'ADD':
            # Add the filters
            for filter_name in line[1:]:
                ret.append(triggers[filter_name])
        else:
            new_trigger_name = line[0]
            if line[1] == "TITLE":
                new_trigger = TitleTrigger(line[2])
            elif line[1] == "DESCRIPTION":
                new_trigger = DescriptionTrigger(line[2])
            elif line[1] == "BEFORE":
                new_trigger = BeforeTrigger(line[2])
            elif line[1] == "AFTER":
                new_trigger = AfterTrigger(line[2])
            elif line[1] == "OR":
                try:
                    new_trigger = AndTrigger(triggers[line[2]], triggers[line[3]])
                except:
                    raise ValueError
            elif line[1] == "AND":
                try:
                    new_trigger = OrTrigger(triggers[line[2]], triggers[line[3]])
                except:
                    raise ValueError
            else:
                raise SyntaxError
            
            triggers[new_trigger_name] = new_trigger
    return ret



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

