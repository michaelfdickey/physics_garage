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

# pgui.py

moduleName = "pgui.py"

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
#import pgui
#import pclass
#import pbproc

# ************************************************************************************************************************
# ************************************************************************************************************************
# 	button Specific Variables
# ************************************************************************************************************************
# ************************************************************************************************************************

# maybe have small / medium and large button heights and widths? also move these to pgvar?

buttonHeight = 20
display_origin = pgvar.pygame_window_height - 380   #display options origin
forces_origin = pgvar.pygame_window_height - 800
scale_time_origin = pgvar.pygame_window_height - 860
scale_display_origin = pgvar.pygame_window_height -940
display_dimensions_origin = pgvar.pygame_window_height - 1160
calculation_dimensions_origin = pgvar.pygame_window_height - 1100
standard_origin = pgvar.pygame_window_height - 1040
onscreen_message_txt_origin = pgvar.pygame_window_width - 800

group02_origin = pgvar.pygame_window_height - 960
group03_origin = pgvar.pygame_window_height - 1020
dropdown01_origin = pgvar.pygame_window_height - 600
dev_column_origin = pgvar.pygame_window_width - pgvar.UI_menuButton_width

bMenu02_origin = pgvar.pygame_window_width - pgvar.UI_menuButton_width

# ************************************************************************************************************************
# ************************************************************************************************************************
# 	button dictionaries	#
# ************************************************************************************************************************
# ************************************************************************************************************************

# Standard

lStandard = {}
lStandard["name"] = "lStandard"						
lStandard["origin_x"] = 0									
lStandard["origin_y"] = standard_origin			
lStandard["width"] = pgvar.UI_sideBar_width					
lStandard["height"] = buttonHeight							
lStandard["label_txt"] = "Standard: "				
lStandard["type"] = "label"									
lStandard["enabled"] = False									
lStandard["color"] = pgvar.UI_label_color 					
lStandard["group"] = "Standard"						
lStandard["visible"] = True
lStandard["available"] = True						# disables the button entirely from the program						

bStdMetric = {}
bStdMetric["name"] = "bStdMetric"											
bStdMetric["origin_x"] = 0											
bStdMetric["origin_y"] = standard_origin + buttonHeight		
bStdMetric["width"] = pgvar.UI_sideBar_width / 2						
bStdMetric["height"] = 20											
bStdMetric["label_txt"] = " Metric "										
bStdMetric["type"] = "group"											
bStdMetric["enabled"] = False										
bStdMetric["color"] = pgvar.UI_button_color							
bStdMetric["group"] = "Standard"							
bStdMetric["visible"] = True			
bStdMetric["available"] = True


bStdImperial = {}
bStdImperial["name"] = "bStdImperial"											
bStdImperial["origin_x"] = pgvar.UI_sideBar_width / 2												
bStdImperial["origin_y"] = standard_origin + buttonHeight		
bStdImperial["width"] = pgvar.UI_sideBar_width / 2						
bStdImperial["height"] = 20											
bStdImperial["label_txt"] = " Imperial "										
bStdImperial["type"] = "group"											
bStdImperial["enabled"] = False										
bStdImperial["color"] = pgvar.UI_button_color							
bStdImperial["group"] = "Standard"							
bStdImperial["visible"] = True		
bStdImperial["available"] = True

lUnitSystem = {}
lUnitSystem["name"] = "lUnitSystem"						
lUnitSystem["origin_x"] = 0									
lUnitSystem["origin_y"] = standard_origin	 + (2 * buttonHeight)		
lUnitSystem["width"] = pgvar.UI_sideBar_width					
lUnitSystem["height"] = buttonHeight							
lUnitSystem["label_txt"] = "Unit System: "				
lUnitSystem["type"] = "label"									
lUnitSystem["enabled"] = False									
lUnitSystem["color"] = pgvar.UI_label_color 					
lUnitSystem["group"] = "Standard"						
lUnitSystem["visible"] = True									
lUnitSystem["available"] = True

tUnitSys = {}
tUnitSys["name"] = "tUnitSys"											
tUnitSys["origin_x"] = 0											
tUnitSys["origin_y"] = standard_origin + (3 * buttonHeight)		
tUnitSys["width"] = pgvar.UI_sideBar_width - 20						
tUnitSys["height"] = 20											
tUnitSys["label_txt"] = " MKS "										
tUnitSys["type"] = "group"											
tUnitSys["enabled"] = False										
tUnitSys["color"] = pgvar.UI_button_color							
tUnitSys["group"] = "Standard"							
tUnitSys["visible"] = True			
tUnitSys["available"] = True

bUnitSysOpener = {}
bUnitSysOpener["name"] = "bUnitSysOpener"											
bUnitSysOpener["origin_x"] = pgvar.UI_sideBar_width - 20											
bUnitSysOpener["origin_y"] = standard_origin + (3 * buttonHeight)		
bUnitSysOpener["width"] = 20					
bUnitSysOpener["height"] = 20											
bUnitSysOpener["label_txt"] = ">>"										
bUnitSysOpener["type"] = "group"											
bUnitSysOpener["enabled"] = False										
bUnitSysOpener["color"] = pgvar.UI_button_color							
bUnitSysOpener["group"] = "Standard"							
bUnitSysOpener["visible"] = True		
bUnitSysOpener["available"] = True

# # Display Dimensions

lDisplayDimensions = {}
lDisplayDimensions["name"] = "lDisplayDimensions"						# button_name
lDisplayDimensions["origin_x"] = 0									# button_origin_x
lDisplayDimensions["origin_y"] = display_dimensions_origin			# button_origin_y
lDisplayDimensions["width"] = pgvar.UI_sideBar_width					# button_width
lDisplayDimensions["height"] = buttonHeight							# button_height
lDisplayDimensions["label_txt"] = "Display Dimensions"				# button_label_txt
lDisplayDimensions["type"] = "label"									# buttonType
lDisplayDimensions["enabled"] = False									# buttonEnabled
lDisplayDimensions["color"] = pgvar.UI_label_color 					# buttonColor
lDisplayDimensions["group"] = "DisplayDimensions"						# buttonGroup
lDisplayDimensions["visible"] = True									# buttonVisible
lDisplayDimensions["available"] = True

b1D = {}
b1D["name"] = "b1D"											# button_name
b1D["origin_x"] = 0											# button_origin_x
b1D["origin_y"] = display_dimensions_origin + buttonHeight		# button_origin_y
b1D["width"] = pgvar.UI_sideBar_width	 / 3						# button_width
b1D["height"] = 20											# button_height
b1D["label_txt"] = "  1D"										# button_label_txt
b1D["type"] = "group"											# buttonType
b1D["enabled"] = False										# buttonEnabled
b1D["color"] = pgvar.UI_button_color							# buttonColor
b1D["group"] = "displayDimensions"							# buttonGroup
b1D["visible"] = True											# buttonVisible
b1D["available"] = True

b2D = {}
b2D["name"] = "b2D"									# button_name
b2D["origin_x"] = (pgvar.UI_sideBar_width / 3) 		# button_origin_x
b2D["origin_y"] = display_dimensions_origin + buttonHeight			# button_origin_y
b2D["width"] = pgvar.UI_sideBar_width	 / 3				# button_width
b2D["height"] = 20									# button_height
b2D["label_txt"] = "  2D"								# button_label_txt
b2D["type"] = "group"									# buttonType
b2D["enabled"] = False								# buttonEnabled
b2D["color"] = pgvar.UI_button_color					# buttonColor
b2D["group"] = "displayDimensions"					# buttonGroup
b2D["visible"] = True									# buttonVisible
b2D["available"] = True

b3D = {}
b3D["name"] = "b3D"									# button_name
b3D["origin_x"] = (pgvar.UI_sideBar_width / 3) * 2 		# button_origin_x
b3D["origin_y"] = display_dimensions_origin + buttonHeight			# button_origin_y
b3D["width"] = pgvar.UI_sideBar_width	 / 3				# button_width
b3D["height"] = 20									# button_height
b3D["label_txt"] = "  3D"								# button_label_txt
b3D["type"] = "group"									# buttonType
b3D["enabled"] = False								# buttonEnabled
b3D["color"] = pgvar.UI_button_color					# buttonColor
b3D["group"] = "displayDimensions"					# buttonGroup
b3D["visible"] = True									# buttonVisible
b3D["available"] = True


# # Calculation Dimensions

lCalculationDimensions = {}
lCalculationDimensions["name"] = "lCalculationDimensions"					# button_name
lCalculationDimensions["origin_x"] = 0									# button_origin_x
lCalculationDimensions["origin_y"] = calculation_dimensions_origin			# button_origin_y
lCalculationDimensions["width"] = pgvar.UI_sideBar_width					# button_width
lCalculationDimensions["height"] = buttonHeight							# button_height
lCalculationDimensions["label_txt"] = "Calculation Dimens"			# button_label_txt
lCalculationDimensions["type"] = "label"									# buttonType
lCalculationDimensions["enabled"] = False									# buttonEnabled
lCalculationDimensions["color"] = pgvar.UI_label_color 					# buttonColor
lCalculationDimensions["group"] = "CalculationDimensions"					# buttonGroup
lCalculationDimensions["visible"] = True									# buttonVisible
lCalculationDimensions["available"] = True

bCalc1D = {}
bCalc1D["name"] = "bCalc1D"											# button_name
bCalc1D["origin_x"] = 0											# button_origin_x
bCalc1D["origin_y"] = calculation_dimensions_origin + buttonHeight		# button_origin_y
bCalc1D["width"] = pgvar.UI_sideBar_width	 / 3						# button_width
bCalc1D["height"] = 20											# button_height
bCalc1D["label_txt"] = "  1D"										# button_label_txt
bCalc1D["type"] = "group"											# buttonType
bCalc1D["enabled"] = False										# buttonEnabled
bCalc1D["color"] = pgvar.UI_button_color							# buttonColor
bCalc1D["group"] = "calculationDimesions"							# buttonGroup
bCalc1D["visible"] = True											# buttonVisible
bCalc1D["available"] = True

