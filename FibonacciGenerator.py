def  fibonacci(n):

	if n == 1  or n == 0:
		return n;
	else:
		return fibonacci(n-2) + fibonacci(n - 1)
numero = int(input("Enter a valid number: "))
if numero < 0:
	print("Number is invalid")
i = 0
print("FIBONACCI: ")

for i in range(0, numero):
	print(fibonacci(i))
	print(fibonacci(i))