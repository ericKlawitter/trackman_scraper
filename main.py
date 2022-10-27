import argparse
import scraper

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="The URL of the trackman report", metavar="url", type=str)
args = parser.parse_args()

if args.url:
    scraper.scrape(args.url)
