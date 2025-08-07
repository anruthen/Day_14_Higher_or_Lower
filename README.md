# Day 14 – Higher Lower Game 📊

A terminal-based game where the user compares two personalities and guesses who has more Instagram followers.

## Features

- Randomly selected public figures with name, profession, and country
- Player guesses who has more followers: A or B
- Score increases with correct answers
- B becomes new A in the next round
- Game continues until a wrong guess
- Final score is shown at the end
- Clean ASCII visuals for logo and comparison

## How It Works

- The game selects two random entries from a dataset.
- The player sees both figures’ names, descriptions, and countries.
- The player chooses who they believe has more followers.
- If correct, the score increases and the game continues.
- If incorrect, the game ends and the final score is displayed.

## Example Output
```
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Beyoncé a Musician, from United States

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Compare B: David Beckham a Footballer, from United Kingdom
Who has more followers? Type 'A' or 'B':
```
## Skills Learned

- Working with dictionaries and nested data
- Random selection and validation of entries
- Modular code with parameterized functions
- Implementing loop-based game logic
- Managing game state and score tracking
- Console input/output and formatting