bCalc2D = {}
bCalc2D["name"] = "bCalc2D"											# button_name
bCalc2D["origin_x"] = (pgvar.UI_sideBar_width / 3) 				# button_origin_x
bCalc2D["origin_y"] = calculation_dimensions_origin + buttonHeight		# button_origin_y
bCalc2D["width"] = pgvar.UI_sideBar_width	 / 3						# button_width
bCalc2D["height"] = 20											# button_height
bCalc2D["label_txt"] = "  2D"										# button_label_txt
bCalc2D["type"] = "group"											# buttonType
bCalc2D["enabled"] = False										# buttonEnabled
bCalc2D["color"] = pgvar.UI_button_color							# buttonColor
bCalc2D["group"] = "calculationDimesions"							# buttonGroup
bCalc2D["visible"] = True											# buttonVisible
bCalc2D["available"] = True

bCalc3D = {}		
bCalc3D["name"] = "bCalc3D"												# button_name
bCalc3D["origin_x"] = (pgvar.UI_sideBar_width / 3) * 2					# button_origin_x
bCalc3D["origin_y"] = calculation_dimensions_origin + buttonHeight			# button_origin_y
bCalc3D["width"] = pgvar.UI_sideBar_width	 / 3							# button_width
bCalc3D["height"] = 20												# button_height
bCalc3D["label_txt"] = "  3D"											# button_label_txt
bCalc3D["type"] = "group"												# buttonType
bCalc3D["enabled"] = False											# buttonEnabled
bCalc3D["color"] = pgvar.UI_button_color								# buttonColor
bCalc3D["group"] = "calculationDimesions"								# buttonGroup
bCalc3D["visible"] = True												# buttonVisible
bCalc3D["available"] = True


# # Forces Buttons

lForces = {}
lForces["name"] = "lForces"								# button_name
lForces["origin_x"] = 0									# button_origin_x
lForces["origin_y"] = forces_origin						# button_origin_y
lForces["width"] = pgvar.UI_sideBar_width					# button_width
lForces["height"] = buttonHeight							# button_height
lForces["label_txt"] = "Forces:"							# button_label_txt
lForces["type"] = "label"									# buttonType
lForces["enabled"] = False								# buttonEnabled
lForces["color"] = pgvar.UI_label_color 					# buttonColor
lForces["group"] = "forces"								# buttonGroup
lForces["visible"] = True									# buttonVisible
lForces["available"] = True

bForceGravity = {}
bForceGravity["name"] = "bForceGravity"								
bForceGravity["origin_x"] = 0									
bForceGravity["origin_y"] = forces_origin + 20						
bForceGravity["width"] = pgvar.UI_sideBar_width - 20					
bForceGravity["height"] = buttonHeight							
bForceGravity["label_txt"] = "Gravity"							
bForceGravity["type"] = "sticky"									
bForceGravity["enabled"] = False								
bForceGravity["color"] = pgvar.UI_button_color 					
bForceGravity["group"] = "forces"								
bForceGravity["visible"] = True									
bForceGravity["available"] = True

bForceGravityOpener = {}
bForceGravityOpener["name"] = "bForceGravityOpener"								
bForceGravityOpener["origin_x"] = pgvar.UI_sideBar_width - 20									
bForceGravityOpener["origin_y"] = forces_origin + 20						
bForceGravityOpener["width"] = 20				
bForceGravityOpener["height"] = buttonHeight							
bForceGravityOpener["label_txt"] = ">>"							
bForceGravityOpener["type"] = "dropdown"									
bForceGravityOpener["enabled"] = False								
bForceGravityOpener["color"] = pgvar.UI_button_color 					
bForceGravityOpener["group"] = "forces"								
bForceGravityOpener["visible"] = True	
bForceGravityOpener["available"] = True

bForceElectromagnetic = {}
bForceElectromagnetic["name"] = "bForceElectromagnetic"								
bForceElectromagnetic["origin_x"] = 0									
bForceElectromagnetic["origin_y"] = forces_origin + 40						
bForceElectromagnetic["width"] = pgvar.UI_sideBar_width - 20					
bForceElectromagnetic["height"] = buttonHeight							
bForceElectromagnetic["label_txt"] = "Electromagnetic"							
bForceElectromagnetic["type"] = "sticky"									
bForceElectromagnetic["enabled"] = False								
bForceElectromagnetic["color"] = pgvar.UI_button_color 					
bForceElectromagnetic["group"] = "forces"								
bForceElectromagnetic["visible"] = True									
bForceElectromagnetic["available"] = True

bForceElectromagneticOpener = {}
bForceElectromagneticOpener["name"] = "bForceElectromagneticOpener"								
bForceElectromagneticOpener["origin_x"] = pgvar.UI_sideBar_width - 20									
bForceElectromagneticOpener["origin_y"] = forces_origin + 40						
bForceElectromagneticOpener["width"] = 20				
bForceElectromagneticOpener["height"] = buttonHeight							
bForceElectromagneticOpener["label_txt"] = ">>"							
bForceElectromagneticOpener["type"] = "dropdown"									
bForceElectromagneticOpener["enabled"] = False								
bForceElectromagneticOpener["color"] = pgvar.UI_button_color 					
bForceElectromagneticOpener["group"] = "forces"								
bForceElectromagneticOpener["visible"] = True	
bForceElectromagneticOpener["available"] = True	

bForceStrongNuclear = {}
bForceStrongNuclear["name"] = "bForceStrongNuclear"								
bForceStrongNuclear["origin_x"] = 0									
bForceStrongNuclear["origin_y"] = forces_origin + 60						
bForceStrongNuclear["width"] = pgvar.UI_sideBar_width - 20					
bForceStrongNuclear["height"] = buttonHeight							
bForceStrongNuclear["label_txt"] = "Strong Nuclear"							
bForceStrongNuclear["type"] = "sticky"									
bForceStrongNuclear["enabled"] = False								
bForceStrongNuclear["color"] = pgvar.UI_button_color 					
bForceStrongNuclear["group"] = "forces"								
bForceStrongNuclear["visible"] = True									
bForceStrongNuclear["available"] = True

bForceStrongNuclearOpener = {}
bForceStrongNuclearOpener["name"] = "bForceStrongNuclearOpener"								
bForceStrongNuclearOpener["origin_x"] = pgvar.UI_sideBar_width - 20									
bForceStrongNuclearOpener["origin_y"] = forces_origin + 60						
bForceStrongNuclearOpener["width"] = 20				
bForceStrongNuclearOpener["height"] = buttonHeight							
bForceStrongNuclearOpener["label_txt"] = ">>"							
bForceStrongNuclearOpener["type"] = "dropdown"									
bForceStrongNuclearOpener["enabled"] = False								
bForceStrongNuclearOpener["color"] = pgvar.UI_button_color 					
bForceStrongNuclearOpener["group"] = "forces"								
bForceStrongNuclearOpener["visible"] = True	
bForceStrongNuclearOpener["available"] = True

bForceWeakNuclear = {}
bForceWeakNuclear["name"] = "bForceWeakNuclear"								
bForceWeakNuclear["origin_x"] = 0									
bForceWeakNuclear["origin_y"] = forces_origin + 80						
bForceWeakNuclear["width"] = pgvar.UI_sideBar_width - 20					
bForceWeakNuclear["height"] = buttonHeight							
bForceWeakNuclear["label_txt"] = "Weak Nuclear"							
bForceWeakNuclear["type"] = "sticky"									
bForceWeakNuclear["enabled"] = False								
bForceWeakNuclear["color"] = pgvar.UI_button_color 					
bForceWeakNuclear["group"] = "forces"								
bForceWeakNuclear["visible"] = True									
bForceWeakNuclear["available"] = True

bForceWeakNuclearOpener = {}
bForceWeakNuclearOpener["name"] = "bForceWeakNuclearOpener"								
bForceWeakNuclearOpener["origin_x"] = pgvar.UI_sideBar_width - 20									
bForceWeakNuclearOpener["origin_y"] = forces_origin + 80						
bForceWeakNuclearOpener["width"] = 20				
bForceWeakNuclearOpener["height"] = buttonHeight							
bForceWeakNuclearOpener["label_txt"] = ">>"							
bForceWeakNuclearOpener["type"] = "dropdown"									
bForceWeakNuclearOpener["enabled"] = False								
bForceWeakNuclearOpener["color"] = pgvar.UI_button_color 					
bForceWeakNuclearOpener["group"] = "forces"								
bForceWeakNuclearOpener["visible"] = True	
bForceWeakNuclearOpener["available"] = True

bForceDarkEnergy = {}
bForceDarkEnergy["name"] = "bForceDarkEnergy"								
bForceDarkEnergy["origin_x"] = 0									
bForceDarkEnergy["origin_y"] = forces_origin + 100						
bForceDarkEnergy["width"] = pgvar.UI_sideBar_width - 20					
bForceDarkEnergy["height"] = buttonHeight							
bForceDarkEnergy["label_txt"] = "Dark Energy"							
bForceDarkEnergy["type"] = "sticky"									
bForceDarkEnergy["enabled"] = False								
bForceDarkEnergy["color"] = pgvar.UI_button_color 					
bForceDarkEnergy["group"] = "forces"								
bForceDarkEnergy["visible"] = True									
bForceDarkEnergy["available"] = True

bForceDarkEnergyOpener = {}
bForceDarkEnergyOpener["name"] = "bForceDarkEnergyOpener"								
bForceDarkEnergyOpener["origin_x"] = pgvar.UI_sideBar_width - 20									
bForceDarkEnergyOpener["origin_y"] = forces_origin + 100						
bForceDarkEnergyOpener["width"] = 20				
bForceDarkEnergyOpener["height"] = buttonHeight							
bForceDarkEnergyOpener["label_txt"] = ">>"							
bForceDarkEnergyOpener["type"] = "dropdown"									
bForceDarkEnergyOpener["enabled"] = False								
bForceDarkEnergyOpener["color"] = pgvar.UI_button_color 					
bForceDarkEnergyOpener["group"] = "forces"								
bForceDarkEnergyOpener["visible"] = True	
bForceDarkEnergyOpener["available"] = True

