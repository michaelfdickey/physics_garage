# ************************************************************************************************#
# ************************************************************************************************#
#	Directory Structure
# ************************************************************************************************#
# ************************************************************************************************#

#	/photonmain.py 		# primary program
#	/pgvar.py 			# global variable declarations
#	/pgui.py 			# photon gui elements and buttons
#	/pfunc.py 			# functions
#	/pclass.py 			# button processing class that handles drawing / displaying UI
#	/pbproc.py 			# processing sticky, group, dropdown etc button actions
#	/photon_ref.py 		# references, dev notes, style guide, modification instructions

# pfunc.py

moduleName = "pfunc.py"

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
import pgvar
#import pfunc
import pgui
import pclass
#import pbproc

# ************************************************************************************************#
# ************************************************************************************************#
#	initial variables for this module
# ************************************************************************************************#
# ************************************************************************************************#

created_particles = []	# instantiated particles
my_buttons = []			#initializes my_buttons list, each button is added to this for display
buttonToDraw = {}			#each button is loaded into this dictionary, added to my_buttons list

# FPS related variables
cSec = 0
cFrame = 0
FPS = 0

screen = pygame.display.set_mode((pgvar.pygame_window_width, pgvar.pygame_window_height))

# ************************************************************************************************#
# ************************************************************************************************#
#	functions
# ************************************************************************************************#
# ************************************************************************************************#



####### -------------------------------------##########
####### for printing Linu Number when debugging  ##########
####### -------------------------------------##########

def lineNum():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno



####### -------------------------------------##########
####### Initializes the UI and display screen       ##########
####### -------------------------------------##########

def initializeDisplay():
	print moduleName, lineNum(), "starting MAIN code"
	print moduleName, lineNum(), "- initializing pygame display"

	# # Pygame display	
	screen = pygame.display.set_mode((pgvar.pygame_window_width, pgvar.pygame_window_height))
	pygame.display.set_caption('Physics garage v0.01')

	# # #  draw background
	print moduleName, lineNum(), "- drawing background"
	screen.fill(pgvar.color_background)

	# # draw borders & frames for interface
	print moduleName, lineNum(), "- drawing borders and frames"
	pygame.draw.rect(screen, pgvar.UI_background_color, (0, 0, pgvar.pygame_window_width, pgvar.UI_topBar_height))
	pygame.draw.rect(screen, pgvar.UI_background_color, (0,0, pgvar.UI_sideBar_width, pgvar.pygame_window_height))

	# # draw buttons!
	print moduleName, lineNum(), "- drawing buttons"

	defineButtons()
	
	for i, button in enumerate(my_buttons):
		button.display()
	
	print moduleName, lineNum(), "initializing display completed"



####### ---------------------------------------------------------------------##########
####### takes all buttons defined in dictionary and adds them to a list  for drawing   ##########
####### ---------------------------------------------------------------------##########
def defineButtons():
	del my_buttons[:] 	# this clears and resets the my_buttons list, other it just keeps getting appended

	# source info for this part: https://realpython.com/iterate-through-dictionary-python/
	#print moduleName, lineNum(), "defineButtons() - started" 
	# iterates through the nested button dictionary, dumps each button into buttonToDraw, then displays ads to the list
	for allButtonsID, allButtonsValue in pgui.allButtons.items():
		for key in allButtonsValue:
			buttonToDraw[key] = allButtonsValue[key]

		### -------------------------- ###
		button_name = buttonToDraw["name"]
		button_origin_x = buttonToDraw["origin_x"]
		button_origin_y = buttonToDraw["origin_y"]
		button_width = buttonToDraw["width"]
		button_height = buttonToDraw["height"]
		button_label_txt = buttonToDraw["label_txt"]
		buttonType = buttonToDraw["type"]
		buttonEnabled = buttonToDraw["enabled"]
		buttonColor = buttonToDraw["color"]
		buttonGroup = buttonToDraw["group"]
		buttonVisible = buttonToDraw["visible"]
		buttonAvailable = buttonToDraw["available"]

		# define button then add button to display list
		created_button = pclass.Button((button_origin_x,button_origin_y), button_name, button_width, button_height, button_label_txt, buttonType, buttonEnabled,  buttonColor, buttonVisible, buttonAvailable)
		my_buttons.append(created_button)
		#print " my_buttons length: ", len(my_buttons)


	#print moduleName, lineNum(), "defineButtons() - completed"



