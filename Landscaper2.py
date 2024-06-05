import psycopg2
import json

def main():
    # The main function that controls the flow of the game.
    # It sets up the database connection, creates the game state table if it doesn't exist,
    # and handles the game loop, including loading and saving the game state, processing user choices,
    # and checking for win conditions.
    conn = psycopg2.connect(
        host="localhost",
        database="lawnmower_game",
        user="skunian",
        password="formula01"
    )

    create_table(conn)

    while True:
        money = 0
        tools = {"teeth": 1}

        money, tools = load_game_state(conn)

        while True:
            print(f"\nYou currently have ${money} and the following tools:")
            for tool, count in tools.items():
                print(f"- {count} {tool}")

            print("\nWhat would you like to do?")
            print("1. Spend the day cutting lawns")
            print("2. Buy a tool")
            print("3. Sell a tool")
            print("4. Save the game")
            print("5. Reset the game")
            print("6. Quit the game")
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                money += earn_money(tools)
            elif choice == "2":
                money = buy_tool(tools, money)
            elif choice == "3":
                money = sell_tool(tools, money)
            elif choice == "4":
                save_game_state(conn, money, tools)
            elif choice == "5":
                print("\nResetting the game...")
                break
            elif choice == "6":
                print("\nThank you for playing. Goodbye!")
                conn.close()
                return
            else:
                print("\nInvalid choice. Please try again.")

            if "team" in tools and money >= 1000:
                print("\nCongratulations! You've won the game!")
                break
            else:
                print("\nYou need $1000 to win the game. Keep working!")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("\nThank you for playing. Goodbye!")
            break

    conn.close()

def create_table(conn):
    # Create the game_state table in the database if it doesn't already exist.
    # The table has columns for id (primary key), money (integer), and tools (JSON).
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS game_state (
            id SERIAL PRIMARY KEY,
            money INTEGER,
            tools JSON
        )
    """)
    conn.commit()
    cur.close()

def save_game_state(conn, money, tools):
    # Save the current game state to the database.
    # It deletes any existing game state records and inserts a new record with the current money and tools.
    cur = conn.cursor()
    cur.execute("DELETE FROM game_state")
    cur.execute("INSERT INTO game_state (money, tools) VALUES (%s, %s)", (money, json.dumps(tools)))
    conn.commit()
    cur.close()
    print("\nGame state saved.")

def load_game_state(conn):
    # Load the saved game state from the database.
    # It retrieves the money and tools values from the game_state table.
    # If a saved game state exists, it returns the loaded values.
    # If no game state is found, it returns the default starting values.
    cur = conn.cursor()
    cur.execute("SELECT money, tools FROM game_state")
    result = cur.fetchone()
    cur.close()
    if result:
        money, tools = result
        if isinstance(tools, str):
            tools = json.loads(tools)
        print("\nGame state loaded.")
        return money, tools
    else:
        return 0, {"teeth": 1}

def earn_money(tools):
    # Calculate the amount of money earned based on the tools owned by the player.
    # Each tool has a specific earning rate:
    # - Teeth: $1 per day
    # - Rusty Scissors: $5 per day
    # - Old-timey Push Lawnmower: $50 per day
    # - Fancy Battery-powered Lawnmower: $100 per day
    # - Team of Starving Students: $250 per day
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
    # Display the available tools for purchase and handle the tool buying process.
    # It prompts the user to choose a tool to buy and checks if the player has enough money.
    # If the purchase is successful, it deducts the tool price from the player's money and adds the tool to their inventory.
    print("\nAvailable tools:")
    print("1. Rusty Scissors ($5)")
    print("2. Old-timey Push Lawnmower ($25)")
    print("3. Fancy Battery-powered Lawnmower ($250)")
    print("4. Team of Starving Students ($500)")
    print("5. Cancel")

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
    # Display the tools available for sale and handle the tool selling process.
    # It prompts the user to choose a tool to sell and checks if the player owns the selected tool.
    # If the sale is successful, it adds half of the tool's original price to the player's money and removes the tool from their inventory.
    print("\nTools available for sale:")
    for tool, count in tools.items():
        if tool != "teeth" and count > 0:
            print(f"{tool} ({count} available)")

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

if __name__ == "__main__":
    main()