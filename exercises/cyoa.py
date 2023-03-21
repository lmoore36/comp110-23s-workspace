"""Choose Your Own Adventure - EX06!"""

__author__ = "730556876"

player: str = input("What is your name?")

def greet(player: str) -> str:
  """Greets player"""
  player_ready: str = input("Type yes or no.")
  
  print(f"Hello {player}! Are you ready to find out which UNC dorm you are?")
  print(player_ready)
  #if player_ready == "yes":
    #main() 


#greet()  

#def main (name:str) -> str:
  #return None
  
#if __name__ == "__main__":
  #main()
