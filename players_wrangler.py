import numpy as np
import pandas as pd
import re

data = open('players_raw_data.txt').read()
data = re.sub(r'<[^>]*>', '', data)
data = re.sub(r'^\s*$', '', data)
data = data.split('\n')
data = [line for line in data if len(line) > 0]
data = [line for line in data if not line.count('Hits')]
data = [line for line in data if not line.count('Traits')]
data = [line for line in data if not line.count('Potential')]
data = [line for line in data if not line.count('Long shots')]
data = [line for line in data if not line.count('Crossing')]
data = [line for line in data if not line.count('Defensive')]
data = [line for line in data if not line.count('Attacking')]
data = [line for line in data if not line.count('Penalties')]
data = [line for line in data if not line.count('Preferred')]
data = [line for line in data if not line.count('Finishing')]
data = [line for line in data if not line.count('Stamina')]
data = [line for line in data if not line.count('Aggression')]
data = [line for line in data if not line.count('Sliding')]
data = [line for line in data if not line.count('Agility')]
data = [line for line in data if not line.count('Composure')]
data = [line for line in data if not line.count('Dribbling')]
data = [line for line in data if not line.count('Ball control')]
data = [line for line in data if not line.count('handling')]
data = [line for line in data if not line.count('Nationality')]
data = [line for line in data if not line.count('Skill')]
# print(q.strip())
# for i, line in enumerate(data):
#     print(i, line)

data[318] = 'West Ham United'
data[338] = 'Watford'
data[430] = 'West Bromwich Albion'
data[674] = 'Stoke City'
data[878] = 'Leicester City'
data[922] = 'Watford'
data[942] = 'Stoke City'
data[1082] = 'Crystal Palace'
data[1118] = 'Swansea City'
data[1282] = 'Huddersfield Town'
data[1342] = 'Newcastle United'
data[1362] = 'Watford'
data[1586] = 'Swansea City'
data[1670] = 'Huddersfield Town'
data[1746] = 'Huddersfield Town'

names = []
i = 0
while i < len(data):
    names.append(data[i])
    i += 4

teams = []
i = 2
while i < len(data):
    team = ''.join([letter for letter in data[i] if letter.isalpha() or letter == ' ']).strip()
    teams.append(team)
    i += 4

feet = []
inches = []
pounds = []
acceleration = []
speed = []
shot_power = []
i = 3
while i < len(data):
    feet.append(int(data[i].split("'")[0]))
    inches.append(int(data[i].split("'")[1].split('"')[0]))
    pounds.append(int(data[i].split("'")[1].split('"')[1].split('lbs')[0]))
    rest = int(data[i].split("'")[1].split('"')[1].split('lbs')[1])
    acceleration.append(int(rest//10000))
    speed.append(int(rest // 100 % 100))
    shot_power.append(int(rest % 100))
    i += 4

df = pd.DataFrame([])
df['Name'] = names
df['Team'] = teams
df['Feet'] = feet
df['Inches'] = inches
df['Pounds'] = pounds
df['Acceleration'] = acceleration
df['Speed'] = speed
df['Shot_power'] = shot_power
df['Centimeters'] = np.round(2.54 * (df['Feet'] * 12 + df['Inches']))
df['Kilograms'] = np.round(0.453592 * df['Pounds'])
df['Radius'] = (df['Centimeters'] - 160) // 10 + 21
del df['Feet']
del df['Inches']
del df['Pounds']
print(df['Centimeters'].min())
print(df['Centimeters'].max())
print(df['Radius'].min())
print(df['Radius'].max())
print(df['Kilograms'].min())
print(df['Kilograms'].max())
df.to_csv(open('players.csv', 'w'), index_label='Index')
