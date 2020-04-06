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
img_asteroid2 = "images/meteorGrey_med1.png"
img_asteroid3 = "images/meteorGrey_small1.png"

img_laser = "images/laserBlue01.png"


ASTEROID_SPEED = 1.5

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
        print(f"degrees is {degrees}")
        self.dx = self.dx+float(math.cos(math.radians(degrees)) * v_in)
        self.dy = self.dy+float(math.sin(math.radians(degrees)) * v_in)
        print(f"x {self.dx} y {self.dy} {degrees}")
class Laser():
    radius=30
    vms = ASTEROID_SPEED
    traveled=600
    def __init__(self,x,y,angle,velocity):
        self.alive=True
        self.center=Point(x,y)
        self.velocity=velocity
        self.absolute=(self.velocity.dx*self.velocity.dx) + (self.velocity.dy*self.velocity.dy)
        self.absolute=math.sqrt(self.absolute)+10
        print(f"absolute is {self.absolute}")
        self.velocity.setFromHypo(angle,self.absolute)
        #self.velocity.dx =self.velocity.dx
        #self.velocity.dy =self.velocity.dy
        self.texture = arcade.load_texture(img_laser)
        self.radius=LARGE_RADIUS
        self.angle=angle
        self.width = self.texture.width
        self.height = self.texture.height
    def is_off_screen(self,s_width,s_height):
        if self.center.x > s_width:
            self.center.x = 1
            print("flip 1")
        elif self.center.y > s_height:
            self.center.y = 1
            print("flip 2")
        elif self.center.y < 0:
            self.center.y = s_height-1
            print("flip 3")
        elif self.center.x < 0:
            print("flip 4")
            self.center.x = s_width-1
    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle)        
    def fire(self, angle):
        self.angle=angle
        self.velocity.setFromHyp(self,angle,vms)
    def advance(self):
        new_x = self.center.x+self.velocity.dx
        new_y = self.center.y+self.velocity.dy
        travel=math.sqrt(self.velocity.dy*self.velocity.dy + self.velocity.dx*self.velocity.dx)
        self.center=Point(new_x,new_y)
        print(f" traveled {travel}")
        self.traveled= self.traveled-travel
        print(f" remaining to {self.traveled}")
    def is_off_screen(self,s_width,s_height):
        if self.center.x > s_width:
            self.center.x = 0
        elif self.center.y > s_height:
            self.center.y = 0
        elif self.center.y < 0:
            self.center.y = s_height-1
        elif self.center.x < 0:
            self.center.x = s_width-1
class Asteroid():

    base_speed=.5
    def __init__(self):
        self.texture = arcade.load_texture(img_asteroid1)
        self.radius=LARGE_RADIUS
        self.rotation=1
        self.width = self.texture.width
        self.height = self.texture.height
        self.alpha = 255
        self.init_v=self.base_speed
        self.alive=True
        x=random.uniform(0,SCREEN_WIDTH)
        y=random.uniform(0,SCREEN_HEIGHT)
        half_height=SCREEN_HEIGHT/2
        half_width=SCREEN_WIDTH/2
        if abs(x-half_width)<self.radius:
            x=x+90
        if abs(y-half_height)<self.radius:
            y=y+90
        self.center=Point(x,y)
        self.angle=random.uniform(0,360)
        self.velocity=Velocity(0,0)
        self.velocity.setFromHypo(self.angle,self.init_v)
        self.score=1
    def draw(self):
        #print(f" angle {self.angle}")
        
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, self.alpha)        
        self.angle=self.angle+1
        if self.angle>360:
            self.angle=1
    def advance(self):
        new_x = self.center.x+self.velocity.dx
        new_y = self.center.y+self.velocity.dy
        self.center=Point(new_x,new_y)
    def is_off_screen(self,s_width,s_height):
        if self.center.x > s_width:
            self.center.x = 0
        elif self.center.y > s_height:
            self.center.y = 0
        elif self.center.y < 0:
            self.center.y = s_height-1
        elif self.center.x < 0:
            self.center.x = s_width-1
    def break_apart(self):
        c = MediumAsteroid()
        c.center=Point(self.center.x,self.center.y)
        c.velocity = Velocity(self.velocity.dx,self.velocity.dy+.2)
        d = MediumAsteroid()
        d.center=Point(self.center.x,self.center.y)
        d.velocity = Velocity(self.velocity.dx,self.velocity.dy-.2)
        e = SmallAsteroid()
        e.center=Point(self.center.x,self.center.y)
        e.velocity = Velocity(self.velocity.dx+.5,self.velocity.dy-.2)
        debris = [c,d,e]
        
        return debris
        
    
    
