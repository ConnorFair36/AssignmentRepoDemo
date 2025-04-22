import tkinter as tk
from tkinter import ttk
from handle_accounts import PatientAccount
import patient
import str_verification as str_ver
# stores the window and all the functions used by it
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("The Medication Adherence System")
        # add all frames here
        self.frames = {
            "welcome" : WelcomePatient(parent=self),
            "patient sign in" : PatientSignIn(parent=self),
            "patient create account" : PatientCreateAcc(parent=self),
            "patient profile" : PatientProfile(parent=self),
            "edit patient profile" : EditPatientProfile(parent=self),
            "view patient meds": PatientViewMeds(parent=self),
            "view patient med x": PatientViewMedX(parent=self),
            "edit patient med x": PatientEditMedX(parent=self),
            # utility frames
            "Patient NavBar": PatientPofileNavBar(parent=self)
        }

        # sets the welcome page as the first page
        self.current = self.frames["welcome"]
        self.current.pack(fill="both", expand="true")
        self.window_state = "welcome"

        self.utilites = []
        # stores the Patient or doctor account object
        self.account: PatientAccount = None
        # a free variable that can be used to send anything from one frame to another
        # USE SPARINGLY!!!!!!!!
        self.broadcast = None
    
    def switch_to(self, target: str):
        """Switches the current frame in the window to the target frame"""
        # don't change the window if we are already in it
        if target == self.window_state:
            pass
        # updates the frame and the state of the program
        for widget in self.utilites:
            widget.pack_forget()
        self.utilites = []
        self.current.pack_forget()
        self.current = self.frames[target]
        self.current.pack(fill="both", expand="true")
        self.window_state = target
        # runs any other updates needed on the window
        if hasattr(self.current, "update_frame"):
            self.current.update_frame()
        # adds the navbar to the frames that need it
        if self.window_state in ["patient profile", "edit patient profile", "view patient meds", "view patient med x",
                                   "edit patient med x"]:
            self.utilites.append(self.frames["Patient NavBar"])
            self.utilites[-1].pack(side="bottom")
        self.update_idletasks()


# Patient frames
class WelcomePatient(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="WelcomePatient")
        self.title.pack()

        self.log_in = ttk.Button(self, text="Login", command=self.sign_in_doc)
        self.log_in.pack()

        self.create_acc = ttk.Button(self, text="Create Account", command=self.create_doc)
        self.create_acc.pack()
    
    def sign_in_doc(self):
        self.parent.switch_to("patient sign in")
    
    def create_doc(self):
        self.parent.switch_to("patient create account")


class PatientSignIn(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="PatientSignIn")
        self.title.pack()

        self.label1 = tk.Label(self, text="Name:")
        self.label1.pack()

        self.name_in = tk.Entry(self)
        self.name_in.pack()

        self.label2 = tk.Label(self, text="Password:")
        self.label2.pack()

        self.password_in = tk.Entry(self)
        self.password_in.pack()

        self.log_in_button = ttk.Button(self, text="Sign In!", command=self.attempt_sign_in)
        self.log_in_button.pack()

        self.go_back = ttk.Button(self, text="Go Back", command=self.return_to_wel)
        self.go_back.pack()

    def return_to_wel(self):
        self.parent.switch_to("welcome patient")

    def attempt_sign_in(self):
        name = self.name_in.get()
        password = self.password_in.get()
        print(name, password)
        if str_ver.valid_name(name) and str_ver.valid_password(password):
            if self.parent.account.find_account(name, password):
                print(self.parent.account.account["name"])
                self.parent.switch_to("patient profile")
            else:
                print("account doesn't exist, lol")
        else:
            print("invalid name or password")  


