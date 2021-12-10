fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
  if "a" in x:
    new_list.append(x)

print(new_list)

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


newlist = [x for x in fruits if x != "apple"]

print(newlist)

newlist = [x for x in fruits]

print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x if x != "mango" else 0  for x in fruits]
print(newlist)

def list_fruits(fruit):
    if(fruit != 'apple') :
        return fruit
    else:
        return 0
newlist =[list_fruits(x) for x in fruits]
print(newlist)
