import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact number", "Email-ID"])
        writer.writerow(info_list)

if __name__=='__main__':
    condition=True
    student_num=1
while(condition):
    student_info=input("Enter the details of #{} : ".format(student_num))
    print("Entered details: "+student_info)

    student_info_list=student_info.split(' ')
    print("Entered student details split: "+str(student_info_list))
    print("\nThe entered info is -\nName: {}\nAge: {}\nContact_number: {}\nEmail: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    choice_check=input("Is the entered info correct? (yes/no): ")
    if choice_check=='yes':
        write_into_csv(student_info_list)
        condition_check=input("Enter yes/no: ")
        if condition_check=='yes' :
            condition=True
            student_num+=1
        elif condition_check=='no' :
            condition=False
    elif choice_check=='no' :
        print("\nPlease re-enter the info: ")

