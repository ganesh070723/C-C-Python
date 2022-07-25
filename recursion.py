def first():
    second()
    print("I'm the first Method")
def second():
    third()
    print("I'm the second Method")
def third():
    fourth()
    print("I'm the Third Method")
def fourth():
    print("I'm the Fourth Method")

first()

# def first(n):
#     if n > 0:
# 
#         print(f" {n}")
#         first(n - 1)
# 
# first(5)