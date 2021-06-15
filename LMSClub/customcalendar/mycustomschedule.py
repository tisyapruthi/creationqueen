from flask import Flask, render_template, request
import mytemplate
import json

app = Flask(__name__)

""" approute is a decorator which allows you to make a route to a different page in a website. """
@app.route('/')
def hello_world():
    """ this is a Jinja template (the add schedule design thing.). Jinja templates replace a lot of code in your
    program and save you a lot of work. """
    scheduledic = readfromfile()
    return render_template("AddScheduleDESIGN.html", result= scheduledic)

def savetofile (schedule):
    with open ("mycustomschedule", "w") as mycustomsched:
        mycustomsched.write(json.dumps(schedule))
        # json is a thing that helps you with dictionaries and lists,
    mycustomsched.close()

def init_file():
    blank_schedule = {"9:10-10:25": ["", "", "", "", ""],
     "10:35-11:40": ["", "", "", "", ""],
     "11:50-12:50": ["", "", "", "" ""]}
    savetofile(blank_schedule)
    # over here you are creating a blank schedule table in which the user will fill in all the blank spaces.

def readfromfile ():
    with open ("mycustomschedule", "r") as readthelines:
        dataread= readthelines.read ()
    returnread= json.loads(dataread)
    return returnread

def convertdict (sourcedict):
    thisdict = {}
    for key in sourcedict:
        x = key.rsplit("$")
        position = 0
        if x[1] == "Monday":
            position = 0
        elif x[1] == "Tuesday":
            position = 1
        elif x[1] == "Wednesday":
            position = 2
        elif x[1] == "Thursday":
            position = 3
        elif x[1] == "Friday":
            position = 4
        if x[0] not in thisdict:
            thisdict[x[0]] = ["", "", "", "", ""]
        thisdict [x[0]][position] = sourcedict[key]

    return thisdict

@app.route('/tisya')
def hello_tisya():
    return mytemplate.html_title()

@app.route('/studentform')
def student():
    return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        destination = request.form
        returndict = convertdict(destination)
        savetofile(returndict)
        return render_template("results.html", result = returndict)


if __name__ == '__main__':
    init_file()
    app.run()



