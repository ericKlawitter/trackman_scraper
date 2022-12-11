import statistics
from collections import defaultdict

grouped_stats_conf = {
    'median': statistics.median,
    'stdev': statistics.stdev,
    'max': max,
    'min': min,
    'avg': statistics.mean,
}


def group_stats(config, shots):
    grouped_stats = []
    if 'clubs' in config:
        all = config['clubs']['all'] ## TODO support by club settings
        if 'stats' in all:
            process_stats(all['stats'], shots)
        if 'groups' in all:
            process_groups(all['groups'], shots)




        club_stats = config['clubs']
        all_stats = club_stats['all'] if 'all' in club_stats else {}
        for shot in shots:
            # Group by club and report_id only
            # for each stat in club, apply group[swing_stat].config_stat
           if shot.club in club_stats:
               pass
           elif all_stats:
                pass

def process_stats(stat_config, shots):
    aggregated_sessions = defaultdict(list)
    for shot_key, shot in shots.items():
        aggregated_sessions[(shot_key['Club'], shot_key['Date'], shot_key['ReportId'])].append(shot)

    grouped_stats = {}
    for stat, funcs in stat_config.items():
        for session, shots in aggregated_sessions.items():
            for func in funcs:
                pass

def process_groups(group_config, shots):
    pass

'''
{"clubs":
{"all":[{"stats":[{"height":["median"]},{"path":["stdev","median"]},{"faceToPath":["stdev","median"]},
\{"clubSpeed":["median"]},{"ballSpeed":["median"]},{"impactHeight":["median","stdev"]},
{"impactOffset":["median","stdev"]},{"swingDir":["median"]},{"carry":["median","stdev"]},
{"side":["median","stdev"]},{"spinRate":["median"]}]},

{"groups":[{"shots":[15,30,45,60]},{"daysBack":[10,20,30,50,75]}]}]}}

'''