class SmallAsteroid(Asteroid):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(img_asteroid3)
        self.width = self.texture.width
        self.height = self.texture.height
        self.rotation=5
        self.radius=2
    def break_apart(self):
        debris =[]
        return debris
class MediumAsteroid(Asteroid):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(img_asteroid2)
        self.width = self.texture.width
        self.height = self.texture.height
        self.rotation=-2
        self.radius=5
    def break_apart(self):
        c = SmallAsteroid()
        c.center=Point(self.center.x,self.center.y)
        c.velocity = Velocity(self.velocity.dx+.5,self.velocity.dy+.5)
        d = SmallAsteroid()
        d.center=Point(self.center.x,self.center.y)
        d.velocity = Velocity(self.velocity.dx-.5,self.velocity.dy-.5)
        debris = [c,d]
        return debris
class Ship:
    """
    The ship is a rectangle that tracks the mouse.
    hitbox is a circle
    
    """
    radius=30
    def __init__(self):
        self.keys=[]
        self.texture = arcade.load_texture(img_ship)
        self.radius=LARGE_RADIUS
        self.rotation=1
        self.width = self.texture.width
        self.height = self.texture.height
        self.alpha = 255
        self.center = Point()
        self.center.x = SCREEN_WIDTH/2
        self.center.y = SCREEN_HEIGHT/2
        self.velocity=Velocity(0,0)
        self.angle = 180
        
    def advance(self):
        for key in self.keys:
            increase=0.25
            if key == arcade.key.LEFT:
                self.angle=self.angle-3
            elif key == arcade.key.RIGHT:
                self.angle=self.angle+3
            elif key == arcade.key.DOWN :
                self.velocity.setFromHypo(self.angle-90,increase)
            elif key == arcade.key.UP:
                self.velocity.setFromHypo(self.angle+90,increase)
        new_x = self.center.x+self.velocity.dx
        new_y = self.center.y+self.velocity.dy
        self.center=Point(new_x,new_y)
    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, self.alpha)  
    def is_off_screen(self,s_width,s_height):
        if self.center.x > s_width:
            self.center.x = 1
            print("flip 1")
        elif self.center.y > s_height:
            self.center.y = 1
            print("flip 2")
        elif self.center.y < 0:
            self.center.y = s_height-1
            print("flip 3")
        elif self.center.x < 0:
            print("flip 4")
            self.center.x = s_width-1

