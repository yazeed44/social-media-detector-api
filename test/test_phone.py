import unittest


class TestMain(unittest.TestCase):
    def test_print_factory(self):
        name: str = "bassam"
        output: str = f"Hello {name}"
        self.assertEqual(output, f"Hello {name}")
