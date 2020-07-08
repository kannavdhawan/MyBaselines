print("hello US")
runway= "free"
if runway=="free":
    print("go")




print('loops')
i=0
while(i<5):
    print(i)
    i+=1

for i in range(0,5,1):
    print(i)


landings=200
takeoffs=100
print("no of landings", landings)
print("no of takeoffs "+str(takeoffs))

print("escape sequence")
print("hello \n\nnew line")
print("hello\t\ttabs")
print("A slash \" see")
print("hello see both in same line",end="")
print("same line with 2 prints")

num=int("10")+20
print(num)
strings=str(20)+str(209)
print(strings)
print(type(num))



# functions 


print("function")
def function_name(variable1,variable2):
    sum=variable1+variable2
    return sum
result=function_name(2,4)
print(result)


print("problem")
def tickets(adults,children):
    rate_per_adult=37550
    rate_per_child=(rate_per_adult)/3
    total=(adults*rate_per_adult+children*rate_per_child)
    tax=total*0.07
    after_tax=total+tax
    after_discount=after_tax-after_tax*0.10
    return after_discount
# no_adults=input("enter number of adults")
# no_children=input("enter no of children")
# result=tickets(int(no_adults),int(no_children))
result=total_price_round=tickets(5,2)
print("final price is",result)



# if else continue break pass


for airline in ["emirates" , "airasia", "dakota", "noairline"]:
    if airline=="noairline":
        break # to come out of loop 
    print(airline,'\t',end="")

for airline in ["emirates" , "airasia", "dakota", "noairline"]:
    if airline=="emirates":
        print("\nfirstloopexecuted")
    elif airline=="airasia":
        print("secondloopexecuted")
    else:
        pass # used to do nothing
    continue #skip lines below useful when multiple if statements and no need to go for if statement after first if
    print("skipped")

#Lists


airline=["emirates", "dakota","daone"]
if "dakota" in airline:
    print("found")

print("list of list\n\n")
planes=[["emirates",10],["dakota",80],["daone",900]]
print("No of planes with",planes[2][0]," are ",planes[2][1])
# print(planes[0])

#tuple 

airlines=("daone",) # () are for readability ...   comma for single element 
print(airlines)

tuple1="hello",
tuple2="hello2",
tup_= tuple1+tuple2+("hello3",)
print(tup_)

# function proper

def calculate_bill_amount(gems_list,gems_price,gems_req,req_qty):
    bill_total=0
    index=[]
    for i in gems_req:
        if i in gems_list:
            index.append(gems_list.index(i))
    for i in index:
        j=0
        bill_total=bill_total+gems_price[i]*req_qty[j]    
        j+=1
    return bill_total

gems_list=["emerald","ivory","ruby","garnet"]
gems_price=[100000,200000,222233,22222222]
gems_req=["emerald","ivory"]
req_qty=[1,1]
bill_amount=calculate_bill_amount(gems_list,gems_price,gems_req,req_qty)
print(bill_amount)


# strings
pancard="ABCDEF"
for i in range(0,len(pancard)):
    print(pancard[i])
if "Z" in pancard:
    print("found")
# set -- unoredered group of values with no duplicate values 
set1={1,2,3,4}
print(type(set1))

list=[1,2,3,2,2,1,1,1,1]
set2=set(list)
print(set2)

#dictionary 

airline_details={"Airlines":"DaOne","owner":"kannav dhawan"}
print(airline_details["owner"])

for key,value in airline_details.items():
    print(key,":::",value)
airline_details["owner"]="KANNAV DHAWAN"
print(airline_details["owner"])

# return false or true 
def func1(a,b):
    if a>b:
        return True
    else:
        return False
a,b=5,6
if(func1(a=a,b=b)): #can mention the argument name for flexibiity
    print("True")
else:
    print("False")

# mutability ---> string is immutable whereas list is mutable. to make string and int mutate inside the function, use global inside.


pages=[]
pages.append(340)

def func2(val1,*vals): # all the vals will be a tuple
    print(val1)
    print(vals)
    print(vals[0])

func2(1,2,3,4,5,6)


pages.append(356)