####### ---------------------------------------------------------------------##########
####### this determines what button has been clicked on                                                                ##########
####### ---------------------------------------------------------------------##########
def findButton(buttons, x, y):
	for b in buttons:
		if x <= b.x + b.x_width:
			if x >= b.x:
				if y >= b.y:
					if y <= b.y + b.y_height:
						print moduleName, lineNum(), "selected button label_txt = ", b.button_name
						return b
	return None


####### ---------------------------------------------------------------------##########
####### something to do with updating text field buttons                                                                ##########
####### ---------------------------------------------------------------------##########

def enumerateButtons():
	for i, button in enumerate(my_buttons):
		button.display()	


####### ---------------------------------------------------------------------##########
####### Redraw the backgroundm, buttons, screen, etc.                                                                 ##########
####### ---------------------------------------------------------------------##########

def redrawEverything():
	#print lineNum(), "redrawEverything() - started"
	
	#print lineNum(), "drawing background"
	screen.fill(pgvar.color_background)

	###*** ALERT ALERT ALERT -> re-enable below to get drid and origin working ***
	# check if draw grids is enabled, and draw if so
	if pgui.buttonGrid["enabled"] == True:
		drawGrid()

	
	# check if draw origin is enabled, and draw if so. 
	if pgui.buttonOrigin["enabled"] == True:
		drawOrigin()

		
	#print lineNum(), "drawing borders and frames"
	pygame.draw.rect(screen, pgvar.UI_background_color, (0, 0, pgvar.pygame_window_width, pgvar.UI_topBar_height))
	pygame.draw.rect(screen, pgvar.UI_background_color, (0,0, pgvar.UI_sideBar_width, pgvar.pygame_window_height))

	#print lineNum(), "redifining buttons and redrawing"
	defineButtons()
	for i, button in enumerate(my_buttons):
		button.display()

	#print lineNum(), "redrawEverything() - completed"


def redrawPortal():
	print lineNum(), "redrawBackground() started"
	pygame.draw.rect(screen, pgvar.color_background, (pgvar.UI_sideBar_width, pgvar.UI_topBar_height, pgvar.pygame_window_width, pgvar.pygame_window_height))
	#screen.fill(pgvar.color_background)
	if pgui.buttonGrid["enabled"] == True:
		drawGrid()
	if pgui.buttonOrigin["enabled"] == True:
		drawOrigin()





####### ---------------------------------------------------------------------##########
####### Functions for counting and displaying FPS (frames per second)                               ##########
####### ---------------------------------------------------------------------##########
def show_fps():
	fps_overlay = pgvar.fps_font.render("FPS:"+str(FPS), True, pgvar.UI_button_txt_color)
	screen.blit(fps_overlay, (pgvar.pygame_window_width - 100, pgvar.pygame_window_height - 30))

def count_fps():
	global cSec, cFrame, FPS, deltatime
	if cSec == time.strftime("%S"):
		cFrame += 1
	else:
		FPS = cFrame
		cFrame = 0
		cSec = time.strftime("%S")


####### ---------------------------------------------------------------------##########
####### on screen message box 									                                        ##########
####### ---------------------------------------------------------------------##########
def show_message_txt():
	pygame.draw.rect(screen, pgvar.color_blue, (pgui.onscreen_message_txt_origin, pgvar.pygame_window_height - 30, 600, 20))   
	message_txt_overlay = pgvar.message_font.render(pgvar.message_txt, True, pgvar.UI_button_txt_color)
	screen.blit(message_txt_overlay, (pgui.onscreen_message_txt_origin, pgvar.pygame_window_height - 30))




