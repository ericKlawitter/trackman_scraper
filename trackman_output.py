import csv
from pathlib import Path
from trackman_html_constants import data_points
import os


class TrackmanOutput:
    def __init__(self, date, report_id, club):
        self.date = date
        self.file_name = 'out/' + club + '.csv'
        # stat headers - e.g. ball speed, club path, etc. Assume all the same for each club for now
        self.shots = []
        self.headers = ['Date', 'ReportId', 'ShotNum'] + data_points
        self.club = club
        self.report_id = report_id

    def write(self):
        file = Path(self.file_name)
        if file.is_file():
            self.shots = self.combine_existing_rows()
            os.remove(self.file_name)
        self.write_new_file()

    def combine_existing_rows(self):
        with open(self.file_name, 'r') as original_file:
            reader = csv.DictReader(original_file, fieldnames=self.headers)
            next(reader, None) # skip header for existing file
            keys = {(self.report_id, self.date, shot['ShotNum']): shot for shot in self.shots}
            combined_shots = []
            for row in reader:
                key = (row['ReportId'], row['Date'], row['ShotNum'])
                if key in keys:
                    combined_shots.append(row.update(keys[key]))
                    del keys[key]
                else:
                    combined_shots.append(row)
            combined_shots.extend(keys.values())
            return combined_shots


    def write_new_file(self):
        with open(self.file_name, 'w') as output_file:
            writer = csv.DictWriter(output_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL,
                                    fieldnames=self.headers)
            writer.writeheader()
            for shot in self.shots:
                writer.writerow(shot)

    def add_shot(self, stats):
        self.shots.append(stats)


"""
    def append_file(self):
        with open(self.file_name + '_TMPT', 'r') as original_file, open(self.file_name, 'a') as new_file:
            writer = csv.DictWriter(output_file, fieldnames=self.headers)
            reader = csv.DictReader(output_file, fieldnames=self.headers)
            for row in reader:
                for shot in self.shots:
                    if row['ReportId'] == self.report_id and row['Date'] == self.date and row['ShotNum'] == shot['ShotNum']:
                        row.update(shot)
                        writer.writerow(row)
                    else:
                        writer.writerow(shot)
"""


