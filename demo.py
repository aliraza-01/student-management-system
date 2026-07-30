
# #Challenge 1
# students = [
#     {
#         "Name": "Ali",
#         "Roll Number": 101,
#         "Age": 20
#     },
#     {
#         "Name": "Ahmed",
#         "Roll Number": 102,
#         "Age": 22
#     },
#     {
#         "Name": "Sara",
#         "Roll Number": 103,
#         "Age": 19
#     }
# ]


# for student in students:
#     if student["Roll Number"] == 103:
#         print(f"Name: {student["Name"]}")
#         print(f"Roll Number: {student["Roll Number"]}")
#         print(f"Age: {student["Age"]}")
#         break
   


#Challenge 2
students = [
    {
        "Name": "Ali",
        "Roll Number": 101,
        "Age": 20
    },
    {
        "Name": "Ahmed",
        "Roll Number": 102,
        "Age": 22
    },
    {
        "Name": "Sara",
        "Roll Number": 103,
        "Age": 19
    }
]

roll_no = int(input("Please enter your roll Number: "))
for student in students:
    if student["Roll Number"] == roll_no:
        print(f"Name: {student["Name"]}")
        print(f"Roll Number: {student["Roll Number"]}")
        print(f"Age: {student["Age"]}")
        break
    print("Student Not Found")
   
