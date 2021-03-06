# ************************************************************************************************#
# ************************************************************************************************#
#	Directory Structure
# ************************************************************************************************#
# ************************************************************************************************#

#	see pg_ref.py

moduleName = "pge.py"

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
#import pclass
#import pbproc
#import pge

# ************************************************************************************************************************
# ************************************************************************************************************************
#  SCALES
# ************************************************************************************************************************
# ************************************************************************************************************************

"""
# scales:
0	10e-35	Planck length 
1	10e-34
2	10e-33
3	10e-32
4	10e-31
5	10e-30
6	10e-29
7	10e-28
8	10e-27
9	10e-26
10	10e-25
11	10e-24	yoctometre (ym)		Effective cross section radius of 1 MeV neutrino

19	10e-16	.1 femtometer 		.8414 fm = charge radius of Proton, 2.1 fermi (femtometers) radius of Deuteron
20	10e-15	femtrometer (fm)		1.5 fm = Size of 11 MeV proton
21	10e-14	10 femtometers 		1.75 fm - 15 fm Diameter range of atomic Nuclei
22	10e-13	.1 picometer
23	10e-12	1 picometer (pm)		1 pm - distance between atomic nuclei in a white dwarf

Fermi Gas Model - includes the pauli exclusion principle - the least amount of QM to add to the liquid drop model of the nuclear
								

good list to integrate
https://en.wikipedia.org/wiki/Orders_of_magnitude_(length)#femtometre_to_picometre_range
"""


current_scale = {}
current_scale["scale"] = 1e-15
current_scale["dict"] = "dScale20"
current_scale["display"] = "1 fm (1.0x10-15 m)"

dScale00 = {} #Planck Length
dScale01 = {}

dScale18 = {}
dScale18["scale"] = 1e-17
dScale18["description"] = "0.01 femtometer"
dScale18["display"] = ".01 fm (1.0x10-17 m)"
dScale18["note"] = ".8414 fm = charge radius of Proton"
# https://en.wikipedia.org/wiki/Orders_of_magnitude_(length)#1_femtometre


dScale19 = {}
dScale19["scale"] = 1e-16
dScale19["description"] = "0.1 femtometer"
dScale19["display"] = ".1 fm (1.0x10-16 m)"
dScale19["note"] = ".8414 fm = charge radius of Proton"
# https://en.wikipedia.org/wiki/Orders_of_magnitude_(length)#1_femtometre

dScale20 = {}
dScale20["scale"] = 1e-15
dScale20["description"] = "1 femtometer"
dScale20["display"] = "1 fm (1.0x10-15 m)"
dScale20["note"] = "1.5 fm = Size of 11 MeV Proton"

dScale21 = {}
dScale21["scale"] = 1e-14
dScale21["description"] = "10 femtometers"
dScale21["display"] = "10 fm (1.0x10-14 m)"
dScale21["note"] = "1.75 fm - 15 fm Diameter range of atomic Nuclei"


# ****** Update scale values based on new scale selected

