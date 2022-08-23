def largestnum(a,b,c):
    if(a>=b) and (a>=c):
        largest=a
    elif(b>=a) and (b>=c):
        largest=b
    else:
        largest=c
    return largest
a=10
b=40
c=90
print(largestnum(a,b,c))