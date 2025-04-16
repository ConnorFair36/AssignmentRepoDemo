import tkinter as tk
from tkinter import ttk
# from menu_frames import *
# stores the window and all the functions used by it
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("The Medication Adherence System")
        # add all frames here
        self.welcome = Welcome(parent=self)
        self.welcome_doctor = WelcomeDoctor(parent=self)
        self.welcome_patient = WelcomePatient(parent=self)
        self.doctor_sign_in = DoctorSignIn(parent=self)
        self.doctor_create_account = DoctorCreateAcc(parent=self)
        self.doctor_profile = DoctorProfile(parent=self)

        # sets the welcome page as the first page
        self.current = self.welcome
        self.welcome.pack(fill="both", expand="true")
    
    def switch_to(self, target):
        """Switches the current frame in the window to the target frame"""
        self.current.pack_forget()
        self.current = target
        self.current.pack(fill="both", expand="true")


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
        self.parent.switch_to(self.parent.welcome_doctor)

    def user_is_pat(self):
        self.parent.switch_to(self.parent.welcome_patient)


class WelcomeDoctor(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="WelcomeDoctor")
        self.title.pack()

        self.log_in = ttk.Button(self, text="Login", command=self.sign_in_doc)
        self.log_in.pack()

        self.create_acc = ttk.Button(self, text="Create Account", command=self.create_doc)
        self.create_acc.pack()
    
    def sign_in_doc(self):
        self.parent.switch_to(self.parent.doctor_sign_in)
    
    def create_doc(self):
        self.parent.switch_to(self.parent.doctor_create_account)


class DoctorSignIn(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="DoctorSignIn")
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
        self.parent.switch_to(self.parent.doctor_profile)


class DoctorCreateAcc(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="DoctorCreateAcc")
        self.title.pack()

        self.label1 = tk.Label(self, text="Name:")
        self.label1.pack()
        self.name_in = tk.Entry(self)
        self.name_in.pack()

        self.label2 = tk.Label(self, text="Password:")
        self.label2.pack()
        self.password_in = tk.Entry(self)
        self.password_in.pack()

        self.label3 = tk.Label(self, text="Phone Number:")
        self.label3.pack()
        self.phone_in = tk.Entry(self)
        self.phone_in.pack()

        self.label4 = tk.Label(self, text="Email:")
        self.label4.pack()
        self.email_in = tk.Entry(self)
        self.email_in.pack()

        self.label5 = tk.Label(self, text="Institution Name:")
        self.label5.pack()
        self.institution_name_in = tk.Entry(self)
        self.institution_name_in.pack()

        self.create_account_button = ttk.Button(self, text="Create Account!", command=self.attempt_create_account)
        self.create_account_button.pack()
    
    def attempt_create_account(self):
        # TODO merge with the the existing create account code from handle accounts
        self.parent.switch_to(self.parent.doctor_profile)


class DoctorProfile(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="DoctorProfile")
        self.title.pack()

        self.labels = [tk.Label(self, text="<NAME>"), tk.Label(self, text="<PHONE#>"), tk.Label(self, text="<EMAIL>"),
                       tk.Label(self, text="<INSTITUTION NAME>")]
        for label in self.labels:
            label.pack()

    # TODO add buttons for patient list, edit account, profile and logout



class WelcomePatient(ttk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent


if __name__ == "__main__":
    MainWindow().mainloop()
