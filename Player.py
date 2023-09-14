class Player:
  def play(self):
      print("the Player is playing cricket.")
class batsman (Player):
  def play(self):
      print ("the batsman is batting.")
class bowler (Player):
  def play(self):
      print ("the bowler is bowling.")
Batsman = Batsman ()
bowler = Bowler ()
batsman.play()
bowler.play()
