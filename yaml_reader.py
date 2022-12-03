import yaml
import statistics

grouped_stats_conf = {
    'median': statistics.median,
    'stdev': statistics.stdev,
    'max': max,
    'min': min,
    'avg': statistics.mean,
}


## TODO support by club settings
def group_stats(shots):
    config = get_grouped_stats()
    club = shots[0]['Club']
    if 'clubs' in config:
        club_stats = config['clubs']
        if club in club_stats:
            pass
        elif 'all' in club_stats:
            pass


def get_grouped_stats():
    file_name="conf/grouped_stats.yaml"
    with open(file_name, 'r') as stream:

        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print("error loading yaml", e)
