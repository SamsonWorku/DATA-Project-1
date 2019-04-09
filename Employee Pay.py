x = "This Test Worked."
print(x)
Name=['Mary', 'John', 'Bob', 'Mel', 'Jen', 'Sue', 'Ken', 'Dave', 'Beth', 'Ray']
ID=['001', '002', '003', '004', '005', '006', '007','008', '009' , '010']
Pay_Rate=[15.00, 22.00, 35.00, 43.00, 17.00, 29.00, 40.00, 20.00, 37.00, 16.50]
Hours_Worked=[40, 25, 4, 62, 33, 45, 36, 17, 37, 80]

employees = list(zip (ID, Name, Pay_Rate, Hours_Worked))

for employee in employees:
	print("hours worked for " + employee[1] + " is " + str(employee[3]))
	if employee[3] <= 40: # hours worked
		pay=(employee[2] * employee[3])  #print(Hours_Worked * Pay_Rate)
		print("Pay For USD"), print(pay)
		
	else:
		pay= (employee[2] * 40) +  ((employee[2] * 1.5) * (employee[3]-40))
		print("Pay For USD"), print(pay)  #print(Hours_Worked - 40 * (Pay_Rate + 1.5) + (40 * Pay_Rate))
		