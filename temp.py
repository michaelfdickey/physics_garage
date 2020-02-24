# co-ordinates

creating particle:
get game x y -> get scale ->  get relative to origin co-ordinates -> create particle. 

displaying particle
get rel org coord -> get scale -> convert to game x y -> display particle

updating particle position
get rel org coord -> get scale -> convert to game x y -> display particle -> update position -> get game x y -> get scale ->  get relative to origin co-ordinates -> create particle. 


#temp.py

# # how to concatonate strings and ints:

positionX  = 50
positionXstr = str(int(positionX))
gameX = "gameX "
gameX = gameX + positionXstr
print gameX