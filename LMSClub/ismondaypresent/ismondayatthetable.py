'''Day                Time.               Subject
   Monday   	      10:00 - 11:00 AM    Period 1
                      11:30-12:30 AM.     Math
   Tuesday     	      9:00-11:00 AM       PE
                      10:00-11:00 AM.     Science
'''
def IfMondayPresent (schedule1):

	'''Here I defined my function with a parameter. Then on the next line it's saying that 
	the variable "Ismondaythere" is equal to finding the word Monday in the schedule string.
	Then in the next line it tells that "Ifismondaythere" then greater than equal to zero. 
	This means that if a number greater than 0 comes in when finding the word monday, it
	should print Monday is present. This is because when using the find function, if the 
	number "-1" comes, that means what you are trying to find is not present. If greater, 
	that means it is present. This is how I used the string find function to find Monday!'''

	Ismondaythere = schedule1.find ("Monday")
	if Ismondaythere >= 0:
		print ("Monday is present.")
	else:
		print ("Monday is not present.")



schedule = """Day		Time		Subject 
Monday		9:10 - 10:15	ELA
Monday		10:35 - 11:40	Social Studies
Monday		12:10 - 1:15	PE
Tuesday		9:10 - 10:15	Elective
Tuesday		10:35 - 11:40	Math
Tuesday		12:10 - 1:15	Science"""

'''Above is a multi-line string. This is just a string that is packed together
with multiple lines instead of making a bunch of strings with different lines.'''

print (schedule.upper())

IfMondayPresent (schedule)