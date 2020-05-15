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
import pge

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
						if b.buttonVisible == True:
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

	# check is scale label is enabled, then draw scale
	if pgui.tScaleSelection["enabled"] == True:
		drawScale()
		
	#print lineNum(), "drawing borders and frames"
	pygame.draw.rect(screen, pgvar.UI_background_color, (0, 0, pgvar.pygame_window_width, pgvar.UI_topBar_height))
	pygame.draw.rect(screen, pgvar.UI_background_color, (0,0, pgvar.UI_sideBar_width, pgvar.pygame_window_height))

	#print lineNum(), "redifining buttons and redrawing"
	defineButtons()
	for i, button in enumerate(my_buttons):
		button.display()

	
	if pgui.bPlaySimulation["enabled"] == False:
		for i, particle in enumerate(created_particles):
			particle.move()	


	#print lineNum(), "redrawEverything() - completed"


def redrawPortal():
	print lineNum(), "redrawBackground() started"
	pygame.draw.rect(screen, pgvar.color_background, (pgvar.UI_sideBar_width, pgvar.UI_topBar_height, pgvar.pygame_window_width, pgvar.pygame_window_height))
	#screen.fill(pgvar.color_background)
	if pgui.buttonGrid["enabled"] == True:
		drawGrid()
	if pgui.buttonOrigin["enabled"] == True:
		drawOrigin()
	if pgui.tScaleSelection["enabled"] == True:
		drawScale()




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

	# DRAWING THE VERTICAL GRID LINES

	grid_h_units = pgvar.pygame_window_width / grid_width
	grid_h_units = grid_h_units / 2

	grid_h_draw = 0
	while grid_h_draw <= grid_h_units:
		# the total width of the game window is divided by grid spacing then a line is drawn on either side of the origin until count = grid spacing
		pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_center_h - (grid_width * grid_h_draw),0),(grid_center_h - (grid_width * grid_h_draw),pgvar.pygame_window_height)],1)
		pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(grid_center_h + (grid_width * grid_h_draw),0),(grid_center_h + (grid_width * grid_h_draw),pgvar.pygame_window_height)],1)
		grid_h_draw = grid_h_draw + 1

	# DRAWING THE HORIZONTAL GRID LINES

	grid_v_units = pgvar.pygame_window_height / grid_height
	grid_v_units = grid_v_units / 2

	grid_v_draw = 0
	while grid_v_draw <= grid_v_units:
		pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_center_v - (grid_width * grid_v_draw)),(pgvar.pygame_window_width,grid_center_v - (grid_width * grid_v_draw))],1)
		pygame.draw.lines(screen, pgvar.color_yellow_grid, False, [(0,grid_center_v + (grid_width * grid_v_draw)),(pgvar.pygame_window_width,grid_center_v + (grid_width * grid_v_draw))],1)
		grid_v_draw = grid_v_draw + 1		


####### ---------------------------------------------------------------------##########
####### Draw Scale Label                                                                                                                       	      ##########
####### ---------------------------------------------------------------------##########


