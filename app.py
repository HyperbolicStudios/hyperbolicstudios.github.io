from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/projects/grantstreet.html")
def grantstreet():
    return render_template('projects/grantstreet.html')

@app.route("/projects/house.html")
def house():
    return render_template('projects/house.html')

@app.route("/projects/commons.html")
def commons():
    return render_template('projects/commons.html')

@app.route("/projects/map.html")
def map():
    return render_template('projects/map.html')

@app.route("/projects/parklet.html")
def parklet():
    return render_template('projects/parklet.html')
@app.route("/projects/bookends.html")
def bookends():
    return render_template('projects/bookends.html')

@app.route("/projects/mariner.html")
def mariner():
    return render_template('projects/mariner.html')

@app.route("/projects/watercourse.html")
def watercourse():
    return render_template('projects/watercourse.html')

@app.route("/projects/clock.html")
def clock():
    return render_template('projects/clock.html')

@app.route("/projects/bikewheel.html")
def bikewheel():
    return render_template('projects/bikewheel.html')


@app.route("/projects/keyboard.html")
def keyboard():
    return render_template('projects/keyboard.html')
if __name__ == "__main__":
    app.run(debug=True)
