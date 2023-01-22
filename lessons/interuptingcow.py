"""Knock Knock joke with conditionals"""

inter_cow: str = input("Do you want an interupting cow joke?")

print("Knock Knock")
if (inter_cow == "yes"):
    print("...who's there?")
    print("Interupting cow.")
    print("...interrupting cow who---")
    print("MOOOOO")
else:
    print("Oh ok :(")
    if (input == "you're not funny"):
        print("Wow, that hurts my feelings :(")
