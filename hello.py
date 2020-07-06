from admission_menu import adm


print("option 1: admission menu")
print("option 2: stud data")
print("option 3: fees details")


inputt=int(input("enter option (1-3): "))

if inputt>3:
    print("not a valid input")
if inputt==1:
    adm()
    