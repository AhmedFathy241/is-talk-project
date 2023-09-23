import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
from homepage import Home


class Stack:
    items = []

    def __int__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return None if self.is_empty() else self.items.pop()

    def peek(self):
        return None if self.is_empty() else self.items[-1]


class LoginPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login Page")
        self.root.geometry("1000x850")
        self.root.configure(background='white')

        self.logo = tk.PhotoImage(file='logo1.png')
        self.logo_lab = tk.Label(self.root, image=self.logo, bg="white")
        self.logo_lab.place(x=200, y=150)

        self.userLogo_label = tk.Label(
            self.root, text="is talk", font="Impact 65 bold", fg="#EB496F", bg="white")
        self.userLogo_label.place(x=500, y=0)

        self.userLogin_label = tk.Label(
            self.root, text="Login Here", font="Impact 35 bold", fg="#EB496F", bg="white")
        self.userLogin_label.place(x=90, y=100)

        self.userEmail_label = tk.Label(
            self.root, text="Email", font="Arial 15 bold", bg="white")
        self.userEmail_label.place(x=90, y=180)

        self.userEmail = tk.Entry(self.root, font="Arial 12", bg="gray90")
        self.userEmail.place(x=90, y=210)

        self.userPassword_label = tk.Label(
            self.root, text="Password", font="Arial 15 bold", bg="white")
        self.userPassword_label.place(x=90, y=280)

        self.userPassword = tk.Entry(self.root, font="Arial 12", show="*", bg='gray90')
        self.userPassword.place(x=90, y=310)

        self.login_button = tk.Button(
            self.root, text='Login  >>', font="Arial 12 bold", fg="white", bg="#EB496F", command=Home)
        self.login_button.place(x=90, y=340)

        self.userRegister_label = tk.Label(
            self.root, text="Don't have an account!", font="Arial 10 bold", fg="red")
        self.userRegister_label.place(x=90, y=400)
        self.register_button = tk.Button(self.root, text='Register  >>',
                                         font="Arial 12 bold", fg="white", bg="#EB496F", command=self.register_page)
        self.register_button.place(x=90, y=430)

        self.root.mainloop()

    def register_page(self):
        self.root.destroy()
        obj.push(RegisterPage())
        obj.peek()

    def go_to_home_page(self):
        user_email = self.userEmail.get().lower().strip()
        user_password = self.userPassword.get().strip()

        file = open('Project_3.json', 'r')
        all_data = json.load(file)
        file.close()

        user_found = False
        for data in all_data:
            if "mail" in data and "Password" in data:
                if user_email == data['mail'] and user_password == data['Password']:
                    print(data['name'])
                    user_found = True
                    homepage = Home(self, user_name=data['name'])
                    homepage.show_home_content()
                    break

        if not user_found:
            messagebox.showwarning("Alert!", "Wrong email or password")
            self.userEmail.delete(0, 'end')
            self.userPassword.delete(0, 'end')

    # def login(self):
    #     email = self.userEmail.get()
    #     password = self.userPassword.get()
    #
    #     if self.validate_login(email, password):
    #         self.root.withdraw()
    #         # home = Home(self.parent)
    #         # home.show()
    #
    # def validate_login(self, email, password):
    #     if email == "example@example.com" and password == "password":
    #         return True
    #     else:
    #         messagebox.showerror("Login Failed", "Invalid email or password.")
    #         return False


class RegisterPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Register Page")
        self.root.geometry("1000x850")
        self.root.configure(background='white')

        self.userRegister_label = tk.Label(
            self.root, text="Register Here", font="Impact 35 bold", fg="#EB496F", bg="white")
        self.userRegister_label.place(x=90, y=40)

        self.userName_label = tk.Label(
            self.root, text="Name", font="Arial 10 bold", bg="white")
        self.userName_label.place(x=90, y=120)

        self.userName = tk.Entry(self.root, font="arial 12", bg="gray90", validatecommand=self.validate)
        self.userName.place(x=90, y=140)

        self.userPhone_label = tk.Label(
            self.root, text="Phone number", font="Arial 10 bold", bg="white")
        self.userPhone_label.place(x=90, y=180)

        self.userPhone = tk.Entry(self.root, font="arial 12", bg="gray90")
        self.userPhone.place(x=90, y=200)

        self.userMail_label = tk.Label(
            self.root, text="Email", font="Arial 10 bold", bg="white")
        self.userMail_label.place(x=90, y=240)

        self.userMail = tk.Entry(self.root, font="arial 12", bg="gray90")
        self.userMail.place(x=90, y=260)

        self.userGovernorate_label = tk.Label(
            self.root, text="Governorate", font="Arial 10 bold", bg="white")
        self.userGovernorate_label.place(x=90, y=300)

        self.cities = tk.StringVar(self.root)
        self.cities.set("cities")

        options = [
            "Alexandria", "Aswan", "Asyut", "Beheira", "Beni Suef", "Cairo", "Dakahlia", "Damietta", "Faiyum",
            "Gharbia", "Giza", "Ismailia", "Kafr El Sheikh", "Luxor", "Matrouh", "Minya", "Monufia", "New Valley",
            "North Sinai", "Port Said", "Qalyubia", "Qena", "Red Sea", "Sharqia", "Sohag", "South Sinai", "Suez"]

        self.cities_menu = ttk.Combobox(
            self.root, textvariable=self.cities, values=options)
        self.cities_menu.bind("<<ComboboxSelected>>", self.on_selection_change)
        self.cities_menu.place(x=90, y=320)

        self.userGender_label = tk.Label(
            self.root, text="Gender", font="Arial 10 bold", bg="white")
        self.userGender_label.place(x=90, y=360)

        self.userGender = tk.Entry(self.root, font="arial 12", bg="gray90")
        self.userGender.place(x=90, y=380)

        self.userAge_label = tk.Label(
            self.root, text="age", font="Arial 10 bold", bg="white")
        self.userAge_label.place(x=90, y=420)

        self.userAge = tk.Entry(self.root, font="arial 12", bg="gray90")
        self.userAge.place(x=90, y=440)

        self.userPass_label = tk.Label(
            self.root, text="Password", font="Arial 10 bold", bg="white")
        self.userPass_label.place(x=90, y=480)

        self.userPass = tk.Entry(self.root, font="arial 12", bg="gray90")
        self.userPass.place(x=90, y=500)

        self.userNationalID_label = tk.Label(
            self.root, text="National ID", font="Arial 10 bold", bg="white")
        self.userNationalID_label.place(x=90, y=540)

        self.userNationalID = tk.Entry(self.root, font="arial 12", bg="gray90")
        self.userNationalID.place(x=90, y=560)

        self.register_button = tk.Button(
            self.root, text='Register  >>', font="Arial 12 bold", fg="white", bg="#EB496F", command=self.store_in_db)
        self.register_button.place(x=90, y=600)

        self.Back_button = tk.Button(
            self.root, text='<< Back', font="Arial 12 bold", fg="white", bg="#EB496F", command=self.back_to_login_page)
        self.Back_button.place(x=200, y=600)

    def on_selection_change(self):
        city = self.cities.get()
        print(f"You selected: {city}")

    def store_in_db(self):
        file = open('Project_3.json', 'r')
        data = json.load(file)
        file.close()
        userdata = {"name": self.userName.get(), "phone": self.userPhone.get(),
                    "mail": self.userMail.get(), "Governorate": self.cities.get(),
                    "Gender": self.userGender.get(), "Age": self.userAge.get(),
                    "Password": self.userPass.get(), "National ID": self.userNationalID.get()}
        data.append(userdata)

        file = open("Project_3.json", "w")
        json.dump(data, file, indent=2)
        file.close()

        messagebox.showinfo(
            'successful!', f"REGISTERED SUCCESSFULLY(:-")
        self.root.withdraw()
        LoginPage()

    @staticmethod
    def validate(value):
        if value == "":
            messagebox.showerror("Error", "Please enter a username.")
            return False
        return True

    def back_to_login_page(self):
        self.root.withdraw()
        obj.pop()
        obj.peek()


obj = Stack()
obj.push(LoginPage())
obj.peek()





#    @staticmethod
#     def searchItem(target):
#         file = open('Project_3.json', 'r')
#         all_data = json.load(file)
#         file.close()
#
#         # start of binary search
#         i = 0
#         lift = 0
#         right = len(all_data) - 1
#         target =target.lower()
#         targetlength = len(target)
#         while lift <= right:
#             i += 1
#             mid = (right + lift) // 2
#             print((all_data[mid]["name"])[0:targetlength])
#
#             if ((all_data[mid]["name"])[0:targetlength]).lower() == target:
#                 print('Steps:', i, all_data[mid])
#                 break
#
#             elif ((all_data[mid]["name"])[0:targetlength]).lower() < target:
#                 lift = mid + 1
#             else:
#                 right = mid - 1
#
#
# obj = Home
# x = input("enter")
# obj.searchItem(x)