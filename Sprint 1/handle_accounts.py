import json

# handles the creation, update and deletion of a patient or doctor account
class _Account:
    def __init__(self, filename: str):
        self.filename = filename
        self.account = {}
        self.all_records = self.__get_all_records()

    def __get_all_records(self) -> list[dict]:
        all_records = []
        try:
            with open(self.filename, mode="r", encoding="utf-8") as f:
                try:
                    all_records = json.load(f)
                except json.decoder.JSONDecodeError:
                    pass
        except FileNotFoundError:
            print(f"File 'allPatients.json' not found! Aborting")
            exit(1)
        f.close()
        return all_records

    def __update_records(self) -> None:
        with open(self.filename, mode="w", encoding="utf-8") as f:
            json.dump(self.all_records, f, indent=4)
            f.close()

    def find_account(self, name: str, password: str) -> bool:
        """Finds an account by name and password in the account type's .json.
                    :return: True if the account was found, False otherwise.
                """
        all_names_and_passwords = [[r["name"], r["password"]] for r in self.all_records]
        try:
            index = all_names_and_passwords.index([name, password])
            self.account = self.all_records[index]
        except ValueError:
            return False
        return True

    def create_account(self, new_account: dict[str, str|int]) -> None:
        self.account = new_account
        self.all_records.append(new_account)
        self.__update_records()

    def update_account(self, filtered_changes: dict[str, str]) -> None:
        self.account.update(filtered_changes)
        all_id = [r["id"] for r in self.all_records]
        self.all_records[all_id.index(self.account["id"])].update(filtered_changes)
        self.__update_records()

    def delete_account(self) -> None:
        """Deletes the current user's account from this Account types .json file and this object.
        :return: None"""
        self.all_records.remove(self.account)
        self.__update_records()
        self.account = {}

# id|name|password|phone#|email|birthday|sex|insuranceProvider
class PatientAccount(_Account):
    def __init__(self):
        super().__init__("allPatients.json")

    def create_account(self, name: str, password: str, phone_number: str, email: str, birthday: str, sex: str, insur_prov: str) -> None:
        """creates a new account and saves it in allPatients.json.
        :param name: The name of the new account.
        :param password: <PASSWORD>.
        :param phone_number: all 10 digits with no parentheses or dashes.
        :param email: Email address.
        :param birthday: MM-DD-YYYY format.
        :param sex: 'M' or 'F' ONLY.
        :param insur_prov: Insurance provider name.
        :return: None"""
        next_id = 0 if len(self.all_records) == 0 else self.all_records[-1]["id"] + 1
        new_patient_account = {"id": next_id,
                     "name": name,
                     "password": password,
                     "phone": phone_number,
                     "email": email,
                     "birthday": birthday,
                     "sex": sex,
                     "insurance provider": insur_prov}
        super().create_account(new_patient_account)

    def update_account(self, name="", password="", phone_number="", email="", birthday="", sex="", insur_prov="") -> None:
        """Updates an existing account and saves it in allPatients.json.
        :param name: The updated name of the account.
        :param password: <PASSWORD>.
        :param phone_number: all 10 digits with no parentheses or dashes.
        :param email: Email address.
        :param birthday: MM-DD-YYYY format.
        :param sex: "M" or "F" ONLY.
        :param insur_prov: Insurance provider name.
        :return: None"""
        changes_dict = {"name": name,
                        "password": password,
                        "phone": phone_number,
                        "email": email,
                        "birthday": birthday,
                        "sex": sex,
                        "insurance provider": insur_prov}
        filtered_changes = {key: value for key, value in changes_dict.items() if value != ""}
        # replaces all updated records in the currently stored account
        super().update_account(filtered_changes)

# userID|name|password|phone#|email|institutionName
class DoctorAccount(_Account):
    def __init__(self):
        super().__init__("allDoctors.json")

    def create_account(self, name: str, password: str, phone_number: str, email: str, institution_name: str) -> None:
        """creates a new account and saves it in allDoctors.json.
        :param name: The name of the new account.
        :param password: <PASSWORD>.
        :param phone_number: all 10 digits with no parentheses or dashes.
        :param email: Email address.
        :param institution_name: name of the doctor's institution.
        :return: None"""
        next_id = 0 if len(self.all_records) == 0 else self.all_records[-1]["id"] + 1
        new_doctor_account = {"id": next_id,
                               "name": name,
                               "password": password,
                               "phone": phone_number,
                               "email": email,
                               "institution name": institution_name}
        super().create_account(new_doctor_account)

    def update_account(self, name="", password="", phone_number="", email="", institution_name="") -> None:
        """Updates an existing account and saves it in allDoctors.json.
        :param name: The name of the new account.
        :param password: <PASSWORD>.
        :param phone_number: all 10 digits with no parentheses or dashes.
        :param email: Email address.
        :param institution_name: name of the doctor's institution.
        :return: None"""
        changes_dict = {"name": name,
                        "password": password,
                        "phone": phone_number,
                        "email": email,
                        "institution name": institution_name}
        filtered_changes = {key: value for key, value in changes_dict.items() if value != ""}
        # replaces all updated records in the currently stored account
        super().update_account(filtered_changes)

if __name__ == "__main__":
    temp = DoctorAccount()
    temp.create_account("temp Docman", "password",
                        "9876543210", "email@web.com",
                        "hell")
    print(temp.account)
    #temp.update_account(email="no@maybe.net")
    #print(temp.account)
    temp.delete_account()
    print(temp.account)