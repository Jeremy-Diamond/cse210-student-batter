import random
from game import constants
from game.action import Action

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
        #marquee.set_text("")
        for brick in bricks:
            if brick.get_position().equals(ball.get_position()):                 
                #delete brick and redirect ball
                bricks.remove(brick)
                ball.set_velocity(ball.get_velocity().get_y())
                break

        #Creat for loop for paddle ball collision
                #redirect ball
