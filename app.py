from constants import TEAMS, PLAYERS

print(f'BASKETBALLL TEAM STATS TOOL \n \n ----MENU---- \n \n Here are your choices: \n A) Display Team Stats \n B) Quit \n ')

def stats(team):
    print(f'total players:  \n')

show = input('Enter an option (A/B):  ')

if show == 'A':
    print(f'A) Panthers \n B) Bandits \n C) Warriors \n ')
    select_team = input('Enter an option (A/B/C):  ')
if select_team == 'A':
    print(stats(panthers))