bForceNewOther = {}
bForceNewOther["name"] = "bForceNewOther"								
bForceNewOther["origin_x"] = 0									
bForceNewOther["origin_y"] = forces_origin + 120						
bForceNewOther["width"] = pgvar.UI_sideBar_width - 20					
bForceNewOther["height"] = buttonHeight							
bForceNewOther["label_txt"] = "New / Other"							
bForceNewOther["type"] = "sticky"									
bForceNewOther["enabled"] = False								
bForceNewOther["color"] = pgvar.UI_button_color 					
bForceNewOther["group"] = "forces"								
bForceNewOther["visible"] = True									
bForceNewOther["available"] = True

bForceNewOtherOpener = {}
bForceNewOtherOpener["name"] = "bForceNewOtherOpener"								
bForceNewOtherOpener["origin_x"] = pgvar.UI_sideBar_width - 20									
bForceNewOtherOpener["origin_y"] = forces_origin + 120						
bForceNewOtherOpener["width"] = 20				
bForceNewOtherOpener["height"] = buttonHeight							
bForceNewOtherOpener["label_txt"] = ">>"							
bForceNewOtherOpener["type"] = "dropdown"									
bForceNewOtherOpener["enabled"] = False								
bForceNewOtherOpener["color"] = pgvar.UI_button_color 					
bForceNewOtherOpener["group"] = "forces"								
bForceNewOtherOpener["visible"] = True	
bForceNewOtherOpener["available"] = True

# # Scale Time

lScaleTime = {}
lScaleTime["name"] = "lScaleTime"								# button_name
lScaleTime["origin_x"] = 0									# button_origin_x
lScaleTime["origin_y"] = scale_time_origin						# button_origin_y
lScaleTime["width"] = pgvar.UI_sideBar_width					# button_width
lScaleTime["height"] = buttonHeight							# button_height
lScaleTime["label_txt"] = "Time Step"							# button_label_txt
lScaleTime["type"] = "label"									# buttonType
lScaleTime["enabled"] = False								# buttonEnabled
lScaleTime["color"] = pgvar.UI_label_color 					# buttonColor
lScaleTime["group"] = "forces"								# buttonGroup
lScaleTime["visible"] = True									# buttonVisible
lScaleTime["available"] = True

bScaleTime = {}
bScaleTime["name"] = "bScaleTime"								
bScaleTime["origin_x"] = 0									
bScaleTime["origin_y"] = scale_time_origin	 + 20					
bScaleTime["width"] = pgvar.UI_sideBar_width - 20					
bScaleTime["height"] = buttonHeight							
bScaleTime["label_txt"] = "1 s / frame"							
bScaleTime["type"] = "sticky"									
bScaleTime["enabled"] = False								
bScaleTime["color"] = pgvar.UI_button_color					
bScaleTime["group"] = "forces"								
bScaleTime["visible"] = True									
bScaleTime["available"] = True

bScaleTimeOpener = {}
bScaleTimeOpener["name"] = "bScaleTimeOpener"								
bScaleTimeOpener["origin_x"] = pgvar.UI_sideBar_width - 20									
bScaleTimeOpener["origin_y"] = scale_time_origin + 20					
bScaleTimeOpener["width"] = 20					
bScaleTimeOpener["height"] = buttonHeight							
bScaleTimeOpener["label_txt"] = ">>"							
bScaleTimeOpener["type"] = "dropdown"									
bScaleTimeOpener["enabled"] = False								
bScaleTimeOpener["color"] = pgvar.UI_button_color					
bScaleTimeOpener["group"] = "forces"								
bScaleTimeOpener["visible"] = True			
bScaleTimeOpener["available"] = True

# # Display options buttons:

labelDisplay = {}
labelDisplay["name"] = "displayLabel"								# button_name
labelDisplay["origin_x"] = 0										# button_origin_x
labelDisplay["origin_y"] = display_origin							# button_origin_y
labelDisplay["width"] = pgvar.UI_sideBar_width					# button_width
labelDisplay["height"] = 20										# button_height
labelDisplay["label_txt"] = "Display Options:"					# button_label_txt
labelDisplay["type"] = "label"									# buttonType
labelDisplay["enabled"] = False									# buttonEnabled
labelDisplay["color"] = pgvar.UI_button_color						# buttonColor
labelDisplay["group"] = "origin"									# buttonGroup
labelDisplay["visible"] = True									# buttonVisible
labelDisplay["available"] = True

buttonOrigin = {}
buttonOrigin["name"] = "origin"								# button_name
buttonOrigin["origin_x"] = 0									# button_origin_x
buttonOrigin["origin_y"] = display_origin + (buttonHeight )		# button_origin_y
buttonOrigin["width"] = pgvar.UI_sideBar_width				# button_width
buttonOrigin["height"] = 20									# button_height
buttonOrigin["label_txt"] = "Origin                      +"				# button_label_txt
buttonOrigin["type"] = "sticky"								# buttonType
buttonOrigin["enabled"] = False								# buttonEnabled
buttonOrigin["color"] = pgvar.UI_button_color					# buttonColor
buttonOrigin["group"] = "origin"								# buttonGroup
buttonOrigin["visible"] = True								# buttonVisible
buttonOrigin["available"] = True

buttonGrid = {}
buttonGrid["name"] = "grid"									# button_name
buttonGrid["origin_x"] = 0									# button_origin_x
buttonGrid["origin_y"] = display_origin + (buttonHeight * 2)	# button_origin_y
buttonGrid["width"] = pgvar.UI_sideBar_width					# button_width
buttonGrid["height"] = 20										# button_height
buttonGrid["label_txt"] = "Grid                          #"					# button_label_txt
buttonGrid["type"] = "sticky"									# buttonType
buttonGrid["enabled"] = False									# buttonEnabled
buttonGrid["color"] = pgvar.UI_button_color					# buttonColor
buttonGrid["group"] = "grid"									# buttonGroup
buttonGrid["visible"] = True									# buttonVisible
buttonGrid["available"] = True

buttonFPS = {}
buttonFPS["name"] = "fps"										# button_name
buttonFPS["origin_x"] = 0										# button_origin_x
buttonFPS["origin_y"] = display_origin + (buttonHeight * 3)		# button_origin_y
buttonFPS["width"] = pgvar.UI_sideBar_width					# button_width
buttonFPS["height"] = 20										# button_height
buttonFPS["label_txt"] = " FPS "								# button_label_txt
buttonFPS["type"] = "sticky"									# buttonType
buttonFPS["enabled"] = False									# buttonEnabled
buttonFPS["color"] = pgvar.UI_button_color					# buttonColor
buttonFPS["group"] = "fps"									# buttonGroup
buttonFPS["visible"] = True									# buttonVisible
buttonFPS["available"] = True

bForceVectors = {}
bForceVectors["name"] = "bForceVectors"									# button_name
bForceVectors["origin_x"] = 0										# button_origin_x
bForceVectors["origin_y"] = display_origin + (buttonHeight * 4)		# button_origin_y
bForceVectors["width"] = pgvar.UI_sideBar_width					# button_width
bForceVectors["height"] = 20										# button_height
bForceVectors["label_txt"] = " Force Vectors "						# button_label_txt
bForceVectors["type"] = "sticky"									# buttonType
bForceVectors["enabled"] = False									# buttonEnabled
bForceVectors["color"] = pgvar.UI_button_color						# buttonColor
bForceVectors["group"] = "vectors"									# buttonGroup
bForceVectors["visible"] = True									# buttonVisible
bForceVectors["available"] = True

bDistComponents = {}
bDistComponents["name"] = "bDistComponents"							# button_name
bDistComponents["origin_x"] = 0										# button_origin_x
bDistComponents["origin_y"] = display_origin + (buttonHeight * 5)		# button_origin_y
bDistComponents["width"] = pgvar.UI_sideBar_width						# button_width
bDistComponents["height"] = 20										# button_height
bDistComponents["label_txt"] = " Distances xyzh"						# button_label_txt
bDistComponents["type"] = "sticky"									# buttonType
bDistComponents["enabled"] = False									# buttonEnabled
bDistComponents["color"] = pgvar.UI_button_color						# buttonColor
bDistComponents["group"] = "vectors"									# buttonGroup
bDistComponents["visible"] = True										# buttonVisible
bDistComponents["available"] = True


# # Scale Time

lScaleLabel = {}
lScaleLabel["name"] = "lScaleLabel"							# button_name
lScaleLabel["origin_x"] = 0									# button_origin_x
lScaleLabel["origin_y"] = scale_display_origin				# button_origin_y
lScaleLabel["width"] = pgvar.UI_sideBar_width									# button_width
lScaleLabel["height"] = 20									# button_height
lScaleLabel["label_txt"] = "Display Scale :"							# button_label_txt
lScaleLabel["type"] = "label"								# buttonType
lScaleLabel["enabled"] = False								# buttonEnabled
lScaleLabel["color"] = pgvar.UI_label_color				# buttonColor
lScaleLabel["group"] = "Scale"								# buttonGroup
lScaleLabel["visible"] = True									# buttonVisible
lScaleLabel["available"] = True

bScaleMinus = {}
bScaleMinus["name"] = "bScaleMinus"							# button_name
bScaleMinus["origin_x"] = 0									# button_origin_x
bScaleMinus["origin_y"] = scale_display_origin + 20			# button_origin_y
bScaleMinus["width"] = pgvar.UI_sideBar_width / 3				# button_width
bScaleMinus["height"] = 20									# button_height
bScaleMinus["label_txt"] = "   - "								# button_label_txt
bScaleMinus["type"] = "pushy"									# buttonType
bScaleMinus["enabled"] = False								# buttonEnabled
bScaleMinus["color"] = pgvar.UI_button_color					# buttonColor
bScaleMinus["group"] = "Scale"								# buttonGroup
bScaleMinus["visible"] = True									# buttonVisible
bScaleMinus["available"] = True

