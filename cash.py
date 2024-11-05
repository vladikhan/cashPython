from cs50 import get_float

# Get the amount of change owed
while True:
    change = get_float("Change owed: ")
    if change > 0:
        break

# Convert dollars to cents
cents = round(change * 100)

# Calculate the number of coins
quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

# Sum of all coins
total_coins = quarters + dimes + nickels + pennies

# Print the results
print(f"quarters: {quarters}")
print(f"dimes: {dimes}")
print(f"nickels: {nickels}")
print(f"pennies: {pennies}")
print(f"total coins: {total_coins}")


