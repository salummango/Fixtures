# MATCHES ARE BALANCED
def generate_double_round_robin_fixtures(teams):
    """Generates a double round robin schedule for the given teams."""
    
    num_teams = len(teams)
    num_rounds = 2 * (num_teams - 1)
    matches = []

    for i in range(num_rounds):
        round_matches = []

        # Split teams into two halves
        half = num_teams // 2
        first_half = teams[:half]
        second_half = teams[half:]

        # Match teams from first half with those in second half
        for j in range(half):
            if i % 2 == 0:
                round_matches.append((first_half[j], second_half[-(j + 1)]))
            else:
                round_matches.append((second_half[-(j + 1)], first_half[j]))

        # Rotate teams for the next round
        teams = teams[1:] + teams[:1]

        matches.append(round_matches)

    return matches

if __name__ == "__main__":
    num_teams = int(input("Enter the number of teams: "))
    teams = []

    for i in range(num_teams):
        team_name = input(f"Enter the name of team {i+1}: ")
        teams.append(team_name)

    fixtures = generate_double_round_robin_fixtures(teams)

    print("\nGenerated Fixtures:\n")
    for round_num, round_matches in enumerate(fixtures):
        print(f"Round {round_num + 1}:")
        for match in round_matches:
            print(f"{match[0]} vs {match[1]}")
        print()