def scaleUpdate():

	# this needs to be smarter once I add more scales, looping through and updating accordingly. 

	if current_scale["scale"] == 1e-17:
		pgui.bScaleOption18["enabled"] = True
		pgui.bScaleOption18["color"] = pgvar.UI_button_selected_color
		pgui.tScaleSelection["label_txt"] = dScale18["display"]

		#pgui.bScaleOption18["enabled"] = False
		pgui.bScaleOption19["enabled"] = False
		pgui.bScaleOption20["enabled"] = False
		pgui.bScaleOption21["enabled"] = False

		#pgui.bScaleOption18["color"] = pgvar.UI_button_color
		pgui.bScaleOption19["color"] = pgvar.UI_button_color
		pgui.bScaleOption20["color"] = pgvar.UI_button_color
		pgui.bScaleOption21["color"] = pgvar.UI_button_color

		pfunc.defineButtons()
		for i, button in enumerate(pfunc.my_buttons):
			button.display()	
		#pfunc.redrawEverything()


	if current_scale["scale"] == 1e-16:
		pgui.bScaleOption19["enabled"] = True
		pgui.bScaleOption19["color"] = pgvar.UI_button_selected_color
		pgui.tScaleSelection["label_txt"] = dScale19["display"]

		pgui.bScaleOption18["enabled"] = False
		#pgui.bScaleOption19["enabled"] = False
		pgui.bScaleOption20["enabled"] = False
		pgui.bScaleOption21["enabled"] = False

		pgui.bScaleOption18["color"] = pgvar.UI_button_color
		#pgui.bScaleOption19["color"] = pgvar.UI_button_color
		pgui.bScaleOption20["color"] = pgvar.UI_button_color
		pgui.bScaleOption21["color"] = pgvar.UI_button_color

		pfunc.defineButtons()
		for i, button in enumerate(pfunc.my_buttons):
			button.display()	
		#pfunc.redrawEverything()

	if current_scale["scale"] == 1e-15:
		pgui.bScaleOption20["enabled"] = True
		pgui.bScaleOption20["color"] = pgvar.UI_button_selected_color
		pgui.tScaleSelection["label_txt"] = dScale20["display"]	
	
		pgui.bScaleOption18["enabled"] = False
		pgui.bScaleOption19["enabled"] = False
		#pgui.bScaleOption20["enabled"] = False
		pgui.bScaleOption21["enabled"] = False

		pgui.bScaleOption18["color"] = pgvar.UI_button_color
		pgui.bScaleOption19["color"] = pgvar.UI_button_color
		#pgui.bScaleOption20["color"] = pgvar.UI_button_color
		pgui.bScaleOption21["color"] = pgvar.UI_button_color

		pfunc.defineButtons()
		for i, button in enumerate(pfunc.my_buttons):
			button.display()	
		#pfunc.redrawEverything()

	if current_scale["scale"] == 1e-14:		
		pgui.bScaleOption21["enabled"] = True
		pgui.bScaleOption21["color"] = pgvar.UI_button_selected_color
		pgui.tScaleSelection["label_txt"] = dScale21["display"]

		pgui.bScaleOption18["enabled"] = False
		pgui.bScaleOption19["enabled"] = False
		pgui.bScaleOption20["enabled"] = False
		#pgui.bScaleOption21["enabled"] = False

		pgui.bScaleOption18["color"] = pgvar.UI_button_color
		pgui.bScaleOption19["color"] = pgvar.UI_button_color
		pgui.bScaleOption20["color"] = pgvar.UI_button_color
		#pgui.bScaleOption21["color"] = pgvar.UI_button_color

		pfunc.defineButtons()
		for i, button in enumerate(pfunc.my_buttons):
			button.display()	
		#pfunc.redrawEverything()


# ************************************************************************************************************************
# ************************************************************************************************************************
#  Particles to be inserted
# ************************************************************************************************************************
# ************************************************************************************************************************

pProton = {}
pProton["symbol"] = "p+"			#in program symbol ref
pProton["diameter"] = 1.6828		#meters, but effective diameter changes based on energy
pProton["scale"] = 1e-15			#default scale for particle where particle 1 < particle < 10
pProton["mass"] = 1.673e-27			#kg
pProton["charge"] = 1				#postive charge 1
pProton["class"] = "Baryon"
pProton["half-life"] = 0

print "pProton scale type", type(pProton["scale"])


# # example proton information:
"""
.8414 fm 		proton charge radius
1.5 fm 		size of an 11 MeV proton 

1 fm				Approximate limit of the gluon-mediated color force between quarks[6][7]
1.5 fm			Size of an 11 MeV proton[8]
2.81794 fm		Classical electron radius[9]
3 fm				Approximate limit of the meson-mediated nuclear binding force[6][7]
1.75 to 15 fm		Diameter range of the atomic nucleus[1][10]
https://en.wikipedia.org/wiki/Orders_of_magnitude_(length)#femtometre_to_picometre_range
"""

# so, scale examples
"""
1 pixel =			size of proton in pixels \ rounded
.01 femtometer 	84.14	84
.1 femtometer 	8.414	8
1 femtometer 		.8414	1
10 femto meters	.08414	1
"""






# testing out import decimal
num1 = 1.2e-27
num2 = .8e-28
num3 = num1 + num2
print "num3:", num3
num4 = num1 * num2
print "num4:", num4
num5 = 1
num6 = num1 + num5
print "num6:", num6
print type(num1)
print decimal.Decimal(num1)
num10 = 1.2e+20
print decimal.Decimal(num10)
num11 = 1.2e-20
print decimal.Decimal(num11)
num7 = '%.2E' % decimal.Decimal('408000000000.00000000')
print num7
num12 = 6.67408e-11
print num12
#print '%.2E' num12

