# ************************************************************************************************#
# ************************************************************************************************#
#	Directory Structure
# ************************************************************************************************#
# ************************************************************************************************#

#	see pg_ref.py

moduleName = "pgvar.py"
testText = "test string from pgvar.py"


# ************************************************************************************************#
# ************************************************************************************************#
#	Import Modules
# ************************************************************************************************#
# ************************************************************************************************#

# # public python modules
import pygame
import random
import math
import sys
import time 			# for FPS functions
import inspect		# for displaying the line number of the code in print commands

# # unique modules for this app
"""
import pgvar
import pfunc
import pgui
import pclass
import pbproc
"""

# ************************************************************************************************#
#	Initial Variables
# ************************************************************************************************#


# # screen size
pygame_window_width = 1600
pygame_window_height = 1200

# # pygame fonts
pygame.font.init()																# needs to be called at the start of the program
myfont = pygame.font.SysFont('Arial',15)
font_sml = pygame.font.SysFont('Arial',13)	
font_med = pygame.font.SysFont('Arial',15)
font_lrg = pygame.font.SysFont('Arial',17)
font_xlrg = pygame.font.SysFont('Arial',19)										# GUI font type and size
fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 15)
message_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 15)		# on screen message box display


# # pre-defined colors
color_black = (0,0,0)
color_red = (255,0,0)
color_red_dark = (128,0,0)
color_orange = (255,165,0)
color_green = (0,255,0)
color_green_dark = (0,128,0)
color_blue = (0,0,255)
color_blue_dark = (0,0,128)
color_white = (255,255,255)
color_pink = (255,200,200)
color_gray = (128,128,128)
color_yellow = (255,255,0)
color_yellow_grid = (128,128,0)

# # interface formatting
UI_topBar_height = 20
UI_sideBar_width = 120  
UI_menuButton_width = 150
UI_popup_small_width = 200
UI_popup_small_height = 180
UI_popup_small_origin_x = (pygame_window_width / 2) - (UI_popup_small_width / 2)
UI_popup_small_origin_y = (pygame_window_height / 2) - (UI_popup_small_height / 2)
UI_popup_medium_width = 400
UI_popup_medium_height = 400
UI_popup_large_width = 600
UI_popup_large_height = 600

# interface colors
color_background= (0,0,0)
UI_background_color = (102, 0, 51)				# the color of the bar along the side and top
UI_button_border_color = (153, 127, 76)			# color of the border box around the button
UI_button_color = (204, 0, 102)					# the default color of the button
UI_button_click_color = (255, 128 , 255)		# the color a button turns temporarily when clicked on
UI_label_color = (150,50,100)					# label color 
UI_text_entry_box_color = (100,0,50)			# the color of text entry boxes
UI_text_entry_box_color_active = (125,50,50)	# the color of text entry boxes
UI_button_group_color = (125, 50, 100)			
UI_button_txt_color = (255,255,0)				# color of text label of button
UI_button_selected_color = (225,100,225)		# color button turns to when toggled on

# disabled buttons
UI_button_disabled = (75,25,50)					# a completely disabled button / option not currently available
UI_button_disabled_text = (64,64,0)

# pygame keys pressed
key_pressed_space = False




# # FPS related variables
cSec = 0
cFrame = 0
FPS = 0

# # by default, no UI objects are selected at start
selected_uiObject = None					
selected_button = None

# # on screen message text
message_txt = ""

# # other
entered_text = ""

# # FORCES

forceGravity = 1
forceElectromagnetic = 5

# ************************************************************************************************#
#	Initial lists
# ************************************************************************************************#

my_uiObjects = []							# this list will hold all the UI elements
display_overlay_origin = []				# list containing the origin line elements
display_overlay_grid = []					# list containing the grid line elements

# ************************************************************************************************#
#	Initial dictionaries
# ************************************************************************************************#

selectedButton = {}