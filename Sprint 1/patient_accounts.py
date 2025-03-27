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
        with open("allPatients.json", mode="w", encoding="utf-8") as f:
            json.dump(all_records, f, indent=4)
            f.close()

    # TODO update an account
    # TODO delete an account


if __name__ == "__main__":
    temp = PatientAccount()
    temp.create_account("John Doe", "notapassword999", "8048040845", "yeet@none.com", "12-31-1880", "M", "none")
    print(temp.patient_account)