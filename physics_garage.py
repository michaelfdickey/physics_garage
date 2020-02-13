# ************************************************************************************************#
# ************************************************************************************************#
#	Directory Structure
# ************************************************************************************************#
# ************************************************************************************************#

#	/physics_garage.py 		# primary program
#	/pgvar.py 			# global variable declarations
#	/pgui.py 			# photon gui elements and buttons
#	/pfunc.py 			# functions
#	/pclass.py 			# button processing class that handles drawing / displaying UI
#	/pbproc.py 			# processing sticky, group, dropdown etc button actions
#	/photon_ref.py 		# references, dev notes, style guide, modification instructions

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
import decimal

# # unique modules for this app
import pgvar
import pfunc
import pgui
import pclass
import pbproc
import pge

# ************************************************************************************************#
# ************************************************************************************************#
#	inistial variables (for this module)
# ************************************************************************************************#
# ************************************************************************************************#

moduleName = "physics_garage.py"
screen = pygame.display.set_mode((pgvar.pygame_window_width, pgvar.pygame_window_height))

# ************************************************************************************************#
# ************************************************************************************************#
#	MAIN CODE
# ************************************************************************************************#
# ************************************************************************************************#

####### INITIALIZE DISPLAY ##########

pfunc.initializeDisplay()


####### Print Reference Variables ##########

print moduleName, pfunc.lineNum(), "Current Scale: ", pge.current_scale["scale"]

####### MAIN PROGRAM LOOP ##########

running = True

