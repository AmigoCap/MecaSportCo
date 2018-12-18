import json

match_lower = {}

with open("match1.json") as json_file:  
    data = json.load(json_file)
    
    events = [data['events'][40]] #in order to keep only the first event

match_lower["gameid"]="0021500061"
match_lower["gamedate"] ="2015-11-04"
match_lower["events"]=events

pos_players_ball = match_lower['events'][0]['moments']

pos_reduce = pos_players_ball[100:150]

with open('match_lower.txt', 'w') as outfile:  
    json.dump(match_lower, outfile)
    
new = open("pos_reduce_observable.txt","w")
new.write(str(pos_reduce))