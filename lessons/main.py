# This is code is for using the turles library


# Start with the prettifier

# ------------------------------------------------------
from rich import print as rprint # For rprinting
from rich.pretty import pprint # For pretty printing
from rich import inspect # For inspect
from rich.console import Console # For console.print
from rich.markdown import Markdown # For markdown
from rich.panel import Panel # For Panel()
from rich import box # For Panel Boxes
from rich.prompt import Prompt # For Prompting
from rich.style import Style # For styles colors
from rich.text import Text # For text Styles
console = Console() # Standard code to access console
from rich.traceback import install
install(show_locals=True)
# -------------------------------------------------------

# Using turtle
from turtle import Turtle, Screen
timmy = Turtle()
rprint(timmy)

my_screen = Screen()
rprint(my_screen.canvheight)

# Shapes and colors
timmy.shape("turtle")
timmy.color("coral")
timmy.shapesize(stretch_wid=3, stretch_len=3, outline=1)
timmy.screen.bgcolor("#020617")
# Make it move 1oo

def t_m():
    for i in range(0,10):
        timmy.forward(100)
        timmy.backward(100)
        timmy.left(20)
        timmy.right(50)

# This
t_m()
my_screen.exitonclick()
