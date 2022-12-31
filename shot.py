class Shot:
    def __init__(self, club, report_id, shot_num, date, properties):
        self.club = club
        self.report_id = report_id
        self.shot_num = shot_num
        self.date = date
        self.stats = properties
        self.stats['ReportId'] = report_id
        self.stats['ShotNum'] = shot_num
        self.stats['Date'] = date

    def key(self):
        return (self.club, self.report_id, self.shot_num, self.date)

    @staticmethod
    def from_row(row):
        return Shot(row['Club'], row['ReportId'], row['ShotNum'], row['Date'], row)

