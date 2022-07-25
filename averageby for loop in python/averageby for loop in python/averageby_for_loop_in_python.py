print("WELCOME TO AVERAGE HEIGHT FINDER..\n\n")

student_heights=input("enter the heights one by one by space : ").split()
count=0
total=0
for height in student_heights:
    total+=int(height)
    count+=1
   
avg= total/count
average =round(avg)

print(f"THE AVERAGE HEIGHT IS :{average}")