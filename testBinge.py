import unittest
from binge_party import getTitleJSONData, getProvJsonData, printProvResults

class TestBinge(unittest.TestCase):
    def test_getTitleJSONData(self):
        api_key = '25cd471bedf2ee053df9b1705494367d'
        title = 'avengers'
        f_type = 'movie'
        self.assertNotEqual(getTitleJSONData(api_key, title, f_type), None)

    def test_getProvJSONData(self):
        f_type = 'tv'
        resultID = '268'
        api_key = '25cd471bedf2ee053df9b1705494367d'
        self.assertTrue('US' in getProvJsonData(f_type, resultID, api_key))


if __name__ == '__main__':
    unittest.main()
