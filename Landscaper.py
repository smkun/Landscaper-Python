def main():
    money = 0
    tool = "teeth"

    while True:
        print(f"\nYou currently have ${money} and are using your {tool}.")
        print("What would you like to do?")
        print("1. Spend the day cutting lawns")
        print("2. Buy a tool")
        print("3. Quit the game")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            money += earn_money(tool)
        elif choice == "2":
            tool = buy_tool(tool, money)
            if tool == "team":
                if money >= 1000:
                    print("\nCongratulations! You've won the game!")
                    break
                else:
                    print("\nYou need $1000 to win the game. Keep working!")
        elif choice == "3":
            print("\nThank you for playing. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

def earn_money(tool):
    if tool == "teeth":
        return 1
    elif tool == "scissors":
        return 5
    elif tool == "old-timey":
        return 50
    elif tool == "fancy":
        return 100
    elif tool == "team":
        return 250

def buy_tool(current_tool, money):
    if current_tool == "teeth":
        if money >= 5:
            print("\nYou bought a pair of rusty scissors!")
            return "scissors"
        else:
            print("\nYou don't have enough money to buy rusty scissors.")
    elif current_tool == "scissors":
        if money >= 25:
            print("\nYou bought an old-timey push lawnmower!")
            return "old-timey"
        else:
            print("\nYou don't have enough money to buy an old-timey push lawnmower.")
    elif current_tool == "old-timey":
        if money >= 250:
            print("\nYou bought a fancy battery-powered lawnmower!")
            return "fancy"
        else:
            print("\nYou don't have enough money to buy a fancy battery-powered lawnmower.")
    elif current_tool == "fancy":
        if money >= 500:
            print("\nYou hired a team of starving students!")
            return "team"
        else:
            print("\nYou don't have enough money to hire a team of starving students.")

    return current_tool

if __name__ == "__main__":
    main()