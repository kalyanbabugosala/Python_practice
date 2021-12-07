#Functions


#General classification
'''def fun():
    print("Hi this is python session")
    return

fun()
'''

'''def fun(string):
    print("hi this is"+string+" Thank you")
    return

string = input("Enter your name:")
fun(string)
'''

'''def fun():
    print("Without parameter passing return value from fun()")
    return 10
print(fun())
'''

'''
def fun(a,b):
    print("a:",a);print("b:",b)
    return a*b
print(fun(2,4))
'''


#Extra functions in python

#Default Arguments
'''
def fun(a,b,c=10):
    print("a=",a,"b=",b,"c=",c)
    return
fun(2,4)
'''

#Required Arguments
'''
def fun(a,b,c):
    print("a=",a,"b=",b,"c=",c)
    return
fun(10,20,30)
'''

#keyword arguments
'''
def fun(name,age,org='TS'):
    print("name:",name,"Age:",age,"Org:",org)
    return
fun(age=21,name="Kalyan")
'''


#Variable Arguments
'''
def fun(*list):
    print("List:",list)
    return

fun(10,20,30,40)
fun(10,10,20,30,40,'Kalyan','m')
fun()
'''



#Lambda Expressions

'''
def fun(a,b):
    a=a+b
    return a
fun(a,b)

'''


'''x = lambda a,b:a+b
print(x(10,20))

'''


#Filter->a new list contains items for which the function evaluates to True
'''
list1=[1,2,5,6,8,3,0,12,10]

even_list=filter(lambda x:x%2==0,list1)

print(list(even_list))
'''

#map->a new list contains items returned by that function for each item
'''
list1=[1,2,5,6,8,3,0,12,10]

even_list=map(lambda x:x%2==0,list1)

print(list(even_list))
'''


'''
def fun(a):
    if(a or a==0):
        return True
    else:
        return False

        

list1=(1,2,5,6,8,3,0,12,10)

even_list=filter(fun,list1)#map() also

print(list(even_list))
'''












