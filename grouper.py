import statistics
from collections import defaultdict

grouped_stats_conf = {
    'median': statistics.median,
    'stdev': statistics.stdev,
    'max': max,
    'min': min,
    'avg': statistics.mean,
}

def get_by_club_shots(all_shots):
    by_club_shots = defaultdict(list)
    for shot in all_shots:
        by_club_shots[shot.club].append(shot)
    for club, club_shots in by_club_shots.items():
        sorted_club_shots = sorted(club_shots, key=lambda x: (x.date, x.shot_num))
        sorted_club_shots.reverse()
        by_club_shots[club] = sorted_club_shots
    return by_club_shots


# list of groupings based on each daysBack/shotNum defined in YAML
def group_stats(config, shots):
    if 'clubs' in config:
        all = config['clubs']['all'] ## TODO support by club settings
        if 'stats' in all and 'groups' in all:
            stats = all['stats'].items()  # e.g. Height: [stddev, median]
            groups = all['groups']
            by_club_shots = get_by_club_shots(shots)
            if 'shots' in groups:

                for num_shots in groups['shots']:
                    pass
                    # decision - both shots and daysback groupings create a single, NEW file with each file containing
                    # every grouping for every club.
            if 'daysBack' in groups:
                print(groups['daysBack'])
            return
        else:
            print("both 'stats' and 'groups' need to be defined in grouped yaml")
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