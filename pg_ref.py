# ************************************************************************************************#
# ************************************************************************************************#
#	Directory Structure
# ************************************************************************************************#
# ************************************************************************************************#

#	/physics_garage.py 	# primary program
#	/pbproc.py 			# processing sticky, group, dropdown etc button actions. e.g. click one button, disable the others in the group. 
#	/pgvar.py 			# global variable declarations
#	/pgui.py 			# photon gui elements and buttons
#	/pfunc.py 			# functions
#	/pclass.py 			# button processing class that handles drawing / displaying UI
#	/photon_ref.py 		# references, dev notes, style guide, modification instructions
#	/pge.py 			# element definitions, such as all the variables assocated with particles


# photon_ref.py

moduleName = "photon_ref.py"

# ************************************************************************************************#
#	Particle Placement Flow
# ************************************************************************************************#

# Create
			[Create Particle]    -->    [Record Position] --> 
|"physics_garage.py"   |
|"pfunc.InsertProton"  |  -->  

# Display
[query particle position and scale] --> [round position for display] --> [display position]

# move
[query particle real position and scale] --> [move particle and update position] --> [round position for display] --> [display position]

[query particle real position and scale] --> [round position for display] [hide old position] --> [move particle and update real position] 
--> [round position for display] --> [display new position]


# ************************************************************************************************#
#	DEV log
# ************************************************************************************************#

# # TO DO
#- Insert particle proton should draw correct size based on current scale (in progress) 
- test each scale ^ to be sure
- sizes of particles should correctly change size and position when zooming in and out. 
- link print absolute position of particle and diam with an enabme button in pbclass.py 



- when you click on background, all open menus should close
- determine license - If you aren’t sure which license you should use for your project, check out choosealicense.com.
- integrate functionality of 2D_vector_003-mouse_click.py
- toggle vectors by force type? (maybe in force >> while display -> vectors toggles all)
- insert - particle - proton / antiproton
- insert - container - bottle
- insert - environment - magnetic field / STP earth atmosphere, etc. 
- selecting scale should by default enable / disable forces, e.g. a pm scale gravity is disabled, at Mm strong nuclear is disabled
 when you enable container magnetic field it will curve charge particle trajectories, you can view magnetic force vectors and component vectors as well as force magnitudes
 start at the particle level and build up and out
 process all pushy buttons / all sticky buttons / all group buttons etc with a function for each, i.e. not specifying behavior for each individual button. if you enable a group button, the others in the same group are disabled

# # DONE
# completed transfer of program to a modular design 


# ************************************************************************************************#
#	Files, Notes and Functionality incorporated 
# ************************************************************************************************#

#	\physics_garage\version_013\pgmain.py 					IN PROGRESS
#	\github\michaelfdickey\photon_pygui\photongui01.py 		IN PROGRESS
#	\physics_garage\2D_vector_003-mouse_click02.py 			COMPLETED


# ************************************************************************************************#
#	Style Guide
# ************************************************************************************************#

"""
Follow PEP 8, when sensible. https://www.python.org/dev/peps/pep-0008/

Naming
Variables, functions, methods, packages, modules
	Variables:
		local: v_lower_case_with_underscores
		global: gv_lower_case_with_underscores
	Lists:
		l_lower_case_with_underscores
		gl_lower_case_with_underscores (global list)
	Dictionaries:
		d_lower_case_with_underscores
		gd_lower_case_with_underscores (global dictionary)
	Constants:
		k_ALL_CAPS_WITH_UNDERSCORES
		gk_ALL_CAPS
Functions, Classes and Exceptions
	Functions:
		fCapWords
	Classes:
		cCapWords
Protected methods and internal functions
	_single_leading_underscore(self, ...)
Private methods
	__double_leading_underscore(self, ...)

To keep in line with the style guide, keep module names short, lowercase, and be sure to avoid using special symbols 

"""
# ************************************************************************************************#
#	program handling
# ************************************************************************************************#

Create Element 
	get mouse x / mouse y 
	


# ************************************************************************************************#
#	Menus
# ************************************************************************************************#

Left Main Menu
	Display Dimensions
		1D, 2D, 3D
	Calculation Dimensions
		1D, 2D, 3D
	Calculation Domain (determines which formulas are used for the calculations)
		Classical
		Relativistic
		Quantum Mechanical
	Standard
		Metric or Imperial
	Unit System
		Metric
			M*Kg*S, Cm*g*s
		Imperial
			IPS, FPS 
	Display scale	
		-, +, >> (opens fixed display scales)
		pm (1.0 x 10^12m)
	Time Step
		1s / frame
	Forces
		Gravity
		Electromagnetic
		Strong nuclear
		Weak Nuclear 
		Dark Energy
		New / Other

Insert
	Particle
		proton
		neutron
		electron
	Emitter
	Container
	Environment 
	Detector


If you want to really optimize calculation of n-body in any programming language, check out Barnes-Hut trees.
https://en.wikipedia.org/wiki/Barnes%E2%80%93Hut_simulation


# ********************************************************************************************#
# 	UPDATE GUIDES
# ********************************************************************************************#


adding a new scale:

"""
1) add scale option button dictionary in pgui.py 
2) fix y origin "bScaleOption20["origin_y"] = scale_display_origin - 20"
3) add it to allButtons[97] = bScaleOption18 at the bottom of pgui.py
4) add it to def scaleUpdate(): in pge.py 
5) add it to pbproc # # # Scale Options Processing
6) also add it to # # # Scale Opener BUTTON in pbproc.py
7) added to physics_garage.py # # #PUSHY EVENT PROCESSING # # #
"""