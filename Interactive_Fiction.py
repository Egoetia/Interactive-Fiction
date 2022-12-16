class Scene:
  def __init__(self, description, choices):
    self.description = description
    self.choices = choices

class Choice:
  def __init__(self, description, result):
    self.description = description
    self.result = result

def start():
  # Create a scene with a description and a list of choices
  opening_scene = Scene("You are standing in a dark forest. You see a faint light in the distance.", [
    Choice("Go towards the light.", go_towards_light),
    Choice("Stay where you are.", stay)
  ])

  # Display the scene and allow the player to make a choice
  print(opening_scene.description)
  for i, choice in enumerate(opening_scene.choices):
    print(f"{i+1}. {choice.description}")
  choice = int(input("Enter your choice: ")) - 1
  opening_scene.choices[choice].result()

def go_towards_light():
  print("You follow the light and find your way out of the forest.")

def stay():
  print("You decide to stay where you are and eventually starve to death.")

start()
