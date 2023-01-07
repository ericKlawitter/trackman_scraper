from shot import Shot
from grouped_output import GroupedRow, GroupedStat
import statistics

club_8Iron = '8Iron'

rep1_shot1 = Shot(club_8Iron, '234', 1, '12/10/2022', {
    'Height': 133,
    'Side': 20.2,
    'Ball Speed': 118.9,
    'Spin Rate': 7015,
    'ShotNum': 1,
    'Date': '12/10/2022'
})
rep2_shot1 = Shot(club_8Iron, '123', 1, '12/22/2022',
                  {
                      "Height": 100,
                      "Face To Path": 1.1,
                      "Carry": 270.8,
                      'Club Path': -1.3,
                      'Low Point': '1.1 A',
                      'ShotNum': 1,
                      'Date': '12/22/2022'
                  })
rep2_shot2 = Shot(club_8Iron, '123', 2, '12/22/2022',
                  {
                      'Height': 94,
                      'Face To Path': -0.7,
                      'Total': 154.2,
                      'Dyn. Loft': 20.9,
                      'Spin Axis': -3.8,
                      'ShotNum': 2,
                      'Date': '12/22/2022'
                  })

grouped_stat_1 = GroupedStat('Height', max, [100, 94, 55])
grouped_stat_2 = GroupedStat('Height', statistics.stdev, [100, 94, 55])
grouped_stat_3 = GroupedStat('Carry', statistics.median, [190, 169, 186, 182])

start_date = '10/31/2022'
end_date = '11/28/2022'

grouped_row_1 = GroupedRow(club_8Iron, [grouped_stat_1, grouped_stat_2], start_date, end_date)
grouped_row_2 = GroupedRow('6Iron', [grouped_stat_3], start_date, end_date)
