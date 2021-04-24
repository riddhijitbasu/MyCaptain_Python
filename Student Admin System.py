import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact_Number", "E-Mail_Id"])
        writer.writerow(info_list)
if __name__ == '__main__':
    condition = True
    student_no=1
    while condition:
        student_info = input("Enter student detail in format for student #{}: (Name, Age, Contact_Number, E-Mail_Id) ".format(student_no))
        student_info_list = student_info.split(" ")
        print("\n The entered information is: \n Name: {}\n Age: {}\n Contact Number: {}\n E-Mail Id: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        choice_check=input("Is the entered information correct? yes/no: ")
        if choice_check == "yes":
            write_into_csv(student_info_list)
            condition_check = input("enter yes/no for Do you want to enter another student info? ")
            if condition_check == "yes":
                condition = True
                student_no = student_no + 1
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
            print("Please re-enter info")