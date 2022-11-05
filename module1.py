'''First code for module,
this is very simple code for beginner to 
understand the concept of modules then I have 
user built functions(like-greet,sqrt,area,volume,prct) in it to explore more in it.'''
x=1+2
x=3*x
x
def greet(n):
	text="Hello " +n+"!"
	print(text)
def sqrt(n):
	x=n**(1/2)
	return x'''
def area(l,b):
	area=l*b
	return area
areas=area(12,10)
print(areas)
def volume(l,b,h):
	volume=l*b*h
	return volume
volumes=volume(10,12,100)
print(volumes)
def prct(mo,mm):
	percentage=(mo/mm)*100
	return percentage
my_percentage=prct(510,600)
print(my_percentage)
	
