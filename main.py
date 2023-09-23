import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
from homepage import Home


class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("1000x850")
        self.configure(background='white')

        self.logo = tk.PhotoImage(file='logo1.png')
        self.logo_lab = tk.Label(self, image=self.logo, bg="white")
        self.logo_lab.place(x=200, y=150)

        self.userLogo_label = tk.Label(
            self, text="is talk", font="Impact 65 bold", fg="#EB496F", bg="white")
        self.userLogo_label.place(x=500, y=0)

        self.userLogin_label = tk.Label(
            self, text="Login Here", font="Impact 35 bold", fg="#EB496F", bg="white")
        self.userLogin_label.place(x=90, y=100)

        self.userEmail_label = tk.Label(
            self, text="Email", font="Arial 15 bold", bg="white")
        self.userEmail_label.place(x=90, y=180)

        self.userEmail = tk.Entry(self, font="Arial 12", bg="gray90")
        self.userEmail.place(x=90, y=210)

        self.userPassword_label = tk.Label(
            self, text="Password", font="Arial 15 bold", bg="white")
        self.userPassword_label.place(x=90, y=280)

        self.userPassword = tk.Entry(self, font="Arial 12", show="*", bg='gray90')
        self.userPassword.place(x=90, y=310)

        self.login_button = tk.Button(
            self, text='Login  >>', font="Arial 12 bold", fg="white", bg="#EB496F", command=self.check_user_account)
        self.login_button.place(x=90, y=340)

        self.userRegister_label = tk.Label(
            self, text="Don't have an account!", font="Arial 10 bold", fg="red")
        self.userRegister_label.place(x=90, y=400)
        self.register_button = tk.Button(self, text='Register  >>',
                                         font="Arial 12 bold", fg="white", bg="#EB496F", command=self.register_page)
        self.register_button.place(x=90, y=430)

    def check_user_account(self):
        user_email = self.userEmail.get().lower().strip()
        user_password = self.userPassword.get().strip()

        file = open('Project_3.json', 'r')
        all_data = json.load(file)
        file.close()

        user_found = False
        self.userIndex = -1
        for data in all_data:
            self.userIndex += 1
            if "mail" in data and "Password" in data:
                if user_email == data['mail'] and user_password == data['Password']:
                    print(data['name'])
                    user_found = True
                    homepage = Home(self, user_name=data['name'],
                                    user_password=data['Password'],
                                    userIndex=self.userIndex)
                    homepage.show_home_content()
            self.userIndex += 1

        if not user_found:
            messagebox.showwarning("Alert!", "Wrong email or password")
            self.userEmail.delete(0, 'end')
            self.userPassword.delete(0, 'end')

    def register_page(self):
        register_window = RegisterPage()
        self.destroy()
        register_window.mainloop()


class RegisterPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Register Page")
        self.geometry("1000x850")
        self.configure(background='white')

        self.userRegister_label = tk.Label(
            self, text="Register Here", font="Impact 35 bold", fg="#EB496F", bg="white")
        self.userRegister_label.place(x=90, y=40)

        self.userName_label = tk.Label(
            self, text="Name", font="Arial 10 bold", bg="white")
        self.userName_label.place(x=90, y=120)
        self.userName = tk.Entry(self, font="arial 12", bg="gray90")
        self.userName.place(x=90, y=140)

        self.userPhone_label = tk.Label(
            self, text="Phone number", font="Arial 10 bold", bg="white")
        self.userPhone_label.place(x=90, y=180)
        self.userPhone = tk.Entry(self, font="arial 12", bg="gray90")
        self.userPhone.place(x=90, y=200)

        self.userMail_label = tk.Label(
            self, text="Email", font="Arial 10 bold", bg="white")
        self.userMail_label.place(x=90, y=240)
        self.userMail = tk.Entry(self, font="arial 12", bg="gray90")
        self.userMail.place(x=90, y=260)

        self.userGovernorate_label = tk.Label(
            self, text="Governorate", font="Arial 10 bold", bg="white")
        self.userGovernorate_label.place(x=90, y=300)
        self.cities = tk.StringVar(self)

        options = [
            "Alexandria", "Aswan", "Asyut", "Beheira", "Beni Suef", "Cairo", "Dakahlia", "Damietta", "Faiyum",
            "Gharbia", "Giza", "Ismailia", "Kafr El Sheikh", "Luxor", "Matrouh", "Minya", "Monufia", "New Valley",
            "North Sinai", "Port Said", "Qalyubia", "Qena", "Red Sea", "Sharqia", "Sohag", "South Sinai", "Suez"]

        self.cities_menu = ttk.Combobox(
            self, textvariable=self.cities, values=options)
        self.cities_menu.bind("<<ComboboxSelected>>")
        self.cities_menu.place(x=90, y=320)

        genders = ["Male", "Female"]
        self.userGender_label = tk.Label(
            self, text="Gender", font="Arial 10 bold", bg="white")
        self.userGender_label.place(x=90, y=360)
        self.gender_combobox = ttk.Combobox(self, values=genders)
        self.gender_combobox.place(x=90, y=380)

        self.userAge_label = tk.Label(
            self, text="Age", font="Arial 10 bold", bg="white")
        self.userAge_label.place(x=90, y=420)
        self.userAge = tk.Entry(self, font="arial 12", bg="gray90")
        self.userAge.place(x=90, y=440)

        self.userPass_label = tk.Label(
            self, text="Password", font="Arial 10 bold", bg="white")
        self.userPass_label.place(x=90, y=480)
        self.userPass = tk.Entry(self, font="arial 12", bg="gray90")
        self.userPass.place(x=90, y=500)

        self.userNationalID_label = tk.Label(
            self, text="National ID", font="Arial 10 bold", bg="white")
        self.userNationalID_label.place(x=90, y=540)
        self.userNationalID = tk.Entry(self, font="arial 12", bg="gray90")
        self.userNationalID.place(x=90, y=560)

        self.register_button = tk.Button(
            self, text='Register  >>', font="Arial 12 bold", fg="white", bg="#EB496F",
            command=self.store_in_db)
        self.register_button.place(x=90, y=600)

        self.Back_button = tk.Button(
            self, text='<< Back', font="Arial 12 bold", fg="white", bg="#EB496F",
            command=self.go_to_login_page)
        self.Back_button.place(x=200, y=600)

    def go_to_login_page(self):
        self.destroy()
        login_page = LoginPage()
        login_page.mainloop()

    def store_in_db(self):
        if self.validate() is False:
            messagebox.showerror("Error", "Please fill all data.")
        else:
            userdata = {"name": self.userName.get(), "phone": self.userPhone.get(),
                        "mail": self.userMail.get(), "Governorate": self.cities_menu.get(),
                        "Gender": self.gender_combobox.get(), "Age": self.userAge.get(),
                        "Password": self.userPass.get(), "National ID": self.userNationalID.get()}

            file = open('Project_3.json', 'r')
            user_data = json.load(file)
            user_data.append(userdata)

            file = open("Project_3.json", "w")
            json.dump(user_data, file, indent=2)
            file.close()

            messagebox.showinfo('successful!', f"REGISTERED SUCCESSFULLY(:-")
            self.go_to_login_page()

    def validate(self):
        if self.userName.get() == "":
            return False
        if self.userPhone.get() == "":
            return False
        if self.userMail.get() == "":
            return False
        if self.cities_menu == "":
            return False
        if self.gender_combobox.get() == "":
            return False
        if self.userAge.get() == "":
            return False
        if self.userPass.get() == "":
            return False
        if self.userNationalID.get() == "":
            return False


if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
