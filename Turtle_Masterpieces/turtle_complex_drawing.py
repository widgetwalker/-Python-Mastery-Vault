import mysql.connector
import random

# Function to get players from the selected table
def get_players_from_table(table_name):
    try:
        conn = mysql.connector.connect(
            host='localhost',        # e.g., 'localhost'
            user='root',             # your MySQL username
            password='aaaaaaa',      # your MySQL password
            database='my_game'       # your database name
        )
        cursor = conn.cursor()
        
        cursor.execute(f'SELECT * FROM {table_name}')
        players = cursor.fetchall()
        
        conn.close()
        return players
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

# Function to validate team composition
def validate_team_composition(team):
    categories = {'WK': 0, 'BOWL': 0, 'BAT': 0, 'AR': 0}
    for player in team:
        categories[player[2]] += 1
    
    # Team composition rules
    if categories['WK'] < 1:
        return False, "Team must have at least 1 wicket-keeper"
    if categories['BOWL'] < 3:
        return False, "Team must have at least 3 bowlers"
    if categories['BAT'] < 3:
        return False, "Team must have at least 3 batsmen"
    return True, "Team composition is valid"

# Function to create a team based on user selection
def create_team(players):
    team = []
    categories = {'WK': 0, 'BOWL': 0, 'BAT': 0, 'AR': 0}
    
    print("\nAvailable players:")
    for player in players:
        print(f"SNO: {player[0]}, Player Name: {player[1]}, Category: {player[2]}, Bat Rate: {player[3]}, Bowl Rate: {player[4]}")
    
    while len(team) < 11:
        selected_snos = input("\nEnter the SNOs of the players you want to select (separated by spaces): ")
        selected_snos = selected_snos.split()
        
        # Validate the selected SNOs
        for sno in selected_snos:
            try:
                sno = int(sno)
                selected_player = next((p for p in players if p[0] == sno), None)
                if selected_player and selected_player not in team:
                    player_category = selected_player[2]
                    categories[player_category] += 1
                        team.append(selected_player)
                    print(f"Added {selected_player[1]} ({player_category}) to team")
                elif selected_player in team:
                    print(f"Player {selected_player[1]} is already in team")
                else:
                    print(f"Invalid SNO: {sno}")
            except ValueError:
                print(f"Invalid input: {sno}. Please enter valid SNOs.")
        
        # Show current team composition
        print(f"\nCurrent team composition: {len(team)}/11")
        for category, count in categories.items():
            print(f"{category}: {count}")
        
        if len(team) == 11:
            is_valid, message = validate_team_composition(team)
            if not is_valid:
                print(f"\nError: {message}")
                # Remove last added players to allow reselection
                team = team[:-len(selected_snos)]
                for cat in categories:
                    categories[cat] = sum(1 for p in team if p[2] == cat)
            else:
                print("\nTeam is complete and valid!")
            break
        elif len(team) > 11:
            print("Too many players selected. Please try again.")
            team = team[:11]  # Keep only first 11 players
            for cat in categories:
                categories[cat] = sum(1 for p in team if p[2] == cat)

    return team

# Function to conduct a toss
def toss():
    return random.choice(['Heads', 'Tails'])

