newName = input("What's your name? ")
while True:
    newAge = input("How old are you? ")
    try:
        int(newAge)
        break
    except ValueError:
        print("that ain't a number twin")


if(newName == "mason" and newAge == "67"):
    print("hello sigma 67 mason :zany_face:")
else:
    print(f"You are {newName} and you are {newAge} years old.")

if(newAge < 0):
    print("lil bro aint even born yet :sob:")
elif(newAge < 30):
    print("hello twin :heart:")
elif(newAge < 70):
    print("hello unc :heart:")
else:
    print("dang bro is your coffin comfy? :skull:")


newGradeBoundaries = ["fail", "near pass", "pass", "merit", "distinction"]

while newGrade not in newGradeBoundaries:
    newGrade = input("What grade did you get? ")
    if(newGrade in newGradeBoundaries):
        break
    else:
        print("that aint what i asked")
    
if(newGrade == "fail"):
    print("damn bro you about as sharp as a sphere")
elif(newGrade == "near pass"):
    print("you almost made it bro")
elif(newGrade == "pass"):
    print("good job bro")
elif(newGrade == "merit"):
    print("nice one twin you kinda smart")
else:
    print("twin is the next einstein :heart:")