import time

def sigma():
    print("omg really, are you sure?")
    response=input("(yes/no): ") # I hate that I gotta define this var for the input, theres probably another way im just dumb.
    if response=="yes":
        sigma()
    else:
        print("ok")

print("Hello Chat!")
time.sleep(2)
name=input("What is your name? ")
if name=="Bob":
    sigma()
else:
    print("Oh, ok. I thought you where bob.")