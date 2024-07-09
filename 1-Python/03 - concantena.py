
name = input("Enter the name of the game \n")
yearLaunch = int(input("Enter the year of the game \n")) 
gamePrice = float(input("Enter the price of the game \n"))
planIncluded = input("it's included in the plan \n")

print("## Game data ##")
print("================")

print("\n Name of the game = ",name, "\n Years of the game = ", yearLaunch,
      "\n Price of the game = ",gamePrice, "\n It's included plan = ",planIncluded)

# Way with f string
print(f"\n Name of the game = {name}\n Year of the game = {yearLaunch}\n Price of the game = {gamePrice}\n It's included plan = {planIncluded}")

hgh