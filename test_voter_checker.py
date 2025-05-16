import unittest
from voter_checker import is_eligible_to_vote

class TestVoterEligibility(unittest.TestCase):
    
def test_underage_voter(self):
    self.assertFalse(self.underage_voter(17,True))

def test_non_citizen_voter(self):
    self.assertFalse(self.is_eligible_to_vote(25,False))

def test_underage_non_citizen(self):
    self.assertFalse(self.is_eligible_to_vote(16,False))

def test_exactly_18_and_non_citizen(self):
     self.assertFalse(self.is_eligible_to_vote(18,False))

def test_negative_age(self):
    self.assertFalse(self.is_eligible_to_vote(-18,False))

if__name__ == "__main__":
unittest.main()
    