import unittest
from solution.main import welcomeUser

class TestWelcomeApp(unittest.TestCase):
    def test_single(self):
        assert("Welcome, Nikita" == welcomeUser("Nikita"))

if __name__ == '__main__':
    unittest.main()