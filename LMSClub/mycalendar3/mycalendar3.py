'''Day           Time.               Subject
Monday   	     10:00 - 11:00 AM    Period 1
                 11:30-12:30 AM.     Math
Tuesday          9:00-11:00 AM       PE
                 10:00-11:00 AM.     Science
'''

def PrintMyPeriod (day, time, subject):
	print (day + "\t\t" + time + "\t" + subject)

def PrintAllPeriods (periods):
	
	print ("Day\t\tTime\t\tSubject ")
	for period in periods:
	
		#to do a loop, you have to write "for" and then write your variable & parameters, then a colon. Then write what you 
		#want to be inside your loop and it will repeat as many times as there are entries in your list.

		PrintMyPeriod (period[0], period[1], period[2])

periods = [("Monday", "9:10 - 10:15", "ELA"), ("Monday", "10:35 - 11:40", "Social Studies"),
			("Monday", "12:10 - 1:15", "PE"), ("Tuesday", "9:10 - 10:15", "Elective"), ("Tuesday", "10:35 - 11:40", "Math"), 
			("Tuesday", "12:10 - 1:15", "Science")]


'''To find a specific tuple you count until you find the number of it, find the second number, then box-bracket it, then 
you add a circle parentheses around it.'''

PrintAllPeriods (periods)

