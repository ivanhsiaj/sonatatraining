def largestnum(no1,no2,no3):
    if(no1>=no2) and (no1>=no3):
        largest=no1
    elif(no2>=no1) and (no2>=no3):
        largest=no2
    else:
        largest=no3
    return largest
no1=10
no2=40
no3=90
print(largestnum(no1,no2,no3))