bScalePlus = {}
bScalePlus["name"] = "bScalePlus"								# button_name
bScalePlus["origin_x"] = pgvar.UI_sideBar_width / 3			# button_origin_x
bScalePlus["origin_y"] = scale_display_origin	 + 20				# button_origin_y
bScalePlus["width"] = pgvar.UI_sideBar_width / 3 										# button_width
bScalePlus["height"] = 20										# button_height
bScalePlus["label_txt"] = "   + "								# button_label_txt
bScalePlus["type"] = "pushy"									# buttonType
bScalePlus["enabled"] = False									# buttonEnabled
bScalePlus["color"] = pgvar.UI_button_color					# buttonColor
bScalePlus["group"] = "Scale"									# buttonGroup
bScalePlus["visible"] = True									# buttonVisible		
bScalePlus["available"] = True

bScaleOpener = {}
bScaleOpener["name"] = "bScaleOpener"								# button_name
bScaleOpener["origin_x"] =  (pgvar.UI_sideBar_width / 3)*2			# button_origin_x
bScaleOpener["origin_y"] = scale_display_origin + 20					# button_origin_y
bScaleOpener["width"] =  pgvar.UI_sideBar_width / 3										# button_width
bScaleOpener["height"] = 20										# button_height
bScaleOpener["label_txt"] = "  >>"									# button_label_txt
bScaleOpener["type"] = "textEntry"								# buttonType
bScaleOpener["enabled"] = False									# buttonEnabled
bScaleOpener["color"] = pgvar.UI_button_color						# buttonColor
bScaleOpener["group"] = "Scale"									# buttonGroup
bScaleOpener["visible"] = True									# buttonVisible	
bScaleOpener["available"] = True

tScaleSelection = {}
tScaleSelection["name"] = "tScaleSelection"							# button_name
tScaleSelection["origin_x"] = 0										# button_origin_x
tScaleSelection["origin_y"] = scale_display_origin + 40				# button_origin_y
tScaleSelection["width"] = pgvar.UI_sideBar_width						# button_width
tScaleSelection["height"] = 20										# button_height
tScaleSelection["label_txt"] = ".1fm (1.0 x 10^-16m)"					# button_label_txt
tScaleSelection["type"] = "sticky"									# buttonType
tScaleSelection["enabled"] = False									# buttonEnabled
tScaleSelection["color"] = pgvar.UI_button_color						# buttonColor
tScaleSelection["group"] = "Scale"									# buttonGroup
tScaleSelection["visible"] = True										# buttonVisible		
tScaleSelection["available"] = True



# # Changing Resolution Button and label

lResolution = {}
lResolution["name"] = "lResolution"
lResolution["origin_x"] = 0
lResolution["origin_y"] = pgvar.pygame_window_height - 220
lResolution["width"] =pgvar.UI_sideBar_width
lResolution["height"] = 20
lResolution["label_txt"] = "Resolution:"
lResolution["type"] = "label"
lResolution["enabled"] = True
lResolution["color"] = pgvar.UI_label_color
lResolution["group"] = "Resolution"
lResolution["visible"] = True
lResolution["available"] = True

tResolution = {}												# tName = text element, lName = label, bName = button, mName = menu
tResolution["name"] = "tResolution"							# button_name
tResolution["origin_x"] = 0									# button_origin_x
tResolution["origin_y"] = pgvar.pygame_window_height - 200		# button_origin_y
tResolution["width"] = pgvar.UI_sideBar_width - 20				# button_width
tResolution["height"] = 20									# button_height
tResolution["label_txt"] = pgvar.pygame_window_width, pgvar.pygame_window_height							# button_label_txt
tResolution["type"] = "dropdown"								# buttonType
tResolution["enabled"] = False								# buttonEnabled
tResolution["color"] = pgvar.UI_button_color					# buttonColor
tResolution["group"] = "Resolution"							# buttonGroup
tResolution["visible"] = True									# buttonVisible
tResolution["available"] = True

bResolutionOpener = {}
bResolutionOpener["name"] = "bResolutionOpener"					# button_name
bResolutionOpener["origin_x"] = pgvar.UI_sideBar_width - 20		# button_origin_x
bResolutionOpener["origin_y"] = pgvar.pygame_window_height - 200	# button_origin_y
bResolutionOpener["width"] = 20									# button_width
bResolutionOpener["height"] = 20									# button_height
bResolutionOpener["label_txt"] = ">>"								# button_label_txt
bResolutionOpener["type"] = "dropdown"							# buttonType
bResolutionOpener["enabled"] = False								# buttonEnabled
bResolutionOpener["color"] = pgvar.UI_button_color				# buttonColor
bResolutionOpener["group"] = "Resolution"							# buttonGroup
bResolutionOpener["visible"] = True								# buttonVisible
bResolutionOpener["available"] = True


## Simulation Control

lSimulationControl = {}
lSimulationControl["name"] = "lSimulationControl"
lSimulationControl["origin_x"] = 0
lSimulationControl["origin_y"] = pgvar.pygame_window_height - 160
lSimulationControl["width"] =pgvar.UI_sideBar_width
lSimulationControl["height"] = 20
lSimulationControl["label_txt"] = "Simulation Control:"
lSimulationControl["type"] = "label"
lSimulationControl["enabled"] = True
lSimulationControl["color"] = pgvar.UI_label_color
lSimulationControl["group"] = "SimulationControl"
lSimulationControl["visible"] = True
lSimulationControl["available"] = True

bPlaySimulation = {}
bPlaySimulation["name"] = "bPlaySimulation"
bPlaySimulation["origin_x"] = 0
bPlaySimulation["origin_y"] = pgvar.pygame_window_height - 140
bPlaySimulation["width"] = pgvar.UI_sideBar_width
bPlaySimulation["height"] = 20
bPlaySimulation["label_txt"] = "Play Simulation"
bPlaySimulation["type"] = "sticky"
bPlaySimulation["enabled"] = False
bPlaySimulation["color"] = pgvar.UI_button_color
bPlaySimulation["group"] = "SimulationControl"
bPlaySimulation["visible"] = True
bPlaySimulation["available"] = True

bPauseSimulation = {}
bPauseSimulation["name"] = "bPauseSimulation"
bPauseSimulation["origin_x"] = 0
bPauseSimulation["origin_y"] = pgvar.pygame_window_height - 120
bPauseSimulation["width"] = pgvar.UI_sideBar_width
bPauseSimulation["height"] = 20
bPauseSimulation["label_txt"] = "Pause Simulation"
bPauseSimulation["type"] = "sticky"
bPauseSimulation["enabled"] = True
bPauseSimulation["color"] = pgvar.UI_button_selected_color
bPauseSimulation["group"] = "SimulationControl"
bPauseSimulation["visible"] = True
bPauseSimulation["available"] = True

bSaveSimulation = {}
bSaveSimulation["name"] = "bSaveSimulation"
bSaveSimulation["origin_x"] = 0
bSaveSimulation["origin_y"] = pgvar.pygame_window_height - 100
bSaveSimulation["width"] = pgvar.UI_sideBar_width
bSaveSimulation["height"] = 20
bSaveSimulation["label_txt"] = "Save Simulation"
bSaveSimulation["type"] = "sticky"
bSaveSimulation["enabled"] = True
bSaveSimulation["color"] = pgvar.UI_button_disabled
bSaveSimulation["group"] = "SimulationControl"
bSaveSimulation["visible"] = True
bSaveSimulation["available"] = False

bLoadSimulation = {}
bLoadSimulation["name"] = "bLoadSimulation"
bLoadSimulation["origin_x"] = 0
bLoadSimulation["origin_y"] = pgvar.pygame_window_height - 80
bLoadSimulation["width"] = pgvar.UI_sideBar_width
bLoadSimulation["height"] = 20
bLoadSimulation["label_txt"] = "Load Simulation"
bLoadSimulation["type"] = "sticky"
bLoadSimulation["enabled"] = True
bLoadSimulation["color"] = pgvar.UI_button_disabled
bLoadSimulation["group"] = "SimulationControl"
bLoadSimulation["visible"] = True
bLoadSimulation["available"] = False

bClearSimulation = {}
bClearSimulation["name"] = "bClearSimulation"
bClearSimulation["origin_x"] = 0
bClearSimulation["origin_y"] = pgvar.pygame_window_height - 60
bClearSimulation["width"] = pgvar.UI_sideBar_width
bClearSimulation["height"] = 20
bClearSimulation["label_txt"] = "Clear Simulation"
bClearSimulation["type"] = "pushy"
bClearSimulation["enabled"] = True
bClearSimulation["color"] = pgvar.UI_button_color
bClearSimulation["group"] = "SimulationControl"
bClearSimulation["visible"] = True
bClearSimulation["available"] = True


# # Exit Button:

buttonExit = {}
buttonExit["name"] = "exit"
buttonExit["origin_x"] = 0
buttonExit["origin_y"] = pgvar.pygame_window_height - 20
buttonExit["width"] = pgvar.UI_sideBar_width
buttonExit["height"] = 20
buttonExit["label_txt"] = "EXIT"
buttonExit["type"] = "pushy"
buttonExit["enabled"] = True
buttonExit["color"] = pgvar.UI_button_color
buttonExit["group"] = "buttonExit"
buttonExit["visible"] = True
buttonExit["available"] = True


####################################################################################
### ---------------------------------------------------------------------------- ####
### DEV BUTTONS FOR REFERENCE
### ----------------------------------------------------------------------------####
###################################################################################

# # reference pushy button

