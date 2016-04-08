# Exercise 4
# times table generator - via user input

# input from the user which times table you want to compute
times_table = int(input("Enter the times table you want "))

# input from user how many times you want - upper limit
upper_limit = int(input("Enter the tables upper Limit "))

i = 0  #set the start value

# loop thru the times table and print
for i in range(upper_limit):
    print(str(i+1)+" x "+str(times_table)+" = ",str((i+1)*times_table))
