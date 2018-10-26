Input_number = input ("Ener a comma separated list of numbers:")
print(type((Input_number)))

user_input= Input_number.split(",")
print(type((user_input)))

index=0
sum=0

for x in user_input:
    sum += float (user_input[index])**2
    index+= 1
print ("Sum of squares:" , sum )