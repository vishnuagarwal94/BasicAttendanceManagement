Info = (('001','Vishnu'),('002','Jitu'))
Id = input("Enter Login Id :")
Name =input("Enter Name :") 
Detail =(Id,Name)
if Detail in Info:
    print("User Authenticate & Login Successful ")
    Detail = {}
    def add():
        Registration_no = input("Enter student registration number :")
        Name = input("Enter student name :")
        while Registration_no !='Exit':
            data={Registration_no : Name}
            Detail.update(data)
            Registration_no = input("Enter Registration number again :")
            Name = input("Enter student name :")
        return Detail
    add()
    print(Detail)
    def edit():
        Registration_no = input("Student Registration Number :")
        Name = input("Enter Name to update :")
        while Registration_no !='Exit':
            for i in range(len(Detail)):
                if Registration_no in Detail:
                    Detail[Registration_no]=Name
            Registration_no = input("Student Registration Number :")
            Name = input("Enter Name to update :")
        return Detail
    edit()
    print(Detail)
    def view():
        return Detail
    view()
    print(Detail)
    def delete():
        Registration_no = input("Enter Registration number to delete :")
        while Registration_no !='Exit':
            for i in range(len(Detail)):
                if Registration_no in Detail:
                    del Detail[Registration_no]
            Registration_no = input("Enter Registration number to delete :")
        return Detail
    delete()
    print(Detail)
    P ={}
    Record = []
    def display():
        date = input("Enter  date to attendance :")
        while date!= 'Exit':
            Registration_no = input("Enter Registration Number :")
            while Registration_no != 'Exit':
                if Registration_no in Detail:
                    Attendance = input("Enter student present or not :")
                    if Attendance == "P":   
                        P.update({(date,Registration_no) : "P"})
                        Record.append({Registration_no : (date,"P")})
                Registration_no = input("Enter Registration Number :")
            date = input("Enter another date to attendance :")
        return P,Record
    display()
    print(P)
    print(Record)
    Report = []
    def report():
        Registration_no = input("Enter Registration Number :")
        date = input("Enter Date to search Attendance :")
        if (date,Registration_no) in P:
            Report.append(P[(date,Registration_no)])
        return Report
    report()
    print(Report)
    repo = []
    def rep():
        date = input("Enter date to Attendance Report :")
        if date in Record:
            repo.append(Record[date])
        return repo
    rep()
    print(repo)
else:
    print("User Not Authenticate")