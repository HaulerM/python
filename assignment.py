#1. We have the following student details and marks enter these details from the keyboard
#student name = Rita Liz
#student number =SEP23/BCS/14
#Programming =78
#Data science =89
#Computer applications =55
#Calculate the average mark and print the number in 3 decimal places

#2. Write a programme converts celcius temperature to fahrenheit, the programme should ask a user to enter the temperature in degree celcius and display the temperature in fahrenheit.
#3. A car's mile per gallaton can be calculated with the following formula; miles driven and gallons used.
#It should calculate the cars miles and display the results.

#1 
student_name = "Rita Liz"
student_number = "SEP23/BSC/14"
programming = 78
data_science = 89
computer_application =55

total_sum = programming + data_science + computer_application
print(f"The sum is {total_sum}")
number =3
average_mark = total_sum / number
print(f"The average marks is {average_mark:3f}")

#3
miles_driven = float(input("enter miles driven"))
gallons_of_car_used =float(input("enter amount of gallons used"))
mpg = miles_driven / gallons_of_car_used
print(f"The number of miles driven per gallons used is {mpg:.2f}")