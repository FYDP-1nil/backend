import uuid
import random


def simulateGame(league_uuid, home: str, away:str, home_roster:list[str], away_roster:list[str]) -> None:
    # Simulate a league game between home and away with n events per quarter
    game_uuid = uuid.uuid4()
    print(f"insert into basketballgames(id,leagueId,home,away,starttime) values ('{game_uuid}','{league_uuid}','{home}','{away}','2023-02-23T22:42:43+00:00');")
    for q in range(1,5):
        for n in range(0, 100):
            event_uuid = uuid.uuid4()
            play_type = random.choice(['point','foul','turnover','block','steal','rebound'])
            teams = [home, away]
            teamFor, teamAgainst = random.sample(teams, 2)
            # insert event into the database
            print(f"insert into basketballgameevents(id,gameId,playType,period,teamFor,teamAgainst) values ('{event_uuid}','{game_uuid}','{play_type}',{q},'{teamFor}','{teamAgainst}');")

            # insert sub-tables based on play type
            if play_type == 'point':
                point = random.choice([1,2,3])
                result = random.choice(['made', 'miss'])
                assist = random.choice([True, False])
                if result == 'miss':
                    assist = False
                if teamFor == home:
                    player = random.choice(home_roster)
                    if assist:
                        players_without_scorer = [p for p in home_roster if p != player]
                        assist_player = random.choice(players_without_scorer)
                        print(f"insert into basketballpoints(eventId,player,assist,result,point) values ('{event_uuid}', '{player}', '{assist_player}', '{result}', {point});")
                    else: # no assist
                        print(f"insert into basketballpoints(eventId,player,result,point) values ('{event_uuid}','{player}','{result}',{point});")
                else: # TeamFor == teamB
                    player = random.choice(away_roster)
                    if assist:
                        players_without_scorer = [p for p in away_roster if p != player]
                        assist_player = random.choice(players_without_scorer)
                        print(f"insert into basketballpoints(eventId,player,assist,result,point) values ('{event_uuid}', '{player}', '{assist_player}', '{result}', {point});")
                    else: # no asssit
                        player = random.choice(away_roster)
                        print(f"insert into basketballpoints(eventId,player,result,point) values ('{event_uuid}','{player}','{result}',{point});")
            elif play_type == 'foul':
                player = random.choice(home_roster) if teamFor == home else random.choice(away_roster)
                print(f"insert into basketballfouls(eventId,player,reason) values ('{event_uuid}','{player}','{random.choice(['Holding', 'Pushing'])}');")
            elif play_type == 'steal':
                player = random.choice(home_roster) if teamFor == home else random.choice(away_roster)
                print(f"insert into basketballsteals(eventId,player) values ('{event_uuid}','{player}');")
            elif play_type == 'block':
                player = random.choice(home_roster) if teamFor == home else random.choice(away_roster)
                print(f"insert into basketballblocks(eventId,player) values ('{event_uuid}','{player}');")
            elif play_type == 'rebound':
                player = random.choice(home_roster) if teamFor == home else random.choice(away_roster)
                print(f"insert into basketballrebounds(eventId,player) values ('{event_uuid}','{player}');")
            elif play_type == 'turnover':
                player = random.choice(home_roster) if teamFor == home else random.choice(away_roster)
                print(f"insert into basketballturnovers(eventId,player) values ('{event_uuid}','{player}');")
            else:
                print(f"Invalid play type")



if __name__ == '__main__':
    user_uuid = uuid.uuid4()
    print(f"insert into users values ('{user_uuid}', 'iram', 'iram_1nil@gmail.com', 'somehash');")

    # create 3 leagues
    league1_uuid = uuid.uuid4()
    print(f"insert into leagues values ('{league1_uuid}', 'basketball', 'Small Ballers', 'password');")
    league2_uuid = uuid.uuid4()
    print(f"insert into leagues values ('{league2_uuid}', 'basketball', 'Medium Ballers', 'password');")
    league3_uuid = uuid.uuid4()
    print(f"insert into leagues values ('{league3_uuid}', 'basketball', 'Big Ballers', 'password');")



    playersTeamA = ['Adam', 'Alain', 'Abby', 'Abdul', 'Alice']
    playersTeamB = ['Banin', 'Bonnie', 'Ben', 'Barry', 'Beckham']
    playersTeamC = ['Cody', 'Caleb', 'Cauchy', 'Cameron', 'Camel']
    playersTeamD = ['Daniel', 'Denver', 'Dickson', 'Dapper', 'Doppler']

    simulateGame(league1_uuid, "TeamA", "TeamB", playersTeamA, playersTeamB)
    simulateGame(league1_uuid, "TeamC", "TeamD", playersTeamC, playersTeamD)
    simulateGame(league1_uuid, "TeamA", "TeamC", playersTeamC, playersTeamD)
    simulateGame(league1_uuid, "TeamB", "TeamC", playersTeamC, playersTeamD)
    simulateGame(league1_uuid, "TeamD", "TeamA", playersTeamC, playersTeamD)
