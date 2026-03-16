import pickle
def set_data():
    rollno=int(input("enter the rollno:"))
    name=input("enter the name:")
    marks=int(input("enter the marks:"))
    print()
    #create a dictionary
    student={}
    student["rollno"]=rollno
    student["name"]=name
    student["marks"]=marks
    return student
def display_data(student):
    student("ROLL.NO:",student["rollno"])
    print("NAME",student["name"])
    print("MARKS",student["marks"])
    print()
def write_record():
    outfile=open("student.dat","ab")
    pickle.dump(set_data(),outfile)
    outfile.close()
def read_record():
    infile=open("student.dat","rb")
    while True:
        try:
            student=pickle.load(infile)
            display_data(student)
        except EOFError:
            break
        infile.close()
def search_record():
    infile=open("student.dat","rb")
    rollno=int(input("enter the roll no you want to search:"))
    fume=False
    while True:
        try:
            student=pickle.load(infile)
            if student["rollno"]==rollno:
                display_data(student)
                fume=True
                break
        except EOFError:
            break
    if fume==False:
        print("record not found")
        print()
        infile.close()
def show_choice():
    print("\nMENU")
    print("1.ADD RECORD")
    print("2.DISPLAY RECORD")
    print("3.SERARCH A RECORD")
    print("4.EXIT")
def main():
    while True:
        show_choice()
        choice=input("enter the choice:")
        print()
        if choice=="1":
            write_record()
        elif choice=="2":
            read_record()
        elif choice=="3":
            search_record()
        elif choice=="4":
            break
        else:
            print("ENTER A VALID INPUT")
main()
