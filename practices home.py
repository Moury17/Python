# A= 5
# B=3.1416
# C=A+B
# print(type(C))
# #implicit type casting
# A_float=float(A)
# print("Converted y to float:", A_float)
# a=10
# b=3.5
# c=True
# d=a+b
# print(d, type(d))
# e=a+c
# print(e, type(e))
# X={1:300,2:200,3:300}
# print(type(X))
# X=str(X)
# print(X)
# a=[2,3,4]
# # 
# obj=tuple(a)
# print(obj)
#exercise 3.1:
# name=input('Enter a name:')
# print("Hello",name+"!","Welcome to the python programming course.")
#Exercise 3.2:
# string=input("Enter a word:")
# if len(string)<2:
#     new_string=""
# else:
#     new_string=string[:2]+string[-2:]
# print("New string:", new_string)
#Exercise 3.3:
student={
    "Name":"Farhana Afser Moury",
    "Roll":"20GLM050",
    "Dept":"Geology and Mining",
    "CGPA":"3.57",
    "Marks":{
        'Mining Geology': 40,
        'Engineering Geology':36,
        'Mineralogy':45
    }
}
# print(student)
# print(student['Name'],student['Roll'],student['Marks']['Mineralogy'])
# a=int(input("input a number:"))
# b=int(input("Enter another number:"))
# ans=(a+b)/b
# # print(int(ans))
# x=2<<2**2+1
# print(x)
# number=int(input("enter a number:"))
# if(number % 2 == 0):
#     print(f"The {number} is Even")
# else:
#     print(f"The {number} is Odd")
# def weekday(n):
#     match n:
#         case 0: return "Monday"
#         case 1: return"Tuesday"
#         case 2: return "Wednesday"
#         case 3: return "thurseday"
#         case 4: return "Friday"
#         case 5: return "Saterday"
#         # case 6: return "Sunday"
#         case _: return "Invalid day number"
# # print(weekday(4))
# # print(weekday(8))
# print(weekday(6))
