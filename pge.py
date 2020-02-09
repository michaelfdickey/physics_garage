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
#	/pge.py 				# element definitions, such as all the variables assocated with particles

# pgui.py

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
#import pfunc
#import pgui
#import pclass
#import pbproc


# ************************************************************************************************************************
# ************************************************************************************************************************
#  Element that can be added to the simulation Dictionaries
# ************************************************************************************************************************
# ************************************************************************************************************************

# Proton

pProton = {}
pProton["symbol"] = "p+"
pProton["diameter"] = .8414e-15			#meters, but effective diameter changes based on energy
pProton["scale"] = "femtometer"
pProton["mass"] = 1.673e-27				#kg
pProton["charge"] = 1
pProton["class"] = "Baryon"
pProton["half-life"] = 0


print "pProton mass:", pProton["mass"]

# so, scale examples
"""
1 pixel =			size of proton in pixels \ rounded
.01 femtometer 	84.14	84
.1 femtometer 	8.414	8
1 femtometer 		.8414	1
10 femto meters	.08414	1
"""

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
19	10e-16	.1 femtometer 		.8414 fm = charge radius of Proton
20	10e-15	femtrometer (fm)		1.5 fm = Size of 11 MeV proton
21	10e-14	10 femtometers 		1.75 fm - 15 fm Diameter range of atomic Nuclei

								

good list to integrate
https://en.wikipedia.org/wiki/Orders_of_magnitude_(length)#femtometre_to_picometre_range
"""

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

