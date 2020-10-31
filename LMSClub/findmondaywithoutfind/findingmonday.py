'''Day                Time.               Subject
   Monday   	      10:00 - 11:00 AM    Period 1
                      11:30-12:30 AM.     Math
   Tuesday     	      9:00-11:00 AM       PE
                      10:00-11:00 AM.     Science
'''
def IfMondayPresent (schedule1):

	'''I wrote this function because now we don't even need the "find" function! Over here all
	we are doing is defining the function with a parameter. Then we said, "if Monday is THERE"
	inside the schedule, then print "Monday is not there" and vice versa with Monday is not 
	there. ("else" means if anything else happens.) This basically proves that you don't need
	the string find function to find something in a string. '''
	
	if "Monday" in schedule1:
		print ("Monday is there!")
	else:
		print ("Monday is not there...")


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

length = len (schedule)
print ("The schedule is " + str (length) + " characters long.")

'''Above you used "str" to convert the integer into a little string of it's own.'''