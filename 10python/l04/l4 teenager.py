# l4 ex 1 TEENAGER prompt name & age then if test against 13

#   prompt and input name and age of person 
name1=input("Name of Person 1 ")
age1=int(input("Age of person 1 "))

# use an IF statement to check against 13 years
if age1 < 13:
    print (name1," is still a child")
else:
    print (name1," is a teenager ")
print ("Program Done")
