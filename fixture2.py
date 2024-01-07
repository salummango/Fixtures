# DATES ARE NOT IN THE SAME WEEK AND ARE REPEATED IN ALL ROUNDS
import json
from datetime import datetime, timedelta

def load_rules_from_json(file_path):
    """Load rules from a JSON file."""
    with open(file_path, 'r') as file:
        rules = json.load(file)
    return rules

def generate_double_round_robin_fixtures(teams, rules):
    """Generates a double round robin schedule with dates based on the given teams and rules."""

    num_teams = len(teams)
    num_rounds = 2 * (num_teams - 1)
    matches = []

    start_date_str = next(rule['value'] for rule in rules if rule['name'] == 'LeagueStartDate')
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

    # Inside the loop for each round
    for i in range(num_rounds):
        round_matches = []

        # Split teams into two halves
        half = num_teams // 2
        first_half = teams[:half]
        second_half = teams[half:]

        match_date = start_date  # Reset match date for each round

        # Match teams from the first half with those in the second half
        for j in range(half):
            if i % 2 == 0:
                home_team, away_team = first_half[j], second_half[-(j + 1)]
            else:
                home_team, away_team = second_half[-(j + 1)], first_half[j]

            # Assign dates based on rules
            weekend_rule = next(rule for rule in rules if rule['name'] == 'WeekendScheduling')
            while match_date.strftime('%A') not in weekend_rule['value']:
                match_date += timedelta(days=1)

            round_matches.append((home_team, away_team, match_date.strftime('%Y-%m-%d')))
            match_date += timedelta(days=1)

        # Rotate teams for the next round
        teams = teams[1:] + teams[:1]

        matches.append(round_matches)

    return matches, start_date

if __name__ == "__main__":
    num_teams = int(input("Enter the number of teams: "))
    teams = []

    for i in range(num_teams):
        team_name = input(f"Enter the name of team {i+1}: ")
        teams.append(team_name)

    rules = load_rules_from_json('rule.json')
    fixtures, start_date = generate_double_round_robin_fixtures(teams, rules)

    print("\nGenerated Fixtures:\n")
    for round_num, round_matches in enumerate(fixtures):
        print(f"Round {round_num + 1}: ({start_date.strftime('%Y-%m-%d')} to {start_date + timedelta(days=6)})")
        for match in round_matches:
            print(f"{match[0]} vs {match[1]} - {match[2]}")
        print()
