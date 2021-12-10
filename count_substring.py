string ="hi kalyan this is python snake i will byte you kalyan abcdcdc"
sub_string="cdc"
c=0
for i in range(0,len(string)):
    if string[i:].startswith(sub_string):
        c +=1
print(c)

s="qA2"
list1=[]
for i in s:
    list1.append(i.isalnum())
print(any(list1))
list1=[]
for i in s:
    list1.append(i.isalpha())
print(any(list1))
list1=[]
for i in s:
    list1.append(i.isdigit())
print(any(list1))
list1=[]
for i in s:
    list1.append(i.islower())
print(any(list1))
list1=[]
for i in s:
    list1.append(i.upper())
print(any(list1))


n = int(input())
m = int(input())


for i in range(1,n//2): 
    c= ".|." * (2*i-1)
    print(c.center(m,'-'))

print("WELCOME".center(m,'-'))

for i in range(n//2,1): 
    c=".|." * i
    print(c.center(m,'-'))
