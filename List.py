a = [2,5,3,"kalyan"]
print(a)
print(id(a))   
a[2] = 4
print(a)
print(id(a))  #before and after changing the value in a id is same -> mutable
#a[4] = 6  # list assignment out of range
#print(id(a))

#linear data structure
print("\n linear data structure\n")
a += [6]  #by adding like this it wont change the id of a
print(id(a))
a =a + ['vinay','kalyan']  # by adding like this id of a will change
print(a)
print(id(a))
 #zero based index
print(a[0])

#nesteed list
a = [1,2,3,[56,7],67,9,0]
print(a)
print(a[0],a[1],a[2],a[3],a[4],a[5],a[6])
print(a[3][0],a[3][1])

#list operations

#length
print(len(a))

#repetition
print(a[2]*3)#9
print(a[3]*3) # [56,7,56,7,56,7]

#membership
print(3 in a)
print(4 in a)

#iteration
a = [1,2,3,4,5,6]
for i in a:
    print(i*i)
    i=i+1

print(a[1::]) #2 3 4 5 6
print(a[1::2])  # 2 4 6
print(a[::-1])# 6 5 4 3 2 1

del(a)
#print(a)  # here a is deleting so,getting error

#list methods
a =[2,3,4]
a.append(4)
print("append method : ", a )
#a.append(4,5) #list.append() takes exactly one argument (2 given)
a.append([4,5]) # it was like nested list
print(a)
b=[3,4,5]
a.extend(b)
print('extend method',a)
print(a[1])
a.insert(1,5)  # insert the second argument at the place of 1st argument
print('insert method',a)
print(a[1])
a.insert(20,5)#when we give the 1st argumnt greater than the list size it will inset at the end of the list
print('insert method',a) 
a.remove(3)
print('remove method',a) 
#a.remove(10) #if the given element is not present in the list it will through error
#print('remove method',a)
res=a.pop(3) # it removes an element at the given index and returns that elemnt
print('pop method',res)
print('remove method',a)
a.clear() #emptie the list
print('clear method',a)

a = [3,5,4,2,6,4,3]
res=a.index(4) # returns the index of fist occurence of the ele 
print('index method',a)
print('index method',res)
res=a.count(3) # returns the count of 3
print('count method',res)
a.sort()
print('sort method',a)
a.reverse()
print('reverse method',a)
b=a.copy() #shallow copy
print('copy method',b)
print('id of a',id(a)) #here ids are different 
print('id of b',id(b))
d =[1,2,3]
c = d #deep copy
print('id of a',id(d)) #here ids are same
print('id of c',id(c)) #when we change any thing in c its also reflect in a
c[1] = 3
print('c',c)
print('d',d)
b[1] = 0
print('b',b)
print('a',a)

##built in functions

print("all fun",all(a)) #true
print("all fun",all(d)) #false
print("any fun",any(d)) #true
print("any fun",any(a)) #false
print("enumerate fun",list(enumerate(d))) ##[(0,1),(1,3),(3,3)]
print("enumerate fun",list(enumerate(d,20)))  ##[(20,1),(21,3),(22,3)]
print("len fun",len(a)) #it will return the length of a
a = "123456"
a=list(a)
print("list fun",a)
print("max fun",max(a))
print("min fun",min(a))
print("sum fun",sum(b))
