# Imports

import os
import pandas as pd
from rich import print
from date import handle_date

pd.options.mode.chained_assignment = None  # default='warn'


def calculate_profit(input_date):
    if not handle_date(input_date):
        print(
            f"[bold red]:thumbs_down: Het datatype voor deze parameter is niet juist. Dit moet een string zijn: YYYY-MM-DD\n:thumbs_down: The data type for this parameter is incorrect. This should be a string: YYYY-MM-DD[/bold red]"
        )
        return
    elif handle_date(input_date):
        input_date = pd.to_datetime(input_date)
    if not os.path.isfile("sold.csv"):
        print(
            f"[bold magenta]:exclamation_mark: Er is nog niets ingekocht!\n:exclamation_mark: Nothing bought yet.[/bold magenta]"
        )
    if not os.path.isfile("bought.csv"):
        print(
            f"[bold magenta]:exclamation_mark: Er is nog niet verkocht!\n:exclamation_mark: Nothing sold yet.[/bold magenta]"
        )
    elif os.path.isfile("sold.csv") & os.path.isfile("bought.csv"):
        sold = pd.read_csv("sold.csv")
        bought = pd.read_csv("bought.csv")

        bought["buy_date"] = pd.to_datetime(bought["buy_date"])
        bought["bought"] = input_date >= bought["buy_date"]
        bought_true = bought[bought["bought"] == True]

        sold["sell_date"] = pd.to_datetime(sold["sell_date"])
        sold["sold"] = input_date >= sold["sell_date"]
        sold_true = sold[sold["sold"] == True]

        bought_true["buy_price"] = pd.to_numeric(
            bought_true["buy_price"])
        bought_true["quantity"] = pd.to_numeric(bought_true["quantity"])
        bought_true["costs"] = (
            bought_true["quantity"] * bought_true["buy_price"]
        )

        sold_true["sell_price"] = pd.to_numeric(sold_true["sell_price"])
        sold_true["quantity"] = pd.to_numeric(sold_true["quantity"])
        sold_true["benefit"] = sold_true["quantity"] * \
            sold_true["sell_price"]

        total_costs = bought_true["costs"].sum()
        total_benefit = sold_true["benefit"].sum()
        total_profit = total_benefit - total_costs
        date = input_date.strftime("%Y-%m-%d")

        if int(total_benefit) == 0:
            print(
                f"[bold blue]Er zijn geen producten ingekocht op/voor {date}\nThere are no products bought on/before {date}[/bold blue]"
            )
        if int(total_costs) == 0:
            print(
                f"[bold blue]Er zijn geen producten verkocht op/voor {date}\nThere are no products sold on/before {date}[/bold blue]"
            )
        else:
            print(
                f"Producten zijn gekocht op/voor {date}.\nProducts are bought on/before {date}."
            )
            print(bought_true)
            print(
                f"Producten zijn ingekocht op/voor {date}.\nProducts are sold on/before {date}."
            )
            print(sold_true)
            print(
                f"[bold green]:euro_banknote: Totale kosten:/ Total costs:[/bold green]\n[bold]€[/bold] {str(total_costs)}"
            )
            print(
                f"[bold green]:euro_banknote: Totale bruto:/ Total bruto:[/bold green]\n[bold]€[/bold] {str(total_benefit)}"
            )
            print(
                f"[bold green]:euro_banknote: Totale winst:/ Total profit:[/bold green]\n[bold]€[/bold] {str(total_profit)}"
            )
