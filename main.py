import argparse
import scraper
import yaml_reader
from trackman_output import TrackmanOutput
import grouper


def output_all(shots):
    output = TrackmanOutput(shots[0].date, shots[0].report_id, shots[0].club, shots)
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
        session_shots = scraper.get_all_shots(url)
        all_shots.extend(session_shots)
        output_all(session_shots)
    if args.grouped:
        group_config = yaml_reader.get_config('conf/grouped_stats.yaml')
        grouper.group_stats(group_config, all_shots)



