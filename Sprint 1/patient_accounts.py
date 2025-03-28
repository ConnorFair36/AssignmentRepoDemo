import json

# handles the creation, update and deletion of a new patient account, and loads in the current patient medications
# into the medsList.json
# id|name|password|phone#|email|birthday|sex|insuranceProvider
def _get_all_records() -> list[dict]:
    all_records = []
    try:
        with open("allPatients.json", mode="r", encoding="utf-8") as f:
            try:
                all_records = json.load(f)
            except json.decoder.JSONDecodeError:
                pass
    except FileNotFoundError:
        print(f"File 'allPatients.json' not found! Aborting")
        exit(1)
    f.close()
    return all_records

def _update_records(all_records: list[dict]) -> None:
    with open("allPatients.json", mode="w", encoding="utf-8") as f:
        json.dump(all_records, f, indent=4)
        f.close()

class PatientAccount:
    def __init__(self):
        self.patient_account = {}

    def find_account(self, name: str, password: str) -> bool:
        """Finds an account by name and password in allPatients.json.
            :return: True if the account was found, False otherwise.
        """
        # gets all the records from allPatients.json
        all_records = _get_all_records()
        # matches the name and password inputted and returns true if it is in the list
        all_names_and_passwords = [[r["name"], r["password"]] for r in all_records]
        try:
            index = all_names_and_passwords.index([name, password])
            self.patient_account = all_records[index]
        except ValueError:
            return False
        return True

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
        all_records = _get_all_records()
        next_id = all_records[-1]["id"] + 1
        self.patient_account = {"id": next_id,
                     "name": name,
                     "password": password,
                     "phone": phone_number,
                     "email": email,
                     "birthday": birthday,
                     "sex": sex,
                     "insurance provider": insur_prov}
        all_records.append(self.patient_account)
        _update_records(all_records)

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
        self.patient_account.update(filtered_changes)
        # updates the account in the .json file
        all_records = _get_all_records()
        all_id = [r["id"] for r in all_records]
        all_records[all_id.index(self.patient_account["id"])].update(filtered_changes)
        _update_records(all_records)

    def delete_account(self) -> None:
        """Deletes the current user's account from allPatients.json and this object.
        :return: None"""
        all_records = _get_all_records()
        all_id = [r["id"] for r in all_records]
        all_records.remove(self.patient_account)
        _update_records(all_records)
        self.patient_account = {}


if __name__ == "__main__":
    temp = PatientAccount()
    temp.find_account("John Doe", "notapassword999")
    print(temp.patient_account)
    temp.update_account(insur_prov="I'm too broke :(")
    print(temp.patient_account)
    temp.delete_account()
    print(temp.patient_account)