# Function for computer to select a team
def computer_select_team(players):
    team = []
    categories = {'WK': 0, 'BOWL': 0, 'BAT': 0, 'AR': 0}
    
    # First, select one wicket-keeper with best batting rate
    wicket_keepers = [p for p in players if p[2] == 'WK']
    if wicket_keepers:
        wk = max(wicket_keepers, key=lambda x: x[3])  # Select WK with best batting rate
        team.append(wk)
        categories['WK'] += 1
    
    # Select bowlers (at least 3) with best bowling rates
    bowlers = [p for p in players if p[2] == 'BOWL' and p not in team]
    bowlers.sort(key=lambda x: x[4], reverse=True)  # Sort by bowling rate
    selected_bowlers = bowlers[:4]  # Take top 4 bowlers
    for bowler in selected_bowlers:
        team.append(bowler)
        categories['BOWL'] += 1
    
    # Select batsmen (at least 3) with best batting rates
    batsmen = [p for p in players if p[2] == 'BAT' and p not in team]
    batsmen.sort(key=lambda x: x[3], reverse=True)  # Sort by batting rate
    selected_batsmen = batsmen[:4]  # Take top 4 batsmen
    for batsman in selected_batsmen:
        team.append(batsman)
        categories['BAT'] += 1
    
    # Fill remaining slots with all-rounders and best available players
    remaining_slots = 11 - len(team)
    if remaining_slots > 0:
        # First try to add all-rounders
        all_rounders = [p for p in players if p[2] == 'AR' and p not in team]
        all_rounders.sort(key=lambda x: x[3] + x[4], reverse=True)  # Sort by combined rates
        for ar in all_rounders[:remaining_slots]:
            team.append(ar)
            categories['AR'] += 1
            remaining_slots -= 1
        
        # If still need players, add best available
        if remaining_slots > 0:
            remaining_players = [p for p in players if p not in team]
            remaining_players.sort(key=lambda x: x[3] + x[4], reverse=True)
            for player in remaining_players[:remaining_slots]:
                team.append(player)
                categories[player[2]] += 1
    
    print("\nComputer's Selected Team:")
    for player in team:
        print(f"SNO: {player[0]}, Name: {player[1]}, Category: {player[2]}, Bat Rate: {player[3]}, Bowl Rate: {player[4]}, Runs: {player[5]}")
    
    return team

# Function to simulate computer's bowling decisions
def computer_select_bowler(available_bowlers, current_score=0, current_over=0):
    # Computer strategy: Choose bowler based on bowling rate and match situation
    if current_score < 30:  # Early game - use best bowlers
        return max(range(len(available_bowlers)), key=lambda i: available_bowlers[i][4])
    elif current_score > 100:  # High score - use aggressive bowlers
        return max(range(len(available_bowlers)), key=lambda i: available_bowlers[i][4] * 1.2)
    else:  # Mid game - mix strategy
        return max(range(len(available_bowlers)), key=lambda i: available_bowlers[i][4] + random.randint(0, 10))

# Function to simulate computer's batting decisions
def computer_select_batsman(available_batsmen, batting_team, current_score=0, wickets=0):
    if wickets >= 8:  # Last batsmen - choose highest bowling rate for defense
        return max(available_batsmen, key=lambda i: batting_team[i][4])
    elif current_score < 30:  # Early game - choose stable batsmen
        return max(available_batsmen, key=lambda i: batting_team[i][3])
    else:  # Mid/Late game - aggressive batting
        return max(available_batsmen, key=lambda i: batting_team[i][3] * 1.2)

