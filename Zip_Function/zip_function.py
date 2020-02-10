'''
Python Trick - The zip function
'''

names = ['Rohit','Akshay','Sagar','Rahul','Swapna']
ages = [26, 26, 27, 28, 27]

for name, age in zip(names, ages):
	print(name, age)