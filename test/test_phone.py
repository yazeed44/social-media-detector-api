"""docs"""
import unittest
from yocial.app_utils import verifier


class TestMain(unittest.TestCase):
    """docs"""

    def test_verifier(self):
        """
        unit test for verifier phone number logic
        """
        valid_number: str = "0591122334"
        invalid_number_long_number: str = "05911223344"
        invalid_number_short_number: str = "052111223"
        invalid_number_wrong_prefix: str = "0511122334"
        self.assertEqual(verifier(valid_number), True)
        self.assertEqual(verifier(invalid_number_long_number),
                         False, "Number length should be 10")
        self.assertEqual(verifier(invalid_number_short_number),
                         False, "Number length should be 10")
        self.assertEqual(verifier(invalid_number_wrong_prefix),
                         False, "Number should start with allowed prefix")


if __name__ == '__main__':
    unittest.main()