bPushyExample = {}
bPushyExample["name"] = "bPushyExample"
bPushyExample["origin_x"] = dev_column_origin	
bPushyExample["origin_y"] = pgvar.pygame_window_height - 720
bPushyExample["width"] =pgvar.UI_sideBar_width
bPushyExample["height"] = 20
bPushyExample["label_txt"] = "Pushy Example"
bPushyExample["type"] = "pushy"
bPushyExample["enabled"] = True
bPushyExample["color"] = pgvar.UI_button_color
bPushyExample["group"] = "PushyExample"
bPushyExample["visible"] = True
bPushyExample["available"] = True

# # Sticky Buttons 
# # once clicked, they stay enabled, until clicked again which disables them

labelSticky = {}
labelSticky["name"] = "sticky_label"
labelSticky["origin_x"] = dev_column_origin	
labelSticky["origin_y"] = pgvar.pygame_window_height - 820
labelSticky["width"] = pgvar.UI_sideBar_width
labelSticky["height"] = 20
labelSticky["label_txt"] = "Sticky Buttons"
labelSticky["type"] = "label"
labelSticky["enabled"] = True
labelSticky["color"] = pgvar.UI_label_color
labelSticky["group"] = "sticky_buttons"
labelSticky["visible"] = True
labelSticky["available"] = True

buttonSticky01 = {}
buttonSticky01["name"] = "sticky01"
buttonSticky01["origin_x"] = dev_column_origin	
buttonSticky01["origin_y"] = pgvar.pygame_window_height - 760
buttonSticky01["width"] = pgvar.UI_sideBar_width
buttonSticky01["height"] = 20
buttonSticky01["label_txt"] = "Sticky 01"
buttonSticky01["type"] = "sticky"
buttonSticky01["enabled"] = False
buttonSticky01["color"] = pgvar.UI_button_color
buttonSticky01["group"] = "sticky01"
buttonSticky01["visible"] = True
buttonSticky01["available"] = True

buttonSticky02 = {}
buttonSticky02["name"] = "sticky02"
buttonSticky02["origin_x"] = dev_column_origin	
buttonSticky02["origin_y"] = pgvar.pygame_window_height - 780
buttonSticky02["width"] = pgvar.UI_sideBar_width
buttonSticky02["height"] = 20
buttonSticky02["label_txt"] = "Sticky 02"
buttonSticky02["type"] = "sticky"
buttonSticky02["enabled"] = False
buttonSticky02["color"] = pgvar.UI_button_color
buttonSticky02["group"] = "sticky02"
buttonSticky02["visible"] = True
buttonSticky02["available"] = True

buttonSticky03 = {}
buttonSticky03["name"] = "sticky03"								# button_name
buttonSticky03["origin_x"] = dev_column_origin										# button_origin_x
buttonSticky03["origin_y"] = pgvar.pygame_window_height - 800		# button_origin_y
buttonSticky03["width"] = pgvar.UI_sideBar_width					# button_width
buttonSticky03["height"] = 20										# button_height
buttonSticky03["label_txt"] = "Sticky 03"							# button_label_txt
buttonSticky03["type"] = "sticky"									# buttonType
buttonSticky03["enabled"] = False									# buttonEnabled
buttonSticky03["color"] = pgvar.UI_button_color 					# buttonColor
buttonSticky03["group"] = "sticky03"								# buttonGroup
buttonSticky03["visible"] = True									# buttonVisible
buttonSticky03["available"] = True

# # Group 01 Buttons:
# # Group buttons are buttons where only one button in the defined group can be enabled, the buttons are mutually exclusive
# # enabling one disables the other in the same group

labelGroup01 = {}
labelGroup01["name"] = "group01_label"							# button_name
labelGroup01["origin_x"] = dev_column_origin											# button_origin_x
labelGroup01["origin_y"] = pgvar.pygame_window_height - 900		# button_origin_y
labelGroup01["width"] = pgvar.UI_sideBar_width					# button_width
labelGroup01["height"] = 20										# button_height
labelGroup01["label_txt"] = "Group 01"							# button_label_txt
labelGroup01["type"] = "label"									# buttonType
labelGroup01["enabled"] = False									# buttonEnabled
labelGroup01["color"] = pgvar.UI_label_color 						# buttonColor
labelGroup01["group"] = "group01"									# buttonGroup
labelGroup01["visible"] = True									# buttonVisible
labelGroup01["available"] = True

bGroup01Button01 = {}
bGroup01Button01["name"] = "Group01Button01"						# button_name
bGroup01Button01["origin_x"] = dev_column_origin										# button_origin_x
bGroup01Button01["origin_y"] = pgvar.pygame_window_height - 880	# button_origin_y
bGroup01Button01["width"] = pgvar.UI_sideBar_width				# button_width
bGroup01Button01["height"] = 20									# button_height
bGroup01Button01["label_txt"] = "Group 01 Button 01"				# button_label_txt
bGroup01Button01["type"] = "group"								# buttonType
bGroup01Button01["enabled"] = True								# buttonEnabled
bGroup01Button01["color"] = pgvar.UI_button_selected_color		# buttonColor
bGroup01Button01["group"] = "group01"								# buttonGroup
bGroup01Button01["visible"] = True								# buttonVisible
bGroup01Button01["available"] = True

bGroup01Button02 = {}
bGroup01Button02["name"] = "Group01Button02"						# button_name
bGroup01Button02["origin_x"] = dev_column_origin										# button_origin_x
bGroup01Button02["origin_y"] = pgvar.pygame_window_height - 860	# button_origin_y
bGroup01Button02["width"] = pgvar.UI_sideBar_width				# button_width
bGroup01Button02["height"] = 20									# button_height
bGroup01Button02["label_txt"] = "Group 01 Button 02"				# button_label_txt
bGroup01Button02["type"] = "group"								# buttonType
bGroup01Button02["enabled"] = False								# buttonEnabled
bGroup01Button02["color"] = pgvar.UI_button_color					# buttonColor
bGroup01Button02["group"] = "group01"								# buttonGroup
bGroup01Button02["visible"] = True								# buttonVisible
bGroup01Button02["available"] = True

# # Group 02 Buttons:

labelGroup02 = {}
labelGroup02["name"] = "group02_label"							# button_name
labelGroup02["origin_x"] = dev_column_origin											# button_origin_x
labelGroup02["origin_y"] = group02_origin							# button_origin_y
labelGroup02["width"] = pgvar.UI_sideBar_width					# button_width
labelGroup02["height"] = 20										# button_height
labelGroup02["label_txt"] = "Group 02"							# button_label_txt
labelGroup02["type"] = "label"									# buttonType
labelGroup02["enabled"] = False									# buttonEnabled
labelGroup02["color"] = pgvar.UI_label_color 						# buttonColor
labelGroup02["group"] = "group02"									# buttonGroup
labelGroup02["visible"] = True									# buttonVisible
labelGroup02["available"] = True

bGroup02Button01 = {}
bGroup02Button01["name"] = "Group02Button01"						# button_name
bGroup02Button01["origin_x"] = dev_column_origin										# button_origin_x
bGroup02Button01["origin_y"] = group02_origin	 + 20					# button_origin_y
bGroup02Button01["width"] = pgvar.UI_sideBar_width / 2				# button_width
bGroup02Button01["height"] = 20									# button_height
bGroup02Button01["label_txt"] = "OptionA"							# button_label_txt
bGroup02Button01["type"] = "group"								# buttonType
bGroup02Button01["enabled"] = True								# buttonEnabled
bGroup02Button01["color"] = pgvar.UI_button_selected_color		# buttonColor
bGroup02Button01["group"] = "group02"								# buttonGroup
bGroup02Button01["visible"] = True								# buttonVisible
bGroup02Button01["available"] = True

bGroup02Button02 = {}
bGroup02Button02["name"] = "Group02Button02"						# button_name
bGroup02Button02["origin_x"] = dev_column_origin + (pgvar.UI_sideBar_width / 2)			# button_origin_x
bGroup02Button02["origin_y"] = group02_origin	 + 20					# button_origin_y
bGroup02Button02["width"] = pgvar.UI_sideBar_width / 2				# button_width
bGroup02Button02["height"] = 20									# button_height
bGroup02Button02["label_txt"] = "OptionB"							# button_label_txt
bGroup02Button02["type"] = "group"								# buttonType
bGroup02Button02["enabled"] = False								# buttonEnabled
bGroup02Button02["color"] = pgvar.UI_button_color					# buttonColor
bGroup02Button02["group"] = "group02"								# buttonGroup
bGroup02Button02["visible"] = True								# buttonVisible
bGroup02Button02["available"] = True

# # Group 03 Buttons:

labelGroup03 = {}
labelGroup03["name"] = "group03_label"							# button_name
labelGroup03["origin_x"] = dev_column_origin										# button_origin_x
labelGroup03["origin_y"] = group03_origin							# button_origin_y
labelGroup03["width"] = pgvar.UI_sideBar_width					# button_width
labelGroup03["height"] = 20										# button_height
labelGroup03["label_txt"] = "Group 03"							# button_label_txt
labelGroup03["type"] = "label"									# buttonType
labelGroup03["enabled"] = False									# buttonEnabled
labelGroup03["color"] = pgvar.UI_label_color 						# buttonColor
labelGroup03["group"] = "group03"									# buttonGroup
labelGroup03["visible"] = True									# buttonVisible
labelGroup03["available"] = True

bGroup03Button01 = {}
bGroup03Button01["name"] = "Group03Button01"						# button_name
bGroup03Button01["origin_x"] = dev_column_origin									# button_origin_x
bGroup03Button01["origin_y"] = group03_origin + 20					# button_origin_y
bGroup03Button01["width"] = pgvar.UI_sideBar_width / 3				# button_width
bGroup03Button01["height"] = 20									# button_height
bGroup03Button01["label_txt"] = " A "								# button_label_txt
bGroup03Button01["type"] = "group"								# buttonType
bGroup03Button01["enabled"] = True								# buttonEnabled
bGroup03Button01["color"] = pgvar.UI_button_selected_color		# buttonColor
bGroup03Button01["group"] = "group03"								# buttonGroup
bGroup03Button01["visible"] = True								# buttonVisible
bGroup03Button01["available"] = True

