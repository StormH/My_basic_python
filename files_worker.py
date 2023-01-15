# import csv
#
# with open('schedules.csv', 'w', newline='') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     filewriter.writerow(['departure point',  'departure time', 'destination point', 'arrival time', 'cost ticket'])
#     filewriter.writerow(['earth', '12:00', 'moon', '18:00', '100uah'])
#     filewriter.writerow(['earth', '13:00', ' jupiter', '19:00', '200uah'])
#     filewriter.writerow(['earth', '14:00', ' Mars', '20:00', '300uah'])
#
# with open('schedules.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(f"{row['departure point']=}, {row['departure time']=},"
#               f"{row['destination point']=},{row['arrival time']=}, {row['cost ticket']}")
#
##################################################################################################################
import json

data = {}
data['schedule'] = []
data['schedule'].append({
    'departure point': 'Earth',
    'departure time': '12:00',
    'destination point': 'Moon',
    'arrival time': '17:00',
    'ticket cost': '200uah'
})
data['schedule'].append({
    'departure point': 'Earth',
    'departure time': '13:00',
    'destination point': 'Jupiter',
    'arrival time': '18:00',
    'ticket cost': '300uah'
})
data['schedule'].append({
    'departure point': 'Earth',
    'departure time': '12:00',
    'destination point': 'Mars',
    'arrival time': '19:00',
    'ticket cost': '400uah'
})

with open('schedule.json', 'w') as outfile:
    json.dump(data, outfile)

print(f"{data, outfile =}")
