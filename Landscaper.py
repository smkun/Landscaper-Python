def main():
    # Game loop
    while True:
        # Initialize money and tools for each new game
        money = 0
        tools = {"teeth": 1}

        # Game round loop
        while True:
            # Display current money and tools
            print(f"\nYou currently have ${money} and the following tools:")
            for tool, count in tools.items():
                print(f"- {count} {tool}")

            # Display game menu and get user's choice
            print("\nWhat would you like to do?")
            print("1. Spend the day cutting lawns")
            print("2. Buy a tool")
            print("3. Sell a tool")
            print("4. Reset the game")
            print("5. Quit the game")
            choice = input("Enter your choice (1-5): ")

            # Process user's choice
            if choice == "1":
                money += earn_money(tools)
            elif choice == "2":
                money = buy_tool(tools, money)
            elif choice == "3":
                money = sell_tool(tools, money)
            elif choice == "4":
                print("\nResetting the game...")
                break
            elif choice == "5":
                print("\nThank you for playing. Goodbye!")
                return
            else:
                print("\nInvalid choice. Please try again.")

            # Check if the player has won the game
            if "team" in tools:
                if money >= 1000:
                    print("\nCongratulations! You've won the game!")
                    break
                else:
                    print("\nYou need $1000 to win the game. Keep working!")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("\nThank you for playing. Goodbye!")
            break

def earn_money(tools):
    # Calculate earnings based on the tools owned
    earnings = 0
    for tool, count in tools.items():
        if tool == "teeth":
            earnings += 1 * count
        elif tool == "scissors":
            earnings += 5 * count
        elif tool == "old-timey":
            earnings += 50 * count
        elif tool == "fancy":
            earnings += 100 * count
        elif tool == "team":
            earnings += 250 * count
    return earnings

def buy_tool(tools, money):
    # Display available tools for purchase
    print("\nAvailable tools:")
    print("1. Rusty Scissors ($5)")
    print("2. Old-timey Push Lawnmower ($25)")
    print("3. Fancy Battery-powered Lawnmower ($250)")
    print("4. Team of Starving Students ($500)")
    print("5. Cancel")

    # Get user's choice and process the purchase
    choice = input("Enter the number of the tool you want to buy (1-5): ")
    if choice == "1":
        if money >= 5:
            tools["scissors"] = tools.get("scissors", 0) + 1
            print("\nYou bought a pair of rusty scissors!")
            money -= 5
        else:
            print("\nYou don't have enough money to buy rusty scissors.")
    elif choice == "2":
        if money >= 25:
            tools["old-timey"] = tools.get("old-timey", 0) + 1
            print("\nYou bought an old-timey push lawnmower!")
            money -= 25
        else:
            print("\nYou don't have enough money to buy an old-timey push lawnmower.")
    elif choice == "3":
        if money >= 250:
            tools["fancy"] = tools.get("fancy", 0) + 1
            print("\nYou bought a fancy battery-powered lawnmower!")
            money -= 250
        else:
            print("\nYou don't have enough money to buy a fancy battery-powered lawnmower.")
    elif choice == "4":
        if money >= 500:
            tools["team"] = tools.get("team", 0) + 1
            print("\nYou hired a team of starving students!")
            money -= 500
        else:
            print("\nYou don't have enough money to hire a team of starving students.")
    elif choice == "5":
        print("\nTool purchase canceled.")
    else:
        print("\nInvalid choice. Tool purchase canceled.")
    return money

def sell_tool(tools, money):
    # Display tools available for sale
    print("\nTools available for sale:")
    for tool, count in tools.items():
        if tool != "teeth" and count > 0:
            print(f"{tool} ({count} available)")

    # Get user's choice and process the sale
    tool_to_sell = input("Enter the name of the tool you want to sell (or 'cancel' to go back): ")
    if tool_to_sell.lower() == "cancel":
        print("\nTool sale canceled.")
    elif tool_to_sell in tools and tools[tool_to_sell] > 0:
        tools[tool_to_sell] -= 1
        if tools[tool_to_sell] == 0:
            del tools[tool_to_sell]
        if tool_to_sell == "scissors":
            money += 2
        elif tool_to_sell == "old-timey":
            money += 12
        elif tool_to_sell == "fancy":
            money += 125
        elif tool_to_sell == "team":
            money += 250
        print(f"\nYou sold a {tool_to_sell} for half its price.")
    else:
        print("\nInvalid tool name or you don't have that tool.")
    return money

# Run the game when the script is executed directly
if __name__ == "__main__":
    main()