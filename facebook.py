# from tkinter import *
# import sqlite3
# from tkinter import messagebox






# root = Tk()
# root.title("Facebook")


# #databases


# #create database or connect to one



# conn = sqlite3.connect("Facebook.db")

# #create cursor
# c = conn.cursor()  #to execute queries on sqlite3

# # c.execute("""CREATE TABLE User(
# #     FirstName text,
# #     LastName text,
# #     Age text,
# #     Address text,
# #     City text,
# #     Zipcode text,
# #     Password text,
# #     Gender text



# # )""")



# def submit():
#     First_name.delete(0,END)
#     Last_name.delete(0,END)
#     Age.delete(0,END)
#     Address.delete(0,END)
#     City.delete(0,END)
#     Zipcode.delete(0,END)
#     Password.delete(0,END)
#     Gender.delete(0,END)
    

# delete_box = Entry(root,width=30)
# delete_box.grid(row=9,column=1,pady=5)

# delete_label= Label(root,text="Delete ID")
# delete_label.grid(row=9,column=0,pady=5)


# First_name= Entry(root, width=30)
# First_name.grid(row=0,column=1,padx=20)

# firstname_label= Label(root,text="First Name")
# firstname_label.grid(row=0,column=0)

# Last_name =Entry(root,width=30)
# Last_name.grid(row=1,column=1)


# lastname_label= Label(root,text="Last Name")
# lastname_label.grid(row=1,column=0)

# Age= Entry(root,width=30)
# Age.grid(row=2,column=1)

# Age_label=Label(root,text="Age")
# Age_label.grid(row=2,column=0)

# Address = Entry(root,width=30)
# Address.grid(row=3,column=1)

# Address_label=Label(root,text="Address")
# Address_label.grid(row=3,column=0)

# City= Entry(root,width=30)
# City.grid(row=4,column=1)

# City_label=Label(root,text="City")
# City_label.grid(row=4,column=0)

# Zipcode= Entry(root,width=30)
# Zipcode.grid(row=5,column=1)

# Zipcode_label=Label(root,text="Zipcode")
# Zipcode_label.grid(row=5,column=0)

# Password= Entry(root,width=30)
# Password.grid(row=6,column=1)

# Password_label=Label(root,text="Password")
# Password_label.grid(row=6,column=0)

# Gender= Entry(root,width=30)
# Gender.grid(row=7,column=1)

# Gender_label=Label(root,text="Gender")
# Gender_label.grid(row=7,column=0)


# def submit():
    
#     conn = sqlite3.connect("Facebook.db")

#     #create cursor
#     c = conn.cursor()  #to execute queries on sqlite3

#     c.execute("INSERT INTO User VALUES (:FirstName, :LastName, :Age,:Address,:City,:Zipcode,:Password,:Gender)",{
#         'FirstName':First_name.get(),
#         'LastName':Last_name.get(),
#         'Age':Age.get(),
#         'Address':Address.get(),
#         'City':City.get(),
#         'Zipcode':Zipcode.get(),
#         'Password':Password.get(),
#         'Gender':Gender.get()
#     })
#     messagebox.showinfo("User", "insterted successfully")

#     conn.commit()
#     conn.close()

# def query():
#     conn= sqlite3.connect("Facebook.db")
#     c = conn.cursor()
#     c.execute("SELECT *,oid FROM User")

#     records = c.fetchall()
#     print(records)

#     # print_records=""
#     # for record in records:
#     #     print_records+=str(record[0])+" "+str(record[1])
#     # print(print_records)
#     conn.commit()
#     conn.close()

# def delete():
#     conn= sqlite3.connect("Facebook.db")
#     c = conn.cursor()
#     c.execute("DELETE from User WHERE oid ="+ delete_box.get())
#     print("deleted successfully")
#     conn.commit()
#     conn.close()

# def update():
#     conn=sqlite3.connect("Facebook.db")
#     c=conn.cursor()
#     record_id=delete_box.get()
        
