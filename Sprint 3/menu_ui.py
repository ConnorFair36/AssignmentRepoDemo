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
            "welcome" : Welcome(parent=self),
            "sign in" : SignIn(parent=self),
            "create account" : CreateAcc(parent=self),
            "profile" : Profile(parent=self),
            "edit profile" : EditProfile(parent=self),
            "view meds": ViewMeds(parent=self),
            "view med x": ViewMedX(parent=self),
            "edit med x": EditMedX(parent=self),
            # utility frames
            "NavBar": PofileNavBar(parent=self)
        }

        # sets the welcome page as the first page
        self.current = self.frames["welcome"]
        self.current.pack(fill="both", expand="true")
        self.window_state = "welcome"

        self.utilites = []
        # stores the Patient account object
        self.account: PatientAccount = None
        self.med_manager: patient.patient = None
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
        if self.window_state in ["profile", "edit profile", "view meds", "view med x",
                                   "edit med x"]:
            self.utilites.append(self.frames["NavBar"])
            self.utilites[-1].pack(side="bottom")
        self.update_idletasks()
    
    def create_acc(self):
        """Creates the meds manager, requires the account to exist."""
        if self.account == None:
            pass
        user_info = self.account.account
        first_name, last_name = user_info["name"].split()
        birthday_list = list(map(int, user_info["birthday"].split("-")))
        self.med_manager = patient.patient(first_name, last_name, user_info["phone"], user_info["insurance provider"], birthday_list)


# Patient frames
class Welcome(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="WelcomePatient")
        self.title.pack()

        self.log_in = ttk.Button(self, text="Login", command=self.sign_in_doc)
        self.log_in.pack()

        self.create_acc = ttk.Button(self, text="Create Account", command=self.create_doc)
        self.create_acc.pack()
    
    def sign_in_doc(self):
        self.parent.account = PatientAccount()
        self.parent.switch_to("sign in")
    
    def create_doc(self):
        self.parent.account = PatientAccount()
        self.parent.switch_to("create account")


class SignIn(ttk.Frame):
    def __init__(self, parent: MainWindow):
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

    def update_frame(self):
        # clears out any data left over
        self.name_in.delete(0, tk.END)
        self.password_in.delete(0, tk.END)

    def return_to_wel(self):
        self.parent.account = None
        self.parent.switch_to("welcome")

    def attempt_sign_in(self):
        name = self.name_in.get()
        password = self.password_in.get()
        print(name, password)
        if str_ver.valid_name(name) and str_ver.valid_password(password):
            if self.parent.account.find_account(name, password):
                print(self.parent.account.account["name"])
                self.parent.create_acc()
                self.parent.switch_to("profile")
            else:
                print("account doesn't exist, lol")
        else:
            print("invalid name or password")  


class CreateAcc(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="Create Account")
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

    def update_frame(self):
        # clears out any data left over
        for label in self.labels:
            self.entries[label].delete(0, tk.END)

    def return_to_wel(self):
        self.parent.account = None
        self.parent.switch_to("welcome")
    
    def attempt_create_account(self):
        inputs = {key: entry.get() for key, entry in self.entries.items()}
        compare_functions = [str_ver.valid_name, str_ver.valid_password, str_ver.valid_phone_num,
                              str_ver.valid_email, str_ver.valid_birthday, str_ver.valid_sex, str_ver.valid_insurance]
        all_valid = [fun(inputs[name]) for fun, name in zip(compare_functions, self.labels)]
        if False not in all_valid:
            self.parent.account.create_account(inputs["Name"], inputs["Password"], inputs["Phone Number"], 
                                               inputs["Email"], inputs["Birthday"], inputs["Sex"], inputs["Insurance Provider"])
            self.parent.create_acc()
            self.parent.switch_to("profile")


class PofileNavBar(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="Profile")
        self.title.pack()

        self.to_profile_button = ttk.Button(self, text="Profile", command=self.go_to_profile)
        self.to_profile_button.pack(side="right")

        self.to_pat_list = ttk.Button(self, text="Medications", command=self.view_meds)
        self.to_pat_list.pack(side="left")
    
    def go_to_profile(self):
        self.parent.switch_to("profile")
    
    def view_meds(self):
        self.parent.switch_to("view meds")


