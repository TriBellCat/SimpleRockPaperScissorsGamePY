from random import randint


# Increases player score if player won
def pwon(playscore):
    print("You won this turn!")
    playscore += 1
    return playscore


def cwon(compscore):
    print("You lose this turn!")
    compscore += 1
    return compscore


def main():
    # List of choices: rock, paper , scissors, but with initials only
    c = ["R", "P", "S"]

    # Initializes randomness to Computer
    computer = c[randint(0, 2)]

    # The number of turns that pass
    turn = 0

    # The scores of the player and computer respectively
    pscore = 0
    cscore = 0

    while turn <= 10:
        print("Turn: ", turn)
        player = input("Type one: Rock (R), Paper (P), Scissors (S) ")
        # print("Computer chose ", computer)
        if player == computer:
            print("Tie!")
            turn += 1
        elif player == "R":
            if computer == "Paper":
                cscore = cwon(cscore)
                turn += 1
            else:
                pscore = pwon(pscore)
                turn += 1
        elif player == "P":
            if computer == "Scissors":
                cscore = cwon(cscore)
                turn += 1
            else:
                pscore = pwon(pscore)
                turn += 1
        elif player == "S":
            if computer == "Rock":
                cscore = cwon(cscore)
                turn += 1
            else:
                pscore = pwon(pscore)
                turn += 1
        else:
            print("Not a valid option!")

        computer = c[randint(0, 2)]

    print("Overall Scores")
    print("Player: ", pscore)
    print("Computer: ", cscore)

    if pscore < cscore:
        print("You lost the game...")
    elif pscore > cscore:
        print("You won the game!")
    else:
        print("It's a tie!")

    return


if __name__ == '__main__':
    # sys.argv = ["programName.py","--input","test.txt","--output","tmp/test.txt"]
    main()
