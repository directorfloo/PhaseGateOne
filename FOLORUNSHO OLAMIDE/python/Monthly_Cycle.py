#/*Formulas
#Next Period Date
#Next Period=LMP+CL
#Ovulation Day
#Ovulation usually occurs 14 days before the next period.
#Ovulation= LMP + ( 𝐶𝐿 − 14)
#Ovulation=LMP+(CL−14)
#Fertile Window
#Sperm can live up to 5 days, egg up to 1 day → fertile window = 5 days before ovulation + ovulation day + 1 day after.
#Fertile Window =(Ovulation) to 
#(Ovulation + 1)
#Fertile Window=(Ovulation−5) to (Ovulation+1)
#Safe Periods
#Safe days are outside the fertile window:
#Before Fertile Window:
#Safe 1 = LMP to (Ovulation − 6)
#Safe 1=LMP to (Ovulation−6)
#After Fertile Window:
#Safe 2 =(Ovulation +2) to Next Period
#Safe 2=(Ovulation+2) to Next Period*/




# 1.The menstrual cycle is the recurring process in the female reproductive system that prepares the body for a possible pregnancy. It is controlled by hormones and #typically lasts 21–35 days (average 28 days). The cycle involves changes in the ovaries and the uterus.*/


#2.



def get_next_period_cycle(last_menstrual_period_start_date, cycle_length):
	
	if int(last_menstrual_period_start_date, cycle_length) < 0:
		raise ValueError
	elif type(last_menstrual_period_start_date, cycle_length) == str:
		raise ValueError
	else:
		next_period = last_menstrual_period_start_date + cycle_length
		return next_period

def get_ovulation_cycle(last_menstrual_period_start_date, cycle_length):

	if int(last_menstrual_period_start_date, cycle_length) < 0:
		raise ValueError
	elif type(last_menstrual_period_start_date, cycle_length) == str:
		raise ValueError
	else:
		ovulation = last_menstrual_period_start_date + (cycle_length - 14)
		return ovulation


def get_fertile_window_cycle(ovulation):

	if int(ovulation) < 0:
		raise ValueError
	elif type(ovulation) == str:
		raise ValueError
	else:
		fertile_start = ovulation - 5
		fertile_end = ovulation + 1
		return [fertile_start, fertile_end] 

def get_safe_period(ovulation, last_menstrual_period_start_date, next_period):
	
		
	if int(ovulation, last_menstrual_period_start_date, next_period) < 0:
		raise ValueError
	elif type(ovulation, last_menstrual_period_start_date, next_period) == str:
		raise ValueError
	else:
		safe_before_start = last_menstrual_period_start_date
		safe_before_end = ovulation - 6
		safe_after_start = ovulation + 2
		safe_after_end = next_period
		return [safe_before_start, safe_before_end, safe_after_start, safe_after_end]




