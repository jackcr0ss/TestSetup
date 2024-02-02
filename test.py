# Variable setting
grade = [83, 91, 87, 99, 88]
assigmentsCount = len(grade)
average = 0

# Finding the Average 
for i in grade:
	average += (i/100)
average /= assigmentsCount
average *= 100
average = str(average) + "%"

# TODO

# Add a print statement to print the average! 