####### ---------------------------------------------------------------------##########
####### Draw Grid lines                                                                                                                                       ##########
####### ---------------------------------------------------------------------##########
def drawGrid():
	# # Draw grid
	grid_width = 100
	grid_height = 100

	grid_center_h = pgvar.pygame_window_width / 2
	grid_center_v = pgvar.pygame_window_height / 2

	#grid_width = pgvar.pygame_window_width / 10
	#grid_height = pgvar.pygame_window_height / 10

	grid_h_units = pgvar.pygame_window_width / grid_width
	print type(grid_h_units)
	print "pygram window width = ", pgvar.pygame_window_width
	print "grid_h_units = ",grid_h_units	
	grid_h_units = grid_h_units / 2
	print "grid_h_units = ",grid_h_units	

	# grid center line
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [((pgvar.pygame_window_width / 2),0),((pgvar.pygame_window_width / 2 ),pgvar.pygame_window_height)],1)

	grid_h_draw = 0
	while grid_h_draw <= grid_h_units:
		print"drawing grid line", grid_h_draw 
		pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_center_h - (grid_width * grid_h_draw),0),(grid_center_h - (grid_width * grid_h_draw),pgvar.pygame_window_height)],1)
		pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_center_h + (grid_width * grid_h_draw),0),(grid_center_h + (grid_width * grid_h_draw),pgvar.pygame_window_height)],1)
		grid_h_draw = grid_h_draw + 1


	"""
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [((pgvar.pygame_window_width / 2),0),((pgvar.pygame_window_width / 2 ),pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 1,0),(grid_width * 1,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 2,0),(grid_width * 2,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 3,0),(grid_width * 3,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 4,0),(grid_width * 4,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 5,0),(grid_width * 5,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 6,0),(grid_width * 6,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 7,0),(grid_width * 7,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 8,0),(grid_width * 8,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 9,0),(grid_width * 9,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 10,0),(grid_width * 10,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 11,0),(grid_width * 11,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 12,0),(grid_width * 12,pgvar.pygame_window_height)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_width * 13,0),(grid_width * 13,pgvar.pygame_window_height)],1)
	"""

	"""
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,(pgvar.pygame_window_height / 2)),(pgvar.pygame_window_width, (pgvar.pygame_window_height / 2))],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 1), (pgvar.pygame_window_width,grid_height * 1)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 2), (pgvar.pygame_window_width,grid_height * 2)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 3), (pgvar.pygame_window_width,grid_height * 3)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 4), (pgvar.pygame_window_width,grid_height * 4)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 5), (pgvar.pygame_window_width,grid_height * 5)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 6), (pgvar.pygame_window_width,grid_height * 6)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 7), (pgvar.pygame_window_width,grid_height * 7)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 8), (pgvar.pygame_window_width,grid_height * 8)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 9), (pgvar.pygame_window_width,grid_height * 9)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 10), (pgvar.pygame_window_width,grid_height * 10)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 11), (pgvar.pygame_window_width,grid_height * 11)],1)
	pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_height * 12), (pgvar.pygame_window_width,grid_height * 12)],1)
	"""

####### ---------------------------------------------------------------------##########
####### Draw Origin Lines                                                                                                                                  ##########
####### ---------------------------------------------------------------------##########

def drawOrigin():
	pygame.draw.lines(screen, pgvar.color_red, False, [((pgvar.pygame_window_width / 2),0),((pgvar.pygame_window_width / 2 ),pgvar.pygame_window_height)],2)
	pygame.draw.lines(screen, pgvar.color_red, False, [(0,(pgvar.pygame_window_height / 2)),(pgvar.pygame_window_width, (pgvar.pygame_window_height / 2))],2)


####### ---------------------------------------------------------------------##########
####### Insert Particles                                                                                                                          	##########
####### ---------------------------------------------------------------------##########

def InsertProton(mouseX, mouseY):
	
	# particle characteristics
	particle_size = 8
	particle_type = "proton"
	particle_x = mouseX
	particle_y = mouseY
	speedx = 0
	speedy = 0
	particle_color = (0,255,0)
	particle_thickness = 0
	particle_mass = 0
	particle_charge = 1

	print moduleName, lineNum(), "about to append class"

	particle_to_make = pclass.Particle((particle_x,particle_y), particle_size, particle_type, speedx, speedy, particle_color, particle_thickness, particle_mass, particle_charge)
	created_particles.append(particle_to_make)

	print moduleName, lineNum(), "completed append class"

	#pgvar.message_txt = "YAY"

	"""
	# size of proton 
		# the root mean square charge radius of a proton is about 0.84 - 0.87 fm (or 0.84 x 10 ^ -15 to 0.87 x 10 ^ 15m )
		.855 fm
		.855 x 10 ^-15 m
		8.55 x 10 ^-16m
		1 px = 1.0 x 10-14m or .1 fm 
	"""

