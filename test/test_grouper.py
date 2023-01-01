from unittest import TestCase
import yaml_reader
import grouper
import test.test_objects as tObj


class TestGrouper(TestCase):

    def test_group_stats_stats(self):
        conf = yaml_reader.get_config('resources/groups.yaml')
        grouper.group_stats(conf, [tObj.rep1_shot1, tObj.rep2_shot1, tObj.rep2_shot2])

    def test_group_stats_groups(self):
        pass
    