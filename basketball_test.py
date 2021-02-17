from constants import TEAMS, PLAYERS

clean = PLAYERS.copy()

clean_ = {'name': '',
        'guardians': '',
        'height' : [],
        'experience' : []}

def height_to_int(lst_of_dict = clean):
    for d in lst_of_dict:
        num = d['height'].split(' ')[0]
        num = int(num)
        clean_['height'].append(num)

def xp_to_bool(lst_of_dict = clean):
    for d in lst_of_dict:
        xp = d['experience'].split(' ')[0]
        if xp.lower() == 'yes':
            xp = True
        elif xp.lower() == 'no':
            xp = False
        clean_['experience'].append(xp)


height_to_int(clean)        
xp_to_bool(clean)

print(clean_)
