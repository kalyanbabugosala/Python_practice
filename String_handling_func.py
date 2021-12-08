# Predefined string functions
s="hi kalyan this is python session"

print(s.capitalize())

print(s.center(50,'='))

print("casefold()")
str1="seẞion"
str2="session"

if str1.casefold() == str2.casefold():
    print("Both are same")
else:
    print("both are not equal")

print(s.count("is",0,17))#a.count("sub_str",start='')


print(s.endswith('h',0,12))#true or false

str3="hi kalyan\tthis is python session"
print(str3.expandtabs(4))


print(str1.encode(encoding='UTF-8',errors='strict'))#b'se\xe1\xba\x9eion'

print(s.find("z"))#index of first occurance of a given substring if not found -1

print("Hi {0}!!! This is {1}".format("python","Kalyan"))#template.formats()

print(s.index("is"))#like find()
#print(s.index("za"))#Value error


str4="123456"
print(str4.isalnum())#it returns false when there atleast one special character

str5 = "KalyanBabu007"
print(str5.isalpha())#it returns false when there is no alphabet

str6="123456a"
print(str6.isdecimal())

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print("Is digit()",a.isdigit())

print("Is digit()",b.isdigit())


print("Is decimal()",a.isdecimal())

print("Is decimal",b.isdecimal())

a="Kal yan"
print("identifier is ",a.isidentifier())



str7="kalyan@007"
print(str7.islower())#it returns false even if single character is capital letter

str8 = "1"
print(str8.isnumeric())#1/2


str9 = "kalyanbabu"
print(str9.isprintable())#returns false if one character is non printable eg:\n \t..etc


str10 = "  a"
print(str10.isspace())#it returns false if one character is not a space


str11 = "Hi This Is Kalyan"
print(str11.istitle())#it returns false it is not a titlecased and empty string


str12 = "ISUPPER@___"
print(str12.isupper())#it returns false if one character is not a uppercase


str13 = "@"
str14 = "World"
print(str13.join(str14))


print("LeftJustifier is :",str14.ljust(10,"="))

print("RightJustifier is :",str14.rjust(10,"="))


str15 = "KaLyAn bAbu"
print(str15.lower())

print(str15.upper())

print(str15.swapcase())


str16 = "   Kalyan   "
print(str16)
print(str16.lstrip())
print(str16.rstrip())
print(str16.strip())












