# lesson 2.1 - data types
year = 2013    # integer number
age = 13.75     # decimal number
name = "John"   # string

# now print them out to screen
#print (year)
#print (age)
#print (name)
year = int(input("Enter the Year "))
age = float(input("Enter your age as a decimal "))
name = input("Enter your name ")

# place a comma(,) before and after each variable to oing to a string
print ("Your name is ",name, " you were born in ",year," and are ",age," years old  <Commas only>")

# or STR() function will convert a number to a string data type
print ("Your name is ",name, " you were born in "+ str(year)+" and are "+str(age)+" years old <STR functiomn>")


