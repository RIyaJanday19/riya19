#conditional statements:-
#if...
day=7
if day>=5:
    print("output:its a weekend")
#if else...
day=4
if day>=5 :
    print("output:its a weekend")
else:
    print("output:it's a weekday")
#nested if else...
age = 12

if age < 13:
    print("output:kid")
elif age < 21:
    print("output:Teenager.")
else:
    print("output:adult")
#loops:-
#for loop...
n=4
for i in range(0,n):
    print(i)

#nested for loop
n=7
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("* ", end="")
    print("")

#while loop...
n=5
while(n<10):
    n+=1
    print(n)

#data types
#Default values of Datatypes
a=int()
b=bool()
c=complex()
d=float()
print(a,b,c,d)
print(type(a),type(b),type(c),type(d))
#String to other datatypes
a="10"
b=float(a)
c=int(a)
d=complex(a)
print(b,c,d)
#Int to other datatypesa=15
b=float(a)
c=bool(a)
d=complex(a)
e=str(a)
print(b,c,d,e)
print(type(b),type(c),type(d),type(e))
#Float to other datatypes
a=23.75
b=int(a)
c=bool(a)
d=complex(a)
e=str(a)
print(b,c,d,e)
print(type(b),type(c),type(d),type(e))
#Complex to other Datatypes
a=10+5j
b=int(a)
c=float(a)
d=bool(a)
e=str(a)
print(b,c,d,e)
print(type(b),type(c),type(d),type(e))
#String(Names) to other Datatypes
a="aman"
b=int(a)
c=float(a)
d=complex(a)
e=bool(a)
print(b,c,d,e)
print(type(b),type(c),type(d),type(e))

#Boolean to other Datatypes
a=True
b=int(a)
c=float(a)
d=complex(a)
e=str(a)
print(b,c,d,e)
print(type(b),type(c),type(d),type(e))

f=False
g=int(f)
h=float(f)
i=complex(f)
j=str(f)
print(g,h,i,j)
print(type(g),type(h),type(i),type(j))

#Sets ----------------
print("Sets Example")
set1 = {"apple", "banana", "cherry", False, True, 0}
print(len(set1))
set2 = {"apple", "banana", "cherry"}
print(type(set2))
print("banana" not in set2)
set2.add("pineapple")
print("After adding: ",set2)
tropical = {"mango", "papaya"}
set2.update(tropical)
print("After using update",set2)
set2.remove("apple")
print("After removing apple: ",set2)
set2.discard("banana")
print("After using discard: ",set2)
x = set2.pop()
print(x)
print("After using pop(): ",set2)
set2.clear()
print("After using clear: ",set2)
set3 = {"apple", "banana"}
print("Set 3: ",set3)
del set3
print("After using del: ",set3)

# Tuple 


# List 
# Dictionary