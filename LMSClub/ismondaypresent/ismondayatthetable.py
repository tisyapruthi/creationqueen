'''Day           Time.                        Subject
Monday   10:00 - 11:00 AM    Period 1
                  11:30-12:30 AM.    Math
Tuesday     9:00-11:00 AM     PE
                  10:00-11:00 AM.    Science
'''
def IfMondayPresent (schedule1):
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

print (schedule.upper())

school = schedule.find ("Monday")

IfMondayPresent (schedule)