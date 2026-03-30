'''a=[1,2,3,4,5,6,7,8,9]
b=[]
for i in a:
    if i % 2==0:
        b.append(i)
for i in a:
    if i % 2 != 0:
        b+=[i]
print(b)
a=input('enter your name:')
b=int(input('enter your age:'))
if b >= 18:
        print("you are eligible to apply")
else:
    print("you are not eligible to apply") 
a=float(input("enter the number whose table you want:"))
for i in range(101):
     print(a,"x",i,"=",a*i)
a=int(input("enter the year:"))
if a % 4==0:
    print('it a leap year')
else:
    print('its not a leap year')
a=eval(input('enter the list:'))
b=[]
c=[]
for i in a:
    if i > 0:
        b.append(i)
    else:
        c.append(i)
print('the list you enter:',a)
print('the negative numbers in your list:',b)
print('thr postive number in your list:',c)
import statistics
a=eval(input('enter the list of integer:'))
a.sort()
print(a)
print(statistics.median(a))'''
a=eval(input('enter the list of integer:'))
a.sort()
b=len(a)
if b % 2==0:
    m=(int(a[int(b/2)])+int(a[int(b/2)-1]))/2
    print(m)
else:
    n=(int(a[int(b/2)]))
    print(n)
    
    
    