user_input = input("\n\nEnter the number's separate with comma's : ").split(",")

reversed_num = []
for num in range(len(user_input) - 1, -1, -1):
    an = int(user_input[num])
    reversed_num.append(an)
print(f"\n\nThe reversed numbers are : {reversed_num}")
print(f"\n\nSum of the  numbers are : {sum(reversed_num)}\n\n")