def distanceParticles(particle1, particle2):
	# calculates distance between each pair of particles
	# # distance x, y, and hypotenuse
	distance_x = abs(particle1.x - particle2.x)
	distance_y = abs(particle1.y - particle2.y)
	hypotenuse = math.sqrt((distance_x * distance_x) + (distance_y * distance_y))

	# # draw reference lines
	if pgui.bDistComponents["enabled"] == True:

		pygame.draw.lines(screen, pgvar.color_red, False, [(particle1.x,particle1.y), (particle2.x,particle1.y)], 1) #p1 - particle2 X
		pygame.draw.lines(screen, pgvar.color_red, False, [(particle2.x,particle2.y), (particle2.x,particle1.y)], 1) #p1 - particle2 y
		pygame.draw.lines(screen, pgvar.color_red, False, [(particle1.x,particle1.y), (particle2.x,particle2.y)], 1) #hypotenuse

		# # paint measurements
		# # # label points
		label_point_1 = pgvar.myfont.render(str("P1"), 1, (255,255,0))
		screen.blit(label_point_1, (particle1.x + 5, particle1.y + 5))

		label_point_2 = pgvar.myfont.render(str("P2"), 1, (255,255,0))
		screen.blit(label_point_2, (particle2.x - 20, particle2.y + 5))

		# # # display X
		label_distance_x = pgvar.myfont.render(str(distance_x), 1, (255,255,0))
		if particle1.x > particle2.x:
			distance_x_label_origin = int(particle1.x-(distance_x/2))
		if particle1.x < particle2.x:
			distance_x_label_origin = int(particle2.x-(distance_x/2))
		if particle1.x == particle2.x:
			distance_x_label_origin = particle1.x
		screen.blit(label_distance_x, (distance_x_label_origin, particle1.y))

		# # # display Y
		label_distance_y = pgvar.myfont.render(str(distance_y), 1, (255,255,0))
		if particle1.y > particle2.y:
			distance_y_label_origin = int(particle1.y-(distance_y/2))
		if particle1.y < particle2.y:
			distance_y_label_origin = int(particle2.y-(distance_y/2))
		if particle1.y == particle2.y:
			distance_y_label_origin = particle1.y
		screen.blit(label_distance_y, (particle2.x, distance_y_label_origin))

		# # # display hypotenuse
		label_hypotenuse = pgvar.myfont.render(str(hypotenuse), 1, (255,255,0))
		screen.blit(label_hypotenuse, (distance_x_label_origin, distance_y_label_origin))

	# # # calculate angles
	dx = particle1.x - particle2.x
	dy = particle1.y - particle2.y
	rads = math.atan2(-dy,dx)
	rads %= 2*math.pi
	degs = math.degrees(rads)
	degs_text = str(degs)+" degrees"
	#print "degrees", degs #degrees where horizontal to the right = 0
	label_angle_degrees = pgvar.myfont.render(str(degs_text), 1, (255,255,0))
	screen.blit(label_angle_degrees, (particle1.x, particle1.y+25))


	# # calculate force
	constant = 2000 # gravitational constant, K, etc
	particle_1 = 100
	particle_2 = 100 #charge / mass, etc
	force = constant * particle_1 * particle_2 / (hypotenuse*hypotenuse)
	#print "Force = ", force
	force_text = str(force)+" force"
	label_force = pgvar.myfont.render(str(force_text), 1, (255,255,0))
	screen.blit(label_force, (particle1.x, particle1.y+50))

	# # draw force vectors
	vector_p1 = (particle1.x, particle1.y)
	vector_len = force
	vector_p1_x = vector_p1[0] + math.cos(math.radians(degs)) * vector_len 
	vector_p1_y = vector_p1[1] + math.sin(math.radians(degs)) * vector_len * -1
	pygame.draw.line(screen, pgvar.color_blue, vector_p1, (vector_p1_x,vector_p1_y), 2)
	#print "vector_p1_x: ", vector_p1_x, "vector_p1_y: ", vector_p1_y
	#print "p1.x =:", p1.x, "vector_p1_x: ", vector_p1_x

	vector_p2 = (particle2.x, particle2.y)
	vector_len = force
	vector_p2_x = vector_p2[0] + math.cos(math.radians(degs)) * vector_len * -1
	vector_p2_y = vector_p2[1] + math.sin(math.radians(degs)) * vector_len
	pygame.draw.line(screen, pgvar.color_blue, vector_p2, (vector_p2_x,vector_p2_y), 2)
	#print "vector_p2_x: ", vector_p2_x, "vector_p2_y: ", vector_p2_y

	# # update particle speedx and speedy
	particle1.speedx = particle1.speedx + ((vector_p1_x - particle1.x) *.0000001)
	particle1.speedy = particle1.speedy + ((vector_p1_y - particle1.y) *.0000001)
	particle2.speedx = particle2.speedx + ((vector_p2_x - particle2.x) *.0000001)
	particle2.speedy = particle2.speedy + ((vector_p2_y - particle2.y) *.0000001) # cause speed way too high
	#print "p1 speed x = ", p1.speedx
	#print "p1 speed y = ", p1.speedy
	#pause = raw_input()