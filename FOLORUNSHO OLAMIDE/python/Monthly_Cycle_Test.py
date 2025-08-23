import unittest
from Monthly_Cycle import (get_next_period_cycle, get_ovulation_cycle, get_fertile_window_cycle, get_safe_period )
class TestMonthlyCycle(unittest.TestCase):

    
    def test_invalid_inputs_negative(self):
        self.assertRaises(ValueError, get_ovulation_cycle, -1, 28)

    def test_invalid_inputs_string(self):
        self.assertRaises(ValueError, get_fertile_window_cycle, "15")

    def test_next_period_cycle(self):
        self.assertEqual(get_next_period_cycle(1, 28), 29) 

    def test_ovulation_cycle(self):
        self.assertEqual(get_ovulation_cycle(1, 28), 15)  

    def test_fertile_window_cycle(self):
        self.assertEqual(get_fertile_window_cycle(15), [10, 16])

    def test_safe_period(self):
        self.assertEqual(get_safe_period(15, 1, 29),[1, 9, 17, 29])