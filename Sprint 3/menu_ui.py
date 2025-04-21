import tkinter as tk
from tkinter import ttk
import handle_accounts as acc
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
            "welcome": Welcome(parent=self),
            # doctor branch
            "welcome doctor" : WelcomeDoctor(parent=self),
            "doctor sign in" : DoctorSignIn(parent=self),
            "doctor create account" : DoctorCreateAcc(parent=self),
            "doctor profile" : DoctorProfile(parent=self),
            "edit doctor profile" : EditDoctorProfile(parent=self),
            "doctor patient list" : DoctorPatientList(parent=self),
            "edit patient on list" : DoctorPatientN(parent=self),
            "edit patient med" : DoctorPatientNMedX(parent=self),
            "generate patient report" : GeneratePatientReport(parent=self),
            # patient branch
            "welcome patient" : WelcomePatient(parent=self),
            "patient sign in" : PatientSignIn(parent=self),
            "patient create account" : PatientCreateAcc(parent=self),
            "patient profile" : PatientProfile(parent=self),
            "edit patient profile" : EditPatientProfile(parent=self),
            "view patient meds": PatientViewMeds(parent=self),
            "view patient med x": PatientViewMedX(parent=self),
            # utility frames
            "Doctor NavBar": DoctorPofileNavBar(parent=self),
            "Patient NavBar": PatientPofileNavBar(parent=self)
        }

        # sets the welcome page as the first page
        self.current = self.frames["welcome"]
        self.current.pack(fill="both", expand="true")
        self.window_state = "welcome"

        self.utilites = []
        # stores the Patient or doctor account object
        self.account: acc.DoctorAccount|acc.PatientAccount = None
        # stores the patient object for a patient's medications
        self.patient_n = None
    
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
        if self.window_state in ["doctor profile", "edit doctor profile", "doctor patient list",
                                 "edit patient on list", "edit patient med", "generate patient report"]:
            self.utilites.append(self.frames["Doctor NavBar"])
            self.utilites[-1].pack(side="bottom")
        elif self.window_state in ["patient profile", "edit patient profile", "view patient meds", "view patient med x"]:
            self.utilites.append(self.frames["Patient NavBar"])
            self.utilites[-1].pack(side="bottom")
        self.update_idletasks()


class Welcome(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="Welcome!\n Are you a Doctor or Patient?")
        self.title.pack()

        self.doctor_button = ttk.Button(self, text="Doctor", command=self.user_is_doc)
        self.doctor_button.pack()

        self.patient_button = ttk.Button(self, text="Patient", command=self.user_is_pat)
        self.patient_button.pack()

    def user_is_doc(self):
        self.parent.account = acc.DoctorAccount()
        self.parent.switch_to("welcome doctor")

    def user_is_pat(self):
        self.parent.account = acc.PatientAccount()
        self.parent.switch_to("welcome patient")


# Doctor frames
class WelcomeDoctor(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="Welcome, Doctor!")
        self.title.pack()

        self.log_in = ttk.Button(self, text="Login", command=self.sign_in_doc)
        self.log_in.pack()

        self.create_acc = ttk.Button(self, text="Create Account", command=self.create_doc)
        self.create_acc.pack()
    
    def sign_in_doc(self):
        self.parent.switch_to("doctor sign in")
    
    def create_doc(self):
        self.parent.switch_to("doctor create account")


class DoctorSignIn(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="Log In")
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

    def attempt_sign_in(self):
        name = self.name_in.get()
        password = self.password_in.get()
        print(name, password)
        if str_ver.valid_name(name) and str_ver.valid_password(password):
            if self.parent.account.find_account(name, password):
                print(self.parent.account.account["name"])
                self.parent.switch_to("doctor profile")

            else:
                print("account doesn't exist, lol")
        else:
            print("invalid name or password")


