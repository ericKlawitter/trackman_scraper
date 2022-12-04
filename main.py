import argparse
import scraper
import yaml_reader

parser = argparse.ArgumentParser()
parser.add_argument("--grouped", help="Indicates output should be grouped according to "
                                      "group_stats.yaml instead of including all shots",
                    const=True, default=False, metavar="grouped", nargs='?')
args = parser.parse_args()
urls = yaml_reader.get_urls()

if urls:
    all_shots = []
    for url in urls:
        all_shots.extend(scraper.get_all_shots(args.url))
    if args.grouped:
        yaml_reader.group_stats(all_shots)