class Profile(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="Profile")
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
        self.parent.switch_to("edit profile")
    
    def logout(self):
        self.parent.account = None
        self.parent.med_manager = None
        self.parent.switch_to("welcome")


class EditProfile(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="EditProfile")
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
            self.parent.switch_to("profile")
    
    def die(self):
        print("DELETE ACCOUNT")
        # deletes the account, medication list and report for this user
        self.parent.med_manager.deleteMedsFiles()
        self.parent.account.delete_account()
        self.parent.account = None
        self.parent.med_manager = None
        self.parent.switch_to("welcome")


class ViewMeds(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="View Meds")

        self.list_container = tk.Canvas(self)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.list_container.yview)

        self.list_container.configure(yscrollcommand=self.scrollbar.set)
        self.list_container.bind('<Configure>', 
                lambda e: self.list_container.configure(scrollregion=self.list_container.bbox("all")))

        self.list_frame = ttk.Frame(self.list_container)
        self.list_container.create_window((0, 0), window=self.list_frame, anchor="nw")

        add_button = ttk.Button(self, text="Add Medication", command=self.add_med)

        self.title.pack()
        add_button.pack()
        self.list_container.pack(side="left", fill="both")
        self.scrollbar.pack(side="right", fill="y")
        

        self.med_frames = []
    
    def update_frame(self):
        # load medication data
        self.all_meds = self.parent.med_manager.getMedsList()
        # remove any frames that already exist
        for frame in self.med_frames:
            frame.pack_forget()
        self.med_frames = []
        # repack the list frame
        for med in self.all_meds:
            self.med_frames.append(ttk.Frame(self.list_frame))
            self.med_frames[-1].pack(fill="x")

            med_name = ttk.Label(self.med_frames[-1], text=med["name"])
            med_name.pack(side="left")
            
            edit_button = ttk.Button(self.med_frames[-1], text="View", command=lambda m=med: self.view_med(m))
            edit_button.pack(side="left")
             
 
    def view_med(self, medication: dict):
        self.parent.broadcast = medication
        self.parent.switch_to("view med x")
    
    def add_med(self):
        self.parent.broadcast = dict()
        self.parent.switch_to("edit med x")
        

class ViewMedX(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="View Med")
        self.title.pack()

        self.labels = [tk.Label(self, text="<NAME>"), tk.Label(self, text="<CONDITIONS>"), 
                       tk.Label(self, text="<SEVERITY>"), tk.Label(self, text="<TIMES TO TAKE>")]
        for label in self.labels:
            label.pack(anchor="w")

        edit_button = ttk.Button(self, text="Edit", command=self.edit_med)
        edit_button.pack(anchor="s")

        gen_rep_button = ttk.Button(self, text="Generate Report", command=self.gen_report)
        gen_rep_button.pack(anchor="s")

        delete_button = ttk.Button(self, text="Delete Medication", command=self.delete_med)
        delete_button.pack(anchor="s")

    def update_frame(self):
        # recive message and delete it
        if self.parent.broadcast == None:
            print("No medication input was given")
            self.parent.switch_to("view meds")
            return
        # get the message and DELETE it from the broadcast to stop something else from getting it
        self.med_x = self.parent.broadcast
        self.parent.broadcast = None
        self.labels[0].config(text=self.med_x["name"])
        self.labels[1].config(text=self.med_x["conditions"])
        self.labels[2].config(text=self.med_x["severity"])
        # saves times as dicts in array
        times_as_str = [self.med_x['time1'], self.med_x['time2'], self.med_x['time3']]
        final_str = ""
        for time, i in zip(times_as_str, range(1,len(times_as_str)+1)):
            # filtering out any times that don't exist
            if(time['hours'] != -1 and time['minutes'] != -1):
                # formatting times
                final_str = final_str + f"Time {i}: {time['hours']}:{time['minutes']:02}\n"
        final_str = "Times to Take At: \n" + final_str#[:-2]
        self.labels[3].config(text=final_str)

    def edit_med(self):
        self.parent.broadcast = self.med_x
        self.parent.switch_to("edit med x")
    
    def gen_report(self):
        print("Not yet, lol")

    def delete_med(self):
        self.parent.med_manager.removeMedicaiton(self.med_x["name"])
        self.parent.switch_to("view meds")


