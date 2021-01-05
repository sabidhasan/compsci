from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer
import os, sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, count=100)

    #init analyzer
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    analyzer = Analyzer(positives, negatives)

    posi = 0
    negs = 0
    neut = 0
    for tweet in tweets:
        score = analyzer.analyze(tweet)
        if score > 0:
            posi += 1
        elif score < 0:
            negs += 1
        else:
            neut += 1

    total = (posi + negs + neut)
    posi = posi / total
    negs = negs / total
    neut = neut / total
    
    # generate chart
    chart = helpers.chart(posi, negs, neut)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name,total=total)
