#singleton tuple
print("singleton tuple")
a=(10)
print(type(a)) # it is int
a=(10,)
print(type(a)) # it is tuple

#packing and unpacking
print("packing and unpacking")

tup = (10,27,"good",8.9)
a,b,c,d = tup
print(a)
print(b)
print(c)
print(d)
print('\n-------------------------------------------------------\n')

a = (2,5,3,"python")
print(a)
print(id(a))   
#a[2] = 4 #in tuple we cant modify the value ->immutable

#a[4] = (6)  #'tuple' object does not support item assignment

print('\n-------------------------------------------------------\n')
#linear data structure
print("\n linear data structure\n")
a += (6,)  #by adding like this also it will change the id of a
print(id(a))
a =a + ('vinay','kalyan')  # by adding like this also id of a will change
print(a)
print(id(a))

print('\n-------------------------------------------------------\n')

 #zero based index
print('zerobased index',a[0])
print('\n-------------------------------------------------------\n')
#nesteed list

print('nested list\n')
a = (1,2,3,[56,7],67,9,0)
print(a)
print(a[0],a[1],a[2],a[3],a[4],a[5],a[6])
print(a[3][0],a[3][1])

#tuple operations
print('\n-------------------------------------------------------\n')
print('tupple operations\n')
a =(2,4,3,"roshini'",5)
#length
print("length",len(a))
#concatenation
print((1,2)+(3,4))
print("a",a)
#repetition
print("repetation",a[2]*3)#9
print("repetation",a[3]*3) # roshini'roshini'roshini'

#membership
print("membership",3 in a)
print("membership",4 in a)

#iteration
print("iteration")
a = (1,2,3,4,5,6)
for i in a:
    print(i*i)
    i=i+1
print('\n-------------------------------------------------------\n')
print("slicing\n")
print(a[1::]) #2 3 4 5 6
print(a[1::2])  # 2 4 6
print(a[::-1])# 6 5 4 3 2 1

del(a)
#print(a)  # here a is deleting so,getting error
print('\n-------------------------------------------------------\n')

#tuple methods
print("tuple methods\n")


a = (3,5,4,2,6,4,3)
res=a.index(4) # returns the index of fist occurence of the ele 
print('index method',a)
print('index method',res)
res=a.count(3) # returns the count of 3
print('count method',res)

print('\n-------------------------------------------------------\n')

##built in functions
print("built in functions")
d =(1,0,3)
print("all fun",all(a)) #true
print("all fun",all(d)) #false
print("any fun",any(d)) #true
print("any fun",any(a)) #false
print("enumerate fun",list(enumerate(d))) ##[(0,1),(1,0),(3,3)]
print("enumerate fun",list(enumerate(d,20)))  ##[(20,1),(21,0),(22,3)]
print("len fun",len(a)) #it will return the length of a
a = "123456"
a=list(a)
print("list fun",a)
print("max fun",max(a))
print("min fun",min(a))
print("sum fun",sum(d))
