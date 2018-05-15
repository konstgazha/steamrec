from datetime import datetime


class DataActualization:
    def month_to_number(self, string):
        month = {
            'янв.': 1,
            'фев.': 2,
            'мар.': 3,
            'апр.': 4,
            'мая.': 5,
            'июн.': 6,
            'июл.': 7,
            'авг.': 8,
            'сен.': 9,
            'окт.': 10,
            'ноя.': 11,
            'дек.': 12
        }
        return month[string]

    def convert_date(self, date):
        date = date.replace(date.split()[1],
                            str(self.month_to_number(date.split()[1])))
        return datetime.strptime(date, '%d %m %Y')

print(DataActualization().convert_date('12 мая. 2016'))