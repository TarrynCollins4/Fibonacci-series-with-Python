"""
	Author: Edgard Diaz
	Date: March 25th 2020
	
	In this code a recursive function is developed to 
	generate the first n numbers of the Fibonacci series
"""

def  fibonacci(n):

	if n == 1  or n == 0:

		return n;

	else:

		return fibonacci(n-2) + fibonacci(n - 1)

print("Hello there, hope you have fun with this fibonacci series")
numero = int(input("ingrese un numero entero  positivo/ Please enter a positive number: "))

if numero < 0:
	print("Numero no valido/ Number invalid")

i = 0

print("Secesion de fibonacci: ")

for i in range(0, numero):
	print(fibonacci(i))
