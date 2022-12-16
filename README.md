# Interactive-Fiction

This code is for a text-based interactive fiction game using PySimpleGUI. The Game class has a start method that creates a PySimpleGUI window with a description of the current scene and a list of choices that the player can make. The Scene class has a description attribute and a choices attribute that is a list of Choice objects. Each Choice object has a description attribute and a result attribute that is a function.

The Game class also has a stats dictionary that can be used to store and retrieve various game statistics, such as the player's health or hunger. The set_stat method allows you to set a stat to a particular value, and the get_stat method allows you to retrieve the value of a stat. If a stat has not been set, get_stat will return 0.

The start method creates an opening scene and displays it to the player in the PySimpleGUI window. The player can then make a choice by clicking one of the buttons in the window. When the player makes a choice, the corresponding Choice object's result function is called. The go_towards_light and stay functions simply print out a message to the console.
