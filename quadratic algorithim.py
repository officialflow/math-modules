from math import sqrt
def quadratic(a,b,c):
	if b**2<(4*a*c):
		print ("complex numbers not allowed,try again")
		return (0,0)
	elif a==0 or c==0:
		print("division by zero not allowed")
	else:
		step0 = 2*a
		step1 = b**2-4*a*c
		step2 = (-1*b) + sqrt(step1)
		step3 = round(step2/step0,2)
		step5 = (-1*b) - sqrt(step1)
		step6 = round(step5/step0,2)
		print(step3,step6)
try:
    a = int(input("input A value: "))
    b = int(input("input B value: "))
    c = int(input("input C value: "))
    quadratic(a,b,c)
	
except ValueError:
    print("please input a number and run again")




