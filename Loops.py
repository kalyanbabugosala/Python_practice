#for loops

'''for i in ["c","perl","python"]:
    print(i)
'''

'''for i in "1234567":
    print(type(int(i)))
''' 
    
#while

'''a=10
while(a>0):
    print("a is:",a)
    a=a-2
'''

#nested loops

'''for a in [1,2,4,-1,0,8]:
    while a:
        if(a==0):
            print("{} is 0".format(a))
        elif(a>0):
            print("{} is positive".format(a))
        else:
            print("{} is negative".format(a))
        break;
'''
#pass-> there is no code to write butwe need to syntactically correct then we can use 'pass'

'''for i in range(0,3):
    for j in range(0,3):
        #print(i,j)
        pass
'''

'''
if 10>0:
    pass
else:
    pass
'''


#break and continue

'''for i in range(1,11):
    if(i%2==0):
        print(i)
    else:
        continue
'''

'''for i in range(1,11):
    if(i == 6):
        break
    else:
        print(i)
'''
'''
     1
    2 3
   4 5 6
  7 8 9 10
11 12 13 14 15

'''

'''
num2=1
n=int(input("Enter the n value"))
for rows in range(1,n+1):
    for sp in range(n,rows,-1):
        print(" ",end='')
    for num in range(rows):
        print(num2,end=' ')
        num2=num2+1
    print("\n")
'''





    

            

