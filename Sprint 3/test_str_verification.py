import unittest
from str_verification import * 

class TestStrVer(unittest.TestCase):
    # testing valid_name
    def test_case_1(self):
        self.assertTrue(valid_name("John Smith"))
    
    def test_case_2(self):
        self.assertFalse(valid_name("A "))
        self.assertFalse(valid_name("Ab "))
        self.assertFalse(valid_name("1233"))
        self.assertFalse(valid_name("!@@##$$%^"))
    
    # testing valid_password
    def test_case_3(self):
        self.assertTrue(valid_password("ALL123%$"))
    
    def test_case_4(self):
        self.assertFalse(valid_password("Allletters"))
        self.assertFalse(valid_password("$h0rt"))
        self.assertFalse(valid_password("NEEds123special"))
        self.assertFalse(valid_password("No#numbers!!!"))
    
    # testing valid_phone_num
    def test_case_5(self):
        self.assertTrue(valid_phone_num("1231231234"))
        self.assertTrue(valid_phone_num("(123)123-1234"))
    
    def test_case_6(self):
        self.assertFalse(valid_phone_num("123123"))
        self.assertFalse(valid_phone_num("(1)123-1234"))
        self.assertFalse(valid_phone_num(""))
        self.assertFalse(valid_phone_num("ABCD!@#$%^&*"))
    
    # testing valid_email
    def test_case_7(self):
        self.assertTrue(valid_email("johnD0e@lol3.com"))
    
    def test_case_8(self):
        self.assertFalse(valid_email("@."))
        self.assertFalse(valid_email("noat.com"))
        self.assertFalse(valid_email("no@dotcom"))
        self.assertFalse(valid_email(""))
        self.assertFalse(valid_email("email$%^@end#%&.co)(*&)"))

    # testing valid_institution_name
    def test_case_9(self):
        self.assertTrue(valid_institution_name("AllAlpha123Num8943 Characters123"))
    
    def test_case_10(self):
        self.assertFalse(valid_institution_name("!@#$%^&*&^%$#@"))
        self.assertFalse(valid_institution_name(""))

    # testing valid_conditions
    def test_case_11(self):
        self.assertTrue(valid_conditions("AllAlpha123Num8943 Characters123"))
    
    def test_case_12(self):
        self.assertFalse(valid_conditions("!@#$%^&*&^%$#@"))
        self.assertFalse(valid_conditions(""))
    
    # testing valid_severity
    def test_case_13(self):
        for x in range(1,6):
            self.assertTrue(valid_severity(str(x)))
    
    def test_case_14(self):
        self.assertFalse(valid_severity("6"))
        self.assertFalse(valid_severity("0"))
        self.assertFalse(valid_severity(""))
        self.assertFalse(valid_severity("11"))
        self.assertFalse(valid_severity("TRDGRESJYTHGFhjtrdhtrfjytrduyjt"))
    
    # testing valid_time
    def test_case_15(self):
        self.assertTrue(valid_time("0:0"))
        self.assertTrue(valid_time("23:59"))
    
    def test_case_16(self):
        self.assertFalse(valid_time("-1:-1"))
        self.assertFalse(valid_time("24:60"))
        self.assertFalse(valid_time("B:A"))
        self.assertFalse(valid_time(""))
    
    # testing valid_birthday
    def test_case_17(self):
        self.assertTrue(valid_birthday("01-01-2001"))
        self.assertTrue(valid_birthday("12-31-2001"))
    
    def test_case_18(self):
        self.assertFalse(valid_birthday("71-81-4991"))
        self.assertFalse(valid_birthday(""))
        self.assertFalse(valid_birthday("aehliuaehv,kwbfb"))
        self.assertFalse(valid_birthday("GARBIGE   12-31-2001"))
        self.assertFalse(valid_birthday("12-31-2001GARBIGE   "))
    
    # testing valid_sex
    def test_case_19(self):
        for x in ["m", "M", "male", "MALE", "f", "F", "female", "FEMALE"]:
            self.assertTrue(valid_sex(x))
    
    def test_case_20(self):
        self.assertFalse(valid_sex(""))
        self.assertFalse(valid_sex("woeiusdfkhjoyiuvcxmnbefhu"))
        self.assertFalse(valid_sex("Q"))
        self.assertFalse(valid_sex("10298347785463")),
        self.assertFalse(valid_sex("!@#$%^&*&^%$#$%^&*"))

    # testing valid_insurance
    def test_case_21(self):
        self.assertTrue(valid_insurance("AllAlpha123Num8943 Characters123"))
    
    def test_case_22(self):
        self.assertFalse(valid_insurance("!@#$%^&*&^%$#@"))
        self.assertFalse(valid_insurance(""))

if __name__ == "__main__":
    unittest.main()