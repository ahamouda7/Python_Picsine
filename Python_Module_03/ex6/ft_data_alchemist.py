import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()

    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")
    capitalized_l = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {capitalized_l}")
    only_capitalize = [p for p in players if (p[0] >= 'A' and p[0] <= 'Z')]
    print(f"New list of capitalized names only: {only_capitalize}")
    print()

    players_dict = {p: random.randint(200, 1000) for p in capitalized_l}
    print(f"Score dict: {players_dict}")
    average = sum(players_dict[p] for p in players_dict) / len(players)
    print(f"Score average is {round(average, 2)}")

    high_score = {n: players_dict[n] for n in players_dict
                  if players_dict[n] > average}
    print(f"High score: {high_score}")
