#Program to count lowercase and uppercase letters in an inputted string
str1 = input("Enter the string :")
print(str1)
uprcase=0
lwrcase=0
i = 0
while i < len (str1):
    if str1[i].islower() == True:
        lwrcase += 1
    if str1[i].isupper() == True:
        uprcase += 1
    i += 1
print("No. of uppercase letters in the string = ",uprcase)
print("No. of lowercase letters in the string = ",lwrcase)









