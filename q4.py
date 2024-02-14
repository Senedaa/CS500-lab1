#print the program name 
print("Calculating the employee salary")
print()

#Define constant
baker1_rate = 15.00
baker2_rate = 16.25
baker3_rate = 17.75

#define overtime limits
baker1_overtime_max = 35
baker2_overtime_max = 40
baker3_overtime_max1= 40
baker3_overtime_max2 = 45

#calculating the overtime rates (the new amount the bakers will be paid per hour)
baker1_overtime_rate = baker1_rate * 1.5
baker2_overtime_rate = baker2_rate * 2.00
baker3_overtime_rate1 = baker3_rate * 1.5
baker3_overtime_rate2 = baker3_rate * 2.00

#get user input
baker1_hours = float(input("Enter the number of hours done by Baker 1? "))
baker2_hours = float(input("Enter the number of hours done by Baker 2? "))
baker3_hours = float(input("Enter the number of hours done by Baker 3? "))

#calculating the gross pay 
if baker1_hours <= baker1_overtime_max:
    grosspay_baker1 = baker1_hours * baker1_rate
else:
    overtime_hour = baker1_hours - baker1_overtime_max
    grosspay_baker1 = baker1_overtime_max * baker1_rate + overtime_hour * baker1_overtime_rate
if baker2_hours <= baker2_overtime_max:
    grosspay_baker2 = baker2_hours * baker2_rate
else:
    overtime_hour = baker2_hours - baker2_overtime_max
    grosspay_baker2 = baker2_overtime_max * baker2_rate + overtime_hour * baker2_overtime_rate
if baker3_hours <= baker3_overtime_max1:
    grosspay_baker3 = baker3_hours * baker3_rate
elif baker3_hours <= baker3_overtime_max2:
    overtime_hour = baker3_hours - baker3_overtime_max1
    grosspay_baker3 = baker3_overtime_max1 * baker3_rate + overtime_hour * baker3_overtime_rate1
else:
    overtime_hour1 = baker3_overtime_max2 - baker3_overtime_max1
    overtime_hour2 = baker3_hours - baker3_overtime_max2
    grosspay_baker3 = (baker3_overtime_max1 * baker3_rate) + (overtime_hour1 * baker3_overtime_rate1) + (overtime_hour2 * baker3_overtime_rate2)

#calculating the tax and net pay
tax_rate = 0.30
tax_baker1 = grosspay_baker1 * tax_rate
netpay_baker1 = grosspay_baker1 - tax_baker1
tax_baker2 = grosspay_baker2 * tax_rate
netpay_baker2 = grosspay_baker2 - tax_baker2
tax_baker3 = grosspay_baker3 *tax_rate
netpay_baker3 = grosspay_baker3 - tax_baker3

#printing the values 
print(f"\nEmployee Salary Summary")
print(f"\nBaker 1 - Hours: {baker1_hours}, Gross Pay: ${grosspay_baker1}, Taxes: ${tax_baker1}, Net Pay: ${netpay_baker1}")
print(f"\nBaker 2 - Hours: {baker2_hours}, Gross Pay: ${grosspay_baker2}, Taxes: ${tax_baker2}, Net Pay: ${netpay_baker2}")
print(f"\nBaker 3 - Hours: {baker3_hours}, Gross Pay: ${grosspay_baker3}, Taxes: ${tax_baker3}, Net Pay: ${netpay_baker3}")