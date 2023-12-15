import random
pin_code=random.randint(1000,9999)

user_input=int(input("enter a 4 digit pin code:"))

if len(str(user_input))!= 4:
    print("please enter 4 digit :")
elif user_input==pin_code :
    print("success ! pin code matched ")
else:
    print("failure !pin code did not match ")
    print(f"the computer generated pinP:{pin_code}")      









