dict={"jaishu":'20-06-2000',"Nayana":'13-08-2001',"sai":'14-06-2001',"Tharun":'21-07-1999'}
print(">>>Welcome to birthdays dictionary.we know birthdays of :")
for name in dict:
    print(name)
print('whos birthday do you want to look up?')
name = input()
if name in dict:
    print(name +' has birthday on ' + dict[name])
else:
    print('we dont have ' + name + 'birthday')