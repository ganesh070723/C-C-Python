a = int(input("Enter the starting trade amount"))
end = int(input("for how many days do you want calculate?"))
for i in range(0, end):
    if i == 0:
        pass
    print(f"day{i} = {a + a}")
