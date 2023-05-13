from flask import Blueprint, render_template, request
from flightdelayai import probability

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    elif request.method == 'POST':
        schedtime = request.form.get("schedtime")
        carrier = request.form.get("carrier")
        distance = request.form.get("distance")
        flightnum = request.form.get("flightnum")
        weather = request.form.get("weather")
        dayweek = request.form.get("dayweek")
        daymonth = request.form.get("daymonth")
        prob = probability(schedtime, carrier, distance, flightnum, weather, dayweek, daymonth)
        return render_template("prediction.html", prob=prob)