# Function to simulate innings
def simulate_innings(batting_team, bowling_team, is_batting_computer=False, is_bowling_computer=False, target=None):
    score = 0
    wickets = 0
    extras = 0  # New variable for extras
    batsman_count = {player[0]: 0 for player in batting_team}
    bowler_count = {player[0]: 0 for player in bowling_team}
    batsman_scores = {player[0]: 0 for player in batting_team}  # Track individual scores

    valid_bowlers = [p for p in bowling_team if p[2] in ['BOWL', 'AR']]
    if len(valid_bowlers) < 5:
        print("Error: Not enough bowlers in the team (minimum 5 required)")
        return score, wickets

    current_batsman_index = [0, 1]  # [striker, non-striker]
    used_bowlers = []

    print("\nStarting innings...")
    for over in range(10):
        print(f"\n=== Over {over + 1} ===")
        striker = batting_team[current_batsman_index[0]]
        non_striker = batting_team[current_batsman_index[1]]

        available_bowlers = [b for b in valid_bowlers if bowler_count[b[0]] < 2 and b[0] not in used_bowlers[-2:]]
        if not available_bowlers:
            print("No available bowlers left. Ending innings.")
            break

        if is_bowling_computer:
            bowler_choice = computer_select_bowler(available_bowlers, score, over)
            bowler = available_bowlers[bowler_choice]
            used_bowlers.append(bowler[0])
            print(f"\nComputer selected bowler: {bowler[1]} (Bowl Rate: {bowler[4]})")
        else:
            print("\nAvailable bowlers (BOWL and AR only):")
            for i, bowler in enumerate(available_bowlers):
                print(f"{i + 1}. {bowler[1]} (SNO: {bowler[0]}, Category: {bowler[2]}, Bowl Rate: {bowler[4]})")

            while True:
                try:
                    bowler_choice = int(input("\nSelect a bowler (enter number): ")) - 1
                    if 0 <= bowler_choice < len(available_bowlers):
                        bowler = available_bowlers[bowler_choice]
                        used_bowlers.append(bowler[0])
                        break
        else:
            print("Invalid choice. Please select a valid bowler.")
                except ValueError:
                    print("Please enter a valid number.")

        print(f"\nStriker: {striker[1]} (Score: {batsman_scores[striker[0]]})")
        print(f"Non-striker: {non_striker[1]} (Score: {batsman_scores[non_striker[0]]})")
        print(f"Bowler: {bowler[1]} (Bowl Rate: {bowler[4]})")

        for ball in range(6):
            if wickets >= 10:
                print("All out!")
                break

            if target is not None and score > target:
                print(f"Target {target} achieved!")
                return score, wickets

            # Add possibility of extras
            if random.random() < 0.1:  # 10% chance of extras
                extra_runs = random.choice([1, 2, 4])  # wide or no-ball
                score += extra_runs
                extras += extra_runs
                print(f"Ball {ball + 1}: Extras +{extra_runs} runs")
            continue

            outcome = random.random() * (striker[3] + bowler[4])
            if outcome < striker[3]:  # Batsman wins
                runs = random.choice([0, 1, 2, 3, 4, 6])  # More realistic run distribution
                score += runs
                batsman_scores[striker[0]] += runs
                print(f"Ball {ball + 1}: {striker[1]} scores {runs} runs")
                
                # Rotate strike for odd runs
                if runs % 2 == 1:
                    current_batsman_index[0], current_batsman_index[1] = current_batsman_index[1], current_batsman_index[0]
                    striker, non_striker = non_striker, striker
            else:  # Bowler wins
            wickets += 1
                print(f"Ball {ball + 1}: {striker[1]} is OUT! (Score: {batsman_scores[striker[0]]})")
                
                available_batsmen = [i for i in range(len(batting_team)) 
                                  if i not in current_batsman_index 
                                  and i < 11]
                
                if not available_batsmen:
                    print("No more batsmen left!")
                    break
                
                if is_batting_computer:
                    new_batsman_idx = computer_select_batsman(available_batsmen, batting_team, score, wickets)
                    current_batsman_index[0] = new_batsman_idx
                    striker = batting_team[new_batsman_idx]
                    print(f"Computer selected new batsman: {striker[1]}")
                else:
                    print("\nAvailable batsmen:")
                    for i in available_batsmen:
                        print(f"{i + 1}. {batting_team[i][1]} (Bat Rate: {batting_team[i][3]})")
                    
                    while True:
                        try:
                            new_batsman_idx = int(input("\nSelect next batsman (enter number): ")) - 1
                            if new_batsman_idx in available_batsmen:
                                current_batsman_index[0] = new_batsman_idx
                                striker = batting_team[new_batsman_idx]
                                break
                    else:
                        print("Invalid choice. Please select a valid batsman.")
                        except ValueError:
                            print("Please enter a valid number.")

                    print(f"New batsman: {striker[1]}")

        batsman_count[striker[0]] += 1

        # End of over summary
        bowler_count[bowler[0]] += 1
        current_batsman_index[0], current_batsman_index[1] = current_batsman_index[1], current_batsman_index[0]
        print(f"\nEnd of over {over + 1}:")
        print(f"Score: {score}/{wickets} (Extras: {extras})")
        print(f"Current Run Rate: {score/(over+1):.2f}")
        if target is not None:
            runs_needed = target - score + 1
            balls_left = (10 - over - 1) * 6
            if balls_left > 0:
                required_rate = (runs_needed * 6) / balls_left
                print(f"Required Run Rate: {required_rate:.2f}")

    # Innings summary
    print("\n=== Innings Summary ===")
    print(f"Final Score: {score}/{wickets} (Extras: {extras})")
    print("\nBatting Performances:")
    for player in batting_team:
        if batsman_scores[player[0]] > 0:
            print(f"{player[1]}: {batsman_scores[player[0]]} runs")

    return score, wickets

