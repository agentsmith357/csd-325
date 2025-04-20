import unittest
from city_function import city_country

class UnitTester(unittest.TestCase):
    def test_city_country(self):
        call_one = city_country("santiago", "chile")
        call_two = city_country("santiago", "chile",population="5000000")
        call_three = city_country("santiago", "chile",population="5000000",language="spanish")

        self.assertEqual(call_one, "Santiago, Chile")
        self.assertEqual(call_two, "Santiago, Chile - population 5000000")
        self.assertEqual(call_three, "Santiago, Chile - population 5000000 - language spanish")

        print(call_one)
        print(call_two)
        print(call_three)

if __name__ == "__main__":
    unittest.main()