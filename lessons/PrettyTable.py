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
from rich.table import Table
console = Console()
from rich.traceback import install
install(show_locals=True)

#------------------

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)

rprint(table)

# Printing the table with the rich package

rprint(Panel.fit('Hey'))

table2 = Table(title="Star Wars Movies")

table2.add_column("Released", justify="right", style="cyan", no_wrap=True)
table2.add_column("Title", style="magenta")
table2.add_column("Box Office", justify="right", style="green")

table2.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table2.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table2.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table2.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table2)