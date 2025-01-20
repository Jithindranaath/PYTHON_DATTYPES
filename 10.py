#STRING
s='naresh'
print(s)
print(type(s))


s2='''nareshit
technology'''
print(s2)


for i in s:
    print(i)


print(s[3])
print(s[-3])

#STRING SLICING (:)
print(s[0:4])   #0 to n-1
print(s[1:-4])
print(s[2:-1])
print(s[0:7:2])   #here 2 is step index

#STRING CONCATANATION
s6='hello'
s7='hi'
s8=s6+s7
print(s8)           #output:hellohi


#operators
# 1-Arithmetic
a=5
b=6
c=a+b
print(c)

#magic method
d=int.__add__(5,6)
e=int.__sub__(5,6)
print(d)
print(e)
f=int.__mul__(5,6)
g=int.__divmod__(7,2)      #output:(divisor,reminder)
print(f)
print(g)

x=10
y=5
z=x//y      #output:quotient
print(z)
z1=x%y      #output:reminder
print(z1)


#practice(task)
import keyword
import sys
print(keyword.kwlist)
print(len(keyword.kwlist))
j=20
k=10
r=k
print(j,type(j),hex(id(j)))
print(k,type(k),hex(id(k)))
print(r,type(r),hex(id(r)))

intvar,floatvar,strvar=96,10.1,'dgfjsy'
print(intvar)
print(floatvar)
print(strvar)

var1=57
print(var1)
print(type(var1))
print(sys.getsizeof(var1))
print(var1,'is interger?',isinstance(var1,int))

var2=57.57
print(var2)
print(type(var2))
print(sys.getsizeof(var2))
print(var2,'is float?',isinstance(var2,float))

var3=2+3j
print(var3)
print(type(var3))
print(sys.getsizeof(var3))
print(var3,'is xomplex?',isinstance(var3,complex))

sys.getsizeof(int)
sys.getsizeof(float)
sys.getsizeof(complex)
sys.getsizeof(str)
sys.getsizeof(bool)

mystr='hello'
mystr2="hello"
mystr3='''helllo
everyone'''
print(mystr,mystr2,mystr3)

str1='python language'
print(str1[8])
print(str1[len(str1)-1])
print(str1[6])
print(str1[0:4])
del str1
print(str1)

j1='hgsurgh'
j2='jdguhg'
j3=j1+j2
print(j3)