def drawScale():
	
	# the stuff needed to figure out where to draw the scale label. taken from the def drawGrid  function above
	grid_width = 100
	grid_height = 100

	grid_center_h = pgvar.pygame_window_width / 2
	grid_center_v = pgvar.pygame_window_height / 2

	grid_h_units = pgvar.pygame_window_width / grid_width
	grid_h_units = grid_h_units / 2

	grid_v_units = pgvar.pygame_window_height / grid_height
	grid_v_units = grid_v_units / 2
	
	#for testing reference:
	#pygame.draw.lines(screen, pgvar.color_yellow, False, [(0,250),(1000,1000)],3)

	pygame.draw.lines(screen, pgvar.color_yellow, False, [(grid_center_h - (grid_width * (grid_h_units - 2)), pgvar.pygame_window_height - 40),(grid_center_h - (grid_width * (grid_h_units - 3)),pgvar.pygame_window_height - 40)],3)
	pygame.draw.lines(screen, pgvar.color_yellow, False, [(grid_center_h - (grid_width * (grid_h_units - 2)), pgvar.pygame_window_height - 30),(grid_center_h - (grid_width * (grid_h_units - 2)),pgvar.pygame_window_height - 50)],3)
	pygame.draw.lines(screen, pgvar.color_yellow, False, [(grid_center_h - (grid_width * (grid_h_units - 3)), pgvar.pygame_window_height - 30),(grid_center_h - (grid_width * (grid_h_units - 3)),pgvar.pygame_window_height - 50)],3)

	current_scale = pgui.tScaleSelection["label_txt"]
	scale_label = pgvar.myfont.render(str(current_scale), 1, (255,255,0))
	screen.blit(scale_label, (grid_center_h - (grid_width * (grid_h_units - 2)), pgvar.pygame_window_height - 30))

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

	# this functionality is moved to pclass processing so the value remains absolute. pclass will adjust for scale
	"""
	# get proton diameter
	particle_diameter = pge.pProton["diameter"]
	print "the particle to be insterted diameter =", particle_diameter

	# compare to current scale
	print "the current scale is = ", pge.current_scale["scale"]
	particle_size = int(particle_diameter / pge.current_scale["scale"])

	if particle_size <= 1:
		particle_size = 1

	print "the particle size in pixels will be: ", particle_size
	"""

	# grab scale for repositioning on zoom
	print "game position X = ", mouseX 
	print "game position Y = ", mouseY
	initial_scale = pge.current_scale["scale"]
	print "scale = ", pge.current_scale["scale"]

	# get absolute 0 to convert to an absolute position
	print "X zero = ", (pgvar.pygame_window_width / 2)
	print "Y zero = ", (pgvar.pygame_window_height / 2)

	particleXabs = mouseX - (pgvar.pygame_window_width / 2)
	particleYabs = (pgvar.pygame_window_height / 2) - mouseY 
	
	print "absolute particle position X = ", particleXabs
	print "absolute particle position Y = ", particleYabs

	print "particleX: ", particleXabs, "particleY: ", particleYabs, "scale: ", initial_scale

	# particle characteristics
	particle_type = "proton"
	particle_size = pge.pProton["diameter"]
	particle_scale = pge.pProton["scale"]
	particle_x = mouseX
	particle_y = mouseY
	speedx = 0
	speedy = 0
	particle_color = (255,0,0)
	particle_thickness = 0
	particle_mass = pge.pProton["mass"]
	particle_charge = pge.pProton["charge"]
	particle_X_abs = particleXabs
	particle_Y_abs = particleYabs
	created_scale = initial_scale


	print moduleName, lineNum(), "about to append class"
	particle_to_make = pclass.Particle((particle_x,particle_y), particle_size, particle_type, speedx, speedy, particle_color, particle_thickness, particle_mass,
		particle_charge, particle_X_abs, particle_Y_abs, particle_scale, created_scale)
	created_particles.append(particle_to_make)
	print moduleName, lineNum(), "completed append class"

	print "length of created_particles", len(created_particles)

	print created_particles

	print " ~~~~~~~~~~~~~~~~~~~"
	print "completed InsertProton"
	print " ~~~~~~~~~~~~~~~~~~~"

	#particle.display()

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

	misc = 1

	#print "particle1.x: ",particle1.x, "particle1.y: ",particle1.y
	#print "particle2.x: ",particle2.x, "particle2.y: ",particle2.y

	"""

	#### processing absolute position of particles

	# get scale modifier
	scale_modifier = pge.current_scale["scale"] / self.scale

	#reset particle size
	draw_particle_size = self.size / scale_modifier
	if draw_particle_size <= 1:
		draw_particle_size = 1

	# # reset position of particle
	initial_scale = self.created_scale
	position_modifier = pge.current_scale["scale"] / initial_scale

	positionX = self.x
	positionY = self.y

	positionX = positionX / position_modifier
	positionY = positionY / position_modifier

	positionX = positionX + (pgvar.pygame_window_width / 2)
	positionY = (pgvar.pygame_window_height / 2) - positionY 

	#### 


	# calculates distance between each pair of particles
	# # distance x, y, and hypotenuse
	distance_x = abs(particle1.x - particle2.x)
	distance_y = abs(particle1.y - particle2.y)
	hypotenuse = math.sqrt((distance_x * distance_x) + (distance_y * distance_y))

	# # draw reference lines
	if pgui.bDistComponents["enabled"] == True:

		pygame.draw.lines(screen, pgvar.color_orange, False, [(particle1.x,particle1.y), (particle2.x,particle1.y)], 1) #p1 - particle2 X
		pygame.draw.lines(screen, pgvar.color_orange, False, [(particle2.x,particle2.y), (particle2.x,particle1.y)], 1) #p1 - particle2 y
		pygame.draw.lines(screen, pgvar.color_orange, False, [(particle1.x,particle1.y), (particle2.x,particle2.y)], 1) #hypotenuse

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
	#pygame.draw.line(screen, pgvar.color_blue, vector_p1, (vector_p1_x,vector_p1_y), 2)
	#print "vector_p1_x: ", vector_p1_x, "vector_p1_y: ", vector_p1_y
	#print "p1.x =:", p1.x, "vector_p1_x: ", vector_p1_x

	vector_p2 = (particle2.x, particle2.y)
	vector_len = force
	vector_p2_x = vector_p2[0] + math.cos(math.radians(degs)) * vector_len * -1
	vector_p2_y = vector_p2[1] + math.sin(math.radians(degs)) * vector_len
	#pygame.draw.line(screen, pgvar.color_blue, vector_p2, (vector_p2_x,vector_p2_y), 2)
	#print "vector_p2_x: ", vector_p2_x, "vector_p2_y: ", vector_p2_y

	# # update particle speedx and speedy
	particle1.speedx = particle1.speedx + ((vector_p1_x - particle1.x) *.0000001)
	particle1.speedy = particle1.speedy + ((vector_p1_y - particle1.y) *.0000001)
	particle2.speedx = particle2.speedx + ((vector_p2_x - particle2.x) *.0000001)
	particle2.speedy = particle2.speedy + ((vector_p2_y - particle2.y) *.0000001) # cause speed way too high
	#print "p1 speed x = ", p1.speedx
	#print "p1 speed y = ", p1.speedy
	#pause = raw_input()

	"""

def Zoom(zoomdir):

	if zoomdir == "-":
		print " ~ ~ ~ ~ ~  running zoomdir '-'   ~ ~ ~ ~ ~ "
		for i, particle in enumerate(created_particles):
			particle.zoomout()
			#particle.move()

	if zoomdir == "+":
		print " ~ ~ ~ ~ ~  running zoomdir '+'   ~ ~ ~ ~ ~ "
		for i, particle in enumerate(created_particles):
			particle.zoomin()
			#particle.move()