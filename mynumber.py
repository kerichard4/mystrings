import math

print(math.cos (75))

# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57

temp=56.8926
temp1=round(56.8926)
print(temp1)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 

temp2=round(56.8926,2)
print(temp2)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893
temp3=round(56.8926,3)
print(temp3)

# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
tempA="56.8926"
temp4=(tempA[3: :1])
temp5= float(temp4)*0.001
print(temp5)
