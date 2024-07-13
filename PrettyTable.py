# File for testin pretty table
# use Ctrl+Shift+F10 to run this


from rich import print as rprint
from rich.pretty import pprint
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt
from rich.style import Style
from rich.text import Text
console = Console()
from rich.traceback import install
install(show_locals=True)

#------------------

from prettytable import PrettyTable
table = PrettyTable()
inspect(table, methods=True)

rprint(f'''
[red] Whatup Whatup Whatup Whatup Whatup
Whatup Whatup Whatup Whatup Whatup
Whatup Whatup Whatup Whatup Whatup
Whatup Whatup Whatup Whatup Whatup
''')
