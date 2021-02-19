from constants import PLAYERS

panthers = []
bandits = []
warriors = []
clean_me = PLAYERS.copy()

#takes "(num) inches" and turns it into to a int
def height_to_int(height_str):
    num = height_str.split(' ')[0]
    return int(num)

#takes yes or no and changes to True or False
def xp_to_bool(xp_str):
    xp = xp_str.split(' ')[0]
    if xp.lower() == 'yes':
        xp = True
    elif xp.lower() == 'no':
        xp = False
    return xp

#takes a list of dicts and loops through preforming the previous functions and replacing the values
def clean_data(clean_me):
    for d in clean_me:
        d['height'] = height_to_int(d['height'])
        d['experience'] = xp_to_bool(d['experience'])

#puts every 3rd player into a different team, I was wondering if we should balance by experience or not
def assign_teams(player_lst):
    for i, d in enumerate(player_lst):
        if i % 3 == 0:
            panthers.append(d)
        elif i % 2 == 0:
            warriors.append(d)
        elif i % 1 == 0:
            bandits.append(d)

#prints various stats about the team
def stats(team):
    xp = 0
    non_xp = 0
    total_players = len(team)
    total_height =  0
    for d in team:
        if d['experience']:
            xp += 1
        else:
            non_xp += 1
        total_height += d['height']
    avg_height =  total_height / total_players
    print(f'\n Total players: {total_players} \n Total experienced: {xp} \n Total inexperienced: {non_xp} \n Average height: {avg_height} \n')

#prints the teams players and their gaurdians
def players_and_guardians(team):
    player_names = []
    guardian_names = []
    for d in team:
        player_names.append(d['name'])
        guardian_names.append(d['guardians'])
    print(f'Players on Team: \n    {", ".join(player_names)} \n\n Guardians: \n    {", ".join(guardian_names)}')

if __name__ == "__main__":

    print(f'\n BASKETBALLL TEAM STATS TOOL \n \n ----MENU---- \n \n Here are your choices: \n A) Display Team Stats \n B) Quit \n ')

    show = input('Enter an option (A/B):  ')
    while show.upper() != 'A' and show.upper() != 'B':
        print('that is not a valid input')
        show = input('Enter an option (A/B):  ')

    clean_data(clean_me)
    assign_teams(clean_me)

    #asks user to select team, and prints their stats, players, and guardians
    if show.upper() == 'A':
        print(f'\n A) Panthers \n B) Bandits \n C) Warriors \n ')
        select_team = input('Enter an option (A/B/C):  ')
        if select_team.upper() == 'A':
            print(stats(panthers))
            print(players_and_guardians(panthers))
        elif select_team.upper() == 'B':
            print(stats(bandits))
            print(players_and_guardians(bandits))
        elif select_team.upper() == 'C':
            print(stats(warriors))
            print(players_and_guardians(warriors))
