import unittest
from datetime import datetime


class TestDataActualization(unittest.TestCase):
    def month_to_number(self, string):
        month = {
            'сен.': 9
        }
        return month[string]

    def test_convert_date(self):
        date = '1 сен. 2015'
        date = date.replace(date.split()[1],
                            str(self.month_to_number(date.split()[1])))
        result = datetime.strptime(date, '%d %m %Y')
        self.assertEqual(result, datetime(2015, 9, 1))

if __name__ == '__main__':
    unittest.main()
