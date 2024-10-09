import pandas as pd
import unittest
import employee
import student

class TestEmployee(unittest.TestCase):
    def test_get_fullname(self):
        # "bob marley"
        firstname = 'Bob'
        lastname = 'Marley'
        self.assertTrue(employee.get_fullname(firstname, lastname), 
                        f"{firstname.lower()} {lastname.lower()}")

    def test_get_average(self):
        df = pd.read_csv("sample_employees.csv")
        salary = df['salary']

        self.assertTrue(employee.get_average(salary),
                        salary.mean())

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


