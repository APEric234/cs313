"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others
This program implements an awesome version of skeet.
"""
import arcade
import math
import random
import time

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

img_ship = "images/playerShip1_orange.png"
img_asteroid1 = "images/meteorGrey_big1.png"
img_asteroid2 = "images/meteorGrey_med.png"
img_asteroid3 = "images/meteorGrey_smal.png"

img_laser = "images/laserBlue01.png"



BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

LARGE_RADIUS = 15

#changed game to have all targets start from center and to actually fall as they travel
class Point():
    def __init__(self,x_position=None,y_position=None):
        if (x_position is None or y_position is None):
            self.x=0
            self.y=0
        else:
            self.x=x_position
            self.y=y_position
    
class Velocity():
    def __init__(self,vx,vy):
        self.dx=vx
        self.dy=vy

    def setFromHypo(self,degrees,v_in):
        
        self.dx = self.dx+int(math.cos(math.radians(degrees)) * v_in)
        self.dy = self.dy+int(math.sin(math.radians(degrees)) * v_in)
        print(f"x {self.dx} y {self.dy}")
class Bullet():
    radius=BULLET_RADIUS
    vms = BULLET_SPEED
    def __init__(self):
        self.alive=True
        self.center=Point(5,5)
        self.velocity=Velocity(0,0)
            
    def draw(self):
        pass
    def fire(self, angle):
        pass
    def advance(self):
        pass
    def is_off_screen(self,s_width,s_height):
        pass
        
class Asteroid():

    base_speed=1.5
    def __init__(self):
        self.texture = arcade.load_texture(img_asteroid1)
        self.radius=LARGE_RADIUS
        self.rotation=1
        self.width = self.texture.width
        self.height = self.texture.height
        self.alpha = 255
        self.init_v=self.base_speed
        self.alive=True
        x=SCREEN_WIDTH/2
        y=SCREEN_HEIGHT/2
        self.center=Point(x,y)
        self.angle=random.uniform(0,360)
        self.velocity=Velocity(0,0)
        self.velocity.setFromHypo(self.angle,self.init_v)
        self.score=1
    def draw(self):
        print(f" angle {self.angle}")
        
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, self.alpha)        
        self.angle=self.angle+1
        if self.angle>360:
            self.angle=1
    def advance(self):
        new_x = self.center.x+self.velocity.dx
        new_y = self.center.y+self.velocity.dy
        self.center=Point(new_x,new_y)
    def hit(self):
        pass
        
    
class SmallAsteroid(Asteroid):
    def __init__(self):
        pass
    def draw(self):
        pass
    def advance(self):
        pass
    def hit(self):
        pass
class MediumAsteroid(Asteroid):
    def __init__(self):
        pass
        
    def draw(self):
        pass
        
class Ship:
    """
    The ship is a rectangle that tracks the mouse.
    hitbox is a circle
    
    """
    def __init__(self):
        pass
    """
        self.texture = arcade.load_texture(img)
        self.center = Point()
        self.center.x = SCREEN_WIDTH/2
        self.center.y = SCREEN_HEIGHT/2
        self.v=Velocity(0,0)
        self.angle = 180
"""
    def draw(self):
        pass
        """
        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(self.x, self.y, width, height, self.texture, angle, alpha)  
"""

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.asteroid_count=0

        self.asteroids = []

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()
        
        
        #draw ship
        # draw each asteroid
        num_drawn=0
        for asteroid in self.asteroids:
            #print(f" num drawn {num_drawn}")
            asteroid.draw()
            num_drawn=num_drawn+1
        # TODO: iterate through your lasers and draw them...

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        
        if self.asteroid_count < 5:
            self.create_target()
            self.asteroid_count=self.asteroid_count+1

        for asteroid in self.asteroids:
            asteroid.advance()


        
    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """
        print("called me")
        b= Asteroid()
        self.asteroids.append(b)
        
        # TODO: Decide what type of target to create and append it to the list

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """
        #do collision checking
    
    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        #not sure if needed leaving

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        #for cycling around screen
        """for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)
        """
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):

        #track proper direction for ship
        #self.rifle.angle = self._get_angle_degrees(x, y)
        pass
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        #bullet = Bullet()
        #bullet.fire(angle)

        #self.bullets.append(bullet)
    def on_key_press(self, x: float, y: float, button: int, modifiers: int):
        #move ship
        pass
    def _get_angle_degrees(self, x, y):
        pass
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        #angle_radians = math.atan2(y, x)

        # convert to degrees
        #angle_degrees = math.degrees(angle_radians)

        #return angle_degrees

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()