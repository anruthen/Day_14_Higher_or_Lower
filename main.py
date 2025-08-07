import game_data
import random
import art

def display(a,b):
    print(f"Compare A: {a["name"]} a {a["description"]}, from {a["country"]}")
    print(art.vs)
    print(f"Against B: {b["name"]} a {b["description"]}, from {b["country"]}")
    u_pick = input("Who has more followers? Type 'A' or 'B': ").lower()
    return u_pick

pick_a = random.choice(game_data.data)
pick_b = random.choice(game_data.data)

game_running = True
score = 0
print(art.logo)
user_pick = display(pick_a, pick_b)
while game_running:
    follower_count_a = pick_a["follower_count"]
    follower_count_b = pick_b["follower_count"]
    if (follower_count_a > follower_count_b and user_pick == "a") or (follower_count_a < follower_count_b and user_pick == "b"):
        score += 1
        print("\n"*20)
        print(art.logo)
        print(f"You are right! Current Score: {score}")
        pick_a = pick_b
        while pick_b == pick_a:
            pick_b = random.choice(game_data.data)
        user_pick = display(pick_a, pick_b)
    else:
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_running = False
