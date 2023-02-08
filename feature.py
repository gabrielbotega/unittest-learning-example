from dataclasses import dataclass
from functools import partial

'''
idea here is to learn how to use pytest/unittest and use TDD
'''
'''
Imagine that you work for yourself and want to create a code that computes how much you should charge for each project
'''


@dataclass
class Projects:
    '''basic info'''
    client: str
    hour_rate: float = 100.0 #my hour price
    hours_needed: int = 1 #how much the proj will consume
    complexity: float = 1 #proj's complexity
    need_visit: bool = False
    visit_cost: float = 100.0
    visit_times: int = 0 #making it 0 forces the addition

    def complexity_level(self, level):
        comp_level = {'easy': 1, 'medium': 1.5, 'hard': 2}
        self.complexity = comp_level[level]

    def  project_price(self) -> float:
        price = self.hour_rate*self.hours_needed*self.complexity + self.visit_cost*self.visit_times if self.need_visit else 0.0
        return price