def main():
    print("\n=== Welcome to Cricket Game - Player vs Computer! ===\n")
    
    # Player selects table and team
    player_table = input("Enter your team name (table name) to select players from: ")
    player_available = get_players_from_table(player_table)
    
    if not player_available:
        print("No players found in your team. Exiting.")
        return
    
    print("\nSelect your team:")
    player_team = create_team(player_available)
    
    # Computer selects from a different team
    computer_table = input("\nEnter computer's team name (table name) to select players from: ")
    while computer_table.lower() == player_table.lower():
        print("Computer must select from a different team!")
        computer_table = input("Enter a different team name for computer: ")
    
    computer_available = get_players_from_table(computer_table)
    if not computer_available:
        print("No players found in computer's team. Exiting.")
        return
    
    # Computer selects team from its own pool
    print("\nComputer is selecting its team...")
    computer_team = computer_select_team(computer_available)
    
    # Display both teams for comparison
    print("\n=== Team Comparison ===")
    print("\nYour Team (from " + player_table + "):")
    for player in player_team:
        print(f"Name: {player[1]}, Category: {player[2]}, Bat Rate: {player[3]}, Bowl Rate: {player[4]}")
    
    print("\nComputer's Team (from " + computer_table + "):")
    for player in computer_team:
        print(f"Name: {player[1]}, Category: {player[2]}, Bat Rate: {player[3]}, Bowl Rate: {player[4]}")
    
    # Toss
    print("\n=== Time for the Toss ===")
    toss_result = toss()
    player_wins_toss = toss_result == 'Heads'
    print(f"\nToss Result: {toss_result}")
    
    if player_wins_toss:
        print("You won the toss!")
        choice = input("Would you like to bat or bowl first? (bat/bowl): ").lower()
        while choice not in ['bat', 'bowl']:
            choice = input("Please enter either 'bat' or 'bowl': ").lower()
        player_bats_first = choice == 'bat'
    else:
        print("Computer won the toss!")
        player_bats_first = random.choice([True, False])
        print(f"Computer chose to {'bat' if not player_bats_first else 'bowl'} first")
    
    # First innings
    print("\n=== First Innings ===")
    if player_bats_first:
        print("\nYou are batting, Computer is bowling")
        score1, wickets1 = simulate_innings(player_team, computer_team, is_batting_computer=False, is_bowling_computer=True)
        print(f"\nFirst Innings Complete - Your score: {score1}/{wickets1}")
        target = score1 + 1
        print(f"\nComputer needs {target} runs to win")
        
        print("\n=== Second Innings ===")
        print("\nComputer is batting, You are bowling")
        score2, wickets2 = simulate_innings(computer_team, player_team, is_batting_computer=True, is_bowling_computer=False, target=target)
        print(f"\nSecond Innings Complete - Computer's score: {score2}/{wickets2}")
        
        if score1 > score2:
            print(f"\nCongratulations! You win by {score1 - score2} runs!")
        elif score2 > score1:
            print(f"\nComputer wins with {10 - wickets2} wickets remaining!")
        else:
            print("\nMatch tied!")
    else:
        print("\nComputer is batting, You are bowling")
        score2, wickets2 = simulate_innings(computer_team, player_team, is_batting_computer=True, is_bowling_computer=False)
        print(f"\nFirst Innings Complete - Computer's score: {score2}/{wickets2}")
        target = score2 + 1
        print(f"\nYou need {target} runs to win")
        
        print("\n=== Second Innings ===")
        print("\nYou are batting, Computer is bowling")
        score1, wickets1 = simulate_innings(player_team, computer_team, is_batting_computer=False, is_bowling_computer=True, target=target)
        print(f"\nSecond Innings Complete - Your score: {score1}/{wickets1}")
        
        if score2 > score1:
            print(f"\nComputer wins by {score2 - score1} runs!")
        elif score1 > score2:
            print(f"\nCongratulations! You win with {10 - wickets1} wickets remaining!")
        else:
            print("\nMatch tied!")

if __name__ == "__main__":
    main()