name = input("name: ")
age = int(input("age: "))
price = float(input("price : "))
age2 = age+1
print("My age is ",age2)
print(type(name))
print(type(age))
print(type(price))
name1 = 'mir'
print(name1)
old = False
A = None
print(type(old))
print(type(A))
#just checking
a = 2
b = 5
sum = a + b 
print(sum)
txt = "@"
print(2,txt)
print ("@")
# str*num
# str+str(concatenation)
txt2 = "2"
print(txt,txt2)
print(txt2+txt)
c = 4.0
print(a+b*c)
print(b**a)
# floor will give closest lesser integer :floor(a/b)=(a//b)
# arithmetic expression with int and float = float
# division and int division(//) will give float
# only +num%-num=-num
# not > and > or

#traffic light
light = input("light: ")
if(light== "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

#number grade calc
marks = int(input("marks: "))
try:
    marks = int(marks)
    if(marks >=80):
        print("A+")
    elif(marks >=70):
        print("A")
    elif(marks >=60):
        print("A-")
    elif(marks >=50):
        print("B")
    elif(marks >=40):
        print("c")
    elif(marks >=33):
        print("D")
    else:
        print("Fail")

except ValueError:
    print("please enter a valid integer")

print("I only eat cake")

food = input("food : ")
eat = "Yes" if food == "cake" else "no"
print(eat)
print("sweet") if food == "cake" else print("not sweet")
# clever if
salary = float(input("salary: "))
tax = salary*(0.1, 0.2) [salary>=50000]
print(tax)
# crl + / for commenting
# operators
#  Arithmetic Operators (+, -, *, /, %, **)
#  Relational / Comparison Operators (==, !=, >, <, >=, <=)
#  Assignment Operators (=, +=, -=, *=, /=, %=, **=)
#  Logical Operators (not, and, or)

# part one done
#change git