class PatientCreateAcc(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="PatientCreateAcc")
        self.title.pack()

        self.labels = ["Name", "Password", "Phone Number", "Email", "Birthday", "Sex", "Insurance Provider"]
        self.format_info = ["", "Must be at least 8 characters long with \none number and one special character", "", "", 
                            "Must be writen as: MM-DD-YYYY", "", ""]
        self.entries = {}
        for label, info in zip(self.labels, self.format_info):
            new_label = ttk.Label(self, text=f"{label}:")
            new_label.pack()
            self.entries[label] = ttk.Entry(self)
            self.entries[label].pack()
            if info != "":
                info_label = ttk.Label(self, text=info, font=("Arial", 10))
                info_label.pack()

        self.create_account_button = ttk.Button(self, text="Create Account!", command=self.attempt_create_account)
        self.create_account_button.pack()

        self.go_back = ttk.Button(self, text="Go Back", command=self.return_to_wel)
        self.go_back.pack()

    def return_to_wel(self):
        self.parent.switch_to("welcome patient")
    
    def attempt_create_account(self):
        inputs = {key: entry.get() for key, entry in self.entries.items()}
        compare_functions = [str_ver.valid_name, str_ver.valid_password, str_ver.valid_phone_num,
                              str_ver.valid_email, str_ver.valid_birthday, str_ver.valid_sex, str_ver.valid_insurance]
        all_valid = [fun(inputs[name]) for fun, name in zip(compare_functions, self.labels)]
        if False not in all_valid:
            self.parent.account.create_account(inputs["Name"], inputs["Password"], inputs["Phone Number"], 
                                               inputs["Email"], inputs["Birthday"], inputs["Sex"], inputs["Insurance Provider"])
            self.parent.switch_to("patient profile")


class PatientPofileNavBar(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="PatientProfile")
        self.title.pack()

        self.to_profile_button = ttk.Button(self, text="Profile", command=self.go_to_profile)
        self.to_profile_button.pack(side="right")

        self.to_pat_list = ttk.Button(self, text="Medications", command=self.view_meds)
        self.to_pat_list.pack(side="left")
    
    def go_to_profile(self):
        self.parent.switch_to("patient profile")
    
    def view_meds(self):
        self.parent.switch_to("view patient meds")


class PatientProfile(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="PatientProfile")
        self.title.pack()

        self.labels = [tk.Label(self, text="<NAME>"), tk.Label(self, text="<PHONE#>"), 
                       tk.Label(self, text="<EMAIL>"), tk.Label(self, text="<BIRTHDAY>"),
                       tk.Label(self, text="<SEX>"), tk.Label(self, text="<INSURANCE PROVIDER>")]
        for label in self.labels:
            label.pack(anchor="w")
        self.edit_button = ttk.Button(self, text="Edit", command=self.edit_profile)
        self.edit_button.pack(anchor="e")

        self.logout_button = ttk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack(anchor="e")

    def update_frame(self):
        patient_info = self.parent.account.account
        label_names = ["name", "phone", "email", "birthday", "sex", "insurance provider"]
        for label, label_name in zip(self.labels, label_names):
            label.config(text=patient_info[label_name])


    def edit_profile(self):
        self.parent.switch_to("edit patient profile")
    
    def logout(self):
        self.parent.account = None
        self.parent.switch_to("welcome")


