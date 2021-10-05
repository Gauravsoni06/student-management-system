from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
class Students:
    def __init__(self,window):
        self.window=window
        self.window.title("student management system")
        self.window.geometry("1350x700+0+0")
        title=Label(self.window,text="STUDENT MANAGEMENT SYSTEM",bd=10,relief=GROOVE,font=("arial",40,"bold"),bg="black",fg="white")
        title.pack(side=TOP,fill=X)
    #============all variable
        self.Roll_No_var = IntVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.DOB_var = StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
    #============manage frame
        Manage_frame=Frame(self.window,bd=8,relief=RIDGE,bg="black")
        Manage_frame.place(x=15,y=100,width=520,height=585)
        m_title=Label(Manage_frame,text="Manage Students",font=("arial",25,"bold"),bg="black",fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)
        lb1_r=Label(Manage_frame,text="Roll No",font=("arial",15,"bold"),bg="black",fg="white")
        lb1_r.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_r=Entry(Manage_frame,textvariable=self.Roll_No_var,font=("arial",15,"bold"),bd=5,relief=GROOVE)
        txt_r.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        lb1_n = Label(Manage_frame, text="Name", font=("arial", 15, "bold"), bg="black", fg="white")
        lb1_n.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_n = Entry(Manage_frame, textvariable=self.Name_var,font=("arial", 15, "bold"), bd=5, relief=GROOVE)
        txt_n.grid(row=2, column=1, pady=10, padx=20, sticky="w")
        lb1_e = Label(Manage_frame, text="Email", font=("arial", 15, "bold"), bg="black", fg="white")
        lb1_e.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_e = Entry(Manage_frame, textvariable=self.Email_var,font=("arial", 15, "bold"), bd=5, relief=GROOVE)
        txt_e.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        lb1_g = Label(Manage_frame, text="Gender", font=("arial", 15, "bold"), bg="black", fg="white")
        lb1_g.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_g=ttk.Combobox(Manage_frame,textvariable=self.Gender_var,font=("arial", 14, "bold"),state="readonly")
        combo_g["values"]=("Male","Female","Others")
        combo_g.grid(row=4,column=1,pady=10, padx=20)
        lb1_c = Label(Manage_frame, text="Contact", font=("arial", 15, "bold"), bg="black", fg="white")
        lb1_c.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_c = Entry(Manage_frame,textvariable=self.Contact_var ,font=("arial", 15, "bold"), bd=5, relief=GROOVE)
        txt_c.grid(row=5, column=1, pady=10, padx=20, sticky="w")
        lb1_d = Label(Manage_frame, text="D.O.B", font=("arial", 15, "bold"), bg="black", fg="white")
        lb1_d.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_d = Entry(Manage_frame, textvariable=self.DOB_var,font=("arial", 15, "bold"), bd=5, relief=GROOVE)
        txt_d.grid(row=6, column=1, pady=10, padx=20, sticky="w")
        lb1_a = Label(Manage_frame, text="Address", font=("arial", 15, "bold"), bg="black", fg="white")
        lb1_a.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_a=Text(Manage_frame,width=32,height=3,font=("arial", 10, "bold"), bd=5, relief=GROOVE)
        self.txt_a.grid(row=7, column=1, pady=10, padx=20, sticky="w")
    #============button frame
        btn_frame = Frame(Manage_frame, bg="black")
        btn_frame.place(x=15, y=492, width=480, height=70 )
        abtn = Button(btn_frame, text="Add",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        ubtn = Button(btn_frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        dbtn = Button(btn_frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        cbtn = Button(btn_frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)
    #============detail frame
        detail_frame = Frame(self.window, bd=8, relief=RIDGE, bg="black")
        detail_frame.place(x=540, y=100, width=790, height=585)
        lb2_s=Label(detail_frame, text="Search by", font=("arial", 15, "bold"), bg="black", fg="white")
        lb2_s.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        combo_s = ttk.Combobox(detail_frame, font=("arial", 14, "bold"),width=10,textvariable=self.search_by, state="readonly")
        combo_s["values"] = ("Roll_No","S_Name", "Contact")
        combo_s.grid(row=0, column=1, pady=10, padx=20)
        txt_s = Entry(detail_frame, font=("arial", 14, "bold"),width="19 ",textvariable=self.search_txt ,bd=5, relief=GROOVE)
        txt_s.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        sbtn= Button(detail_frame, text="Search", width=10,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        sabtn = Button(detail_frame, text="Show all", width=10,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)
    #==========table frame
        table_frame = Frame(detail_frame, bd=8, relief=RIDGE, bg="black")
        table_frame.place(x=10, y=70, width=755, height=490)
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("Roll_No","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll_No",text="Roll_No")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Contact", text="Contact")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Address", text="Address")
        self.student_table["show"]="headings"
        self.student_table.column("Roll_No",width=50)
        self.student_table.column("Name", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Contact", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Address", width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    ########table update
    def add_student(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="admin12345", database='test')
        if self.Roll_No_var.get()=="" or self.Name_var.get()=="":
            messagebox.showerror("error","all feilds are required")
        else:
            mycursor = mydb.cursor()
            mycursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                  self.Name_var.get(),
                                                                                   self.Email_var.get(),
                                                                                    self.Gender_var.get(),
                                                                                     self.Contact_var.get(),
                                                                                      self.DOB_var.get(),
                                                                                       self.txt_a.get("1.0",END)))
            mydb.commit()
            self.fetch_data()
            self.clear()
            mydb.close()
            messagebox.showinfo("success","record has been inserted")
    def fetch_data(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="admin12345", database='test')
        mycursor = mydb.cursor()
        mycursor.execute("select * from students")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,value=row)
            mydb.commit()
        mydb.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.txt_a.delete("1.0",END)
    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents["values"]
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_a.delete("1.0", END)
        self.txt_a.insert(END,row[6])
    def update_data(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="admin12345", database='test')
        if (mydb):
            print("connection successful")
        else:
            print("connection unsuccessful")
        mycursor = mydb.cursor()
        mycursor.execute("update students set S_Name=%s,Email=%s,Gender=%s,Contact=%s,D_O_B=%s,Address=%s where Roll_No=%s",(
                                                                               self.Name_var.get(),
                                                                               self.Email_var.get(),
                                                                               self.Gender_var.get(),
                                                                               self.Contact_var.get(),
                                                                               self.DOB_var.get(),
                                                                               self.txt_a.get("1.0", END),
                                                                               self.Roll_No_var.get()))
        mydb.commit()
        self.fetch_data()
        self.clear()
        mydb.close()
    def delete_data(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="admin12345", database='test')
        if (mydb):
            print("connection successful")
        else:
            print("connection unsuccessful")
        mycursor = mydb.cursor()
        mycursor.execute("delete from students where Roll_No = {first}".format(first=self.Roll_No_var.get()))
        mydb.commit()
        mydb.close()
        self.fetch_data()
        self.clear()
    def search_data(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="admin12345", database='test')
        mycursor = mydb.cursor()
        mycursor.execute("select * from students where {cb} LIKE {rb}".format(cb=(str(self.search_by.get())),rb=("'%"+str(self.search_txt.get())+"%'")))
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,value=row)
            mydb.commit()
        mydb.close()
window=Tk()
ob=Students(window)
window.mainloop()