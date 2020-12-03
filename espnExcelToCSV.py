import xlrd
import pandas as pd

#This file is now archived as it isn't needed for the main app

path = 'football-app\defenseWebPaste.xlsx'
file = xlrd.open_workbook(path)
sheet = file.sheet_by_index(0)

class Player(object):
    def __init__(self, name, position, team, projection):
        self.name = name
        self.position = position
        self.team = team
        self.projection = projection
    def to_dict(self):
        return {
            'player_name': self.name,
            'pos': self.position,
            'team': self.team,
            'projection': self.projection,
        }

players = []
get_position = str(sheet.cell_value(2,1))

if get_position[-1] == "T":
    ROW_PER_PLAYER = 8
    NUM_PLAYERS = int(sheet.nrows / ROW_PER_PLAYER)
    for i in range(NUM_PLAYERS):
        name = sheet.cell_value(i * ROW_PER_PLAYER + 2, 1)
        name = name[:-5]
        team = name
        position = "D/ST"
        points = sheet.cell_value(i * ROW_PER_PLAYER + 4, 7)
        players.append(Player(name, position, team, points))
else:
    ROW_PER_PLAYER = 9
    NUM_PLAYERS = int(sheet.nrows / ROW_PER_PLAYER)
    for i in range(NUM_PLAYERS):
        print(i * 9)
        name = sheet.cell_value(i * ROW_PER_PLAYER + 2, 1)
        team_cell = str(sheet.cell_value(i * ROW_PER_PLAYER + 3, 1))
        print(team_cell)
        points = sheet.cell_value(i * ROW_PER_PLAYER + 6, 8)
        
        if team_cell[-1] == "K":
            position = team_cell[-1]
            team = team_cell[0:-1]
        elif str(team_cell[-2] + team_cell[-1]) == "WR" or str(team_cell[-2] + team_cell[-1]) == "TE":
            position = team_cell[-2] + team_cell[-1]
            team = team_cell[0:-2]
            points = sheet.cell_value(i * ROW_PER_PLAYER + 5, 9)
        else:
            position = team_cell[-2] + team_cell[-1]
            team = team_cell[0:-2]
        players.append(Player(name, position, team,  points))

df = pd.DataFrame.from_dict([player.to_dict() for player in players])


df.to_csv(r'football-app\\espn_Players.csv', index = False)



"""
import requests
from bs4 import BeautifulSoup

URL = 'https://fantasy.espn.com/football/players/projections'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('div', { 'class' : 'layout__column layout__column--1'})
results = results.find('div', { 'class' : 'jsx-531718297 projections-page'})
results = results.find('div', { 'class' : 'jsx-4158115014 loader'})
results = results.find('div', { 'class' : 'LoadAnimation LoadAnimation--lightBG LoadAnimation--md'})

print(results)
"""