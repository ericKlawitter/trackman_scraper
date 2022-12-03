import argparse
import scraper
import yaml_reader

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="The URL of the trackman report", metavar="url", type=str,
                    nargs='+')
parser.add_argument("--grouped", help="Indicates output should be grouped according to "
                                      "group_stats.yaml instead of including all shots",
                    const=True, default=False, metavar="grouped", nargs='?')
args = parser.parse_args()

if args.url:
    all_shots = scraper.get_all_shots(args.url)
    print(all_shots)

