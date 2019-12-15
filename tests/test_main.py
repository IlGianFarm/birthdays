import unittest
from main import parse_allowed_repos
import os


class TestMain(unittest.TestCase):
    def setUp(self):
        # note: this would be better done with tempfile
        self.temporary_file = "/tmp/emptycsv"
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_csv(self):
        u, r = parse_allowed_repos(datafile="/tmp/nonexistentcsv")
        self.assertFalse(u)
        self.assertFalse(r)

    def test_empty_csv(self):
        u, r = parse_allowed_repos(datafile=self.temporary_file)
        self.assertFalse(u)
        self.assertFalse(r)

    def tearDown(self):
        os.remove(self.temporary_file)

if __name__ == "__main__":
    unittest.main()