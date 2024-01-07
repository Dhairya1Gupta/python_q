stu_dict={}



def add_stu():
    stu_id=input("Enter the ID of Student:")
    stu_name=input("Enter the Name of Student:")
    grade=input("Enter the grade of Student:")

    #dictionary created
    stu_data={'Name':stu_name,'Grade':grade}
    stu_dict[stu_id]=stu_data

    print(f"Student with Student ID-{stu_id} added successfully")

def display_stu():
    print("Student Data:")
    for stu_id, i in stu_dict.items():
        print(f"ID: {stu_id}, Name: {i['Name']}, Grade: {i['Grade']}")


while True:
    print("Enter the value: ")
    print("1 : add_student")
    print("2: display_student")
    print("3: exit")

    x=int(input("Enter Your choice:"))
    if x==1:
        add_stu()
    elif x==2:
        display_stu()
    elif x==3:
        print("Program Terminated")
        break
    else:
        print("enter right choice")  