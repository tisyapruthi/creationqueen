import json
scheduledic=  {
    "9:20-10:25": ["Maths", "arts", "science", "", ""],
    "10:35-11:40": ["Goober", "pines", "goop"]
}

def savetofile (schedule):
    with open ("mycustomschedule", "w") as mycustomsched:
        mycustomsched.write(json.dumps(schedule))
    mycustomsched.close()

def readfromfile ():
    with open ("mycustomschedule", "r") as readthelines:
        dataread= readthelines.read ()
    returnread= json.loads(dataread)
    return returnread


if __name__ == '__main__':
    savetofile(scheduledic)
    mydic= readfromfile()
    print (mydic)
