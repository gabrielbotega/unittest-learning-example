'''Here we're going to write the tests.
You must imagine that I've wrote these tests before the feature code. "  def  project_price(self) -> float: pass"'''

import unittest
from feature import Projects

class TestProject(unittest.TestCase):
    #create a setup that will be used in all tests
    def setUp(self) -> None:
        self.project1 = Projects(client= "Google")
    ####### start to write the actual tests tests
    def test_value_porj_is_float(self):
        '''testing if the result is float'''
        self.assertIsInstance(self.project1.project_price(),float)
    
    def test_price_hour(self):
        '''testing returned value of my hour'''
        self.assertAlmostEqual(self.project1.project_price(),100.0)

    def test_price_hour_on_10hr_proj(self):
        '''testing returned value of 10 hour proj'''
        self.project1.hours_needed = 10
        self.assertAlmostEqual(self.project1.project_price(),1000.0)

    def test_price_hour_on_10hr_proj_easy_mode(self):
        '''testing returned value of 10 hour easy proj'''
        self.project1.hours_needed = 10
        self.project1.complexity_level('easy')
        self.assertAlmostEqual(self.project1.project_price(),1000.0)

    def test_price_hour_on_10hr_proj_medium_mode(self):
        '''testing returned value of 10 hour medium proj'''
        self.project1.hours_needed = 10
        self.project1.complexity_level('medium')
        self.assertAlmostEqual(self.project1.project_price(),1500.0)
   
    def test_price_hour_on_10hr_proj_hard_mode(self):
        '''testing returned value of 10 hour hard proj'''
        self.project1.hours_needed = 10
        self.project1.complexity_level('hard')
        self.assertAlmostEqual(self.project1.project_price(),2000.0)
    
    def test_price_hour_on_10hr_proj_hard_mode_with_visit(self):
        '''testing returned value of 10 hour hard proj'''
        self.project1.hours_needed = 10
        self.project1.complexity_level('hard')
        self.project1.need_visit = True
        self.project1.visit_times = 5
        self.assertAlmostEqual(self.project1.project_price(),2500.0)




if __name__ == "__main__":
    unittest.main()