class EditPatientProfile(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="EditPatientProfile")
        self.title.pack()

        self.widgets = [(ttk.Label(self, text="<NAME>"), ttk.Entry(self)), 
                       (ttk.Label(self, text="<PASSWORD>"), ttk.Entry(self)), 
                       (ttk.Label(self, text="<PHONE#>"), ttk.Entry(self)), 
                       (ttk.Label(self, text="<EMAIL>"), ttk.Entry(self)), 
                       (ttk.Label(self, text="<BIRTHDAY>"), ttk.Entry(self)),
                       (ttk.Label(self, text="<SEX>"), ttk.Entry(self)), 
                       (ttk.Label(self, text="<INSURANCE PROVIDER>"), ttk.Entry(self))]
        for label, entry in self.widgets:
            label.pack()
            entry.pack()
        self.edit_button = ttk.Button(self, text="Save", command=self.save_profile)
        self.edit_button.pack(anchor="e")

        self.logout_button = ttk.Button(self, text="DELETE ACCOUNT", command=self.die)
        self.logout_button.pack(anchor="e")
    
    def update_frame(self):
        patient_info = self.parent.account.account
        label_names = ["name","password", "phone", "email", "birthday", "sex", "insurance provider"]
        for label, label_name in zip(self.widgets, label_names):
            label[0].config(text="Current " + label_name.capitalize() + ": " + patient_info[label_name])

    def save_profile(self):
        user_input = [entry.get() for label, entry in self.widgets]
        validate_functions = [str_ver.valid_name, str_ver.valid_password, str_ver.valid_phone_num,
                              str_ver.valid_email, str_ver.valid_birthday, str_ver.valid_sex, str_ver.valid_insurance]
        valid_inputs = [fun(in_str) or in_str == "" for fun, in_str in zip(validate_functions, user_input)]
        if False not in valid_inputs:
            self.parent.account.update_account(name=user_input[0], password=user_input[1], phone_number=user_input[2],
                                            email=user_input[3], birthday=user_input[4], sex=user_input[5], insur_prov=user_input[6])
            self.parent.switch_to("patient profile")
    
    def die(self):
        print("DELETE ACCOUNT")
        self.parent.switch_to("welcome")


class PatientViewMeds(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="PatientViewMeds")
        self.title.pack()

        self.list_container = tk.Canvas(self)
        self.list_container.pack(side="left", fill="both")

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.list_container.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.list_container.configure(yscrollcommand=self.scrollbar.set)
        self.list_container.bind('<Configure>', 
                lambda e: self.list_container.configure(scrollregion=self.list_container.bbox("all")))

        self.list_frame = ttk.Frame(self.list_container)
        self.list_container.create_window((0, 0), window=self.list_frame, anchor="nw")

        for i in range(5):
            med_frame = ttk.Frame(self.list_frame)
            med_frame.pack(fill="x")
            label = ttk.Label(med_frame, text=f"Medication {i}")
            label.pack(side="left")
            button = ttk.Button(med_frame, text=f"Details", command=lambda: self.view_med(f"Medication {i}"))
            button.pack(side="left")

    def view_med(self, medication: str):
        self.parent.switch_to("view patient med x")
        

class PatientViewMedX(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="PatientViewMedX")
        self.title.pack()

        self.labels = [tk.Label(self, text="<NAME>"), tk.Label(self, text="<CONDITIONS>"), 
                       tk.Label(self, text="<SEVERITY>"), tk.Label(self, text="<TIMES TO TAKE>")]
        for label in self.labels:
            label.pack(anchor="w")

        edit_button = ttk.Button(self, text="Edit", command=self.edit_med)
        edit_button.pack(anchor="s")

        gen_rep_button = ttk.Button(self, text="Generate Report", command=self.gen_report)
        gen_rep_button.pack(anchor="s")

    def edit_med(self):
        self.parent.switch_to("edit patient med x")
    
    def gen_report(self):
        print("Not yet, lol")


class PatientEditMedX(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="PatientViewMedX")
        self.title.pack()

        self.widgets = [(ttk.Label(self, text="<NAME>"), ttk.Entry(self)),
                        (ttk.Label(self, text="<CONDITIONS>"), ttk.Entry(self)),
                        (ttk.Label(self, text="<SEVERITY>"), ttk.Entry(self)),
                        (ttk.Label(self, text="<TIME 1>"), ttk.Entry(self)),
                        (ttk.Label(self, text="<TIME 2>"), ttk.Entry(self)),
                        (ttk.Label(self, text="<NAME 3>"), ttk.Entry(self))]

        for label, entry in self.widgets:
            label.pack(anchor="w")
            entry.pack(anchor="w")
        
        save_button = ttk.Button(self, text="Save", command=lambda:self.finish_edit(True))
        save_button.pack(anchor="e")

        cancel_button = ttk.Button(self, text="Cancel", command=lambda:self.finish_edit(False))
        cancel_button.pack(anchor="e")
    
    def finish_edit(self, save: bool):
        self.parent.switch_to("view patient med x")


if __name__ == "__main__":
    MainWindow().mainloop()
