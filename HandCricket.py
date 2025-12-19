import random

RUNS = [0, 1, 2, 3, 4, 5, 6]


def toss():
    print("\nToss Time!")
    user_choice = int(input("1 Head\n2 Tail\nChoose: "))
    toss_result = random.choice(["Head", "Tail"])
    print("Toss result:", toss_result)

    if (user_choice == 1 and toss_result == "Head") or \
       (user_choice == 2 and toss_result == "Tail"):
        print("You won the toss!")
        return "user"
    else:
        print("Computer won the toss!")
        return "computer"


def batting():
    score = 0
    while True:
        user_run = int(input("Enter run: "))
        comp_run = random.choice(RUNS)
        if user_run == comp_run:
            print("Out!")
            break
        score += user_run
    print("Total Score:", score)
    return score


def bowling(target=None):
    score = 0
    while target is None or score < target:
        user_ball = int(input("Enter bowl: "))
        comp_run = random.choice(RUNS)
        print("Computer run:", comp_run)
        if user_ball == comp_run:
            print("Computer Out!")
            break
        score += comp_run
    print("Computer Total:", score)
    return score


def decide_winner(user_score, comp_score):
    if user_score > comp_score:
        print("\nYou won the match!")
    elif comp_score > user_score:
        print("\nComputer won the match!")
    else:
        print("\nMatch Draw!")


def main():
    print("Welcome to Hand Cricket!")
    play = int(input("1 Play\n2 Exit\nChoose: "))
    if play != 1:
        print("Exit")
        return

    toss_winner = toss()

    if toss_winner == "user":
        choice = int(input("1 Batting\n2 Bowling\nChoose: "))
        if choice == 1:
            user_score = batting()
            print("Target:", user_score + 1)
            comp_score = bowling(target=user_score + 1)
        else:
            comp_score = bowling()
            print("Target:", comp_score + 1)
            user_score = batting()
    else:
        comp_choice = random.choice(["Batting", "Bowling"])
        print("Computer chose:", comp_choice)

        if comp_choice == "Batting":
            comp_score = bowling()
            print("Target:", comp_score + 1)
            user_score = batting()
        else:
            user_score = batting()
            print("Target:", user_score + 1)
            comp_score = bowling(target=user_score + 1)

    decide_winner(user_score, comp_score)


if __name__ == "__main__":
    main()
