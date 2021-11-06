import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        bricks = cast["brick"]
        
        for brick in bricks:
            if brick.get_position().equals(ball.get_position()):                 
                #delete brick 
                bricks.remove(brick)
                #redirect ball
                x = ball.get_velocity().get_x()
                y = (ball.get_velocity().get_y()) * -1
                velocity = Point(x,y)
                ball.set_velocity(velocity)

                break

        #Creat for loop for paddle ball collision
       
        

        if paddle.get_position().equals(ball.get_position()):

            x = ball.get_velocity().get_x()
            y = (ball.get_velocity().get_y()) * -1
            velocity = Point(x,y)
            ball.set_velocity(velocity)

        
    