class Game(arcade.Window):


    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        self.first_update=True
        self.asteroid_count=0
        self.lasers = []
        self.asteroids = []
        self.ship = Ship()
        arcade.set_background_color(arcade.color.WHITE)
        self.game_over=False
        self.won=False
    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()
        if not self.first_update and len(self.asteroids)==0:
            """
            Draw "Game over" across the screen.
            """
            for lasers in self.lasers:
                self.remove(lasers)
            for ast in self.asteroids:
                self.remove(ast)
            output = "Cleared them ALL!!"
            second_out = "Hit space to play again"
            self.won=True
            self.ship = Ship()
            arcade.draw_text(output, (SCREEN_WIDTH/2)-250, SCREEN_HEIGHT/2, arcade.color.BLACK, 54)
            arcade.draw_text(second_out, (SCREEN_WIDTH/2)-125, SCREEN_HEIGHT/3, arcade.color.BLACK, 24)
        elif self.game_over:
            
            """
            Draw "Game over" across the screen.
            """
            output = "Game Over"
            second_out = "Hit space to play again"
            self.game_over=True
            self.ship = Ship()
            arcade.draw_text(output, (SCREEN_WIDTH/2)-150, SCREEN_HEIGHT/2, arcade.color.BLACK, 54)
            arcade.draw_text(second_out, (SCREEN_WIDTH/2)-125, SCREEN_HEIGHT/3, arcade.color.BLACK, 24)
        else:
            #draw ship
            # draw each asteroid
            num_drawn=0
            
            for asteroid in self.asteroids:
                #print(f" num drawn {num_drawn}")
                asteroid.draw()
                num_drawn=num_drawn+1
            # TODO: iterate through your lasers and draw them...
            #print(len(self.lasers))
            for laser in self.lasers:
                if laser.traveled<0:
                    self.lasers.remove(laser)
                laser.draw()
            self.ship.draw()
        
    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a asteroid
        
        while self.asteroid_count < 3 and self.first_update:
            self.create_target()
            self.asteroid_count=self.asteroid_count+1
        self.first_update=False

        for asteroid in self.asteroids:
            asteroid.advance()
        for laser in self.lasers:
            laser.advance()
        self.ship.advance()


    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """
        print("called me")
        b= Asteroid()
        self.asteroids.append(b)
    def create_laser(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """
        print("called me2")
        b=Velocity(self.ship.velocity.dx,self.ship.velocity.dy)
        angle_travel = math.tan((self.ship.velocity.dx*self.ship.velocity.dx)+(self.ship.velocity.dy*self.ship.velocity.dy))
        
        laser= Laser(self.ship.center.x,self.ship.center.y,self.ship.angle+90,b)
        print("got y")
        #laser.fire(self.ship.angle)
        print("got x")
        self.lasers.append(laser)
        print("got z")
        #print(len(self.lasers))
        
        # TODO: Decide what type of target to create and append it to the list

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """
        for asteroid in self.asteroids:
            diff_ship_x = asteroid.center.x - self.ship.center.x
            diff_ship_y = asteroid.center.y - self.ship.center.y
            if abs(diff_ship_x) < self.ship.radius+35 and abs(diff_ship_y) < self.ship.radius+35:
                self.game_over=True
            else:
                for laser in self.lasers:
                    diff_x = asteroid.center.x - laser.center.x
                    diff_y = asteroid.center.y - laser.center.y
                    if abs(diff_x) < asteroid.radius+10 and abs(diff_y) < asteroid.radius+10:
                            self.lasers.remove(laser)
                            self.asteroids.remove(asteroid)
                            debris = asteroid.break_apart()
                            for x in debris:
                                self.asteroids.append(x)
                                
        #do collision checking
        
    
    def check_re_enter(self):
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
        for asteroird in self.asteroids:
            asteroird.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT);

        for laser in self.lasers:
            laser.is_off_screen(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.ship.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT);
    
    # might add back later
    #def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):

        #track proper direction for ship

     #   self.ship.angle = self._get_angle_degrees(x, y,self.ship.center.x,self.ship.center.y)
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        if not self.won and not self.game_over:
            angle = self.ship.angle
            print("key pressed")
            self.create_laser()
            print("laser created")
    def on_key_press(self, key, modifiers):
        #move ship
        if not self.won and not self.game_over:
            increase = .2
            if key == arcade.key.LEFT:
                self.ship.keys.append(arcade.key.LEFT)
            elif key == arcade.key.DOWN :
                self.ship.keys.append(arcade.key.DOWN)

            elif key == arcade.key.RIGHT:
                self.ship.keys.append(arcade.key.RIGHT)
            elif key == arcade.key.UP:
                self.ship.keys.append(arcade.key.UP)
        else:
            if key == arcade.key.SPACE:
                self.game_over=False
                self.won=False
                self.first_update=True
                self.asteroid_count=0
                self.asteroids=[]
                self.lasers=[]
            """Called when the user releases a key. """
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if not self.won and not self.game_over:
            if key == arcade.key.LEFT:
                self.ship.keys.remove(arcade.key.LEFT)
            elif key == arcade.key.DOWN :
                self.ship.keys.remove(arcade.key.DOWN)

            elif key == arcade.key.RIGHT:
                self.ship.keys.remove(arcade.key.RIGHT)
            elif key == arcade.key.UP:
                self.ship.keys.remove(arcade.key.UP)
    def _get_angle_degrees(self, x, y,x2,y2):

        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        rel_y=y-y2
        rel_x=x-x2
        #print(rel_x,rel_y)
        angle_radians = math.atan2(rel_x,rel_y)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)
        #print(angle_degrees)
        return angle_degrees

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()