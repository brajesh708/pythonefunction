

# function ka matlab code ko bar bar use karne ka hota he 
# block of code it is coll code 

# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result. 


# funtion 2 type ke hote he( 1 )inbuilt function = print(), max(), min(), type()
# (2 ) user difine function = jo apne bana ke use karenge spose { brajesh(), raj()}


# function ko banate samay ham parametar ka use karte he 
# function ko coll karte samay ham argument ka use karte he  



def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def add(x,y):
    z=x+y
    return z
z= add(10,20)
print(z)


def add(x,y):
    z=x+y
    return z
p=int(input("enter any fist number"))
q=int(input("enter any fist number"))
s=add(p,q)
print(s)



def add(x,y):
    print(x+y)
p=int(input("enter any fist number"))
q=int(input("enter any fist number"))
add(p,q)



print(add(p,q))


# print jab ek line me 2 ya multipal function bar aa jaye too none return karta he 


def add(x=0,y=0):
   z=x+y
   return z
p=int(input("enter any fist number"))
x=add(p)
print(x)

# next day //////////////////////////////////////////////////

def squre(x):
    squre=x*x
    return squre
z=int(input("enter number ..."))
print("hello")
print("welcome")
p=squre(z)
print(p)



# variable lenght argument
def add(*x):
    add=0
    for i in x:
        add=add+i
    print(add)
add(10,20)
add(10,20,30,40)
        
        # keybord variable lenght orgument
def employ_data(**data):
    for i,j in data.items():
     print(i,"=",j)
employ_data(name="brajesh",city="bhopal")


#  22/05/2024 class 
    
#     local vaiable methed 
def add(x):
   y=10
   sum=x+y
   print(sum)
add(10)


# glogale variable methed
y=10
def add(x):
    sum =x+y
    print(sum)
add(10)
print(y)

#  lolac vaiable ka scop rehta he
y=20
def add(x):
    y=10
    sum =x+y
    print(sum)
add(10)
print(y)



#  globale ka use karna he to golobals variable ka use karna padega
y=20
def add(x):
    y=10
    sum =x+globals()['y']
    print(sum)
add(10)
print(y)



#  local vriable ko globle karne ke liye gloable keywoed ka use karte he
def add(x):
    global y
    y=30
    sum =x+globals()['y']
    print(sum)
add(10)
print(y)



# es casee me hamne y ko gloable difin kiya he es liye 50 ko orelafe karke 30 ayega
y=50
def add(x):
    global y
    y=30
    sum =x+globals()['y']
    print(sum)
add(10)
print(y)



#  es condiotin me gloabal velue 30 uda raha he  kyuki esme velue overlap kar raha he
y=50
def add(x):
    global y
    y=30
    sum =x+globals()['y']
    print(sum)
y=80
add(10)
print(y)




x=10
print(x)
print("hello")
x=20
print(x)
print("welcome")


  
 











