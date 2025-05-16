import unittest
from voter_checker import is_eligible_to_vote

class TestVoterEligibility(unittest.TestCase):

def test_underage_voter(self):
    self.assertFalse(self.underage_voter(17,True))
    ("underage")
def test_non_citizen_voter(self):
    self.assertFalse(self.is_eligible_to_vote(25,False))

