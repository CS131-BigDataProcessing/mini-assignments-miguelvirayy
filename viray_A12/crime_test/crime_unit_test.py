import unittest
from io import StringIO
from validate_functions import validate_vict_sex, validate_vict_age, load_csv
from stats_function import calculate_mean_age, calculate_median_age

class TestValidateFunctions(unittest.TestCase):

    #test data
    def setUp(self):
        self.valid_data = [
            {'Vict Sex': 'M', 'Vict Age': '25'},
            {'Vict Sex': 'F', 'Vict Age': '30'},
            {'Vict Sex': 'M', 'Vict Age': '45'},
            {'Vict Sex': 'F', 'Vict Age': '50'}
        ]
        self.invalid_data = [
            {'Vict Sex': 'M', 'Vict Age': '150'},
            {'Vict Sex': 'X', 'Vict Age': '0'},
            {'Vict Sex': '', 'Vict Age': 'None'},
            {'Vict Sex': 'F', 'Vict Age': '-5'}
        ]
    
    #test sex field validation
    def test_validate_vict_sex_valid(self):
        self.assertTrue(validate_vict_sex(self.valid_data))

    def test_validate_vict_sex_invalid(self):
        self.assertFalse(validate_vict_sex(self.invalid_data))

    #test age field validation
    def test_validate_vict_age_valid(self):
        self.assertTrue(validate_vict_age(self.valid_data))

    def test_validate_vict_age_invalid(self):
        self.assertFalse(validate_vict_age(self.invalid_data))

class TestStatsFunction(unittest.TestCase):

    def setUp(self): #test data
        self.data = [
            {'Vict Sex': 'M', 'Vict Age': '25'},
            {'Vict Sex': 'F', 'Vict Age': '30'},
            {'Vict Sex': 'M', 'Vict Age': '45'},
            {'Vict Sex': 'F', 'Vict Age': '50'},
            {'Vict Sex': 'M', 'Vict Age': '55'}
        ]

    def test_calculate_mean_age(self): #check mean calculation
        self.assertAlmostEqual(calculate_mean_age(self.data), 41, delta=0.1)

    def test_calculate_median_age(self): #check median calculation
        self.assertEqual(calculate_median_age(self.data), 45)

    def test_empty_data(self): #edge case: data is empty
        empty_data = []
        with self.assertRaises(ValueError):
            calculate_mean_age(empty_data)

if __name__ == "__main__":
    unittest.main()

