class Shot:
    def __init__(self, club, report_id, shot_num, properties):
        self.club = club
        self.report_id = report_id
        self.shot_num = shot_num
        self.stats = properties

    def key(self):
        return (self.club, self.report_id, self.shot_num)

    @staticmethod
    def from_row(row):
        return Shot(row['Club'], row['ReportId'], row['ShotNum'], row)

class GroupedShot:
    def __init__(self, club, report_id):
        self.club = club
        self.report_id = report_id