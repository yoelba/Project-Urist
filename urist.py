import pyglet
import pyglet.gl
from pyglet.window import key, mouse


window = pyglet.window.Window(1000,800)
dwarfPic = pyglet.image.load('dorf.png')
squarePNG = pyglet.image.load('shitSquare.png')

#variables and such:
turnIndex = 0;

class Dwarf:
	dorfname = pyglet.text.Label('NULL', x=window.width//2-50, y=window.height//2-50, anchor_x='center', anchor_y='center')
	image = pyglet.sprite.Sprite(dwarfPic, x = 0, y = 0)
	def __init__(self, x, y, name):
		global turnIndex
		self.speed = 3
		self.turn = False
		self.turnTimer = self.speed
		self.posY = x
		self.posX = y
		self.dorfname = pyglet.text.Label(name, x=self.posX+50, y=self.posY+130, anchor_x='center', anchor_y='center')
		self.image = pyglet.sprite.Sprite(dwarfPic, x=self.posX, y = self.posY)
	def draw(self):
		self.image.draw()
		self.dorfname.draw()
	def movement(self, symbol, modifiers):
		global turnIndex
		global entities
		if symbol == key.RIGHT:
			self.dorfname.x += 100
			self.image.x += 100
			self.turnTimer -= 1
		elif symbol == key.UP:
			self.dorfname.y += 100
			self.image.y += 100
			self.turnTimer -= 1
		elif symbol == key.DOWN:
			self.dorfname.y -= 100
			self.image.y -= 100
			self.turnTimer -=1
		elif symbol == key.LEFT:
			self.dorfname.x -= 100
			self.image.x -= 100
			self.turnTimer -= 1
		if self.turnTimer == 0:
			self.turn = False
			self.turnTimer = self.speed
			turnIndex += 1
			if turnIndex > len(entities)-1:
				turnIndex = 0


class Square:
	def __init__(self, x, y):
		self.posX = x
		self.posY = y
		self.image = pyglet.sprite.Sprite(squarePNG, x = self.posX, y =self.posY)
	def draw(self):
		self.image.draw()
	
#Our characters today:
entities = list()

entities.append(Dwarf(500,300, "Urist"))
entities.append(Dwarf(300,200, "Dongus"))
entities.append(Dwarf(500,500, "Nathan"))

squares = list()

for i in range(0,10):
	for j in range(0,8): 
		squares.append(Square(100*i,100*j)) 
		

#-----------------

entities[turnIndex].turn = True
for i in range(0,len(entities)):
	entities[i].draw()
	print "WTF"
for entity in entities:
	entity.draw()



#-------------------
@window.event
def on_key_press(symbol, modifiers): #Movement update
	entities[turnIndex].turn = True
	window.clear()
	for square in squares:
		square.draw()
	for entity in entities:
		if entity.turn == True:
			entity.movement(symbol, modifiers)
			#entity.draw()
		entity.draw()	

"""
@window.event
def on_draw():
	for i in range(0,10):
		pyglet.graphics.draw(2, pyglet.gl.GL_LINES,("v2f", (100*i, 0, 100*i, 800)))
	for i in range(0,8):
		pyglet.graphics.draw(2, pyglet.gl.GL_LINES,("v2f", (0, 100*i, window.width, 100*i)))
"""
	
pyglet.app.run()
