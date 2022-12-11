import argparse
import scraper
import yaml_reader
from trackman_output import TrackmanOutput
import grouper


def output_all(shots):
    for k, v in shots.items():
        output = TrackmanOutput(k['Date'], k['ReportId'], k['Club'], v)
        output.write()

parser = argparse.ArgumentParser()
parser.add_argument("--grouped", help="Indicates output should be grouped according to "
                                      "group_stats.yaml instead of including all shots",
                    const=True, default=False, metavar="grouped", nargs='?')
args = parser.parse_args()
urls = yaml_reader.get_config("conf/urls.yaml")['urls']

if urls:
    all_shots = []
    for url in urls:
        all_shots.extend(scraper.get_all_shots(args.url))
        output_all(all_shots)
    if args.grouped:
        group_config = yaml_reader.get_config('conf/grouped_stats.yaml')
        grouper.group_stats(group_config, all_shots)



