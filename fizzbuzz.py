x = "fizz"
y = "buzz"
z = x+y
b = [num for num in range(1,101,1)]
for i in range(len(b)):
    
    if ((b[i]%3 )==0) and ((b[i]%5)==0):
        b[i]=z
    elif ((b[i]%3 )==0) :
        b[i] = x
    elif ((b[i]%5)==0):
        b[i]=y
print(b)

