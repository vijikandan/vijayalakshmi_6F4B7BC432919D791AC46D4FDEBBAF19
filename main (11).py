'''Implement a class called Player that represents a cricket player .the player class should have a 
method called play() which prints "the player is playing cricket. Drive two classes Batsman and 
bowler from the player class override the play() method in each derived class to print " the batsman"
is batting "and "the bowler is bowling ",respectively . write aa program to create object of the both the
Batsman and bowler classes and call the play() method for each object.'''


# Defin the base class Player
class Player:
       def play(self):
           Print("The player is playing cricket.")

# Defin the derived class Batsman
class Batsman(Player):
       def play(self):
           print("The Batsman is Batting.")

# Define the derived class Bowler
class Bowler(Player):
  def play(self):
      print (" The bowler is bowling.") 

# Create objects of Batsman and Bowler Classes
batsman = Batsman() 
bowler = Bowler()

# Call the play() method for each object 
batsman.play()
bowler.play()