class EditMedX(ttk.Frame):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.parent = parent

        self.title = tk.Label(self, text="ViewMedX")
        self.title.pack()

        self.widgets = [(ttk.Label(self, text="Name:"), ttk.Entry(self)),
                        (ttk.Label(self, text="Conditions:"), ttk.Entry(self)),
                        (ttk.Label(self, text="Severity:"), ttk.Entry(self)),
                        (ttk.Label(self, text="Time 1:"), ttk.Entry(self)),
                        (ttk.Label(self, text="Time 2:"), ttk.Entry(self)),
                        (ttk.Label(self, text="Time 3:"), ttk.Entry(self))]

        for label, entry in self.widgets:
            label.pack(anchor="w")
            entry.pack(anchor="w")
        
        save_button = ttk.Button(self, text="Save", command=lambda:self.finish_edit(True))
        save_button.pack(anchor="e")

        cancel_button = ttk.Button(self, text="Cancel", command=lambda:self.finish_edit(False))
        cancel_button.pack(anchor="e")
    
    def update_frame(self):
        # recive message and delete it
        if self.parent.broadcast == None:
            print("No medication input was given")
            self.parent.switch_to("view meds")
        self.med_x = self.parent.broadcast
        self.parent.broadcast = None
        # clear any items left over in the entries from other edits
        for label, entry in self.widgets:
            entry.delete(0, tk.END)
        # if the med_x is being edited, update the labels
        if self.med_x:
            # saves times as dicts in array
            times_as_str = [self.med_x['time1'], self.med_x['time2'], self.med_x['time3']]
            self.widgets[0][1].insert(0, self.med_x["name"])
            self.widgets[1][1].insert(0, self.med_x["conditions"])
            self.widgets[2][1].insert(0, self.med_x["severity"])
            for time, index in zip(times_as_str, range(1,len(times_as_str)+1)):
                # filtering out any times that don't exist
                if(time['hours'] != -1 and time['minutes'] != -1):
                    # formatting and displaying times
                    self.widgets[2 + index][1].insert(0, f"{time['hours']}:{time['minutes']:02}")

    def finish_edit(self, save: bool):
        if save:
            all_inputs = [widget[1].get() for widget in self.widgets]
            all_filtered_inputs = all_inputs[:3] + [time for time in all_inputs[3:] if time != ""]
            validate_functs = [str_ver.valid_conditions, str_ver.valid_conditions, str_ver.valid_severity, str_ver.valid_time, str_ver.valid_time, str_ver.valid_time]
            valid_inputs = [fun(user_in) for fun, user_in in zip(validate_functs, all_filtered_inputs)]
            if False in valid_inputs or len(valid_inputs) < 3:
                print("Invalid input? ", False in valid_inputs)
                print("No time given? ", len(valid_inputs) < 3)
                return
            # convert the times into the correct format for the med_manager
            final_inputs = all_filtered_inputs[:2] + [int(all_filtered_inputs[2])] + [list(map(int, time.split(":"))) for time in all_filtered_inputs[3:]]
            # remove the existing medication if we are editing
            if self.med_x:
                self.parent.med_manager.removeMedicaiton(self.med_x["name"])
            # add medication
            if len(final_inputs) == 4:
                self.parent.med_manager.addMedication(name=final_inputs[0], conditions=final_inputs[1], severity=final_inputs[2], time1=final_inputs[3])
            elif len(final_inputs) == 5:
                self.parent.med_manager.addMedication(name=final_inputs[0], conditions=final_inputs[1], severity=final_inputs[2], time1=final_inputs[3], time2=final_inputs[4])
            elif len(final_inputs) == 6:
                self.parent.med_manager.addMedication(name=final_inputs[0], conditions=final_inputs[1], severity=final_inputs[2], time1=final_inputs[3], time2=final_inputs[4], time3=final_inputs[5])
            # rebuild the dict to broadcast to the view med x
            new_med = self.parent.med_manager.findMed(final_inputs[0])
            self.parent.broadcast = new_med
            self.parent.switch_to("view med x")
        else:
            # if the changes are being canceled, broadcast the original medication info or nothing
            if self.med_x:
                self.parent.broadcast = self.med_x
                self.parent.switch_to("view med x")
            else:
                self.parent.switch_to("view meds")

        


if __name__ == "__main__":
    MainWindow().mainloop()
