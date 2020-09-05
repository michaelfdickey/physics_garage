adding a new scale:

"""
1) add scale option button dictionary in pgui.py 
2) fix y origin "bScaleOption20["origin_y"] = scale_display_origin - 20"
3) add it to allButtons[97] = bScaleOption18 at the bottom of pgui.py
4) add it to def scaleUpdate(): in pge.py 
5) add it to pbproc # # # Scale Options Processing
6) also add it to # # # Scale Opener BUTTON in pbproc.py
7) added to physics_garage.py # # #PUSHY EVENT PROCESSING # # #