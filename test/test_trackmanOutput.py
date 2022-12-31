from unittest import TestCase
import trackman_output
import test.test_objects as test_obj
import os
from pathlib import Path
from test.assertions import assertEqualStrings


class TestTrackmanOutput(TestCase):

    f_name = 'out/8Iron_TEST.csv'

    def tearDown(self):
        if Path(self.f_name).is_file():
            os.remove(self.f_name)

    def test_combine_existing_rows(self):
        self.write_test_csv()
        with open(self.f_name, 'r') as original_file:
            reader = trackman_output.new_csv_reader(original_file)
            next(reader, None)  # skip header for existing file
            for row in reader:
                assertEqualStrings(row['Date'], test_obj.rep1_shot1.date)
                assertEqualStrings(row['ReportId'], test_obj.rep1_shot1.report_id)
                assertEqualStrings(row['ShotNum'], test_obj.rep1_shot1.shot_num)
                assertEqualStrings(row['Height'], test_obj.rep1_shot1.stats['Height'])
                assertEqualStrings(row['Side'], test_obj.rep1_shot1.stats['Side'])
                assertEqualStrings(row['Spin Rate'], test_obj.rep1_shot1.stats['Spin Rate'])
        sut = trackman_output.TrackmanOutput(test_obj.rep2_shot1.date, test_obj.rep2_shot1.report_id,
                                             test_obj.rep2_shot1.club, [test_obj.rep2_shot1, test_obj.rep2_shot2],
                                             '_TEST')
        sut.write()
        with open(self.f_name, 'r') as upd_file:
            reader = trackman_output.new_csv_reader(upd_file)
            next(reader, None) # Skip Header
            s1 = next(reader, None)
            assertEqualStrings(s1['Date'], test_obj.rep1_shot1.date)
            assertEqualStrings(s1['ShotNum'], test_obj.rep1_shot1.shot_num)
            assertEqualStrings(s1['Height'], test_obj.rep1_shot1.stats['Height'])

            s2 = next(reader, None)
            assertEqualStrings(s2['ShotNum'], test_obj.rep2_shot1.shot_num)
            assertEqualStrings(s2['ReportId'], test_obj.rep2_shot1.report_id)
            assertEqualStrings(s2['Face To Path'], test_obj.rep2_shot1.stats['Face To Path'])
            assertEqualStrings(s2['Carry'], test_obj.rep2_shot1.stats['Carry'])

            s3 = next(reader, None)
            assertEqualStrings(s3['ShotNum'], test_obj.rep2_shot2.shot_num)
            assertEqualStrings(s3['Date'], test_obj.rep2_shot2.date)
            assertEqualStrings(s3['Total'], test_obj.rep2_shot2.stats['Total'])
            assertEqualStrings(s3['Dyn. Loft'], test_obj.rep2_shot2.stats['Dyn. Loft'])

    def write_test_csv(self):
       with open(self.f_name, 'w') as test_file:
           writer = trackman_output.new_csv_writer(test_file)
           writer.writeheader()
           writer.writerow(test_obj.rep1_shot1.stats)
