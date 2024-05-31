# Landscaping Business Game

This is a simple text-based game where the player starts a landscaping business with just their teeth and aims to earn money, buy tools, and eventually hire a team of starving students to win the game.

## Game Rules

1. The player starts with $0 and their teeth as the only tool.
2. The player can spend the day cutting lawns and earn money based on the tools they own.
3. The player can buy tools to increase their earning potential:
   - Rusty Scissors: $5, earns $5 per day
   - Old-timey Push Lawnmower: $25, earns $50 per day
   - Fancy Battery-powered Lawnmower: $250, earns $100 per day
   - Team of Starving Students: $500, earns $250 per day
4. The player can sell tools for half their purchase price.
5. The player wins the game when they have a team of starving students and $1000.

## How to Play

1. Run the `landscaping_game.py` script.
2. Follow the on-screen prompts to make choices:
   - Spend the day cutting lawns to earn money.
   - Buy tools to increase your earning potential.
   - Sell tools to get some money back.
   - Reset the game to start over.
   - Quit the game when you're done playing.
3. Keep playing until you reach the winning condition of having a team of starving students and $1000.

## Prerequisites

- Python 3.x

## How to Run

1. Clone the repository or download the `landscaping_game.py` script.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the following command:

   ```
   python landscaping_game.py
   ```

4. The game will start, and you can follow the on-screen prompts to play.

## Game Features

- Multiple tools to buy and use for earning money
- Ability to sell tools for half their purchase price
- Game reset option to start over
- Win condition: Having a team of starving students and $1000

## Code Structure

- `main()`: The main game loop that handles the game flow and user interactions.
- `earn_money(tools)`: Calculates the player's earnings based on the tools they own.
- `buy_tool(tools, money)`: Allows the player to buy tools and updates their tools and money.
- `sell_tool(tools, money)`: Allows the player to sell tools and updates their tools and money.

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues on the GitHub repository.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).