while running:

	if pgui.bPlaySimulation["enabled"] == True:
		pfunc.redrawEverything()

		# # # PARTICLES # # # 	
		# # -- This is updating the particles when the simulation is running -- # #
		for i, particle in enumerate(pfunc.created_particles):
			for particle2 in pfunc.created_particles[i+1:]:
				pfunc.distanceParticles(particle,particle2)
			particle.display()	
			if pgui.bPlaySimulation["enabled"] == True:
				#pfunc.redrawPortal()
				#pfunc.redrawEverything()
				particle.move()
				particle.display()	


	if pgui.buttonFPS["enabled"] == True:
		pygame.draw.rect(screen, pgvar.color_blue, (pgvar.pygame_window_width - 100, pgvar.pygame_window_height - 30, 80, 20))   
		pfunc.count_fps()
		pfunc.show_fps()

	# on screen message box
	# fix to only upate when changed
	pfunc.show_message_txt()



	""" just here for testing and reference. 
	for i, button in enumerate(pfunc.my_buttons):
		button.display() 
	"""

	# # # EVENT PROCESSING # # # 

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:		
			(mouseX, mouseY) = pygame.mouse.get_pos()											# will run continually while button is held down
			print moduleName, pfunc.lineNum(), "mouseX = ", mouseX, "mouseY = ", mouseY			# this if.even MOUSEBUTTONDOWN **MUST** be under the for event in pygame.event.get() to run only once
			selected_button = pfunc.findButton(pfunc.my_buttons, mouseX, mouseY)
			print moduleName, pfunc.lineNum(), "selected button = ", selected_button

			# # # PROCESSING MENU ITEMS # # # 
			# # # # Insert Menu:
			if pgui.mInsert["enabled"] == True:
				if pgui.mInsertoption01["enabled"] == True:
					if mouseX > pgvar.UI_sideBar_width:
						if mouseY > pgvar.UI_topBar_height:
							if selected_button == None:
								print "running InsertProton"
								#pygame.draw.circle(screen, pgvar.color_green, (400, 400), 6, 0)
								pfunc.InsertProton(mouseX, mouseY)
								
								for i, particle in enumerate(pfunc.created_particles):
									for particle2 in pfunc.created_particles[i+1:]:
										pfunc.distanceParticles(particle,particle2)
									particle.display()	
									if pgui.bPlaySimulation["enabled"] == True:
										#pfunc.redrawPortal()
										#pfunc.redrawEverything()
										particle.move()
										particle.display()	


			if selected_button != None: 

				if selected_button.button_label_txt == "EXIT":
					print moduleName,  pfunc.lineNum(), "you pressed exit"
					running = False

				
				# # # PUSHY EVENT processing # # # 

				if selected_button.buttonType == "pushy":
					print moduleName, pfunc.lineNum(), "running MOUSEBUTTONDOWN pushy event"
					print moduleName, pfunc.lineNum(), "selected_button.color  was :", selected_button.color	
					selected_button.color = pgvar.UI_button_click_color
					print moduleName, pfunc.lineNum(), "selected_button.color now : ", selected_button.color			
					selected_button.buttonEnabled = True
					print moduleName, pfunc.lineNum(), "clicked button is a pushy temporary button"

					if selected_button.button_name == "bScaleMinus":
						pgui.bScaleMinus["enabled"] = True
						pgui.bScaleMinus["color"] = pgvar.UI_button_click_color
						pfunc.defineButtons()
						for i, button in enumerate(pfunc.my_buttons):
							button.display()

					if selected_button.button_name == "bScalePlus":
						pgui.bScalePlus["enabled"] = True
						pgui.bScalePlus["color"] = pgvar.UI_button_click_color									
						pfunc.defineButtons()
						for i, button in enumerate(pfunc.my_buttons):
							button.display()

					if selected_button.button_name == "bPushyExample":
						print moduleName, pfunc.lineNum(), "you clicked bPushyExample"
						pgui.bPushyExample["enabled"] = True
						pgui.bPushyExample["color"] = pgvar.UI_button_click_color
						pfunc.defineButtons()
						print moduleName, pfunc.lineNum(), "____drawing buttons from pushy event"
						for i, button in enumerate(pfunc.my_buttons):
							button.display()
						print moduleName, pfunc.lineNum(), "running code for Command01"

					if selected_button.button_name == "bClearSimulation":
						pgui.bClearSimulation["enabled"] = True
						pgui.bClearSimulation["color"] = pgvar.UI_button_click_color
						pfunc.defineButtons()	
						pfunc.created_particles = []		#wipes all particles out of Sim. 
						pfunc.redrawEverything()
						for i, button in enumerate(pfunc.my_buttons):
							button.display()


						# bPushyExample function call goes here:

						# you also need to update the MOUSEBUTTONUP section below to change the color back after releasing button

				# # # OTHER BUTTON TYPES # # #

				if selected_button.buttonType == "sticky":
					print moduleName, pfunc.lineNum(), "running sticky event"
					pbproc.updateStickyButtons(selected_button.button_name)

				if selected_button.buttonType == "group":
					print moduleName, pfunc.lineNum(), "running group type button event"
					pbproc.updateGroupButtons(selected_button.button_name)

				if selected_button.buttonType == "dropdown":
					print moduleName, pfunc.lineNum(), "running dropdown button event"
					pbproc.updateDropdownButtons(selected_button.button_name)

				if selected_button.buttonType == "textEntry":
					print moduleName, pfunc.lineNum(), "running text entry event"
					pbproc.updateTextEntry(selected_button.button_name)

				if selected_button.buttonType == "menu":
					print pfunc.lineNum(), "running menu button event"
					pbproc.updateMenuButtons(selected_button.button_name)




		if event.type == pygame.KEYDOWN:
		 	print "you pressed a key"
		 	if pgui.textField01["enabled"] == True:

			 	if event.key == pygame.K_RETURN:
			 		print(pgvar.entered_text)
			 		#entered_text = ""
					pgui.textField01["label_txt"] = pgvar.entered_text
					pgui.textField01["enabled"] = False
					pgui.textField01["color"] = pgvar.UI_text_entry_box_color
					pfunc.defineButtons()
					pfunc.enumerateButtons()

				elif event.key == pygame.K_BACKSPACE:
					pgvar.entered_text = pgvar.entered_text[:-1]
					pgui.textField01["label_txt"] = pgvar.entered_text
					pfunc.defineButtons()
					pfunc.enumerateButtons()

				else:
			 		if len(pgvar.entered_text) <= 15:
						pgvar.entered_text += event.unicode
						print "entered_text", pgvar.entered_text
						pgui.textField01["label_txt"] = pgvar.entered_text
						pfunc.defineButtons()
						pfunc.enumerateButtons()


		if event.type == pygame.MOUSEBUTTONUP:

			if selected_button != None:
				
				if selected_button.buttonType == "pushy":
					print moduleName,pfunc.lineNum(), "running MOUSEBUTTONUP pushy event"
					print moduleName, pfunc.lineNum(), "selected_button.color  was :", selected_button.color	
					selected_button.color = pgvar.UI_button_color 			#reverts button back to normal color after letting go of mouse
					print moduleName, pfunc.lineNum(), "selected_button.color now : ", selected_button.color	
			
					if selected_button.button_name == "bScaleMinus":
						pgui.bScaleMinus["enabled"] = False
						pgui.bScaleMinus["color"] = pgvar.UI_button_color
						pfunc.defineButtons()
						for i, button in enumerate(pfunc.my_buttons):
							button.display()

					if selected_button.button_name == "bScalePlus":
						pgui.bScalePlus["enabled"] = False
						pgui.bScalePlus["color"] = pgvar.UI_button_color								
						pfunc.defineButtons()
						for i, button in enumerate(pfunc.my_buttons):
							button.display()


					if selected_button.button_name == "bPushyExample":
						print moduleName, pfunc.lineNum(), "you clicked bPushyExample"
						pgui.bPushyExample["enabled"] = False
						pgui.bPushyExample["color"] = pgvar.UI_button_color
						pfunc.defineButtons()
						print moduleName, pfunc.lineNum(), "____drawing buttons from pushy event bPushyExample"
						for i, button in enumerate(pfunc.my_buttons):
							button.display()

					if selected_button.button_name == "bClearSimulation":
						pgui.bClearSimulation["enabled"] = False
						pgui.bClearSimulation["color"] = pgvar.UI_button_color
						pfunc.defineButtons()	
						for i, button in enumerate(pfunc.my_buttons):
							button.display()

			
			for i, button in enumerate(pfunc.my_buttons):
				button.display()	
			

	# always do this last
	pygame.display.flip()