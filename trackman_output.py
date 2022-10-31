import csv
from pathlib import Path


class TrackmanOutput:
    def __init__(self, date, report_id, headers, club):
        self.date = date
        self.file_name = 'out/' + club + '.csv'
        # stat headers - e.g. ball speed, club path, etc. Assume all the same for each club for now
        self.shots = []
        self.headers = headers
        self.club = club
        self.report_id = report_id

    def write(self):
        file = Path(self.file_name)
        if file.is_file():
            self.append_file()
        else:
            self.write_new_file()

    def append_file(self):
        with open(self.file_name, 'a') as output_file:
            writer = csv.writer(output_file)
            for shot in self.shots:
                writer.writerow(shot + [self.date, self.report_id])

    def write_new_file(self):
        with open(self.file_name, 'w') as output_file:
            writer = csv.writer(output_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(self.headers + ['Date', 'ReportId'])
            for shot in self.shots:
                writer.writerow(shot + [self.date, self.report_id])

    def add_shot(self, stats):
        self.shots.append(stats)

