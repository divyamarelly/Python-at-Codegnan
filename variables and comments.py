Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a,b,c=10,20,30
print(a+b+c)
60
print(a)
10
print(b)
20
print(c)
30
print(a>b)
False
print(b>a)
True
print("c")
c
print("abc")
abc
num1=num2=num3=10
>>> print(num1)
10
>>> print(num2)
10
>>> print(num3,num2)
10 10
>>> print(num1>num2)
False
>>> print(num1==num2)
True
>>> print(id(num1))
140735186527432
>>> print(id(num2))
140735186527432
>>> print(id(num3))
140735186527432
>>> print(id(a))
140735186527432
>>> print(id(b))
140735186527752
>>> a,b=257,257
>>> print(id(a),id(b))
2403750370480 2403750370480
>>> a=10
>>> b=20
>>> a,b=b,a
>>> print(a)
20
>>> print(b)
10
>>> a=20
>>> a,b=20,30
>>> print(id(a),id(b))
140735186527752 140735186528072
>>> a,b=b,a
>>> print(id(a),id(b))
140735186528072 140735186527752
>>> print(a,b)
30 20
