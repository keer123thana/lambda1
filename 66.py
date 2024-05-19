#lambda function
#it is a small anonymous function.it can take any number of arguments,but can only have one expression.

#add 10 to argument n and return the result
x=lambda n:n+10
print(x(5))

#multiply arguments a and b and return the result
y=lambda a,b:a*b
print(y(3,4))

#summarize arguments a,b and c and return the result
z=lambda a,b,c:a+b+c
print(z(7,8,9))

#a function definition that takes one argument and that argument will be multiplied with an unknown number:
def myfunc(r):
    return lambda s : s * r

#use this function to make a function that always doubles and triples the number which is sent in
def myfunc(w):
    return lambda v : v * w
doubler=myfunc(5)
print(doubler(8))

def myfunc(d):
    return lambda h : h * d
tripler=myfunc(9)
print(tripler(3))
