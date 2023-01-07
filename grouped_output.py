import csv

class GroupedStat:
    def __init__(self, stat_name, func, data):
        self.stat = stat_name
        self.func = func
        self.func_name = func.__qualname__
        self.result = round(func(data), 3)
        self.csv_header = self.stat + '_' + self.func_name
        self.shots = len(data)

class GroupedRow:
    def __init__(self, club, grouped_stats, start_date, end_date):
        self.club = club
        self.grouped_stats = grouped_stats
        self.num_shots = max(x.shots for x in grouped_stats)
        self.start_date = start_date
        self.end_date = end_date

    def data_map(self):
        d = {
            'Club': self.club,
            'StartDate': self.start_date,
            'EndDate': self.end_date,
            'NumShots': self.num_shots,

        }
        for st in self.grouped_stats:
            d[st.csv_header] = st.result
        return d

field_names = ['Club', 'StartDate', 'EndDate', 'NumShots']

def get_group_headers(grouped_rows):
    res = set()
    for grouped_row in grouped_rows:
        for stat in grouped_row.grouped_stats:
            res.add(stat.csv_header)
    return list(res)


def get_headers(grouped_rows):
    return field_names + get_group_headers(grouped_rows)


def grouped_csv_writer(csvfile, grouped_rows):
    return csv.DictWriter(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL,
                              fieldnames=get_headers(grouped_rows))

def write_grouped(f_name, grouped_rows):
    with open(f_name, 'w') as csvfile:
        writer = grouped_csv_writer(csvfile, grouped_rows)
        writer.writeheader()
        for grouped_row in grouped_rows:
            writer.writerow(grouped_row.data_map())

