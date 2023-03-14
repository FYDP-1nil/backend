import uuid
import random


def simulateGame(league_uuid, home: str, away:str, home_roster:list[str], away_roster:list[str]) -> None:
    # Simulate a league game between home and away with N events per quarter
    N = 100
    game_uuid = uuid.uuid4()
    print(f"insert into gridirongames(id,leagueId,home,away,starttime) values ('{game_uuid}','{league_uuid}','{home}','{away}','2023-02-23T22:42:43+00:00');")
    for qtr in range(1,5):
        for _ in range(0, N):
            event_uuid = uuid.uuid4()
            play_type = random.choice(["throw", "rush", "flag", "kick", "safety", "turnover", "timeout"])
            teams = [home, away]
            teamFor, teamAgainst = random.sample(teams, 2)
            # insert event into the database
            print(f"insert into gridirongameevents(id,gameId,playType,period,teamFor,teamAgainst) values ('{event_uuid}','{game_uuid}','{play_type}',{qtr},'{teamFor}','{teamAgainst}');")

            if play_type not in ['rush', 'throw', 'kick']:
                # nothing to do
                pass
            elif play_type == 'rush':
                player = random.choice(home_roster) if teamFor == home else random.choice(away_roster)
                yard = random.randint(-10, 120)
                result = random.choice(['touchdown', 'non-scoring', '2pt']) if yard > 0 else 'non-scoring'
                print(f"insert into gridironrushes(eventId,player,yard,result) values ('{event_uuid}','{player}',{yard},'{result}');")

            elif play_type == 'throw':
                roster = home_roster if teamFor == home else away_roster
                playerThrowing = random.choice(roster)
                playerReceving = random.choice([player for player in roster if player != playerThrowing])
                yard = random.randint(-10, 120)
                result = random.choice(['touchdown', 'non-scoring', '2pt', 'miss']) if yard > 0 else random.choice(['non-scoring', 'miss'])
                print(f"insert into gridironthrows(eventId,playerThrowing,playerReceiving,yard,result) values ('{event_uuid}','{playerThrowing}','{playerReceving}','{yard}','{result}');")
            elif play_type == 'kick':
                player = random.choice(home_roster) if teamFor == home else random.choice(away_roster)
                yard = random.randint(1, 120)
                result = random.choice(['extra-kick', 'field-goal', 'miss'])
                print(f"insert into gridironkicks(eventId,player,yard,result) values ('{event_uuid}','{player}',{yard},'{result}');")

            else: # shouldn't happen
                print(f"Invalid play type")



if __name__ == '__main__':
    user_uuid = uuid.uuid4()
    print(f"insert into users values ('{user_uuid}', 'iram', 'iram_1nil@gmail.com', 'somehash');")

    # create 3 leagues
    league1_uuid = uuid.uuid4()
    print(f"insert into leagues values ('{league1_uuid}', 'gridiron', 'UW Gridiron', 'password');")
    league2_uuid = uuid.uuid4()
    print(f"insert into leagues values ('{league2_uuid}', 'gridiron', 'UofT Gridiron', 'password');")
    league3_uuid = uuid.uuid4()
    print(f"insert into leagues values ('{league3_uuid}', 'gridiron', 'York Gridiron', 'password');")



    playersTeamA = ['Adam', 'Alain', 'Abby', 'Abdul', 'Alice']
    playersTeamB = ['Banin', 'Bonnie', 'Ben', 'Barry', 'Beckham']
    playersTeamC = ['Cody', 'Caleb', 'Cauchy', 'Cameron', 'Camel']
    playersTeamD = ['Daniel', 'Denver', 'Dickson', 'Dapper', 'Doppler']

    # simulate some games for league 1
    simulateGame(league1_uuid, "TeamA", "TeamB", playersTeamA, playersTeamB)
    simulateGame(league1_uuid, "TeamC", "TeamD", playersTeamC, playersTeamD)
    simulateGame(league1_uuid, "TeamA", "TeamC", playersTeamC, playersTeamD)
    simulateGame(league1_uuid, "TeamB", "TeamC", playersTeamC, playersTeamD)
    simulateGame(league1_uuid, "TeamD", "TeamA", playersTeamC, playersTeamD)
