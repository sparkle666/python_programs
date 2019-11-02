import time, random

team = "Barca"; list_of_players = ["Ter Ster Gen", "Jordi Alba", "Gerrard Pique", 
"Semedo", "Arthur Melo", "Coutinho", "Dembele", "Suarez", "Messi"]

gtime = 90; half_time = 45; 
goals_scored = 0

start_com = ["We are underway at Camp nou.", "And we are off with Barca attacking from left to right.",
"The match begins at Camp nou.", "The refree blows the whistle to begin the match."]

goal_com = ["Goal!! Bullet header from", "Its in. Lovely goal by", "Goooooooal!!!", "Sublime finish from",
"Mesmerizing goal from", "Screamer!!!", "Goal!! From 25 yards!!! By",
"Takes on 2 players and leaves a couple more for dead. Then slots it through the legs of the goalkeeper. By"]

miss_com = ["Missed!!! By ", "Miss!!!", "What a poor finish by", "Easy for the goalkeeper to parry!",
"Hits the cross bar by", "What a miss!!! By"]

half_time_com = ["The refree signals the end of first half.", "Its half time at Camp Nou"]

full_time_com = ["And its the end of the match. Lovely match from both sides", 
"The ref blows the whistle to signal full time"]

injury_com = ["Bad tackle! Limping now is", "Injury on"]

offside_com = ["Offside again from", "The flag is raised for offside against"]

yellow_com = ["A straight Yellow card to", "The referee pulls a Yellow on", "Goes into the book is" ]

def list_event_player(lists, player, ti):
	#This prints event plus the player name
	lent = len(lists)
	text = lists[random.randrange(lent)]
	player1 = list_of_players[random.randrange(1, 9)]
	print("%d':" % ti, text, player1)

def list_event(lists, ti):
	#This prints events that dont need player name like halftime, fulltime
	lent = len(lists)
	text = lists[random.randrange(lent)]
	print("%d':" % ti, text)

def start():
	for x in range(gtime):
		if x == 0:
			list_event(start_com, x)
		if x == 4:
			list_event_player(goal_com, list_of_players, x)
		if x == 8:
			list_event_player(miss_com, list_of_players, x)
		if x == 10:
			list_event_player(miss_com, list_of_players, x)
		if x == 14:
			list_event_player(miss_com, list_of_players, x)
		if x == 18:
			list_event_player(injury_com, list_of_players, x)
		if x == 20:
			list_event_player(miss_com, list_of_players, x)
		if x == 24:
			list_event_player(yellow_com, list_of_players, x)
		if x == 28:
			list_event_player(miss_com, list_of_players, x)
		if x == 34:
			list_event_player(offside_com, list_of_players, x)
		if x == 36:
			list_event_player(miss_com, list_of_players, x)
		if x == 40:
			list_event_player(goal_com, list_of_players, x)
		if x == 44:
			list_event_player(injury_com, list_of_players, x)
		if x == 48:
			list_event_player(goal_com, list_of_players, x)
		if x == 54:
			list_event_player(offside_com, list_of_players, x)
		if x == 58:
			list_event_player(goal_com, list_of_players, x)
		if x == 60:
			list_event_player(injury_com, list_of_players, x)
		if x == 64:
			list_event_player(goal_com, list_of_players, x)
		if x == 67:
			list_event_player(yellow_com, list_of_players, x)
		if x == 69:
			list_event_player(goal_com, list_of_players, x)
		if x == 70:
			list_event_player(miss_com, list_of_players, x)
		if x == 73:
			list_event_player(miss_com, list_of_players, x)
		if x == 78:
			list_event_player(yellow_com, list_of_players, x)
		if x == 80:
			list_event_player(goal_com, list_of_players, x)
		if x == 82:
			list_event_player(miss_com, list_of_players, x)
		if x == 84:
			list_event_player(miss_com, list_of_players, x)
		if x == 85:
			list_event_player(injury_com, list_of_players, x)
		if x == 86:
			list_event_player(goal_com, list_of_players, x)
		if x == 87:
			list_event_player(yellow_com, list_of_players, x)
		if x == 88:
			list_event_player(miss_com, list_of_players, x)

		if x == half_time:
			list_event(half_time_com, x)
			time.sleep(3)
		if x == 89 :
			list_event(full_time_com, x)
		time.sleep(1.2)
start()