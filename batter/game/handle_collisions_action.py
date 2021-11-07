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
       
        paddle_position_x = paddle.get_position().get_x()
        paddle_position_y = paddle.get_position().get_y()
        ball_position_x = ball.get_position().get_x()
        ball_position_y = ball.get_position().get_y()
        

        if paddle_position_y == ball_position_y:
            for paddle_piece in range(11):
                paddle_piece_x = paddle_position_x + paddle_piece 
                if paddle_piece_x == ball_position_x:

                    velocity_y = (ball.get_velocity().get_y()) * -1
                    velocity_x = (ball.get_velocity().get_x())

                    if velocity_x == 1:
                        if paddle_piece <= 3:
                            velocity_x = velocity_x * -1
                    else:
                        if paddle_piece >= 9:
                            velocity_x = velocity_x * -1    
                    
                    velocity = Point(velocity_x,velocity_y)
                    ball.set_velocity(velocity)

        
    