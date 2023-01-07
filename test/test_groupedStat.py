from unittest import TestCase
from test.test_objects import grouped_row_1, grouped_row_2
import grouped_output
from pathlib import Path
import csv
import os
from test.assertions import assertEqualStrings


class TestGroupedStat(TestCase):

    f_name = 'out/8Iron_TEST.csv'
    grouped_rows = [grouped_row_1, grouped_row_2]

    def tearDown(self):
        if Path(self.f_name).is_file():
            os.remove(self.f_name)

    def write_test_csv(self):
        with open(self.f_name, 'w') as test_file:
            writer = grouped_output.grouped_csv_writer(test_file, self.grouped_rows)
            writer.writeheader()

    def testWriteGroupedRows(self):
        grouped_output.write_grouped(self.f_name, [grouped_row_1, grouped_row_2])
        with open(self.f_name, 'r') as upd_file:
            reader = csv.DictReader(upd_file,
                                    fieldnames=grouped_output.get_headers(self.grouped_rows))
            h = next(reader, None)
            self.assertTrue('Club' in h)
            self.assertTrue('StartDate' in h)
            self.assertTrue('EndDate' in h)
            self.assertTrue('NumShots' in h)
            r1 = next(reader, None)
            assertEqualStrings(r1['Club'], grouped_row_1.club)
            assertEqualStrings(r1['StartDate'], grouped_row_1.start_date)
            assertEqualStrings(r1['EndDate'], grouped_row_1.end_date)
            assertEqualStrings(r1['NumShots'], 3)
            assertEqualStrings(r1['Height_stdev'], 24.434)
            assertEqualStrings(r1['Height_max'], 100)
            r2 = next(reader, None)
            assertEqualStrings(r2['Club'], '6Iron')
            assertEqualStrings(r2['Carry_median'], 184.0)