class DoctorCreateAcc(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="Create Account!")
        self.title.pack()

        self.labels = ["Name", "Password", "Phone Number", "Email", "Institution Name"]
        self.entries = {}
        for label in self.labels:
            new_label = ttk.Label(self, text=f"{label}:")
            new_label.pack()
            self.entries[label] = ttk.Entry(self)
            self.entries[label].pack()

        self.create_account_button = ttk.Button(self, text="Create Account!", command=self.attempt_create_account)
        self.create_account_button.pack()
    
    def attempt_create_account(self):
        # TODO merge with the the existing create account code from handle accounts
        inputs = {key: entry.get() for key, entry in self.entries.items()}
        compare_functions = [str_ver.valid_name, str_ver.valid_password, str_ver.valid_phone_num,
                              str_ver.valid_email, str_ver.valid_institution_name]
        all_valid = [fun(inputs[name]) for fun, name in zip(compare_functions, self.labels)]
        if False not in all_valid:
            self.parent.account.create_account(inputs["Name"], inputs["Password"], inputs["Phone Number"], 
                                               inputs["Email"], inputs["Institution Name"])
            self.parent.switch_to("doctor profile")


class DoctorPofileNavBar(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.to_profile_button = ttk.Button(self, text="Profile", command=self.go_to_profile)
        self.to_profile_button.pack(side="right")

        self.to_pat_list = ttk.Button(self, text="Patient List", command=self.go_to_list)
        self.to_pat_list.pack(side="left")
    
    def go_to_profile(self):
        self.parent.switch_to("doctor profile")
    
    def go_to_list(self):
        self.parent.switch_to("doctor patient list")


class DoctorProfile(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="Doctor Profile")
        self.title.pack()

        self.labels = [tk.Label(self, text="<NAME>"), tk.Label(self, text="<PHONE#>"), 
                       tk.Label(self, text="<EMAIL>"), tk.Label(self, text="<INSTITUTION NAME>")]
        for label in self.labels:
            label.pack(anchor="w")
        self.edit_button = ttk.Button(self, text="Edit", command=self.edit_profile)
        self.edit_button.pack(anchor="e")

        self.logout_button = ttk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack(anchor="e")

    def update_frame(self):
        self.labels[0].config(text=self.parent.account.account["name"])
        self.labels[1].config(text=self.parent.account.account["phone"])
        self.labels[2].config(text=self.parent.account.account["email"])
        self.labels[3].config(text=self.parent.account.account["institution name"])

    def edit_profile(self):
        self.parent.switch_to("edit doctor profile")
    
    def logout(self):
        self.parent.account = None
        self.parent.switch_to("welcome")


class EditDoctorProfile(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="Edit Your Profile")
        self.title.pack()

        self.widgets = [(tk.Label(self, text="<NAME>"), ttk.Entry(self)), 
                        (tk.Label(self, text="<PASSWORD>"), ttk.Entry(self)),
                       (tk.Label(self, text="<PHONE#>"), ttk.Entry(self)), 
                       (tk.Label(self, text="<EMAIL>"), ttk.Entry(self)), 
                       (tk.Label(self, text="<INSTITUTION NAME>"), ttk.Entry(self))]
        for label, entry in self.widgets:
            label.pack()
            entry.pack()
        self.edit_button = ttk.Button(self, text="Save", command=self.save_profile)
        self.edit_button.pack(anchor="e")

        self.logout_button = ttk.Button(self, text="DELETE ACCOUNT", command=self.die)
        self.logout_button.pack(anchor="e")

    def update_frame(self):
        self.widgets[0][0].config(text="Current Name: \n" + self.parent.account.account["name"])
        self.widgets[1][0].config(text="Current Password: \n" + self.parent.account.account["password"])
        self.widgets[2][0].config(text="Current Phone Number: \n" + self.parent.account.account["phone"])
        self.widgets[3][0].config(text="Current Email: \n" + self.parent.account.account["email"])
        self.widgets[4][0].config(text="Current Institution Name: \n" + self.parent.account.account["institution name"])

    def save_profile(self):
        user_input = [entry.get() for label, entry in self.widgets]
        validate_functions = [str_ver.valid_name, str_ver.valid_password, str_ver.valid_phone_num, 
                              str_ver.valid_email, str_ver.valid_institution_name]
        valid_inputs = [fun(in_str) or in_str == "" for fun, in_str in zip(validate_functions, user_input)]
        if False not in valid_inputs:
            self.parent.account.update_account(name=user_input[0], password=user_input[1], phone_number=user_input[2],
                                            email=user_input[3], institution_name=user_input[4])
            self.parent.switch_to("doctor profile")
    
    def die(self):
        self.parent.account.delete_account()
        self.parent.account = None
        self.parent.switch_to("welcome")
        

class DoctorPatientList(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="DoctorPatientList")
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

        for i in range(50):
            patient_frame = ttk.Frame(self.list_frame)
            patient_frame.pack(fill="x")
            for j in range(3):
                button = ttk.Button(patient_frame, text=f"Button {i}", command=self.edit_patient)
                button.pack(side="left")
        self.add_button = ttk.Button(self, text="Add Patient", command=self.edit_patient)
        self.add_button.pack()
    
    def edit_patient(self):
        self.parent.switch_to("edit patient on list")


class DoctorPatientN(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="DoctorPatientListEditP")
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

        for i in range(50):
            med_frame = ttk.Frame(self.list_frame)
            med_frame.pack(fill="x")
            for j in range(2):
                button = ttk.Button(med_frame, text=f"Button {i}", command=lambda: self.update_med(False))
                button.pack(side="left")
        
        self.add_button = ttk.Button(self, text="Add Medication", command=lambda: self.update_med(True))
        self.add_button.pack()

        self.gen_rep_button = ttk.Button(self, text="Generate Report", command=self.gen_report)
        self.gen_rep_button.pack()
    
    def gen_report(self):
        self.parent.switch_to("generate patient report")
    
    def update_med(self, is_new: bool):
        print(is_new)
        self.parent.switch_to("edit patient med")


class DoctorPatientNMedX(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="DoctorPatientNMedX")
        self.title.pack()

        self.labels = ["Name:", "Conditions:", "Severity", "Time 1", "Time 2", "Time 3"]
        self.current_data = ["N", "C", "S", "T1", "T2", "T3"]
        self.user_in = []

        for label, data in zip(self.labels, self.current_data):
            title = tk.Label(self, text=label)
            title.pack()
            self.user_in.append(tk.Entry(self))
            self.user_in[-1].insert(0, data)
            self.user_in[-1].pack()
        
        self.save_button = ttk.Button(self, text="Save Changes", command=lambda : self.leave_edit(True))
        self.save_button.pack()

        self.cancel_button = ttk.Button(self, text="Cancel Changes", command=lambda : self.leave_edit(False))
        self.cancel_button.pack()
    
    def leave_edit(self, save: bool):
        print(save)
        self.parent.switch_to("edit patient on list")
    

class GeneratePatientReport(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="GeneratePatientReport")
        self.title.pack()


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

    def attempt_sign_in(self):
        # TODO merge with the the existing sign into account code from handle accounts
        self.parent.switch_to("patient profile")


class PatientCreateAcc(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="PatientCreateAcc")
        self.title.pack()

        self.labels = ["Name", "Password", "Phone Number", "Email", "Birthday", "Sex", "Insurance Provider"]
        self.entries = {}
        for label in self.labels:
            new_label = ttk.Label(self, text=f"{label}:")
            new_label.pack()
            self.entries[label] = ttk.Entry(self)
            self.entries[label].pack()

        self.create_account_button = ttk.Button(self, text="Create Account!", command=self.attempt_create_account)
        self.create_account_button.pack()
    
    def attempt_create_account(self):
        # TODO merge with the the existing create account code from handle accounts
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
    def __init__(self, parent):
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

    def edit_profile(self):
        self.parent.switch_to("edit patient profile")
    
    def logout(self):
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

    def save_profile(self):
        self.parent.switch_to("patient profile")
    
    def die(self):
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
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="PatientViewMedX")
        self.title.pack()

        self.labels = [tk.Label(self, text="<NAME>"), tk.Label(self, text="<CONDITIONS>"), 
                       tk.Label(self, text="<SEVERITY>"), tk.Label(self, text="<TIMES TO TAKE>")]
        for label in self.labels:
            label.pack(anchor="w")


if __name__ == "__main__":
    MainWindow().mainloop()
