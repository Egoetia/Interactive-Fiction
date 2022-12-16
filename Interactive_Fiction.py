import PySimpleGUI as sg

class Scene:
  def __init__(self, description, choices):
    self.description = description
    self.choices = choices

class Choice:
  def __init__(self, description, result):
    self.description = description
    self.result = result

class Game:
  def __init__(self):
    self.stats = {}
  
  def start(self):

    # Set a stat
    game.set_stat("health", 100)

    # Get a stat
    health = game.get_stat("health")
    print(f"Your health is {health}.")

    # Get a stat that hasn't been set
    hunger = game.get_stat("hunger")
    print(f"Your hunger is {hunger}.")

    # Create a scene with a description and a list of choices
    opening_scene = Scene("You are standing in a dark forest. You see a faint light in the distance.", [
      Choice("Go towards the light.", self.go_towards_light),
      Choice("Stay where you are.", self.stay)
    ])

    # Display the scene and allow the player to make a choice
    layout = [
      [sg.Text(opening_scene.description)],
      *[[sg.Button(choice.description, key=i)] for i, choice in enumerate(opening_scene.choices)]
    ]
    window = sg.Window('Interactive Fiction Game', layout)
    while True:
      event, values = window.read()
      if event == sg.WIN_CLOSED:
        break
      opening_scene.choices[int(event)].result()
    window.close()

  def go_towards_light(self):
    print("You follow the light and find your way out of the forest.")

  def stay(self):
    print("You decide to stay where you are and eventually starve to death.")

  def set_stat(self, stat, value):
    self.stats[stat] = value
  
  def get_stat(self, stat):
    return self.stats.get(stat, 0)

game = Game()
game.start()
