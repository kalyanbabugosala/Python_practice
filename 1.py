"""
#this is python Session


print("Python")

print('A','B','C',sep='*',end='_')
print('1','2','3',sep=' ')



print("The value of a = {0} is not valid".format(10))#format function
print(f"The value of a = {0} is not valid")#f-strings
print(f"The value of a = {str} is not valid")#f-string


#print(objects,sep=' ',end='\n',file='stdout',flush='False')

"""

import sys
a=10
b="Kalyan"
c = b + "!!!how are you"

file = open("file1_sample.txt","w")
print(a,b,c,sep='-',end='......?',file=file,flush='True')
print(a,b,c,sep='-',end='......?',file=file,flush='False')

# output is flushed here
# flushing the print() makes sure that the output that is buffered goes to the destination.
print("Hello, world!", end='',flush=False)


