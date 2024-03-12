# LIST COMPREHENSION
# list = [1,2,3]
# new_list = [n + 3 for n in list]
# print(new_list)
#
#
# list = "HAnh"
# new_list = [letter for letter in list]
# print(new_list)
import random

# new_list = [number * 2 for number in range(1,5)]
# print(new_list)

# names = ["Anh", "Vy", "ToanTran", "QuangLong"]
# short_name = [name.upper() for name in names if len(name) <= 3]
# print(short_name)

#DICTIONARY COMPREHENSION
# names = ["Anh", "Vy", "Vu", "Long", "Nhan"]
#
# # new_list = {new_key : new_value for item in names}
# import random
# students_score = {student : random.randint(1,100) for student in names}
#
# # new_list = {new_key:new_value for (key,value) in dictionary.item() if pass}
# pass_student = {student:mark for (student,mark) in students_score.items() if mark > 50}
# print(students_score)
# print(pass_student)

#USING PANDAS
import pandas
student_dict ={
    "name":["Anh", "Vy", "An"],
    "score": [50,60,90]
}
student_data_fram = pandas.DataFrame(student_dict)
# print(student_data_fram)
#Loop through rows of a data fram

for(index, row ) in student_data_fram.iterrows():
    print(row)