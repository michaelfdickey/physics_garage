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

# pclass.py

moduleName = "pclass.py"

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
import pfunc
import pgui
#import pclass
#import pbproc
import pge


# ************************************************************************************************#
# ************************************************************************************************#
#	initialize variables
# ************************************************************************************************#
# ************************************************************************************************#

screen = pygame.display.set_mode((pgvar.pygame_window_width, pgvar.pygame_window_height))
myfont = pgvar.myfont	

# ************************************************************************************************************************
# ************************************************************************************************************************
# 	Classes                    #
# ************************************************************************************************************************
# ************************************************************************************************************************



class Button:
	def __init__ (self, (x,y), button_name, x_width, y_height, button_label_txt, buttonType, buttonEnabled, buttonColor, buttonVisible, buttonAvailable):
		self.button_name = button_name
		self.x = x
		self.x_width = x_width
		self.y = y
		self.y_height = y_height
		self.color = buttonColor
		self.thickness = 0
		self.button_label_txt = button_label_txt
		self.colorBorder = pgvar.UI_button_border_color
		self.buttonType = buttonType  
		self.buttonEnabled = buttonEnabled
		self.buttonVisible = buttonVisible
		self.buttonAvailable = buttonAvailable

	# # displays buttons
	def display(self):

		# render "pushy" type buttons
		if self.buttonType == "pushy":
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			if self.buttonAvailable == False:
				label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_disabled_text)
			elif self.buttonAvailable == True:
				label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_txt_color)
			
			screen.blit(label, (self.x + 5, self.y))

		# render "sticky" type buttons
		elif self.buttonType == "sticky":	
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border
			
			if self.buttonAvailable == False:
				label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_disabled_text)
			elif self.buttonAvailable == True:
				label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_txt_color)
			
			screen.blit(label, (self.x + 5, self.y))

		# render "label" type buttons
		elif self.buttonType == "label":
			self.color = pgvar.UI_label_color																	# since self.color = buttonColor by default, this overwrites that for labels
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			
			if self.buttonAvailable == False:
				label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_disabled_text)
			elif self.buttonAvailable == True:
				label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_txt_color)
			
			screen.blit(label, (self.x + 5, self.y))

		# render "group" type buttons
		elif self.buttonType == "group":	
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "dropdown" type buttons
		elif self.buttonType == "dropdown":	
			
			if self.buttonVisible == True:
				#print lineNum(), "rendering dropdown type buttons, button: ", self.button_name, "buttonVisible?:", self.buttonVisible
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

				label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_txt_color)						# set label
				screen.blit(label, (self.x + 5, self.y))														# draw label



		# render "Menu" type buttons
		elif self.buttonType == "menu":	
			
			if self.buttonVisible == True:
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

				label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_txt_color)
				screen.blit(label, (self.x + 5, self.y))


		elif self.buttonType == "textEntry":	
			pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
			pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

			label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_txt_color)
			screen.blit(label, (self.x + 5, self.y))

		# render "popup" type buttons
		elif self.buttonType == "popup":

			if self.buttonVisible == True:
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

				label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_txt_color)
				screen.blit(label, (self.x + 5, self.y))

		elif self.buttonType == "popup_element":

			if self.button_name == "menu02popup01element03":
				self.buttonVisible = pgui.menu02popup01element03["visible"]
			if self.button_name == "menu02popup01element06":
				self.buttonVisible = pgui.menu02popup01element06["visible"]


			if self.buttonVisible == True:
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				#pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 3)  	#border

				label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_txt_color)
				screen.blit(label, (self.x + 5, self.y))

		elif self.buttonType == "popup_element_button":

			if self.buttonVisible == True:
				pygame.draw.rect(screen, self.color, (self.x, self.y, self.x_width, self.y_height))               		#button
				pygame.draw.rect(screen, self.colorBorder, (self.x, self.y, self.x_width, self.y_height), 1)  	#border

				label = myfont.render(str(self.button_label_txt), 0, pgvar.UI_button_txt_color)
				screen.blit(label, (self.x + 5, self.y))


class Particle:
	def __init__ (self,(x,y),particle_size,particle_type,speedx,speedy, particle_color, particle_thickness, particle_mass, particle_charge, 
		particle_X_abs, particle_Y_abs, particle_scale):
		self.x = particle_X_abs
		self.y = particle_Y_abs
		self.size = particle_size
		self.type = particle_type
		self.color = particle_color
		self.speedx = speedx
		self.speedy = speedy
		self.thickness = particle_thickness
		self.mass = particle_mass
		self.charge = particle_charge
		self.scale = particle_scale
		
		self.drag = .999
		self.angle = 0

	def display(self):
		#print "particle_X_abs = ", self.x
		#print "particle_Y_abs = ", self.y

		# get scale modifier
		print "current scale is :", pge.current_scale["scale"]
		print "particle scale is: ", self.scale
		scale_modifier = pge.current_scale["scale"] / self.scale
		print "the scale modifier is: ", scale_modifier
		#display_scale = current_scale["scale"]
		#particle_scale = self.scale

		# # reset size of particle
		self.size = self.size / scale_modifier
		if self.size <= 1:
			self.size = 1

		# # reset position of particle

		positionX = self.x
		positionY = self.y

		#print "old positionX", positionX
		#print "old positionY", positionY
		#print "scale modifier", scale_modifier

		positionX = positionX * scale_modifier
		positionY = positionY * scale_modifier

		#print "mid positionX", positionX
		#print "mid positionY", positionY


		positionX = self.x + (pgvar.pygame_window_width / 2)
		positionY = (pgvar.pygame_window_height / 2) - self.y 

		#print "new positionX", positionX
		#print "new positionY", positionY




		pygame.draw.circle(screen, self.color, (int(positionX), int(positionY)), int(self.size), int(self.thickness))

	def move(self):

		positionX = self.x + (pgvar.pygame_window_width / 2)
		positionY = (pgvar.pygame_window_height / 2) - self.y 

		# clear out old location of particle
		oldColor = self.color
		self.color = pgvar.color_black
		pygame.draw.circle(screen, self.color, (int(positionX), int(positionY)), int(self.size), int(self.thickness))
		self.color = oldColor

		if pgui.bForceGravity["enabled"] == True:
			# modify speed values
			self.speedy = self.speedy + .00001
			# update location
			positionX = positionX + self.speedx * self.drag
			positionY = positionY + self.speedy * self.drag

		if pgui.bForceElectromagnetic["enabled"] == True:
			# modify speed values
			self.speedx = self.speedx + .00001
			self.speedy = self.speedy + .00001
			# update location
			positionX = positionX + self.speedx * self.drag
			positionY = positionY + self.speedy * self.drag

		#draw new particle location
		pygame.draw.circle(screen, self.color, (int(positionX), int(positionY)), int(self.size), int(self.thickness))

	
	