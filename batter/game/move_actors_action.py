import sys

from pyfiglet import DEFAULT_FONT
from game import constants
from game.action import Action
from game.point import Point
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()
        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()
        if y1 == 2:                             # cealing
            y2 = y2 * -1
        if x1 == 5 or x1 == constants.MAX_X -5: #left and right walls
            x2 = x2 * -1 
        if y1 == constants.MAX_Y:                      
            # y2 = y2 * -1  
            def demo(screen):
                effects = [
                    Cycle(
                        screen,
                        FigletText("GAME", font='big'),
                        int(screen.height / 2 - 8)),
                    Cycle(
                        screen,
                        FigletText("OVER!", font='big'),
                        int(screen.height / 2 + 3)),
                    Stars(screen, 200)
                ]
                screen.play([Scene(effects, 500)])
            Screen.wrapper(demo)
           
        velocity = Point(x2,y2)
        x = 1 + (x1 + x2 - 1) #% (constants.MAX_X - 1) #NEED TO EDIT TO MAKE WALLS
        y = 1 + (y1 + y2 - 1) #% (constants.MAX_Y - 1) #NEED TO EDIT TO MAKE WALLS
        position = Point(x, y)
        actor.set_position(position)
        actor.set_velocity(velocity)

    