##python doesn't allow the modification of a global variable inside a function. Global variable is a simple variable with no global written with it.
#  it is just outside the function 
# if you want to modify a global variable inside a fucntion then do it by using global keyword
# 
val4=4
def func3(newval):
    # val4=newval # wont work
    # print(val4,"old value")
    global val4
    val4=newval # updated
    print(val4,"updated globally")
print(val4)
func3(5)
print(val4)

val4=[4]
def func3(newval):
    val4[0]=newval # updated
    print(val4)
func3(5)
print(val4)
# list is mutable without specifying global inside the function

pages.append(357)
pages.append(358)

pages.append(399)
# exceptions default exceptions 

# importing packages
# import Flights.manage
# import Employees.manage
# Flights.manage.add()
# Employees.manage.add()
import random
print(random.randrange(10,20))

# ceil
x=10.5
import math 
print(math.ceil(x))
print(math.floor(x))
print(math.fabs(x))
print(math.factorial(10))
pages.append(450)
pages.append(461)
pages.append(480)

import time
print(time.localtime())

flight_file=open("flight.txt","w")
flight_file.write("pages")
flight_file.close()

try:
    flight_file=open("flight.txt","r")
    text=flight_file.read()
    print(text)
    #throws exception below and file is open
    flight_file.write("Good Morning")
    flight_file.close
except:
    print("error occured")
    if flight_file.closed:
        print("file is closed")
    else:
        print("file is open")
finally:
    #closing a file is neccesary 
    flight_file.close()
    if flight_file.closed:
        print("closed in finally")
    else:
        print ("still open")


#  regex
pages.append(501)
import re
Input="Flight savana airlines 12244556"
if(re.search(r"a..lines",Input)!=None):
    print("found")
else:
    print("Not found")
# . stands for any character 
#\d checks for a digit 
if(re.search(r"1\d\d\d\d\d\d6",Input)!=None):
    print("digit found")
else:
    print("Not found")
# to search a number between two numbers

if(re.search(r"1[1-4]2",Input)!=None):
    print("number found")
else:
    print("Not found")
# to search either of n words in the input 
if(re.search(r"Fell|Hell","Fellow")!=None):
    print("something found out of two")
else:
    print("Not found")
# \s to check space 

#\d* to check if a number is found 0 or n times
#\d+ 1 or n times
#\d? 0 or 1 times 
# to check if 3 digits are present in the string after A
if(re.search(r"A\d{3}i","A123irline")!=None):
    print("3 digits found")
else:
    print("Not found")

# check if given string is strating with A
# check if string is ending with e 

if(re.search(r"^A||e$","Airline")!=None):
    print("both satisfied")
else:
    print("wrong")
# last character alphanumeric --> \w$
# escape a special character \* 


#sub in re 
# replace the word flight with word plane 
flight="emirates airlines"
flight=re.sub(r"emirates",r"Da-One",flight)
print(flight)

# multithreading 
# uncomment below
pages.append(532)

from threading import Thread
def func_a():
    pass
    # name=input("Enter your name")
    # print("your name is ",name)
def func_b():
    for i in range(0,10):
        print("done")
thread1=Thread(target=func_a)
thread1.start()
thread2=Thread(target=func_b)
thread2.start()

thread1.join()
thread2.join()

pages.append(539)
# lambda 
x,y=1,2
ans=(lambda x,y: x+y)(x,y)
print(ans)

g=lambda x,y: x*(x+y)
print(g(1,3))

h=lambda x: math.factorial(x)
print(h(5))

j=lambda x: x>10
v=11
if j(v):
    print(v,"is greater than 10")
else:
    print("is not greater than 10")

# problem --> count char and digits in sentence

def count(sentence):
    char_count=0
    digit_count=0
    for i in sentence:
        if(re.search(r"[a-z]|[A-Z]",i)):
            char_count+=1
        elif(re.search(r"[0-9]",i)):
            digit_count+=1
    result=[]*2
    result.append(char_count)
    result.append(digit_count)
    return result
sent="emirates 123"
print(count(sent))


pages.append(648)
# problem- return maximum overlap 
# def longest_common_substring(word1,word2):
#     list1=[]
#     for i in word1:
#         for j in word2:
#             if i==j:
#                 list1.append(i)
#                 break

# w1='pirate'
# w2='teepee'
# longest_common_substring(w1,w2)




