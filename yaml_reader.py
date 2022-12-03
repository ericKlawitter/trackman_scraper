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
    grouped_stats = []
    if 'clubs' in config:
        club_stats = config['clubs']
        all_stats = club_stats['all'] if 'all' in club_stats else {}
        for shot in shots:
            # Group by club and report_id only
            # for each stat in club, apply group[swing_stat].config_stat
           if shot.club in club_stats:
               pass
           elif all_stats:
                pass

'''
{'clubs': [{'all': [{'height': ['median']}, {'path': ['stdev', 'median']}, 
{'faceToPath': ['stdev', 'median']}, {'clubSpeed': ['median']}, 
{'ballSpeed': ['median']}, {'impactHeight': ['median', 'stdev']}, 
{'impactOffset': ['median', 'stdev']}, {'swingDir': ['median']},
 {'carry': ['median', 'stdev']}, {'side': ['median', 'stdev']}, {'spinRate': ['median']}]}]}
'''



def get_grouped_stats():
    file_name="conf/grouped_stats.yaml"
    with open(file_name, 'r') as stream:

        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print("error loading yaml", e)
