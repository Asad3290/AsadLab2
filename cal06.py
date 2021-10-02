# calculator in Python(v0.4)
def add(num1, num2):
	return num1 + num2

def sub(num1, num2):
	return num1 - num2

def mul(num1, num2):
	return num1 * num2

def div(num1, num2):
	return num1 / num2

def mod(num1, num2):
	return num1%num2
def square_root(number):
	return number ** 0.5

# main
number = int(input("Enter Number: "))
res = add(5, 3)
print(res)
print(sub(5,3))
print(mul(5,3))
print(div(5,3))
print(mod(5,3))
print("The square root of ", number, "is", square_root(number))  