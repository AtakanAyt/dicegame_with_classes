from random import randint
from time import sleep
from user import Player


# würfel Blackjack
# Spielregeln: Du fängst an zu würfeln (Zahlen zwischen 1-6). Man darf so oft würfeln bis man entweder 18 erreicht oder
# die gessamt gewürfelte zahl 18 übersteigt.
# Will man nicht mehr würfeln oder ist über 18 (bust), würfelt der Computer so oft bis er bei zwischen 16-18 ankommt.
# Wer näher an der 18 ist gewinnt das spiel.

def roll():
    result = (randint(1, 6))
    print(f"Es wurde eine {result} gewürfelt!")
    return result


def user_input(question):
    no = ["no", "n"]
    yes = ["yes", "y"]

    while True:
        decision = input(question).lower()

        if decision not in no and decision not in yes:
            print("Wrong answer")
            continue

        if decision not in no:
            return True
        else:
            return False


def get_score(player="computer"):
    score = 0
    counter = 1

    while True:
        score += roll()

        print(f"{player} rolled {counter} times")
        print(f"{player}'s score is {score}")

        if score > 18:
            print("Bust!")
            return score
        elif score == 18:
            print("Perfect dice!")
            return score

        if player != "computer":
            if not user_input("Do you want to roll again? y/n: "):
                return score

        else:
            if score > 15:
                return score

            sleep(1)

        counter += 1


def determine_cookie(computer_score, player_score, player):
    print(f"{player.get_name()} Score: {player_score}, Dicemonster Score: {computer_score}")

    if player_score > 18:
        print("Computer wins!")
        player.decrease_cookies()
        return

    if computer_score > 18:
        print(f"{player.get_name()} wins!")
        player.increase_cookies()
        return

    if player_score < computer_score:
        print("Computer wins!")
        player.decrease_cookies()
    elif player_score > computer_score:
        print(f"{player.get_name()} wins!")
        player.increase_cookies()
    else:
        print("Draw")


def get_int(question: str) -> int:
    """Checks if answer for given question is integer and returns as such."""
    while True:
        if isinstance(val := int(input(question)), int):
            return val

        print("Wrong value!")


def main():
    users = []
    player = None

    while True:
        if not user_input("Do you want to play? y/n: "):
            print("Until next time!")
            break

        name = input("Your name: ")

        if not users or name not in users:
            age = get_int("Your age: ")

            if age < 18:
                print("Too young!")
                break

            users.append(Player(name))

        for user in users:
            if name == user:
                player = user

        player_score = get_score(name)

        print("-" * 20)
        print("Computer's turn:")
        computer_score = get_score()

        determine_cookie(computer_score, player_score, player)

        users = sorted(users, key=lambda pl_user: pl_user.get_cookies(), reverse=True)

        for user in users:
            print(f"{user.get_name()} has {user.get_cookies()} cookies")


if __name__ == "__main__":
    main()
