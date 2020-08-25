print("Hello! Welcome to the Game.")
name = input("Enter your name:")
age = int(input("Enter your age:"))
choice = input("Do you wanna play(yes/no):").lower()
health = 20

if choice == "yes":
    print("you have total", health, "health")
    side = input("which side you wanna go(left/right):").lower()

    if side == "left":
        ch = input("There is a river ahead of you. you go(around/over) the river:"
        ).lower()

        if ch == "around":
            print("you are across.")
        elif ch == "over":
            print("you are bitten by a croc and lost 5 health.")
            health -= 5

        print("there is a house.")
        ch1 = input("you wanna go in or not(in/out):").lower()

        if ch1 == 'in':
            print("there are zombies there and you got eaten by them and die....")
        elif ch1 == 'out':
            print("there is an axe and many zombies.")
            ans = input("do you wanna fight or run(fight/run):").lower()

            if ans == 'run':
                print("the zombies grabbed you and you die.")
            elif ans == 'fight':
                print("you won but lost 10 health.")
                health -= 10

                if health <= 0:
                    print("your health is 0 and you die.")
                else:
                    print("there are other seviors here.")
                    ans = input("you wanna go with them or go your own way(my way/join them): ").lower()

                    if ans == 'join them':
                        print("they have medicin your health is restored now.")
                        print("you Won!")
                    else:
                        print("your wounds were too deep so you die.")

    else:
        print("you fall down the a clif and die.")

else:
    print("Bye!")