bGroup03Button02 = {}
bGroup03Button02["name"] = "Group03Button02"						# button_name
bGroup03Button02["origin_x"] = dev_column_origin + (pgvar.UI_sideBar_width / 3)			# button_origin_x
bGroup03Button02["origin_y"] = group03_origin + 20					# button_origin_y
bGroup03Button02["width"] = pgvar.UI_sideBar_width / 3				# button_width
bGroup03Button02["height"] = 20									# button_height
bGroup03Button02["label_txt"] = " B "					 			# button_label_txt
bGroup03Button02["type"] = "group"								# buttonType
bGroup03Button02["enabled"] = False								# buttonEnabled
bGroup03Button02["color"] = pgvar.UI_button_color					# buttonColor
bGroup03Button02["group"] = "group03"								# buttonGroup
bGroup03Button02["visible"] = True								# buttonVisible
bGroup03Button02["available"] = True

bGroup03Button03 = {}
bGroup03Button03["name"] = "Group03Button03"						# button_name
bGroup03Button03["origin_x"] = dev_column_origin + ((pgvar.UI_sideBar_width / 3) * 2)		# button_origin_x
bGroup03Button03["origin_y"] = group03_origin + 20					# button_origin_y
bGroup03Button03["width"] = pgvar.UI_sideBar_width / 3				# button_width
bGroup03Button03["height"] = 20									# button_height
bGroup03Button03["label_txt"] = " C "								# button_label_txt
bGroup03Button03["type"] = "group"								# buttonType
bGroup03Button03["enabled"] = False								# buttonEnabled
bGroup03Button03["color"] = pgvar.UI_button_color					# buttonColor
bGroup03Button03["group"] = "group03"								# buttonGroup
bGroup03Button03["visible"] = True								# buttonVisible
bGroup03Button03["available"] = True


# Dropdown 01

labelDropdown = {}
labelDropdown["name"] = "dropdownLabel"						# button_name
labelDropdown["origin_x"] = dev_column_origin					# button_origin_x
labelDropdown["origin_y"] = dropdown01_origin					# button_origin_y
labelDropdown["width"] = pgvar.UI_sideBar_width				# button_width
labelDropdown["height"] = 20									# button_height
labelDropdown["label_txt"] = "Dropdown 01"					# button_label_txt
labelDropdown["type"] = "label"								# buttonType
labelDropdown["enabled"] = False								# buttonEnabled
labelDropdown["color"] = pgvar.UI_button_color				# buttonColor
labelDropdown["group"] = "dropdown01"							# buttonGroup
labelDropdown["visible"] = True								# buttonVisible
labelDropdown["available"] = True

lDropdown01TEXT = {}
lDropdown01TEXT["name"] = "dropdown01TEXT"						# button_name
lDropdown01TEXT["origin_x"] = dev_column_origin					# button_origin_x
lDropdown01TEXT["origin_y"] = dropdown01_origin + 20				# button_origin_y
lDropdown01TEXT["width"] = pgvar.UI_sideBar_width - 20				# button_width
lDropdown01TEXT["height"] = 20									# button_height
lDropdown01TEXT["label_txt"] = "- select -"						# button_label_txt
lDropdown01TEXT["type"] = "dropdown"								# buttonType
lDropdown01TEXT["enabled"] = False								# buttonEnabled
lDropdown01TEXT["color"] = pgvar.UI_button_color					# buttonColor
lDropdown01TEXT["group"] = "dropdown01"							# buttonGroup
lDropdown01TEXT["visible"] = True									# buttonVisible
lDropdown01TEXT["available"] = True

bDropdown01opener = {}
bDropdown01opener["name"] = "dropdown01opener"									# button_name
bDropdown01opener["origin_x"] = dev_column_origin + pgvar.UI_sideBar_width	 - 20		# button_origin_x
bDropdown01opener["origin_y"] = dropdown01_origin + 20								# button_origin_y
bDropdown01opener["width"] = 20													# button_width
bDropdown01opener["height"] = 20													# button_height
bDropdown01opener["label_txt"] = ">>"												# button_label_txt
bDropdown01opener["type"] = "dropdown"											# buttonType
bDropdown01opener["enabled"] = False												# buttonEnabled
bDropdown01opener["color"] = pgvar.UI_button_color								# buttonColor
bDropdown01opener["group"] = "dropdown01"											# buttonGroup
bDropdown01opener["visible"] = True												# buttonVisible
bDropdown01opener["available"] = True

bDropdown01option01 = {}
bDropdown01option01["name"] = "dropdown01option01"					# button_name
bDropdown01option01["origin_x"] = dev_column_origin + pgvar.UI_sideBar_width				# button_origin_x
bDropdown01option01["origin_y"] = dropdown01_origin + 20				# button_origin_y
bDropdown01option01["width"] = 140									# button_width
bDropdown01option01["height"] = 20									# button_height
bDropdown01option01["label_txt"] = " Option 1"							# button_label_txt
bDropdown01option01["type"] = "dropdown"								# buttonType
bDropdown01option01["enabled"] = False								# buttonEnabled
bDropdown01option01["color"] = pgvar.UI_button_color					# buttonColor
bDropdown01option01["group"] = "dropdown01"							# buttonGroup
bDropdown01option01["visible"] = False								# buttonVisible
bDropdown01option01["available"] = True

bDropdown01option02 = {}
bDropdown01option02["name"] = "dropdown01option02"					# button_name
bDropdown01option02["origin_x"] = dev_column_origin + pgvar.UI_sideBar_width				# button_origin_x
bDropdown01option02["origin_y"] = dropdown01_origin + 40				# button_origin_y
bDropdown01option02["width"] = 140									# button_width
bDropdown01option02["height"] = 20									# button_height
bDropdown01option02["label_txt"] = " Option 2"							# button_label_txt
bDropdown01option02["type"] = "dropdown"								# buttonType
bDropdown01option02["enabled"] = False								# buttonEnabled
bDropdown01option02["color"] = pgvar.UI_button_color					# buttonColor
bDropdown01option02["group"] = "dropdown01"							# buttonGroup
bDropdown01option02["visible"] = False								# buttonVisible
bDropdown01option02["available"] = True

bDropdown01option03 = {}
bDropdown01option03["name"] = "dropdown01option03"					# button_name
bDropdown01option03["origin_x"] = dev_column_origin + pgvar.UI_sideBar_width				# button_origin_x
bDropdown01option03["origin_y"] = dropdown01_origin + 60		# button_origin_y
bDropdown01option03["width"] = 140									# button_width
bDropdown01option03["height"] = 20									# button_height
bDropdown01option03["label_txt"] = " Option 3"							# button_label_txt
bDropdown01option03["type"] = "dropdown"								# buttonType
bDropdown01option03["enabled"] = False								# buttonEnabled
bDropdown01option03["color"] = pgvar.UI_button_color					# buttonColor
bDropdown01option03["group"] = "dropdown01"							# buttonGroup
bDropdown01option03["visible"] = False								# buttonVisible
bDropdown01option03["available"] = True


lTextField01 = {}
lTextField01["name"] = "textField01Label"							# button_name
lTextField01["origin_x"] = dev_column_origin						# button_origin_x
lTextField01["origin_y"] = pgvar.pygame_window_height - 660		# button_origin_y
lTextField01["width"] = pgvar.UI_sideBar_width					# button_width
lTextField01["height"] = 20										# button_height
lTextField01["label_txt"] = "Enter Text:"							# button_label_txt
lTextField01["type"] = "label"									# buttonType
lTextField01["enabled"] = False									# buttonEnabled
lTextField01["color"] = pgvar.UI_label_color						# buttonColor
lTextField01["group"] = "text01"									# buttonGroup
lTextField01["visible"] = True									# buttonVisible
lTextField01["available"] = True

textField01 = {}
textField01["name"] = "textField01"							# button_name
textField01["origin_x"] = dev_column_origin									# button_origin_x
textField01["origin_y"] = pgvar.pygame_window_height - 640		# button_origin_y
textField01["width"] = pgvar.UI_sideBar_width					# button_width
textField01["height"] = 20									# button_height
textField01["label_txt"] = "abc123"							# button_label_txt
textField01["type"] = "textEntry"								# buttonType
textField01["enabled"] = False								# buttonEnabled
textField01["color"] = pgvar.UI_text_entry_box_color			# buttonColor
textField01["group"] = "text01"								# buttonGroup
textField01["visible"] = True									# buttonVisible
textField01["available"] = True

mInsert = {}
mInsert["name"] = "InsertMenu"								# button_name
mInsert["origin_x"] = pgvar.UI_sideBar_width + 20				# button_origin_x
mInsert["origin_y"] = 0										# button_origin_y
mInsert["width"] = 150										# button_width
mInsert["height"] = 20										# button_height
mInsert["label_txt"] = " Insert"								# button_label_txt
mInsert["type"] = "menu"										# buttonType
mInsert["enabled"] = False									# buttonEnabled
mInsert["color"] = pgvar.UI_button_color						# buttonColor
mInsert["group"] = "InsertMenu"									# buttonGroup
mInsert["visible"] = True										# buttonVisible
mInsert["available"] = True

mInsertoption01 = {}
mInsertoption01["name"] = "menu01option01"					# button_name
mInsertoption01["origin_x"] = pgvar.UI_sideBar_width + 20		# button_origin_x
mInsertoption01["origin_y"] = 20								# button_origin_y
mInsertoption01["width"] = 150								# button_width
mInsertoption01["height"] = 20								# button_height
mInsertoption01["label_txt"] = " Proton "					# button_label_txt
mInsertoption01["type"] = "menu"								# buttonType
mInsertoption01["enabled"] = False							# buttonEnabled
mInsertoption01["color"] = pgvar.UI_button_color				# buttonColor
mInsertoption01["group"] = "InsertMenu"							# buttonGroup
mInsertoption01["visible"] = False							# buttonVisible
mInsertoption01["available"] = True

