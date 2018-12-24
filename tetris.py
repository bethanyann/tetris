import pygame
import random

 
# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main
 
"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
 
pygame.font.init()
 
# GLOBALS VARS
s_width = 800 #screen width
s_height = 700 #screen height
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30
 
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
 
 
# SHAPE FORMATS
#two shapes for two rotations of the s piece
S = [[\'.....\',
      \'......\',
      \'..00..\',
      \'.00...\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'..00.\',
      \'...0.\',
      \'.....\']]
 
Z = [[\'.....\',
      \'.....\',
      \'.00..\',
      \'..00.\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'.00..\',
      \'.0...\',
      \'.....\']]
 
I = [[\'..0..\',
      \'..0..\',
      \'..0..\',
      \'..0..\',
      \'.....\'],
     [\'.....\',
      \'0000.\',
      \'.....\',
      \'.....\',
      \'.....\']]
 
O = [[\'.....\',
      \'.....\',
      \'.00..\',
      \'.00..\',
      \'.....\']]
 
J = [[\'.....\',
      \'.0...\',
      \'.000.\',
      \'.....\',
      \'.....\'],
     [\'.....\',
      \'..00.\',
      \'..0..\',
      \'..0..\',
      \'.....\'],
     [\'.....\',
      \'.....\',
      \'.000.\',
      \'...0.\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'..0..\',
      \'.00..\',
      \'.....\']]
 
L = [[\'.....\',
      \'...0.\',
      \'.000.\',
      \'.....\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'..0..\',
      \'..00.\',
      \'.....\'],
     [\'.....\',
      \'.....\',
      \'.000.\',
      \'.0...\',
      \'.....\'],
     [\'.....\',
      \'.00..\',
      \'..0..\',
      \'..0..\',
      \'.....\']]
 
T = [[\'.....\',
      \'..0..\',
      \'.000.\',
      \'.....\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'..00.\',
      \'..0..\',
      \'.....\'],
     [\'.....\',
      \'.....\',
      \'.000.\',
      \'..0..\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'.00..\',
      \'..0..\',
      \'.....\']]
 
shapes = [S, Z, I, O, J, L, T] #easy index for shapes
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)] #easy index for shape colors
# index 0 - 6 represent shape
 
 
class Piece(object): # * this is the main structure of our game 
    def _init_(self, x, y, shape)
    self.x=x
    self.y = y
    self.shape=shape
    self.color = shape_colors[shapes.index(shape)]
    self.rotation = 0
  
 
def create_grid(locked_positions = {}): #10/20 grid is created just by making a list full of colors
    #2d list - second dimension is the color
    #this creates the blank grid
    grid[[(0,0,0) for x in rage(10)] for x in range(20)]
    #this creates the drawing for the shapes that have already been placed and are static
    for i in range(len(grid)):
    	for j in range(len(grid[i])):
    		if (j,i) in locked_positions: 
    			c = locked_positions[(j,i)]
    			grid[i][j] = c

    return grid

#tells the computer how to take the shape format and draw a shape
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
    	row = list(line)
    	#'..0..' for example would be the row we're enumerating through
    	for j, column in enumerate(row):
    		if column == '0':
    			positions.append((shape.x + j, shape.y + i))
 
 	for i, pos in enumerate(positions):
 		positions[i] = (pos[0] - 2, pos[1] - 4) #offsets the shape to cut off the left and top dots/periods

 	return positions

#checks grid to see if shape is moving into a valid space
def valid_space(shape, grid):
	 #getting every accepted position that is not alreayd filled and adding it to a tuple
	accepted_pos = [[(j,i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
 	#convert tuple into one dimensional list
 	accepted_pos = [j for sub in accepted_pos for j in sub]

 	#get shape and convert into a position
 	formatted = convert_shape_format(shape)

 	#check to see if this position exists in the accepted positions list
 	for pos in formatted:
 		if pos not in accepted_pos:
 			if pos[1] > -1:
 				return False
 	return True


#are any positions above/outside of the screen? because then we lost
def check_lost(positions):
    for pos in positions:
    	x, y = pos 
    	if y < 1:
    		return True

  	return False

#passes in the list of shapes and picks a random shape to generate
def get_shape(shapes):

    return Piece(5, 0, random.choice(shapes))
 
 
def draw_text_middle(text, size, color, surface):
    pass
  
 #draws the grey lines of the grid structure 
def draw_grid(surface, grid):
	start_x = top_left_x
	start_y = top_left_y
	#for every row draw a line
	for i in range(len(grid)):
		pygame.draw.line(surface, (128,128,128), (start_x, start_y+i*block_size), (sx+play_width, sy+i*block_size))
		#for every column draw a line
		for j in range(len(grid[i])):
			pygame.draw.line(surface, (128,128,128), (start_x+j*block_size, start_y), (start_x+j*block_size, sy+play_height))

#clears the row when all the spaces are filled 
def clear_rows(grid, locked):

	inc = 0 #increment variable/count
	#loops through the grid backwards so you don't overwrite existing rows
	for i in range(len(grid)-1,-1,-1)	
		row = grid[i] #loops through and sets row equal to every row in the grid
		if (0,0,0) not in row: #if no black squares exist in the row, it needs to be cleared
				inc += 1  #holds the value of how many rows have been deleted/removed
				ind = 1
				for j in range(leng(row)): #get every position in the row
					try:
						del locked[(j,i)] #try to delete the row position key/values from locked_positions
					except:
						continue

	#ok now need to shift every row down after the full row has been cleared
	if inc > 0:
		for key in sorted(list(locked), key = lambda x: x[1])[::-1]:
			x,y = key
			if y < ind:
				newKey = (x,y + inc)
				locked[newKey] = locked.pop(key)


	#then add a new row at the top so theres still the same amount of rows as before




#draws the next shape off screen and shows you what it is
#kind of long and complicated
def draw_next_shape(shape, surface):

	font = pygame.font.SysFont('comicsans', 30)
	label = font.render('Next Shape', 1, (255,255,255))
 	
 	#constants to give horizontal middle-right of the screen to display the next piece
 	start_x = top_left_x + play_width + 50
	start_y = top_left_y + play_height/2 - 100
	format = shape.shape[shape.rotation % len(shape.shape)]

	for i, line in enumerate(format):
		row = list(line)
		for j, column in enumerate(row):
			if column == '0':
				pygame.draw.rect(surface, shape.color, (start_x + j*block_size, start_y + i*block_size, block_size, block_size), 0)

	surface.blit(label, (start_x + 10, start_y - 30))



def draw_window(surface, grid):

    surface.fill((0,0,0))
	pygame.font.init()
	font = pygame.font.SysFont('comicsans', 60)
	lavel = font.render('Tetris', 1, (255,255,255))

	#put the title of the game in the middle of the grid
	surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))   

	for i in range(len(grid)): #row
		for j in range(len(grid[i])): #column
			pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

	pygrame.draw.rect(surface, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 4)

	draw_grid(surface, grid)
 	#pygame.display.update()

def main(win):
    
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed =0.27 #how long it will take before each piece begins falling

    #main run loop
    while run: 
    	grid = create_grid(locked_positions) #constantly updates the grid
    	fall_time += clock.get_raw_time()#how long since the last loop ran? 
    	clock.tick()

    	if fall_time/1000 > fall_speed:
    		fall_time = 0
    		current_piece.y += 1
    		if not(valid_space(current_piece, grid)) and current_piece.y > 0:
    			current_piece.y -= 1
    			change_piece = True

    	for event in pygame.event.get() : 
    		if event.type == pygame.QUIT:
    			run = False

    		#determines shape movement based on what key was pressed
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_LEFT:
    				current_piece.x -= 1
    				if not(valid_space(current_piece, grid)):
    					current_piece.x += 1
    			if event.key == pygame.K_RIGHT:
    				current_piece.x += 1
    				if not(valid_space(current_piece, grid)):
    					current_piece.x -= 1
    			if event.key == pygame.K_UP:
    				current_piece.rotation += 1
    				if not(valid_space(current_piece, grid)):
    					current_piece.rotation -= 1
    			if event.key == pygame.K_DOWN:
    				current_piece.y += 1
    				if not(valid_space(current_piece, grid)):
    					current_piece.y -= 1

    	shape_pos = convert_shape_format(current_piece)

    	#draw the actual shape to the grid to see it moving etc
    	for in in range (len(shape_pos)):
    		x,y = shape_pos[i]
    		if y > -1:
    				grid[y][x] = current_piece.color
    	#gets the locked positions and then update the color of grid
    	if change_piece:
    		for pos in shape_pos:
    			p = (pos[0], pos[1])
    			locked_positions[p] = current_piece.color #locked_positions is a dictionary
    		current_piece = next_piece
    		next_piece = get_shape()
    		change_piece = False

    	draw_window(win, grid)
    	draw_next_shape(next_piece, win)
    	pygame.display.update()

    	#checks if the game has been lost and quits the game 
    	if check_lost(locked_positions):
    		run False
	pygame.display.QUIT

 
def main_menu(win):
    main(win)
 

win = pygame.display.set_mode((s_width. s_height))
pygame.display.set_caption('Tetris')
main_menu(win)  # start game