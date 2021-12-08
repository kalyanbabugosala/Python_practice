#Strings

#dir("")

'''
s = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
count = 0
for i in s:
    print(count,s[count])
    count = count + 1
'''
#print(str)


#Characteristics of strings

'''a = 'python'
print(a)

a = "python"
print(a)
'''

'''
a = 'python"world"world'
print(a)

a = "python'world'world"
print(a)
'''

'''
str = "hi this is \'python' session"
print(str)


str = "hi this is \t'python' session"
print(str)

str = "hi this is \n'python' session"
print(str)
'''

#Indexing


str = "PYTHON"
'''
c=0
for i in str:
    print("str[%d]:"%c,i)
    c+=1
'''

'''
print(str)
print("str[0]:",str[0])
print("str[-6]:",str[-6])
'''


#slicing
'''
str = "PYTHON"

print(str[:])
print(str[2:6])
print(str[:5])
print(str[-2:-4:-1])
print(str[-5:-7:-1])
print(str[-5:4:1])
print(str[1:6:2])
'''
#Format specifiers
'''
name = "kalyan"
age = 21

print("Name is %s and age is %d"%(name,age))

x = 12.3456
print("%0.2f"%x)

s = 'k'
i = 65
print("%s %c %x"%(s,i,i))
'''