mInsertoption02 = {}
mInsertoption02["name"] = "menu01option02"					# button_name
mInsertoption02["origin_x"] = pgvar.UI_sideBar_width + 20			# button_origin_x
mInsertoption02["origin_y"] = 40								# button_origin_y
mInsertoption02["width"] = 150								# button_width
mInsertoption02["height"] = 20								# button_height
mInsertoption02["label_txt"] = " Electron "						# button_label_txt
mInsertoption02["type"] = "menu"								# buttonType
mInsertoption02["enabled"] = False							# buttonEnabled
mInsertoption02["color"] = pgvar.UI_button_color				# buttonColor
mInsertoption02["group"] = "InsertMenu"							# buttonGroup
mInsertoption02["visible"] = False							# buttonVisible
mInsertoption02["available"] = True

mInsertoption03 = {}
mInsertoption03["name"] = "menu01option03"					# button_name
mInsertoption03["origin_x"] = pgvar.UI_sideBar_width + 20			# button_origin_x
mInsertoption03["origin_y"] = 60								# button_origin_y
mInsertoption03["width"] = 150								# button_width
mInsertoption03["height"] = 20								# button_height
mInsertoption03["label_txt"] = " Neutron "					# button_label_txt
mInsertoption03["type"] = "menu"								# buttonType
mInsertoption03["enabled"] = False							# buttonEnabled
mInsertoption03["color"] = pgvar.UI_button_color				# buttonColor
mInsertoption03["group"] = "InsertMenu"							# buttonGroup
mInsertoption03["visible"] = False							# buttonVisible
mInsertoption03["available"] = True

mInsertoption04 = {}
mInsertoption04["name"] = "menu01option04"					# button_name
mInsertoption04["origin_x"] = pgvar.UI_sideBar_width	+ 20		# button_origin_x
mInsertoption04["origin_y"] = 80								# button_origin_y
mInsertoption04["width"] = 150								# button_width
mInsertoption04["height"] = 20								# button_height
mInsertoption04["label_txt"] = " Material "					# button_label_txt
mInsertoption04["type"] = "menu"								# buttonType
mInsertoption04["enabled"] = False 							# buttonEnabled
mInsertoption04["color"] = pgvar.UI_button_color				# buttonColor
mInsertoption04["group"] = "InsertMenu"							# buttonGroup
mInsertoption04["visible"] = False							# buttonVisible
mInsertoption04["available"] = True

mInsertoption05 = {}
mInsertoption05["name"] = "menu01option05"					# button_name
mInsertoption05["origin_x"] = pgvar.UI_sideBar_width	+ 20		# button_origin_x
mInsertoption05["origin_y"] = 100								# button_origin_y
mInsertoption05["width"] = 150								# button_width
mInsertoption05["height"] = 20								# button_height
mInsertoption05["label_txt"] = " Instrument / Environment "		# button_label_txt
mInsertoption05["type"] = "menu"								# buttonType
mInsertoption05["enabled"] = False							# buttonEnabled
mInsertoption05["color"] = pgvar.UI_button_color				# buttonColor
mInsertoption05["group"] = "InsertMenu"							# buttonGroup
mInsertoption05["visible"] = False							# buttonVisible
mInsertoption05["available"] = True

bMenu02 = {}
bMenu02["name"] = "menu02"											# button_name
bMenu02["origin_x"] = bMenu02_origin									# button_origin_x
bMenu02["origin_y"] = 0												# button_origin_y
bMenu02["width"] = pgvar.UI_menuButton_width							# button_width
bMenu02["height"] = 20												# button_height
bMenu02["label_txt"] = " Menu 02"										# button_label_txt
bMenu02["type"] = "menu"												# buttonType
bMenu02["enabled"] = False											# buttonEnabled
bMenu02["color"] = pgvar.UI_button_color								# buttonColor
bMenu02["group"] = "menu02"											# buttonGroup
bMenu02["visible"] = True												# buttonVisible
bMenu02["available"] = True

bMenu02popup01 = {}
bMenu02popup01["name"] = "menu02popup01"										# button_name
bMenu02popup01["origin_x"] = bMenu02_origin			# button_origin_x
bMenu02popup01["origin_y"] = 20												# button_origin_y
bMenu02popup01["width"] = 150													# button_width
bMenu02popup01["height"] = 20													# button_height
bMenu02popup01["label_txt"] = " Small Popup"									# button_label_txt
bMenu02popup01["type"] = "menu"												# buttonType
bMenu02popup01["enabled"] = False												# buttonEnabled
bMenu02popup01["color"] = pgvar.UI_button_color								# buttonColor
bMenu02popup01["group"] = "menu02"											# buttonGroup
bMenu02popup01["visible"] = False												# buttonVisible
bMenu02popup01["available"] = True


bMenu02popup02 = {}
bMenu02popup02["name"] = "menu02popup02"							# button_name
bMenu02popup02["origin_x"] = bMenu02_origin		# button_origin_x
bMenu02popup02["origin_y"] = 40										# button_origin_y
bMenu02popup02["width"] = 150										# button_width
bMenu02popup02["height"] = 20										# button_height
bMenu02popup02["label_txt"] = " Medium Popup"						# button_label_txt
bMenu02popup02["type"] = "menu"										# buttonType
bMenu02popup02["enabled"] = False									# buttonEnabled
bMenu02popup02["color"] = pgvar.UI_button_color							# buttonColor
bMenu02popup02["group"] = "menu02"										# buttonGroup
bMenu02popup02["visible"] = False											# buttonVisible
bMenu02popup02["available"] = True

bMenu02popup03 = {}
bMenu02popup03["name"] = "menu02popup03"									# button_name
bMenu02popup03["origin_x"] = bMenu02_origin		# button_origin_x
bMenu02popup03["origin_y"] = 60											# button_origin_y
bMenu02popup03["width"] = 150												# button_width
bMenu02popup03["height"] = 20												# button_height
bMenu02popup03["label_txt"] = " Large Popup"								# button_label_txt
bMenu02popup03["type"] = "menu"											# buttonType
bMenu02popup03["enabled"] = False											# buttonEnabled
bMenu02popup03["color"] = pgvar.UI_button_color							# buttonColor
bMenu02popup03["group"] = "menu02"										# buttonGroup
bMenu02popup03["visible"] = False											# buttonVisible
bMenu02popup03["available"] = True

# ************************************************************************************************#
#	MENU 02 POPUP 01 
# ************************************************************************************************#

# background box
menu02popup01element01 = {}
menu02popup01element01["name"] = "menu02popup01element01"							# button_name
menu02popup01element01["origin_x"] = pgvar.UI_popup_small_origin_x				# button_origin_x
menu02popup01element01["origin_y"] = pgvar.UI_popup_small_origin_y				# button_origin_y
menu02popup01element01["width"] = pgvar.UI_popup_small_width						# button_width
menu02popup01element01["height"] = pgvar.UI_popup_small_height					# button_height
menu02popup01element01["label_txt"] = ""											# button_label_txt
menu02popup01element01["type"] = "popup"											# buttonType
menu02popup01element01["enabled"] = False											# buttonEnabled
menu02popup01element01["color"] = pgvar.UI_background_color						# buttonColor
menu02popup01element01["group"] = "menu02popup01"									# buttonGroup
menu02popup01element01["visible"] = False											# buttonVisible
menu02popup01element01["available"] = True

# Title Bar
menu02popup01element02 = {}
menu02popup01element02["name"] = "menu02popup01element02"							# button_name
menu02popup01element02["origin_x"] = pgvar.UI_popup_small_origin_x				# button_origin_x
menu02popup01element02["origin_y"] = pgvar.UI_popup_small_origin_y				# button_origin_y
menu02popup01element02["width"] = pgvar.UI_popup_small_width						# button_width
menu02popup01element02["height"] = 20												# button_height
menu02popup01element02["label_txt"] = " Menu 02 >> Small Popup"						# button_label_txt
menu02popup01element02["type"] = "popup"											# buttonType
menu02popup01element02["enabled"] = False											# buttonEnabled
menu02popup01element02["color"] = pgvar.UI_button_selected_color					# buttonColor
menu02popup01element02["group"] = "menu02popup01"									# buttonGroup
menu02popup01element02["visible"] = False											# buttonVisible
menu02popup01element02["available"] = True

# description bar
menu02popup01element03 = {}
menu02popup01element03["name"] = "menu02popup01element03"							# button_name
menu02popup01element03["origin_x"] = pgvar.UI_popup_small_origin_x				# button_origin_x
menu02popup01element03["origin_y"] = pgvar.UI_popup_small_origin_y + 20			# button_origin_y
menu02popup01element03["width"] = pgvar.UI_popup_small_width						# button_width
menu02popup01element03["height"] = 20												# button_height
menu02popup01element03["label_txt"] = " Do Something Interesting:"					# button_label_txt
menu02popup01element03["type"] = "popup_element"									# buttonType
menu02popup01element03["enabled"] = False											# buttonEnabled
menu02popup01element03["color"] = pgvar.UI_label_color							# buttonColor
menu02popup01element03["group"] = "menu02popup01"									# buttonGroup
menu02popup01element03["visible"] = False											# buttonVisible
menu02popup01element03["available"] = True

