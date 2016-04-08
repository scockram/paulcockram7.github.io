# l4 ex 1 prompt name & age twice then if test for the oldest

#   prompt and input name and age of person 1
name1=input("Name of Person 1 ")
age1=float(input("Age of person 1 "))

#   prompt and input name and age of person 2
name2=input("Name of Person 2 ")
age2=float(input("Age of person 2 "))

# use an IF statement to see which age is the larger
if age1 > age2:
    print (name1," is older than ",name2)
if age1 < age2:
    print (name1," is younger than ",name2)
if age1 == age2:
    print (name1 ," and ",name2," are the same age")
