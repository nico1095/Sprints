# Program Name: Sprint1.py 
# Course: IT3883/Section W02
# Student Name: Anthony Giso
# Assignment Number: Final exam
# Due Date: 12/10/ 2025
# Purpose:a python program that will interpret pseudo-English statements describing an amount of money in coins and convert them into a dollar amount. 

# Sprint 1 
COIN_VALUES = {
    "penny": 0.01,
    "pennies": 0.01,
    "nickel": 0.05,
    "nickels": 0.05,
    "dime": 0.10,
    "dimes": 0.10,
    "quarter": 0.25,
    "quarters": 0.25
}

def sentence_to_dollars(sentence):
    parts = sentence.split(" and ")
    total = 0.0

    for part in parts:
        tokens = part.split()
        
      quantity = int(tokens[0])
       
      
  
coin_name = tokens[1].lower()

        if coin_name not in COIN_VALUES:
            raise ValueError(f"Unknown value: {coin_name}")

        total += quantity * COIN_VALUES[coin_name]

    return round(total, 2)


# test
if __name__ == "__main__":
    tests = [
        "1 penny and 2 nickels",
        "4 dimes and 7 quarters",
        "1 quarter and 3 pennies",
        "21 pennies and 17 dimes and 52 quarters",
        "95 dimes and 73 quarters and 22 nickels and 36 pennies",
        "1 nickel and 17 quarters",
        "21 nickels and 15 pennies",
        "1 dime and 1 nickel and 1 penny and 1 quarter"
    ]

    for t in tests:
        print(f"{t} -> ${sentence_to_dollars(t)}")