# first button in small popup
menu02popup01element04 = {}
menu02popup01element04["name"] = "menu02popup01element04"					# button_name
menu02popup01element04["origin_x"] = pgvar.UI_popup_small_origin_x + 20			# button_origin_x
menu02popup01element04["origin_y"] = pgvar.UI_popup_small_origin_y + 60			# button_origin_y
menu02popup01element04["width"] = 80										# button_width
menu02popup01element04["height"] = 20										# button_height
menu02popup01element04["label_txt"] = "Something"							# button_label_txt
menu02popup01element04["type"] = "popup_element_button"						# buttonType
menu02popup01element04["enabled"] = False									# buttonEnabled
menu02popup01element04["color"] = pgvar.UI_button_color							# buttonColor
menu02popup01element04["group"] = "menu02popup01"							# buttonGroup
menu02popup01element04["visible"] = False									# buttonVisible
menu02popup01element04["available"] = True

# second button in small popup
menu02popup01element05 = {}
menu02popup01element05["name"] = "menu02popup01element05"						# button_name
menu02popup01element05["origin_x"] = pgvar.UI_popup_small_origin_x + 20		# button_origin_x
menu02popup01element05["origin_y"] = pgvar.UI_popup_small_origin_y + 80		# button_origin_y
menu02popup01element05["width"] = 80											# button_width
menu02popup01element05["height"] = 20											# button_height
menu02popup01element05["label_txt"] = "Interesting"							# button_label_txt
menu02popup01element05["type"] = "popup_element_button"						# buttonType
menu02popup01element05["enabled"] = False										# buttonEnabled
menu02popup01element05["color"] = pgvar.UI_button_color						# buttonColor
menu02popup01element05["group"] = "menu02popup01"								# buttonGroup
menu02popup01element05["visible"] = False										# buttonVisible
menu02popup01element05["available"] = True

# ok / cancel background box
menu02popup01element06 = {}
menu02popup01element06["name"] = "menu02popup01element06"												# button_name
menu02popup01element06["origin_x"] = pgvar.UI_popup_small_origin_x									# button_origin_x
menu02popup01element06["origin_y"] = pgvar.UI_popup_small_origin_y + pgvar.UI_popup_small_height - 60 	# button_origin_y
menu02popup01element06["width"] = pgvar.UI_popup_small_width											# button_width
menu02popup01element06["height"] = 60																	# button_height
menu02popup01element06["label_txt"] = ""																# button_label_txt
menu02popup01element06["type"] = "popup_element"														# buttonType
menu02popup01element06["enabled"] = False																# buttonEnabled
menu02popup01element06["color"] = pgvar.UI_label_color												# buttonColor
menu02popup01element06["group"] = "menu02popup01"														# buttonGroup
menu02popup01element06["visible"] = False																# buttonVisible
menu02popup01element06["available"] = True

# ok button
menu02popup01element07 = {}
menu02popup01element07["name"] = "menu02popup01element07"												# button_name
menu02popup01element07["origin_x"] = pgvar.UI_popup_small_origin_x + 20								# button_origin_x
menu02popup01element07["origin_y"] = pgvar.UI_popup_small_origin_y + pgvar.UI_popup_small_height - 40 	# button_origin_y
menu02popup01element07["width"] = 60																	# button_width
menu02popup01element07["height"] = 20																	# button_height
menu02popup01element07["label_txt"] = " OK "															# button_label_txt
menu02popup01element07["type"] = "popup_element_button"												# buttonType
menu02popup01element07["enabled"] = False																# buttonEnabled
menu02popup01element07["color"] = pgvar.UI_button_color 												# buttonColor
menu02popup01element07["group"] = "menu02popup01"														# buttonGroup
menu02popup01element07["visible"] = False																# buttonVisible
menu02popup01element07["available"] = True

# cancel button
menu02popup01element08 = {}
menu02popup01element08["name"] = "menu02popup01element08"													# button_name
menu02popup01element08["origin_x"] = pgvar.UI_popup_small_origin_x + pgvar.UI_popup_small_width -80		# button_origin_x
menu02popup01element08["origin_y"] = pgvar.UI_popup_small_origin_y + pgvar.UI_popup_small_height - 40 		# button_origin_y
menu02popup01element08["width"] = 60																		# button_width
menu02popup01element08["height"] = 20																		# button_height
menu02popup01element08["label_txt"] = "Cancel"															# button_label_txt
menu02popup01element08["type"] = "popup_element_button"													# buttonType
menu02popup01element08["enabled"] = False																	# buttonEnabled
menu02popup01element08["color"] = pgvar.UI_button_color 													# buttonColor
menu02popup01element08["group"] = "menu02popup01"															# buttonGroup
menu02popup01element08["visible"] = False																	# buttonVisible
menu02popup01element08["available"] = True





# ************************************************************************************************#
#	Dictionary of all buttons, when you add a button / element above ^ you need to add it below as well \/
# ************************************************************************************************#



allButtons = {}


# Display Dimensions
allButtons[82] = lDisplayDimensions
allButtons[62] = b1D
allButtons[63] = b2D
allButtons[64] = b3D

# Calc Dimensions
allButtons[83] = lCalculationDimensions
allButtons[84] = bCalc1D
allButtons[85] = bCalc2D
allButtons[86] = bCalc3D




# Standards
allButtons[87] = lStandard 



allButtons[88] = bStdMetric
allButtons[89] = bStdImperial

allButtons[90] = lUnitSystem
allButtons[91] = tUnitSys
allButtons[92] = bUnitSysOpener

# Forces
allButtons[66] = lForces
allButtons[67] = bForceGravity
allButtons[68] = bForceGravityOpener
allButtons[69] = bForceElectromagnetic
allButtons[70] = bForceElectromagneticOpener
allButtons[71] = bForceStrongNuclear
allButtons[72] = bForceStrongNuclearOpener
allButtons[73] = bForceWeakNuclear
allButtons[74] = bForceWeakNuclearOpener
allButtons[75] = bForceDarkEnergy
allButtons[76] = bForceDarkEnergyOpener
allButtons[77] = bForceNewOther
allButtons[78] = bForceNewOtherOpener

# Scale Time
allButtons[79] = lScaleTime
allButtons[80] = bScaleTime
allButtons[81] = bScaleTimeOpener

# Display Buttons

allButtons[65] = bForceVectors
allButtons[93] = bDistComponents

# Scale
allButtons[57] = bScaleMinus
allButtons[58] = lScaleLabel
allButtons[59] = bScalePlus
allButtons[60] = tScaleSelection
allButtons[61] = bScaleOpener		

# Simulation Control Buttons
allButtons[1] = bPlaySimulation		
allButtons[2] = bPauseSimulation		
allButtons[3] = bSaveSimulation		
allButtons[51] = bClearSimulation
allButtons[53] = bLoadSimulation

#exit button 
allButtons[0] = buttonExit	





### ---------------------####
### DEV AND REFERENCE BUTTONS: 
### ---------------------####

# reference buttons
allButtons[52] = bPushyExample

allButtons[54] = lResolution
allButtons[55]= tResolution
allButtons[56] = bResolutionOpener

allButtons[4] = buttonSticky01		# sticky 01
allButtons[5] = buttonSticky02		# sticky 02
allButtons[6] = buttonSticky03		# sticky 03
allButtons[7] = lSimulationControl			# pushy button group label
allButtons[8] = labelSticky			# stick button group label
allButtons[9] = labelGroup01			# group01 label
allButtons[10] = bGroup01Button01 	# group01 button 01
allButtons[11] = bGroup01Button02		# group01 button 02
allButtons[12] = labelGroup02 		# group02 label
allButtons[13] = bGroup02Button01 	# group02 Button 01
allButtons[14] = bGroup02Button02 	# group02 Button 02
allButtons[15] = labelGroup03 		# group03 label
allButtons[16] = bGroup03Button01 	# group 03 button 01
allButtons[17] = bGroup03Button02 	# group 03 button 02
allButtons[18] = bGroup03Button03		# group 03 button 03
allButtons[19] = labelDisplay 		# label for the display buttons
allButtons[20] = buttonFPS			# FPS button
# allButtons[21] = buttonScale			# Scale button
allButtons[22] = buttonGrid			# Grid button
allButtons[23] = buttonOrigin 		# Origin Button
allButtons[24] = labelDropdown 		# label for the dropdown group
allButtons[25] = lDropdown01TEXT		# Dropdown01 - selected display
allButtons[26] = bDropdown01opener	# Dropdown01 - opener
allButtons[27] = bDropdown01option01 	# Dropdown01 option 01
allButtons[28] = bDropdown01option02 	# Dropdown01 option 02
allButtons[29] = bDropdown01option03 	# Dropdown01 option 03

allButtons[30] = mInsert				# Menu 01
allButtons[31] = mInsertoption01		# Menu 01 - option 01 - Monday
allButtons[32] = mInsertoption02		# Menu 01 - option 02 - Tuesday
allButtons[33] = mInsertoption03		# Menu 01 - option 03 - Wednesday
allButtons[34] = mInsertoption04		# Menu 01 - option 04 - Thursday
allButtons[35] = mInsertoption05		# Menu 01 - option 05 - Friday

allButtons[36] = bMenu02				# Menu 02
allButtons[38] = lTextField01			# Text Field - label
allButtons[39] = textField01			# Text Field - text entry box
allButtons[40] = bMenu02popup01		# Menu 02  - small popup
allButtons[41] = bMenu02popup02		# Menu 02  - Medium popup
allButtons[42] = bMenu02popup03		# Menu 02  - Large popup

# menu02 popup01 elements
allButtons[43] = menu02popup01element01		# Menu 02  - small popup - element 01 - background box
allButtons[44] = menu02popup01element02		# Menu 02  - small popup - element 02 - title bar
allButtons[45] = menu02popup01element03		# Menu 02  - small popup - element 03 - option description
allButtons[46] = menu02popup01element04		# Menu 02  - small popup - element 04 - something button
allButtons[47] = menu02popup01element05		# Menu 02  - small popup - element 05 - interesting button
allButtons[48] = menu02popup01element06		# Menu 02  - small popup - element 06 - ok / cancel background
allButtons[49] = menu02popup01element07		# Menu 02  - small popup - element 06 - ok button
allButtons[50] = menu02popup01element08		# Menu 02  - small popup - element 06 - cancel button

