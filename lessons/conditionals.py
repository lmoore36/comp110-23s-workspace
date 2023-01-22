"""If it's raining tell me to pack and umbrella."""

weather: str = input("What is the weather like?")

if(weather == "rain"): 
    print("Pack an umbrella!")
    print("Let's splash in the puddles.")
else:
    if(weather == "snow"):
        print("Pack a jacket.")
    print("You don't need an umbrella.")
print("Have a lovely day!")