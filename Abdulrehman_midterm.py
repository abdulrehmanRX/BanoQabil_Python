#Q1:Write a Python program to do arithmetical operations addition and division.
num1 =int(input("Enter first number"))
num2 = int(input("Enter second number"))
add = num1 + num2
divi = num1 / num2
print("Addition:",num1," + ",num2," = ",add)
print("Division:",num1," / ",num2," = ",divi)
power = num1 ** num2
print("Power:",num1," ^ ",num2," = ",power)
floor = num1 // num2
print("Floor Division:",num1," // ",num2," = ",floor)


#Q2:Write a Python program to find the area of a triangle.
temp1 = int(input("Enter the length of base of triangle:"))
temp2 = int(input("Enter the height of base of triangle:"))
area = 0.5*temp1*temp2
print("The area of triange is:",area)


#Q3:Write a Python program to convert Celsius to Fahrenheit.
temp_c =int(input("Enter Temperature in Celsius:"))
fahrenheit = (9/5*temp_c)+32
print(temp_c,"degree Celsius is equal to",fahrenheit,"degree Fahrenheit")


#Q4:Write a Python program that return all datatypes that we discussed in the class
str = "Hello World"
int = 10		
float = 10.5
list = [1,2,3,4,5]
tuple = (1,2,3,4,5)
bool = True
set = {1,2,3,4,5}	
print("The data type of",int,"is",type(int))
print("The data type of",float,"is",type(float))
print("The data type of",str,"is",type(str))
print("The data type of",bool,"is",type(bool))
print("The data type of",list,"is",type(list))
print("The data type of",tuple,"is",type(tuple))
print("The data type of",set,"is",type(set))
