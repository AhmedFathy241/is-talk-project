import tkinter as tk
from tkinter.ttk import Frame
import webview
from tkinter import ttk, messagebox
from tkinter import filedialog

from PIL import Image, ImageTk
import json


def show_confirmation_message():
    messagebox.showinfo("تأكيد الحفظ", "تم حفظ الرسالة بنجاح!")


class Home:
    def __init__(self, root, user_name,user_password,userIndex):
        self.content_frame = None
        self.posts_listbox = None
        self.root = root
        self.root.geometry("1000x600")
        self.root.title("IsTock")
        self.json_file = "project_3.json"
        self.image_data = []
        self.user_name = user_name
        self.user_password=user_password
        self.userIndex=userIndex

        self.load_data()

        self.colors = {
            "background": "#f0f0f0",
            "top_bar": "#279eff",
            "sidebar": "#40f8ff",
            "text": "#000000",
        }

        self.user_name = user_name

        self.create_top_bar()
        self.create_sidebar()
        self.create_content_frame()

    def save_post(self, post_text):
        try:
            with open('Project_3.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = []

        for user_data in data:
            if "name" in user_data and user_data["name"] == self.user_name:
                if "posts" not in user_data:
                    user_data["posts"] = []
                user_data["posts"].append({"text": post_text})
                break

        with open('Project_3.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(post_text)
        show_confirmation_message()

    def create_top_bar(self):
        top_frame = tk.Frame(self.root, bg="#DDCFF4")
        top_frame.pack(side="top", fill="x")

        icon1_img = tk.PhotoImage(file="img/istock_profel.png").subsample(5)
        icon2_img = tk.PhotoImage(file="img/istock_video.png").subsample(4)
        icon3_img = tk.PhotoImage(file="img/istock_icon.png").subsample(4)
        icon4_img = tk.PhotoImage(file="img/istockphoto_add.png").subsample(4)

        icon1_button = tk.Button(top_frame, image=icon1_img, height=50, width=150,
                                 command=lambda: self.show_profile_content(), bg="#DDCFF4")

        icon2_button = tk.Button(top_frame,text="watch",height=50,width=150,
                                 command=self.show_video_content, bg="#DDCFF4")
        icon2_button.config(image=icon2_img)
        icon3_button = tk.Button(top_frame, image=icon3_img,height=50,width=150, command=self.show_home_content,
                                 bg="#DDCFF4")
        icon4_button = tk.Button(top_frame, image=icon4_img,height=50,width=150, command=self.show_add_content,
                                 bg="#DDCFF4")
        text_label = tk.Label(top_frame, text="is talk",font="Impact 30 bold", fg="#EB496F", bg="#DDCFF4")

        icon1_button.image = icon1_img
        icon2_button.image = icon2_img
        icon3_button.image = icon3_img
        icon4_button.image = icon4_img

        icon1_button.pack(side="left", padx=0)
        icon2_button.pack(side="left", padx=0)
        icon4_button.pack(side="left", padx=0)
        icon3_button.pack(side="left", padx=0)
        text_label.pack(side="right", padx=20)

    def show_home_content(self):
        self.clear_content()

        try:
            with open('Project_3.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = []

        entry_frame = tk.Frame(self.content_frame, bg="#FED6A8")
        entry_frame.pack(side="top", fill="both")

        inner_frame = tk.Frame(entry_frame, bg="#F7F1FA")
        inner_frame.pack( expand=True,fill="both", pady=0)

        post_entry = tk.Text(inner_frame, font="Arial 12 bold",width=40 )#,height=2)
        post_entry.place(x=235,y=6)

        print(post_entry.get("1.0", "end-1c"))

        save_button = tk.Button(inner_frame, text="Post now",font="Head 12 bold",
                                command=lambda: self.save_post(post_entry.get("1.0", "end-1c")), bg="black",
                                fg="white")
        save_button.pack(side="right", padx=150, pady=10)

        select_image_button = tk.Button(inner_frame, text="Post Image",font="Head 12 bold",
                                        command=self.load_image,bg="black",fg="white")
        select_image_button.place(x=730, y=10)

        lab_or = tk.Label(inner_frame, text="or",font="Head 12 bold", bg="#F7F1FA",fg="#EB496F")
        lab_or.place(x=700, y=17)

        frame_canvas = tk.Canvas(self.content_frame,bg="#EBE5DE")
        frame_canvas.pack(side="left",fill="both",expand=1)

        sc = tk.Scrollbar(self.content_frame,orient="vertical",command=frame_canvas.yview)
        sc.pack(side="right",fill="y")

        frame_canvas.configure(yscrollcommand=sc.set)
        frame_canvas.bind('<Configure>',lambda e:frame_canvas.configure(scrollregion=frame_canvas.bbox("all")))

        second_frame = tk.Frame(frame_canvas,width=500,height=5000,bg="#EBE5DE")
        frame_canvas.create_window(420,0,window=second_frame)
        i = 150
        j = 100
        for post_data in data:
            if "posts" in post_data and isinstance(post_data["posts"], list):
                for post in post_data["posts"]:
                    if "text" in post:
                        post_text = post["text"]
                        user_name = post_data.get("name", "Unknown")
                        frame = tk.LabelFrame(second_frame, width=500, text=user_name, font="Arial 18 bold",
                                              height=300, padx=50)
                        frame.place(y=j)
                        j += 350

                        post_lable = tk.Label(frame, text=post_text, font="Arial 12 bold")
                        post_lable.pack(side="top",pady=10,padx=5)

        for image_info in self.image_data:
            image_path = image_info["path"]
            image = Image.open(image_path)
            image = image.resize((400, 350))
            image = ImageTk.PhotoImage(image)

            image_label = tk.Label(frame, image=image)
            image_label.image = image
            image_label.pack(expand=True, fill="both")

    def show_profile_content(self):
        self.clear_content()

        try:
            with open('Project_3.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = []

        posts_frame = ttk.Frame(self.content_frame)
        posts_frame.pack(expand=True, fill="both")

        scrollbar = ttk.Scrollbar(posts_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.posts_listbox = tk.Listbox(posts_frame, selectmode=tk.SINGLE, height=20, font=("Arial", 14),
                                        yscrollcommand=scrollbar.set)
        self.posts_listbox.pack(expand=True, fill="both", padx=20, pady=(0, 20))
        scrollbar.config(command=self.posts_listbox.yview)

        for post_data in data:
            if "posts" in post_data and isinstance(post_data["posts"], list):
                for post in post_data["posts"]:
                    if "text" in post and post_data.get("name") == self.user_name:  # التحقق من اسم الحساب
                        post_text = post["text"]

                        self.posts_listbox.insert(0, post_text)

                        post_frame = ttk.Frame(self.posts_listbox)
                        post_frame.pack(expand=True, fill="both")

                        separator = ttk.Separator(post_frame, orient="horizontal")
                        separator.pack(expand=True, fill="both")

                        post_label = ttk.Label(post_frame, text=post_text, font=("Arial", 14), wraplength=600,
                                               anchor="w", justify="left")
                        post_label.pack(side="left", expand=True, fill="both")


        for image_info in self.image_data:
            image_path = image_info["path"]
            image = Image.open(image_path)
            image = image.resize((200, 200))
            image = ImageTk.PhotoImage(image)

            image_label = tk.Label(self.posts_listbox, image=image)
            image_label.image = image
            image_label.pack(expand=True, fill="both")

    def show_video_content(self):
        self.clear_content()
        image_grid_frame = tk.Frame(self.content_frame, bg=self.colors["background"])
        image_grid_frame.pack(expand=True, fill="both")

        select_image_button = tk.Button(image_grid_frame, text="Select Image",
                                        command=self.load_image, bg="#279eff", fg="white")
        select_image_button.pack(side="top", pady=10)

        self.image_display_frame = tk.Frame(self.content_frame, bg=self.colors["background"])
        self.image_display_frame.pack(expand=True, fill="both")

        for image_info in self.image_data:
            image_path = image_info["path"]
            image = Image.open(image_path)
            image = image.resize((200, 200))
            image = ImageTk.PhotoImage(image)

            image_label = tk.Label(self.image_display_frame, image=image)
            image_label.image = image
            image_label.pack(expand=True, fill="both")

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.gif")])
        if file_path:
            try:
                image = Image.open(file_path)
                image = image.resize((200, 200))
                image = ImageTk.PhotoImage(image)

                image_label = tk.Label(self.image_display_frame, image=image, bg=self.colors["background"])
                image_label.image = image

                image_label.pack(side="top", padx=10, pady=10)

                self.image_data.append({
                    "path": file_path,
                    "user": self.user_name
                })

                self.update_json_data()
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to open the image: {str(e)}")

    def load_data(self):
        try:
            with open(self.json_file, 'r') as json_file:
                self.json_data = json.load(json_file)
                for user_data in self.json_data:
                    if user_data.get("name") == self.user_name and "images" in user_data:
                        self.image_data = user_data["images"]
        except FileNotFoundError:
            self.json_data = []

    def update_json_data(self):
        for user_data in self.json_data:
            if user_data.get("name") == self.user_name:
                user_data["images"] = self.image_data
                break

        with open(self.json_file, 'w') as json_file:
            json.dump(self.json_data, json_file, indent=4)

    def show_add_content(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="Add a friend", font=("Arial", 20),
                         bg=self.colors["background"], fg=self.colors["text"])
        label.pack(expand=True, fill="both")

    def create_sidebar(self):
        sidebar_frame = tk.Frame(self.root, width=200,bg="#F7F1FA")
        sidebar_frame.pack(side="left", fill="y")

        image = Image.open("logo1.png")
        image = image.resize((150, 110))
        image = ImageTk.PhotoImage(image)

        image_label = tk.Label(sidebar_frame, image=image, bg="#F7F1FA")
        image_label.image = image

        page1_button = tk.Button(sidebar_frame,font="Head 12 bold", text="<< Exit",height=2,fg="white",width=15, command=self.logout,
                                 bg="#EB496F")
        page2_button = tk.Button(sidebar_frame,font="Head 12 bold", text="Games",height=2,fg="white",width=15, command=self.show_games_content,
                                 bg="#EB496F")
        page3_button = tk.Button(sidebar_frame,font="Head 12 bold", text="Edit password",height=2,fg="white",width=15, command=self.edit_info,
                                 bg="#EB496F")

        separator = ttk.Separator(sidebar_frame,orient="horizontal")
        image_label.pack(pady=20)
        separator.pack(fill="x", pady=0)

        page3_button.pack(pady=40)
        page2_button.pack(pady=20)
        page1_button.pack(pady=30)

    def show_page1_content(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="Page 1 Content", font=("Arial", 20),
                         bg=self.colors["background"],
                         fg=self.colors["text"])
        label.pack(expand=True, fill="both")

    def show_games_content(self):
        self.clear_content()
        webview.create_window("Web Page", "https://poki.com/ar", width=800, height=600)
        webview.start()


    def create_content_frame(self):
        self.content_frame = tk.Frame(self.root, bg="#EBE5DE")
        self.content_frame.pack(side="top", fill="both", expand=True)
        self.show_home_content()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def edit_info(self):
        self.clear_content()
        passNow_label = tk.Label(self.content_frame, text="Current password", font="Head 14 bold",bg="#EBE5DE")
        passNow_label.place(x=80, y=153)
        self.passNow = tk.Entry(self.content_frame,width=40,font="Arial 18 bold")
        self.passNow.place(x=260, y=150)
        self.passNow.configure(show="*")

        newPass_label = tk.Label(self.content_frame, text="New password", bg="#EBE5DE",font=("Arial", 14, "bold"))
        newPass_label.place(x=115, y=253)
        self.newPass = tk.Entry(self.content_frame, width=40, font="Arial 18 bold")
        self.newPass.place(x=260, y=250)
        self.newPass.configure(show="*")

        newPass2_label = tk.Label(self.content_frame, text="Confirm new password",bg="#EBE5DE", font=("Arial", 14, "bold"))
        newPass2_label.place(x=35, y=353)
        self.newPass2 = tk.Entry(self.content_frame, width=40, font="Arial 18 bold")
        self.newPass2.place(x=260, y=350)
        self.newPass2.configure(show="*")
        confirmButton = tk.Button(self.content_frame,text="Confirm >>",bg="black",fg="white",font="Arial 12 bold",width=10,command=self.check_password)
        confirmButton.place(x=672, y=395)

    def check_password(self):

        user_password = self.user_password

        if self.passNow.get() == user_password:
            if self.newPass.get() == self.newPass2.get():

                messagebox.showinfo("confirmation message ", " Your pass changed successfully!")

                file = open('Project_3.json', 'r')
                all_data = json.load(file)
                file.close()

                print(all_data)
                print(all_data[self.userIndex - 3]["Password"])
                print(self.userIndex, "hello")

                all_data[self.userIndex - 3]["Password"] = self.newPass.get()

                file = open("Project_3.json", "w")
                json.dump(all_data, file, indent=2)
                file.close()

                print('changed successfully')
            else:

                messagebox.showwarning("Alert!", "New passwords not identical")
                self.passNow.delete(0, 'end')
                self.newPass.delete(0, 'end')
                self.newPass2.delete(0, 'end')

                print('New passwords not identical')

        else:

            messagebox.showwarning("Alert!", "invalid password")
            self.passNow.delete(0, 'end')
            self.newPass.delete(0, 'end')
            self.newPass2.delete(0, 'end')
            print("invalid password")

    def logout(self):
        self.root.quit()
