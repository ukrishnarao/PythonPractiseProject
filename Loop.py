i = 1
while i<=5:
    print ("Krishna is learning Loops\t", i)
    i = i+1

i = 1
while i<=5:
    print ("Krishna is learning python", end = "")
    print(" in year 2022", end = "")
    print ("")
    i = i+1

i = 1
while i <=5:
    print ("Krishna is learning python ", i ,  end = '')
    print()
    i = i+1

i = 1
while i <=5:
    print ("Krishna is learning python ",   end = '')
    j = 1
    while j<=5:
        print(" in year 2022 ")
        j = j+5
    #print()
    i = i+1

i = 1
while i<=100:
    print (i)
    i = i+1


i = 1
while i<=4:
    print("#",end = "" )
    j = 1
    while j<=4:
        print("#",end = "")

        j= j+1
    i = i+1
    print()

print("Krishna - new result set")

#write a code to print all the numbers 1-100 and skip the numbers which are divisible by 3 or 5 - while loop
i = 1
while i<=100:
    if i%3 !=0 and i%5 != 0:
        print(i, end = "\t")
    i = i+1

#write a code to print all the numbers 1-100 and skip the numbers which are divisible by 3 or 5 - for loop
for i in range(1,100):
    if i%3 !=0 and i%5 !=0:
        print (i, end = "\t")

#write a code to print all the numbers 1-100 and skip the numbers which are divisible by 3 - for loop
import math as m
for i in range(1,101,1):
    if i%3 !=0:
        print(i, end = "\t")

#for loop example
for i in ('krishna'):
    print (i, end = "\t")

#for loop example 2
x = ['krishna', 'lavanya', 'khyathi','12','34','56']
for i in (x):
    print (i, end = "\t")

#print 20 tables in an orders
i=1
while i<=20:
    y=1
    while y<=10:
       print(y*(i),end="\t")
       y=y+1
    i=i+1
    print()

#code to print the exact squares below 100
import math as m
for i in range(1,100,1):
    if int(m.sqrt(i))==float(m.sqrt(i)):
        print(i, end = "\t")

#code to use continue in a loop
import math as m
for i in range(1,101,1):
    if i%3==0 or i%5==0:
        continue
    print(i, end = "\t")
print("Out of the loop")

#Code for a simple example for continue and break
x = int(input("Enter the value for x : " ))
for i in range (1,x+1):
    print (i, end = "\t")
# output is 1   2   3   4   5 (if x = 5)
#if you use continue
x = int(input("Enter the value for x : " ))
for i in range (1,x+1):
    if i==3:
        continue
    print (i, end = "\t")
# output is 1   2   4   5 (if x = 5)
#if you use break
x = int(input("Enter the value for x : " ))
for i in range (1,x+1):
    if i==3:
        break
    print (i, end = "\t")
# output is 1   2 (if x = 5)
# pass

#code to print fibonacci series
print("Fibonacci Series Numbers")
limit = int(input("Enter the value for limit: "))
x = 0
y = 1
#print (x, y, end = "\t")
print (x, end = "\t")
print (y, end = "\t")
for i in range (2,limit,1):
    z = x+y
    print (z, end = "\t")
    x = y
    y = z


#code to check whether the input is a prime number or not?
x = int(input("Enter the value of x: "))
if x <2:
    n = 0
elif x == 2:
     n = 1
else:
    for i in range(2,x):
        if x%i ==0:
            n = 0
            break
        else:
            n =1
if n == 0:
    print(x, " is not a prime number")
else:
    print(x, "is a prime number")

#code to check whether the input is a prime number or not?

import math as m
print("Checking the prime number or not?")
x = int(input("Enter the number: "))
if x>2:
    for i in range(2,x,1):
        if x%i ==0:
            print(x, " is not a prime number")
            break
        else:
            print(x, " is a prime number")
            break
elif x==2:
    print (x, " is a prime number")
else:
    print (x, " is not a prime number")













