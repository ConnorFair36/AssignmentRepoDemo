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

	def create_account(self, new_account: dict[str, str | int]) -> None:
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
		if self.account:
			self.all_records.remove(self.account)
			self.__update_records()
			self.account = {}


# id|name|password|phone#|email|birthday|sex|insuranceProvider
class PatientAccount(_Account):
	def __init__(self):
		super().__init__("allPatients.json")

	def create_account(self, name: str, password: str, phone_number: str, email: str, birthday: str, sex: str,
					   insur_prov: str) -> None:
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

	def update_account(self, name="", password="", phone_number="", email="", birthday="", sex="",
					   insur_prov="") -> None:
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
		self.patient_list = []

	# methods for handling the doctor account
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

	def find_account(self, name: str, password: str) -> bool:
		output = super().find_account(name, password)
		self.patient_list = self._get_patient_list()
		return output

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

	# methods for handling the patient list
	def __get_patient_doc_list(self) -> list:
		all_records = []
		try:
			with open("doctorPatients.json", mode="r", encoding="utf-8") as f:
				try:
					all_records = json.load(f)
				except json.decoder.JSONDecodeError:
					pass
		except FileNotFoundError:
			print(f"File 'doctorPatients.json' not found! Aborting")
			exit(1)
		f.close()
		return all_records

	def _get_patient_list(self) -> list[int]:
		"""find the record with the same ID as the doctor to get the list of Patient id's
		:return: list of Patient id's."""
		all_records = self.__get_patient_doc_list()
		all_keys = [list(i.keys())[0] for i in all_records]
		try:
			if self.account:
				index = all_keys.index(str(self.account["id"]))
				return list(all_records[index].values())[0]
		except ValueError:
			return []
		return []

	def __update_patient_list(self) -> None:
		# gets all doctor to patient pairings and puts them in a list
		all_patients = self.__get_patient_doc_list()
		all_keys = [list(i.keys())[0] for i in all_patients]
		# add the updated patient list to the list
		try:
			index = all_keys.index(str(self.account["id"]))
			# if the doctor already has patients, update the existing list
			if len(self.patient_list) == 0:
				# if the doctor has no more patients, remove them from the list
				all_patients.pop(index)
			else:
				all_patients[index][str(self.account["id"])] = self.patient_list
		except ValueError:
			# if the doctor doesn't have patients, append the doctor's list to the end of the file
			all_patients.append({str(self.account["id"]): self.patient_list})

		with open("doctorPatients.json", mode="w", encoding="utf-8") as f:
			json.dump(all_patients, f, indent=4)
			f.close()

	def add_patient(self, name: str) -> bool:
		# gets all the patients from the allPatients.json
		all_patients = []
		try:
			with open("allPatients.json", mode="r", encoding="utf-8") as f:
				try:
					all_patients = json.load(f)
				except json.decoder.JSONDecodeError:
					pass
		except FileNotFoundError:
			print(f"File 'allPatients.json' not found! Aborting")
			exit(1)
		f.close()
		# finds the name in the list, if found the id is added to the list and true is returned
		# else nothing is added and false is returned
		all_names = [r["name"] for r in all_patients]
		try:
			index = all_names.index(name)
			self.patient_list.append(index)
			self.__update_patient_list()
			new_id = all_patients[index]["id"]
			if new_id not in all_patients:
				self.patient_list.append(new_id)
				self.__update_patient_list()
		except ValueError:
			return False
		return True

	def remove_patient(self, pid: int) -> None:
		self.patient_list.remove(pid)
		self.__update_patient_list()


if __name__ == "__main__":
	temp = DoctorAccount()
	temp.find_account("Alice Morgan", "securePass123!")
	print(temp.account)
	print(temp.patient_list)
	temp.add_patient("Sophia Martinez")
	print(temp.patient_list)
	temp.remove_patient(5)
	print(temp.patient_list)
	# temp.update_account(email="no@maybe.net")
	# print(temp.account)
	# temp.delete_account()