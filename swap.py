Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=20

a=a+b
b=a-b
a=a-b
print(a b);
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("{0} {1}".format(a,b));
20 10
print a
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print "Hi kalyan"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print ("Hi kalyan")
Hi kalyan
print("Hi kalyan")
Hi kalyan
print(a,b)
20 10
print(a+b)
30
print(0)
0
print(a b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(kalyan)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(kalyan)
NameError: name 'kalyan' is not defined
print("kalyan")
kalyan
print("a,b")
a,b
print("a={0} and b={1}".format(a,b))
a=20 and b=10