#     c.execute("""UPDATE User SET
#     FirstName=:FirstName,
#     LastName=:LastName,
#     Age=:Age,
#     Address=:Address,
#     City=:City,
#     Zipcode=:Zipcode,
#     Password=:Password,
#     Gender=:Gender
#     WHERE oid=:oid""",
#     {'FirstName':First_name_editor.get(),
#      'LastName':Last_name_editor.get(),
#      'Age':Age_editor.get(),
#      'Address':Address_editor.get(),
#      'City':City_editor.get(),
#      'Zipcode':Zipcode_editor.get(),
#      'Password':Password_editor.get(),
#      'Gender':Gender_editor.get(),

#      'oid':record_id
    
    
#     })

#     conn.commit()
#     conn.close()
#     editor.destroy()


# def edit():
#     global editor
#     editor=Toplevel()
#     editor.title("Update data")
#     editor.geometry("500x500")

#     conn=sqlite3.connect("Facebook.db")
#     c= conn.cursor()
#     record_id=delete_box.get()
#     c.execute("SELECT * FROM User WHERE oid="+record_id)
#     records=c.fetchall()


#     global First_name_editor
#     global Last_name_editor
#     global Age_editor
#     global Address_editor
#     global City_editor
#     global Zipcode_editor
#     global Password_editor
#     global Gender_editor



    

#     First_name_editor= Entry(editor, width=30)
#     First_name_editor.grid(row=0,column=1,padx=20)

#     firstname_label= Label(editor,text="First Name")
#     firstname_label.grid(row=0,column=0)

#     Last_name_editor =Entry(editor,width=30)
#     Last_name_editor.grid(row=1,column=1)


#     lastname_label= Label(editor,text="Last Name")
#     lastname_label.grid(row=1,column=0)

#     Age_editor= Entry(editor,width=30)
#     Age_editor.grid(row=2,column=1)

#     Age_label=Label(editor,text="Age")
#     Age_label.grid(row=2,column=0)

#     Address_editor = Entry(editor,width=30)
#     Address_editor.grid(row=3,column=1)

#     Address_label=Label(editor,text="Address")
#     Address_label.grid(row=3,column=0)

#     City_editor= Entry(editor,width=30)
#     City_editor.grid(row=4,column=1)

#     City_label=Label(editor,text="City")
#     City_label.grid(row=4,column=0)

#     Zipcode_editor= Entry(editor,width=30)
#     Zipcode_editor.grid(row=5,column=1)

#     Zipcode_label=Label(editor,text="Zipcode")
#     Zipcode_label.grid(row=5,column=0)

#     Password_editor= Entry(editor,width=30)
#     Password_editor.grid(row=6,column=1)

#     Password_label=Label(editor,text="Password")
#     Password_label.grid(row=6,column=0)

#     Gender_editor= Entry(editor,width=30)
#     Gender_editor.grid(row=7,column=1)

#     Gender_label=Label(editor,text="Gender")
#     Gender_label.grid(row=7,column=0)

   



    
#     for record in records:
#         First_name_editor.insert(0,record[0])
#         Last_name_editor.insert(0,record[1])
#         Age_editor.insert(0,record[2])
#         Address_editor.insert(0,record[3])
#         City_editor.insert(0,record[4])
#         Zipcode_editor.insert(0,record[5])
#         Password_editor.insert(0,record[6])
#         Gender_editor.insert(0,record[7])
        




#     edit_btn=Button(editor,text="Save",command=update)
#     edit_btn.grid(row=8,column=1)

#     conn.commit()
#     conn.close()



# del_btn= Button(root,text="delete ID",command=delete)
# del_btn.grid(row=10,column=1)

# sub_btn= Button(root,text="Submit",command=submit)
# sub_btn.grid(row=11,column=1)

# query_btn=Button(root,text="show records",command=query)
# query_btn.grid(row=12,column=1)

# edit_btn=Button(root,text="update",command=edit)
# edit_btn.grid(row=13,column=1)



# conn.commit()

# conn.close()

# root.mainloop()

