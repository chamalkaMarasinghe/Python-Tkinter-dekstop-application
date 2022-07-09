from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk
import tkinter.ttk


def login():

    global root2
    global button_add_user
    global button_remove_user
    global button_change_password
    global button_add_new_product
    global button_view_user_information
    global button_display_product_information
    global button_display_full_inventory

    root1 = Tk()
    def check_username_password():

        legal_access = False
        manager = False

        connection = sqlite3.connect("inventory management system/user_details.db")
        cursor = connection.cursor()
        with connection:
            cursor.execute("""CREATE TABLE IF NOT EXISTS users(firstname TEXT, lastname TEXT, username TEXT, password TEXT, post TEXT)""")
            cursor.execute("""SELECT * FROM users""")
            results = cursor.fetchall()
        connection.close()

        username = user_name.get()
        password_ = password.get()

        for elements in results:
            if elements[2] == username and elements[3] == password_:
                legal_access = True
                if elements[4] == "true":
                    manager = True

        if username.lower() == "admin" and password_.lower() == "admin":
            legal_access = True
            manager = True

        if legal_access is True:
            if manager is True:
                manager_menu()

            elif manager is False:
                employee_menu()

        else:
            messagebox.showerror("Login Denied", "incorrect user name or password !")
            entry_username.delete(0, END)
            entry_password.delete(0, END)

    def manager_menu():

        global root2
        global button_add_user
        global button_remove_user
        global button_change_password
        global button_add_new_product
        global button_view_user_information
        global button_display_product_information
        global button_display_full_inventory

        root1.destroy()
        root2 = Tk()

        connection = sqlite3.connect('inventory management system/product_details.db')
        cursor = connection.cursor()
        with connection:
            cursor.execute("""CREATE TABLE IF NOT EXISTS products(id TEXT, name TEXT, price TEXT, stock TEXT)""")
        connection.close()

        # label_username.destroy()
        # entry_username.destroy()
        # label_password.destroy()
        # entry_password.destroy()
        # button_login.destroy()
        # button_exit.destroy()
        # login_frame.destroy()

        #root2.geometry("500x670")
        root2.title("Inventory Management System")
        root2.config(bg='#2B2B2B')
        root2.iconbitmap('inventory management system/Floppy Disk Red.ico')

        app_widths = 500
        app_heights = 670

        screen_widths = root2.winfo_screenwidth()
        screen_heights = root2.winfo_screenheight()

        xx = (screen_widths / 2) - (app_widths / 2)
        yy = (screen_heights / 2) - (app_heights / 2)

        root2.geometry(f"{app_widths}x{app_heights}+{int(xx)}+{int(yy)}")

        title_label = Label(root2, text='INVENTORY MANAGEMENT SYSTEM', fg='#06101c', bg='#27b4df', relief='flat', font=('arial', 18, 'bold'), highlightbackground='white')
        title_label.pack(fill=BOTH, padx=5, pady=25)

        img = Image.open('inventory management system/inventory-warehouse-stock-taking-png-favpng-tcBxjh7EfzEnm94pkErX8Rs7v.png')
        new_width = 260
        width, height = img.size
        ratio = height / width
        new_height = int(new_width * ratio)
        resized_image = img.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(resized_image)
        image_label = Label(image=photo, borderwidth=0)
        image_label.place(x=125, y=100)

        imga = Image.open(
            'inventory management system/6347be827195c69b6b988cb74d302721.jpg')
        new_widtha = 250
        widtha, heighta = imga.size
        ratioa = heighta / widtha
        new_heighta = int(new_widtha * ratioa)
        resized_imagea = imga.resize((new_widtha, new_heighta))
        photoa = ImageTk.PhotoImage(resized_imagea)
        image_label1 = Label(image=photoa, borderwidth=0)
        image_label1.place(x=-50, y=290)

        connection = sqlite3.connect('inventory management system/user_details.db')
        cursor = connection.cursor()
        with connection:
            cursor.execute("""SELECT * FROM users WHERE username= :given_un AND password= :given_pw""", {'given_un': user_name.get() ,'given_pw': password.get()})
            result = cursor.fetchall()
        connection.close()

        if user_name.get().lower() == 'admin' and password.get().lower() == 'admin':
            message = "WELCOME !"
        else:
            message = f"Welcome {result[0][0]} {result[0][1]} "

        manager_menu_frame = LabelFrame(root2, text=message, bg='#2B2B2B', fg='white', padx=40, pady=25)
        manager_menu_frame.place(x=85, y=320)

        button_add_user = Button(manager_menu_frame, text="Add User", width=30, relief='solid', font=("arial", 10, "bold"), command=add_user, activebackground='blue')
        #button_add_user.place(x=130, y=200)

        button_remove_user = Button(manager_menu_frame, text="Remove User", width=30, relief='solid',  font=("arial", 10, "bold"), command=remove_user, activebackground='blue')
        #button_remove_user.place(x=130, y=230)

        button_change_password = Button(manager_menu_frame, text="Change Password", width=30, relief='solid',  font=("arial", 10, "bold"), command=change_password, activebackground='blue')
        #button_change_password.place(x=130, y=260)

        button_add_new_product = Button(manager_menu_frame, text="Add New Product", width=30, relief='solid',  font=("arial", 10, "bold"), command=add_products, activebackground='blue')
        #button_add_new_product.place(x=130, y=290)

        button_view_user_information = Button(manager_menu_frame, text="View User Information", width=30, relief='solid',  font=("arial", 10, "bold"), command=view_users, activebackground='blue')
        #button_view_user_information.place(x=130, y=320)

        # button_delete_product = Button(root1, text="Delete Product", width=30, relief='solid',  font=("arial", 10, "bold"))
        # button_delete_product.place(x=130, y=350)

        button_display_product_information = Button(manager_menu_frame, text="Display Product Information", width=30, relief='solid', font=("arial", 10, "bold"), command=display_product_information, activebackground='blue')
        #button_display_product_information.place(x=130, y=350)

        button_display_full_inventory = Button(manager_menu_frame, text="Display Full Inventory", width=30, relief='solid',  font=("arial", 10, "bold"), command=lambda: display_full_inventory('manager'), activebackground='blue')
        #button_display_full_inventory.place(x=130, y=380)

        button_exit_ = Button(manager_menu_frame, text="Exit", width=30, relief='solid', font=("arial", 10, "bold"), command=root2.destroy, activebackground='blue')
        #button_exit_.place(x=130, y=410)

        blank_label = Label(manager_menu_frame, text='', bg='#2B2B2B', width=30)
        credit_label = Label(manager_menu_frame, text='Application by CHAMALKA MARASINGHE .', bg='#2B2B2B', fg='white')

        button_add_user.grid(row=0, column=0)
        button_remove_user.grid(row=1, column=0)
        button_change_password.grid(row=2, column=0)
        button_add_new_product.grid(row=3, column=0)
        button_view_user_information.grid(row=4, column=0)
        button_display_product_information.grid(row=5, column=0)
        button_display_full_inventory.grid(row=6, column=0)
        blank_label.grid(row=7, column=0)
        button_exit_.grid(row=8, column=0)
        credit_label.grid(row=9, column=0)

        # img = Image.open('inventory management system/207589.png')
        # new_width = 100
        # width, height = img.size
        # ratio = height / width
        # new_height = int(new_width * ratio)
        # resized_image = img.resize((new_width, new_height))
        # photo = ImageTk.PhotoImage(resized_image)
        # image_label = Label(image=photo)
        # image_label.pack()

        # bg2 = PhotoImage(file='inventory management system/207589.png')
        # lbl2 = Label(root1, image=bg2)
        # lbl2.place(x=10, y=10)

        root2.resizable(False, False)
        root2.mainloop()

    def employee_menu():

        global root2
        global button_add_user
        global button_remove_user
        global button_change_password
        global button_add_new_product
        global button_view_user_information
        global button_display_product_information
        global button_display_full_inventory

        root1.destroy()
        root2 = Tk()

        connection = sqlite3.connect('inventory management system/product_details.db')
        cursor = connection.cursor()
        with connection:
            cursor.execute("""CREATE TABLE IF NOT EXISTS products(id TEXT, name TEXT, price TEXT, stock TEXT)""")
        connection.close()

        # label_username.destroy()
        # entry_username.destroy()
        # label_password.destroy()
        # entry_password.destroy()
        # button_login.destroy()
        # button_exit.destroy()
        # login_frame.destroy()

        #root2.geometry("500x670")
        root2.title("Inventory Management System")
        root2.config(bg='#2B2B2B')
        root2.iconbitmap('inventory management system/Floppy Disk Red.ico')

        app_widths = 500
        app_heights = 670

        screen_widths = root2.winfo_screenwidth()
        screen_heights = root2.winfo_screenheight()

        xx = (screen_widths / 2) - (app_widths / 2)
        yy = (screen_heights / 2) - (app_heights / 2)

        root2.geometry(f"{app_widths}x{app_heights}+{int(xx)}+{int(yy)}")

        title_label = Label(root2, text='INVENTORY MANAGEMENT SYSTEM', fg='#06101c', bg='#27b4df', relief='flat',
                            font=('arial', 18, 'bold'))
        title_label.pack(fill=BOTH, padx=5, pady=25)

        img = Image.open(
            'inventory management system/inventory-warehouse-stock-taking-png-favpng-tcBxjh7EfzEnm94pkErX8Rs7v.png')
        new_width = 260
        width, height = img.size
        ratio = height / width
        new_height = int(new_width * ratio)
        resized_image = img.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(resized_image)
        image_label = Label(image=photo, borderwidth=0)
        image_label.place(x=125, y=100)

        imga = Image.open(
            'inventory management system/6347be827195c69b6b988cb74d302721.jpg')
        new_widtha = 250
        widtha, heighta = imga.size
        ratioa = heighta / widtha
        new_heighta = int(new_widtha * ratioa)
        resized_imagea = imga.resize((new_widtha, new_heighta))
        photoa = ImageTk.PhotoImage(resized_imagea)
        image_label1 = Label(image=photoa, borderwidth=0)
        image_label1.place(x=-50, y=290)

        connection = sqlite3.connect('inventory management system/user_details.db')
        cursor = connection.cursor()
        with connection:
            cursor.execute("""SELECT * FROM users WHERE username= :given_un AND password= :given_pw""",
                           {'given_un': user_name.get(), 'given_pw': password.get()})
            result = cursor.fetchall()
        connection.close()

        if user_name.get().lower() == 'admin' and password.get().lower() == 'admin':
            message = "WELCOME !"
        else:
            message = f"Welcome {result[0][0]} {result[0][1]} "

        employee_menu_frame = LabelFrame(root2, text=message, bg='#2B2B2B', fg='white', padx=40, pady=75)
        employee_menu_frame.place(x=85, y=320)

        button_change_password = Button(employee_menu_frame, text="Change Password", width=30, relief='solid',
                                        font=("arial", 10, "bold"), command=change_password, activebackground='blue')
        #button_change_password.place(x=130, y=290)

        button_display_product_information = Button(employee_menu_frame, text="Display Product Information", width=30, relief='solid',
                                                    font=("arial", 10, "bold"), command=display_product_information, activebackground='blue')
        #button_display_product_information.place(x=130, y=320)

        button_display_full_inventory = Button(employee_menu_frame, text="Display Full Inventory", width=30, relief='solid',
                                               font=("arial", 10, "bold"), command=lambda: display_full_inventory("employee"), activebackground='blue')
        #button_display_full_inventory.place(x=130, y=350)

        button_exit_ = Button(employee_menu_frame, text="Exit", width=30, relief='solid', font=("arial", 10, "bold"),
                              command=root2.destroy, activebackground='blue')
        #button_exit_.place(x=130, y=380)

        blank_label = Label(employee_menu_frame, text=' ', bg='#2B2B2B')
        credit_label = Label(employee_menu_frame, text='Application by CHAMALKA MARASINGHE', bg='#2B2B2B', fg='white')

        button_change_password.grid(row=0, column=0)
        button_display_product_information.grid(row=1, column=0)
        button_display_full_inventory.grid(row=2, column=0)
        blank_label.grid(row=3, column=0)
        button_exit_.grid(row=4, column=0)
        credit_label.grid(row=5, column=0)

        root2.resizable(False, False)
        root2.mainloop()

    def add_user():
        button_add_user['state'] = 'disabled'

        def close():
            add_user_window.destroy()
            button_add_user['state'] = 'normal'

        def function_to_add_user():

            first_name = fn.get()
            last_name = ln.get()
            username = un.get()
            pass_word = pw.get()

            if po.get() == 'Manager':
                post = 'true'
            else:
                post = 'false'

            entry_user_name.delete(0, END)
            entry_passwords.delete(0, END)
            entry_first_name.delete(0, END)
            entry_last_name.delete(0, END)

            allow_to_save = True
            connection = sqlite3.connect("inventory management system/user_details.db")
            cursor = connection.cursor()
            with connection:
                cursor.execute("""SELECT * FROM users""")
                results = cursor.fetchall()

            if username.lower() == 'admin' or pass_word.lower() == 'admin':
                allow_to_save = False

            for elements in results:
                if elements[2] == username or elements[3] == pass_word:
                    allow_to_save = False

            if allow_to_save is True:
                with connection:
                    cursor.execute("""INSERT INTO users VALUES(:firstname, :lastname, :username, :password, :post)""", {'firstname': first_name, 'lastname': last_name, 'username': username, 'password': pass_word, 'post': post})
                messagebox.showinfo("saved", 'Saved Successfully !')
            elif allow_to_save is False:
                messagebox.showerror("Used Details", 'Sorry! your details used before.try with another details. ')

            connection.close()

        add_user_window = Toplevel(root2)
        add_user_window.geometry("300x350")
        add_user_window.title("Add User")
        add_user_window.iconbitmap('inventory management system/Floppy Disk Red.ico')


        fn = StringVar()
        ln = StringVar()
        un = StringVar()
        pw = StringVar()
        po = StringVar()

        label_first_name = Label(add_user_window, text="First Name :", font=("arial", 10, 'bold'))
        label_first_name.place(x=15, y=50+60)

        entry_first_name = tkinter.ttk.Entry(add_user_window, textvar=fn, width=30)
        entry_first_name.place(x=105, y=54+60)

        label_last_name = Label(add_user_window, text="Last Name :", font=("arial", 10, 'bold'))
        label_last_name.place(x=15, y=80+60)

        entry_last_name = tkinter.ttk.Entry(add_user_window, textvar=ln, width=30)
        entry_last_name.place(x=105, y=84+60)

        label_user_name = Label(add_user_window, text="User Name :", font=("arial", 10, 'bold'))
        label_user_name.place(x=15, y=110+60)

        entry_user_name = tkinter.ttk.Entry(add_user_window, textvar=un, width=30)
        entry_user_name.place(x=105, y=114+60)

        label_passwords = Label(add_user_window, text="Password  :", font=("arial", 10, 'bold'))
        label_passwords.place(x=15, y=140+60)

        entry_passwords = tkinter.ttk.Entry(add_user_window, textvar=pw, width=30)
        entry_passwords.place(x=105, y=144+60)

        post_list = ["Manager", "Employee"]
        drop_list = OptionMenu(add_user_window, po, *post_list)
        po.set("Manager or Employee ?")
        drop_list.config(width=20)
        drop_list.config(relief='solid')
        drop_list.place(x=15, y=230)

        styl_e = tkinter.ttk.Style()
        styl_e.configure('W.TButton', background='orange')

        button_save = tkinter.ttk.Button(add_user_window, text='  Save  ', width=15, style='W.TButton', command=function_to_add_user)
        button_save.place(x=100, y=230+60)

        add_user_frame = LabelFrame(add_user_window, text='ADD USER', padx=10, pady=10)
        add_user_frame.place(x=50, y=50)

        add_user_window.resizable(False, False)
        add_user_window.protocol("WM_DELETE_WINDOW", close)
        add_user_window.mainloop()

    def change_password():
        button_change_password['state'] = 'disabled'

        def close():
            change_password_window.destroy()
            button_change_password['state'] = 'normal'

        def function_to_change_password():

            legal_update = True

            if password.get() == current.get():
                if new.get() == confirm.get():

                    connection = sqlite3.connect("inventory management system/user_details.db")
                    cursor = connection.cursor()

                    with connection:
                        cursor.execute("""SELECT * FROM users WHERE password = :new_password""", {'new_password': new.get()})
                        results = cursor.fetchall()

                    if len(results) != 0:
                        legal_update = False

                    if legal_update is True:
                        with connection:
                            cursor.execute("""UPDATE users SET password = :new_password WHERE password = :current_password """, {'new_password': new.get(), 'current_password': current.get()})

                        messagebox.showinfo("Success", "Password Updated Successfully ! You must re-login.")

                        entry_current_password.delete(0, END)
                        entry_new_password.delete(0, END)
                        entry_confirm_password.delete(0, END)
                        change_password_window.destroy()
                        root2.destroy()

                    elif legal_update is False:

                        messagebox.showerror("Error", "Your new password already in use !")
                        entry_new_password.delete(0, END)
                        entry_confirm_password.delete(0, END)

                    connection.close()

                elif new.get() != confirm.get():
                    messagebox.showerror('Error', 'Confirm your password !')
                    entry_confirm_password.delete(0, END)

            elif password.get() != current.get():

                entry_current_password.delete(0, END)
                entry_new_password.delete(0, END)
                entry_confirm_password.delete(0, END)
                messagebox.showerror("Error", "Incorrect Password !")

        change_password_window = Toplevel(root2)
        change_password_window.title("Change Password")
        change_password_window.geometry("300x200")
        change_password_window.iconbitmap('inventory management system/Floppy Disk Red.ico')

        current = StringVar()
        new = StringVar()
        confirm = StringVar()

        label_current_password = Label(change_password_window, text="Current : ", width=10, font=('arial', 10, 'bold'))
        label_current_password.place(x=1, y=20)

        entry_current_password = tkinter.ttk.Entry(change_password_window, textvar=current, show='#', width=35)
        entry_current_password.place(x=75, y=24)

        label_new_password = Label(change_password_window, text="New : ", width=10, font=('arial', 10, 'bold'))
        label_new_password.place(x=1, y=50)

        entry_new_password = tkinter.ttk.Entry(change_password_window, textvar=new, show='#', width=35)
        entry_new_password.place(x=75, y=54)

        label_confirm_password = Label(change_password_window, text="Confirm : ", width=10, font=('arial', 10, 'bold'))
        label_confirm_password.place(x=1, y=80)

        entry_confirm_password = tkinter.ttk.Entry(change_password_window, textvar=confirm, show='#', width=35)
        entry_confirm_password.place(x=75, y=84)

        sty_le = tkinter.ttk.Style()
        sty_le.configure("W.TButton", background='orange')

        button_change_password_ = tkinter.ttk.Button(change_password_window, text="Apply", width=9, style='W.TButton', command=function_to_change_password)
        button_change_password_.place(x=115, y=134)

        change_password_window.resizable(False, False)
        change_password_window.protocol("WM_DELETE_WINDOW", close)
        change_password_window.mainloop()

    def view_users():
        button_view_user_information['state'] = 'disabled'

        def close():
            view_users_window.destroy()
            button_view_user_information['state'] = 'normal'

        view_users_window = Toplevel(root2)
        view_users_window.title("View Users")
        view_users_window.geometry("1300x600")
        view_users_window.iconbitmap('inventory management system/Floppy Disk Red.ico')

        imgwz = Image.open(
            'inventory management system/eagle.png')
        new_widthwz = 1300
        widthwz, heightwz = imgwz.size
        ratiowz = heightwz / widthwz
        new_heightwz = int(new_widthwz * ratiowz)
        resized_imagewz = imgwz.resize((new_widthwz, new_heightwz))
        photowz = ImageTk.PhotoImage(resized_imagewz)
        image_labelwz = Label(view_users_window, image=photowz, borderwidth=0)
        image_labelwz.place(x=0, y=0)

        view_users_frame = LabelFrame(view_users_window)
        view_users_frame.pack()

        my_style = ttk.Style()
        my_style.configure('Treeview', rowheight=30)
        my_style.map('Treeview', background=[('selected', 'blue')])

        scroll_bar = Scrollbar(view_users_frame)
        scroll_bar.pack(side=RIGHT, fill=Y)

        user_details_table = ttk.Treeview(view_users_frame, columns=(1, 2, 3, 4, 5), height=35, show='headings', yscrollcommand=scroll_bar.set)
        user_details_table.pack(fill=BOTH, padx=2, pady=2)
        scroll_bar.config(command=user_details_table.yview)

        user_details_table.heading(1, text='First Name')
        user_details_table.heading(2, text='Last Name')
        user_details_table.heading(3, text='User Name')
        user_details_table.heading(4, text='Password')
        user_details_table.heading(5, text='Post')

        my_connection = sqlite3.connect('inventory management system/user_details.db')
        my_cursor = my_connection.cursor()
        with my_connection:
            my_cursor.execute("""SELECT * FROM users""")
            result = my_cursor.fetchall()
        my_connection.close()

        details_list = [[j for j in i]for i in result]

        for i in details_list:
            if i[4] == 'true':
                i[4] = 'Manager'

            if i[4] == 'false':
                i[4] = 'Employee'

            if i[4] == 'Manager':
                i[3] = '*****'

        #for element in details_list:
        #    user_details_table.insert('', 'end', values=element)

        user_details_table.tag_configure("oddrow", background='white')
        user_details_table.tag_configure("evenrow", background='#a76912')

        count = 0
        for element in details_list:
            if count % 2 == 0:
                user_details_table.insert('', 'end', values=element, tag=("evenrow",))
            else:
                user_details_table.insert('', 'end', values=element, tag=("oddrow",))
            count += 1

        view_users_window.resizable(False, False)
        view_users_window.protocol("WM_DELETE_WINDOW", close)
        view_users_window.mainloop()

    def remove_user():
        button_remove_user['state'] = 'disabled'

        def close():
            remove_user_window.destroy()
            button_remove_user['state'] = 'normal'

        def function_to_remove_user():

            response = messagebox.askyesno("Are You Sure ?", 'Are you sure ?')

            if response is True:
                connection = sqlite3.connect("inventory management system/user_details.db")
                cursor = connection.cursor()
                with connection:
                    cursor.execute("""SELECT * FROM users WHERE username = :user_name AND password = :pass_word""", {'user_name': user__name.get(), 'pass_word': pass__word.get()})
                    results = cursor.fetchall()

                if len(results) != 0:
                    with connection:
                        cursor.execute("""DELETE from users WHERE username = :user_name AND password = :pass_word""", {'user_name': user__name.get(), 'pass_word': pass__word.get()})
                    connection.close()

                    messagebox.showinfo("successfully", "Removed successfully !")

                    if user__name.get() == user_name.get() and pass__word.get() == password.get():
                        remove_user_window.destroy()
                        root2.destroy()

                    entry_user__name.delete(0, END)
                    entry_pass__word.delete(0, END)

                elif len(results) == 0:
                    messagebox.showerror("Error", "Could not find any results to delete !")
                    entry_user__name.delete(0, END)
                    entry_pass__word.delete(0, END)

            elif response is False:
                entry_user__name.delete(0, END)
                entry_pass__word.delete(0, END)

        remove_user_window = Toplevel(root2)
        remove_user_window.title("Remove User")
        remove_user_window.geometry("350x200")
        remove_user_window.iconbitmap('inventory management system/Floppy Disk Red.ico')

        user__name = StringVar()
        pass__word = StringVar()

        label_user__name = Label(remove_user_window, text='Username : ', width=10, font=('arial', 10, 'bold'))
        label_user__name.place(x=10, y=20)

        entry_user__name = tkinter.ttk.Entry(remove_user_window, textvar=user__name, width=35)
        entry_user__name.place(x=95, y=20)

        label_pass__word = Label(remove_user_window, text='Password : ', width=10, font=('arial', 10, 'bold'))
        label_pass__word.place(x=10, y=50)

        entry_pass__word = tkinter.ttk.Entry(remove_user_window, textvar=pass__word,  width=35)
        entry_pass__word.place(x=95, y=54)

        s_tyle = tkinter.ttk.Style()
        s_tyle.configure("W.TButton", background='orange')

        button_remove = tkinter.ttk.Button(remove_user_window, text='Remove', width=8, style='W.TButton', command=function_to_remove_user)
        button_remove.place(x=130, y=134)

        remove_user_window.resizable(False, False)
        remove_user_window.protocol("WM_DELETE_WINDOW", close)
        remove_user_window.mainloop()

    def add_products():
        button_add_new_product['state'] = 'disabled'

        def close():
            add_product_window.destroy()
            button_add_new_product['state'] = 'normal'

        def function_to_add_product():
            if p_i_d.get() != '' and p_name.get() != '' and p_price.get() != '' and p_stock.get() != '':
                allow_to_add = True

                connection = sqlite3.connect('inventory management system/product_details.db')
                cursor = connection.cursor()
                with connection:
                    cursor.execute("""SELECT * FROM products""")
                    results = cursor.fetchall()

                for element in results:
                    if p_i_d.get() == element[0]:
                        allow_to_add = False

                if allow_to_add is True:

                    with connection:
                        cursor.execute("""INSERT INTO products VALUES(:i_d, :name, :price, :stock)""", {'i_d': p_i_d.get(), 'name': p_name.get(), 'price': p_price.get(), 'stock': p_stock.get()})
                    connection.close()

                    entry_product_id.delete(0, END)
                    entry_product_name.delete(0, END)
                    entry_product_price.delete(0, END)
                    entry_product_stock.delete(0, END)

                    messagebox.showinfo("Done", "Successfully added into inventory !")

                elif allow_to_add is False:
                    messagebox.showerror("Error", "Product ID has been used before !")
                    entry_product_id.delete(0, END)

            elif p_i_d.get() == '' or p_name.get() == '' or p_price.get() == '' or p_stock.get() == '':
                messagebox.showerror("Empty Blocks", "Fill all blocks before add to inventory !")

        add_product_window = Toplevel(root2)
        add_product_window.title("Add Products")
        add_product_window.geometry("310x350")
        add_product_window.iconbitmap('inventory management system/Floppy Disk Red.ico')

        p_i_d = StringVar()
        p_name = StringVar()
        p_price = StringVar()
        p_stock = StringVar()

        label_product_id = Label(add_product_window, text="Product ID       :", font=("arial", 10, 'bold'))
        label_product_id.place(x=5, y=50 + 60)

        entry_product_id = tkinter.ttk.Entry(add_product_window, textvar=p_i_d, width=30)
        entry_product_id.place(x=115, y=54 + 60)

        label_product_name = Label(add_product_window, text="Product Name :", font=("arial", 10, 'bold'))
        label_product_name.place(x=5, y=80 + 60)

        entry_product_name = tkinter.ttk.Entry(add_product_window, textvar=p_name, width=30)
        entry_product_name.place(x=115, y=84 + 60)

        label_product_price = Label(add_product_window, text="Product Price  :", font=("arial", 10, 'bold'))
        label_product_price.place(x=5, y=110 + 60)

        entry_product_price = tkinter.ttk.Entry(add_product_window, textvar=p_price, width=30)
        entry_product_price.place(x=115, y=114 + 60)

        label_product_stock = Label(add_product_window, text="Product Stock  :", font=("arial", 10, 'bold'))
        label_product_stock.place(x=5, y=140 + 60)

        entry_product_stock= tkinter.ttk.Entry(add_product_window, textvar=p_stock, width=30)
        entry_product_stock.place(x=115, y=144 + 60)

        styl_e_ = tkinter.ttk.Style()
        styl_e_.configure('W.TButton', background='orange')

        button_save = tkinter.ttk.Button(add_product_window, text='  Add To Inventory  ', width=21, style='W.TButton', command=function_to_add_product)
        button_save.place(x=80, y=230 + 60)

        add_product_window.resizable(False, False)
        add_product_window.protocol("WM_DELETE_WINDOW", close)
        add_product_window.mainloop()

    def display_full_inventory(post):
        button_display_full_inventory['state'] = 'disabled'

        def close():
            display_full_entry_window.destroy()
            button_display_full_inventory['state'] = 'normal'

        def delete_product_function():

            def delete():

                connections = sqlite3.connect('inventory management system/product_details.db')
                cursors = connections.cursor()
                with connections:
                    cursors.execute("""SELECT * FROM products""")
                    result = cursors.fetchall()

                found_item = False
                for elements in result:
                    if elements[0] == id_num.get():
                        found_item = True

                if found_item is True:

                    response = messagebox.askyesno("Are you sure ?", "Are you want to delete ?")

                    if response is True:

                        with connections:
                            cursors.execute("""DELETE from products WHERE id = :product_id""", {'product_id': id_num.get()})
                        messagebox.showinfo("Deleted Successfully", "Deleted Successfully !")
                        entry_id.delete(0, END)

                        with connections:
                            cursors.execute("""SELECT * FROM products""")
                            result_after_delete = cursors.fetchall()

                        for record in details_table.get_children():
                            details_table.delete(record)

                        #for line in result_after_delete:
                        #    details_table.insert('', 'end', values=line)
                        details_table.tag_configure("oddrow", background='white')
                        details_table.tag_configure("evenrow", background='#a76912')

                        count_n = 0
                        for element_n in result_after_delete:
                            if count_n % 2 == 0:
                                details_table.insert('', 'end', values=element_n, tag=("evenrow",))
                            else:
                                details_table.insert('', 'end', values=element_n, tag=("oddrow",))
                            count_n += 1

                    elif response is False:
                        entry_id.delete(0, END)

                elif found_item is False:

                    messagebox.showerror("Error", "There are no specified Product in the inventory !")
                    entry_id.delete(0, END)

                connections.close()

            delete_product_window = Toplevel(display_full_entry_window)
            delete_product_window.title("Delete Product")
            delete_product_window.geometry('300x100')
            delete_product_window.iconbitmap('inventory management system/Floppy Disk Red.ico')

            id_num = StringVar()

            label_id = Label(delete_product_window, text='Product ID : ')
            label_id.place(x=10, y=30)

            entry_id = tkinter.ttk.Entry(delete_product_window, textvar=id_num, width=30)
            entry_id.place(x=80, y=32)

            styles = tkinter.ttk.Style()
            styles.configure("W.TButton", background='orange')

            button_to_delete = tkinter.ttk.Button(delete_product_window, text='Delete', width=13, style='W.TButton', command=delete)
            button_to_delete.place(x=100, y=58)

            delete_product_window.resizable(False, False)
            delete_product_window.mainloop()

        def update_product_function_manager():

            def verify():

                my_connection = sqlite3.connect('inventory management system/product_details.db')
                my_cursor = my_connection.cursor()
                with my_connection:
                    my_cursor.execute("""SELECT * FROM products WHERE id = :given_id""", {'given_id': confirm_id.get()})
                    my_result = my_cursor.fetchall()

                if len(my_result) != 0:
                    new_id.set(my_result[0][0])
                    new_name.set(my_result[0][1])
                    new_price.set(my_result[0][2])
                    new_stock.set(my_result[0][3])

                elif len(my_result) == 0:

                    messagebox.showerror("Error", 'There is no specified product in the inventory !')
                    entry_confirm_id.delete(0, END)
                    entry_new_price.delete(0, END)
                    entry_new_stock.delete(0, END)
                    entry_new_name.delete(0, END)
                    entry_new_id.delete(0, END)

                my_connection.close()

            def update():

                allow_to_update = True
                my_connection = sqlite3.connect('inventory management system/product_details.db')
                my_cursor = my_connection.cursor()
                with my_connection:
                    my_cursor.execute("""SELECT * FROM products""")
                    my_results = my_cursor.fetchall()

                for elements in my_results:
                    if elements[0] == confirm_id.get():
                        my_results.remove(elements)

                for elements in my_results:
                    if elements[0] == new_id.get():
                        allow_to_update = False

                if allow_to_update is True:
                    with my_connection:
                        my_cursor.execute("""UPDATE products SET id = :given_id, name = :given_name, price = :given_price, stock = :given_stock WHERE id =:confirmed_id """, {'given_id': new_id.get(), 'given_name': new_name.get(), 'given_price': new_price.get(), 'given_stock': new_stock.get(), 'confirmed_id': confirm_id.get()})
                    messagebox.showinfo("Successfully Updated", 'Successfully Updated !')

                    with my_connection:
                        my_cursor.execute("""SELECT * FROM products""")
                        result_after_update = my_cursor.fetchall()

                    for record in details_table.get_children():
                        details_table.delete(record)

                    #for line in result_after_update:
                    #    details_table.insert('', 'end', values=line)
                    details_table.tag_configure("oddrow", background='white')
                    details_table.tag_configure("evenrow", background='#a76912')

                    counts = 0
                    for elements in result_after_update:
                        if counts % 2 == 0:
                            details_table.insert('', 'end', values=elements, tag=("evenrow",))
                        else:
                            details_table.insert('', 'end', values=elements, tag=("oddrow",))
                        counts += 1

                    entry_confirm_id.delete(0, END)
                    entry_new_id.delete(0, END)
                    entry_new_name.delete(0, END)
                    entry_new_price.delete(0, END)
                    entry_new_stock.delete(0, END)

                elif allow_to_update is False:

                    messagebox.showerror("Error", 'Your new product ID has been used before !')
                    entry_new_id.delete(0, END)

                my_connection.close()

            update_product_window = Toplevel(display_full_entry_window)
            update_product_window.geometry("300x350")
            update_product_window.title("Update Product")
            update_product_window.iconbitmap('inventory management system/Floppy Disk Red.ico')

            new_id = StringVar()
            new_name = StringVar()
            new_price = StringVar()
            new_stock = StringVar()
            confirm_id = StringVar()

            styles = tkinter.ttk.Style()
            styles.configure('W.TButton', background='orange', borderwidth=5)

            label_confirm_id = Label(update_product_window, text="Confirm ID   ", font=("arial", 10, 'bold'))
            label_confirm_id.place(x=15, y=20)

            entry_confirm_id = tkinter.ttk.Entry(update_product_window, textvar=confirm_id, width=30)
            entry_confirm_id.place(x=15, y=50)

            button_confirm_id = tkinter.ttk.Button(update_product_window, text='Verify', width=10, style='W.TButton', command=verify)
            button_confirm_id.place(x=210, y=47)

            label_new_id = Label(update_product_window, text="New ID       :", font=("arial", 10, 'bold'))
            label_new_id.place(x=15, y=50 + 60)

            entry_new_id = tkinter.ttk.Entry(update_product_window, textvar=new_id, width=30)
            entry_new_id.place(x=105, y=54 + 60)

            label_new_name = Label(update_product_window, text="New Name :", font=("arial", 10, 'bold'))
            label_new_name.place(x=15, y=80 + 60)

            entry_new_name = tkinter.ttk.Entry(update_product_window, textvar=new_name, width=30)
            entry_new_name.place(x=105, y=84 + 60)

            label_new_price = Label(update_product_window, text="New Price  :", font=("arial", 10, 'bold'))
            label_new_price.place(x=15, y=110 + 60)

            entry_new_price = tkinter.ttk.Entry(update_product_window, textvar=new_price, width=30)
            entry_new_price.place(x=105, y=114 + 60)

            label_new_stock = Label(update_product_window, text="New Stock  :", font=("arial", 10, 'bold'))
            label_new_stock.place(x=15, y=140 + 60)

            entry_new_stock = tkinter.ttk.Entry(update_product_window, textvar=new_stock, width=30)
            entry_new_stock.place(x=105, y=144 + 60)

            button_update = tkinter.ttk.Button(update_product_window, text='  Update  ', width=15, style='W.TButton', command=update)
            button_update.place(x=100, y=230 + 60)

            update_product_window.resizable(False, False)
            update_product_window.mainloop()

        def update_stock():

            def confirmation():
                allow_to_update = True
                my_connection = sqlite3.connect('inventory management system/product_details.db')
                my_cursor = my_connection.cursor()
                with my_connection:
                    my_cursor.execute("""SELECT * FROM products WHERE id =:given_id""", {'given_id': id_num.get()})
                    result = my_cursor.fetchall()
                my_connection.close()

                if len(result) != 0:

                    new_stock.set(result[0][3])

                elif len(result) == 0:

                    messagebox.showerror("Error", "There is no specified item in inventory !")
                    entry_id.delete(0, END)

                my_connection.close()

            def update_stock_function():
                my_connection = sqlite3.connect('inventory management system/product_details.db')
                my_cursor = my_connection.cursor()

                with my_connection:
                    my_cursor.execute("""UPDATE products SET stock= :given_stock WHERE id =:given_id """, {'given_stock': new_stock.get(), 'given_id': id_num.get()})

                messagebox.showinfo("Successfully Updated", "Successfully Updated !")
                entry_new_stock.delete(0, END)

                for record in details_table.get_children():
                   details_table.delete(record)

                with my_connection:
                    my_cursor.execute("""SELECT * FROM products""")
                    result = my_cursor.fetchall()

                #for elements in result:
                #    details_table.insert('', 'end', values=elements)
                details_table.tag_configure("oddrow", background='white')
                details_table.tag_configure("evenrow", background='#a76912')

                count_ = 0
                for element_ in result:
                    if count_ % 2 == 0:
                        details_table.insert('', 'end', values=element_, tag=("evenrow",))
                    else:
                        details_table.insert('', 'end', values=element_, tag=("oddrow",))
                    count_ += 1

                my_connection.close()

            update_stock_window = Toplevel(display_full_entry_window)
            update_stock_window.title("Update Stock")
            update_stock_window.geometry('360x150')
            update_stock_window.iconbitmap('inventory management system/Floppy Disk Red.ico')

            id_num = StringVar()
            new_stock = StringVar()

            label_id = Label(update_stock_window, text='Product ID : ')
            label_id.place(x=10, y=30)

            entry_id = tkinter.ttk.Entry(update_stock_window, textvar=id_num, width=30)
            entry_id.place(x=80, y=32)

            styles = tkinter.ttk.Style()
            styles.configure('W.TButton', background='orange', borderwidth=5)

            button_confirm = tkinter.ttk.Button(update_stock_window, width=7, text='Verify', style='W.TButton', command=confirmation)
            button_confirm.place(x=270, y=30)

            label_new_stock = Label(update_stock_window, text="New Stock : ")
            label_new_stock.place(x=10, y=54+10+5)

            entry_new_stock = tkinter.ttk.Entry(update_stock_window, textvar=new_stock, width=30)
            entry_new_stock.place(x=80, y=62+10)

            button_update_stock = tkinter.ttk.Button(update_stock_window, text='Update', width=13, style='W.TButton', command=update_stock_function)
            button_update_stock.place(x=100, y=58+60)

            update_stock_window.resizable(False, False)
            update_stock_window.mainloop()

        display_full_entry_window = Toplevel(root2)
        display_full_entry_window.title("Inventory")
        display_full_entry_window.geometry("1300x600")
        display_full_entry_window.iconbitmap('inventory management system/Floppy Disk Red.ico')

        imgw = Image.open(
            'inventory management system/eagle.png')
        new_widthw = 1300
        widthw, heightw = imgw.size
        ratiow = heightw / widthw
        new_heightw = int(new_widthw * ratiow)
        resized_imagew = imgw.resize((new_widthw, new_heightw))
        photow = ImageTk.PhotoImage(resized_imagew)
        image_labelw = Label(display_full_entry_window, image=photow, borderwidth=0)
        image_labelw.place(x=0, y=0)

        full_inventory_frame = LabelFrame(display_full_entry_window)
        full_inventory_frame.pack()

        my_style = ttk.Style()
        my_style.configure('Treeview', rowheight=30)
        my_style.map('Treeview', background=[('selected', 'blue')])

        scroll_y = Scrollbar(full_inventory_frame)
        scroll_y.pack(side=RIGHT, fill=Y)

        connection = sqlite3.connect('inventory management system/product_details.db')
        cursor = connection.cursor()
        with connection:
            cursor.execute("SELECT * FROM products")
            results = cursor.fetchall()
        connection.close()

        details_table = ttk.Treeview(full_inventory_frame, column=(1, 2, 3, 4), show='headings', height=35, yscrollcommand=scroll_y.set)
        details_table.pack(fill=BOTH, pady=2, padx=2)

        scroll_y.config(command=details_table.yview)

        if post == 'manager':

            button_delete = tkinter.ttk.Button(display_full_entry_window, text='Delete Product', width=20, command=delete_product_function)
            button_delete.place(x=1100, y=550)

            button_update_product = tkinter.ttk.Button(display_full_entry_window, text='Update', width=20, command=update_product_function_manager)
            button_update_product.place(x=1100, y=500)

        if post == 'employee':

            button_delete = tkinter.ttk.Button(display_full_entry_window, text='Update Stock', width=20, command=update_stock)
            button_delete.place(x=1100, y=500)

        details_table.heading(1, text='Product ID')
        details_table.heading(2, text='Product Name')
        details_table.heading(3, text='Product Price(RS)')
        details_table.heading(4, text='Available Stock')

        details_table.tag_configure("oddrow", background='white')
        details_table.tag_configure("evenrow", background='#a76912')

        count = 0
        for element in results:
            if count % 2 == 0:
                details_table.insert('', 'end', values=element, tag=("evenrow",))
            else:
                details_table.insert('', 'end', values=element, tag=("oddrow",))
            count += 1

        display_full_entry_window.resizable(False, False)
        display_full_entry_window.protocol("WM_DELETE_WINDOW", close)
        display_full_entry_window.mainloop()

    def display_product_information():
        button_display_product_information['state'] = 'disabled'

        def close():
            display_product_information_window.destroy()
            button_display_product_information['state'] = 'normal'

        def function_display_product_information():

            for records in details_table.get_children():
                details_table.delete(records)

            connection = sqlite3.connect('inventory management system/product_details.db')
            cursor = connection.cursor()

            with connection:
                cursor.execute("""SELECT * FROM products""")
                results = cursor.fetchall()

            connection.close()

            #for records in results:
            #    if entery_search.get().lower() in records[1].lower():
            #        details_table.insert('', 'end', values=records)

            details_table.tag_configure("oddrow", background='white')
            details_table.tag_configure("evenrow", background='#a76912')

            count = 0
            for records in results:
                if entery_search.get().lower() in records[1].lower():
                    if count % 2 == 0:
                        details_table.insert('', 'end', values=records, tag=("evenrow",))
                    else:
                        details_table.insert('', 'end', values=records, tag=("oddrow",))
                    count += 1

        display_product_information_window = Toplevel(root2)
        display_product_information_window.title("Search Products")
        display_product_information_window.geometry("1300x600")
        display_product_information_window.iconbitmap('inventory management system/Floppy Disk Red.ico')

        imgwa = Image.open(
            'inventory management system/eagle.png')
        new_widthwa = 1300
        widthwa, heightwa = imgwa.size
        ratiowa = heightwa / widthwa
        new_heightwa = int(new_widthwa * ratiowa)
        resized_imagewa = imgwa.resize((new_widthwa, new_heightwa))
        photowa = ImageTk.PhotoImage(resized_imagewa)
        image_labelwa = Label(display_product_information_window, image=photowa, borderwidth=0)
        image_labelwa.place(x=0, y=0)

        search = StringVar()

        display_product_information_frame = LabelFrame(display_product_information_window)
        display_product_information_frame.pack()

        my_style = ttk.Style()
        my_style.configure('Treeview', rowheight=30)
        my_style.map('Treeview', background=[('selected', 'blue')])

        scroll_y = Scrollbar(display_product_information_frame)
        scroll_y.pack(side=RIGHT, fill=Y)

        #scroll_bar = Scrollbar(display_product_information_window)
        #scroll_bar.pack(side=RIGHT, fill=Y)

        details_table = ttk.Treeview(display_product_information_frame, column=(1, 2, 3, 4), show='headings', height=35, yscrollcommand=scroll_y.set)
        details_table.pack(fill=BOTH, pady=2, padx=2)

        scroll_y.config(command=details_table.yview)

        details_table.heading(1, text='Product ID')
        details_table.heading(2, text='Product Name')
        details_table.heading(3, text='Product Price(RS)')
        details_table.heading(4, text='Available Stock')

        entery_search = tkinter.ttk.Entry(display_product_information_window, textvar=search, width=30)
        entery_search.place(x=15, y=30)

        s = tkinter.ttk.Style()
        s.configure("W.TButton", background='orange')

        button_search = tkinter.ttk.Button(display_product_information_window, width=20, text='search', style='W.TButton', command=function_display_product_information)
        button_search.place(x=15, y=70)

        display_product_information_window.resizable(False, False)
        display_product_information_window.protocol("WM_DELETE_WINDOW", close)
        display_product_information_window.mainloop()

    #root1.title("Log in")
    #root1.geometry("900x500")
    #root1.iconbitmap('inventory management system/Floppy Disk Red.ico')
    user_name = StringVar()
    password = StringVar()

    app_width = 800
    app_height = 500

    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root1.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
    root1.overrideredirect(1)

    img = Image.open(
        'inventory management system/20426064.png')
    new_width = 800
    width, height = img.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = img.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(resized_image)
    image_label = Label(image=photo, borderwidth=0)
    image_label.place(x=0, y=0)

    login_frame = LabelFrame(root1, bg='#b06d1f', highlightbackground='white', padx=20, pady=50)
    #login_frame.place(x=10+500+60, y=10+250-10)

    label_username = Label(login_frame, text="Username : ", bg='#b06d1f', font=("arial", 10, 'bold'))
    #label_username.place(x=30, y=40)

    entry_username = Entry(root1, textvar=user_name, width=30, borderwidth=0)
    #entry_username.place(x=130, y=44)

    label_password = Label(login_frame, text="Password  : ", bg='#b06d1f', font=("arial", 10, 'bold'))
    #label_password.place(x=30, y=80)

    entry_password = Entry(root1, textvar=password, show='#', width=30, borderwidth=0)
    #entry_password.place(x=130, y=84)

    #button_login = Button(root1, text="Login", bg="#fecb18", width=10, borderwidth=0, font=('arial', 10, 'bold'), command=check_username_password)
    style = tkinter.ttk.Style()
    style.configure('W.TButton', background='orange', borderwidth=5)
    button_login = tkinter.ttk.Button(root1, text="Login", style='W.TButton', command=check_username_password)
    button_login.place(x=100+550-130, y=124+40+24+270-20)

    button_exit = tkinter.ttk.Button(root1, text="Exit", style='W.TButton', command=root1.destroy)
    button_exit.place(x=220+550-130, y=124+40+24+270-20)
    #
    blank_label = Label(login_frame, text=" ", bg='#b06d1f')
    #
    label_username.grid(row=0, column=0)
    blank_label.grid(row=2, column=0)
    entry_username.place(x=100+550-130-35+30, y=124+40+24+270-20-100-30+30)
    label_password.grid(row=3, column=0)
    #blank_label.grid(row=1, column=0)
    entry_password.place(x=100+550-130-35+30+3, y=124+40+24+270-20-70+30+4)

    root1.resizable(False, False)
    root1.mainloop()

#root1 = Tk()

login()

#root1.resizable(False, False)
#root1.mainloop()
