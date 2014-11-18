#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 5



class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "green")
		self.up.grid(row=0,column=1)											
		self.up.bind("<Button-1>", self.moveUp)
		
		self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "yellow")
		self.right.grid(row=1,column=2)
		self.right.bind('<Button-1>', self.moveRight)
		
		self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "yellow")
		self.left.grid(row=1,column=0)
		self.left.bind('<Button-1>', self.moveLeft)
		
		self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "green")
		self.down.grid(row=2,column=1)
		self.down.bind('<Button-1>', self.moveDown)
                
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

		
	def moveUp(self, event):   
		global player
		global drawpad
		x1,y1,x2,y2 = drawpad.coords(player)
		if y1 > 0:
                    drawpad.move(player,0,-10)
        
        def moveRight(self,event):
            global player
            global drawpad
            x1,y1,x2,y2 = drawpad.coords(player)
            if x2 < drawpad.winfo_width():
                drawpad.move(player,10,0)
                
        def moveLeft(self,event):
            global player
            global drawpad
            x1,y1,x2,y2 = drawpad.coords(player)
            if x1 > 0:
                drawpad.move(player,-10,0)
                
        def moveDown(self,event):
            global player
            global drawpad
            x1,y1,x2,y2 = drawpad.coords(player)
            if y2 < drawpad.winfo_height():
                drawpad.move(player,0,10)
    
         
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global target
	    global direction
	    tx1,ty1,tx2,ty2 = drawpad.coords(target)
	    x1,y1,x2,y2 = drawpad.coords(player)
	    
	    if tx1 < 0:
	        direction = 5
	    if tx2 > drawpad.winfo_width():
	        direction = -5
	    drawpad.move(target,direction,0)

            didWeHit = self.collisionDetect()
            if didWeHit:
                 drawpad.after(10, self.animate)
                   
            
	def collisionDetect(self):
                global target
		global drawpad
                global player
                global targetx1,targety1,targetx2,targety2
                x1,y1,x2,y2 = drawpad.coords(player)
                tx1,ty1,tx2,ty2 = drawpad.coords(target)
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)
                if (x1 > tx1 and x2 < t=====x2) and (y1 > ty1 and y2 < ty2):
                    return False
                else:
                    return True
                # Do your if statement - remember to return True if successful!                
		
myapp = MyApp(root)

root.mainloop()