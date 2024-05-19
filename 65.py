def getquot(num):
    return num/3
def getrem(num):
    return num%3
def getnum(func3,num1):
    return func3(num1)
result1=getnum(getquot,200)
result2=getnum(getrem,200)
print(int(result1))
print(result2)
