# Imports

import os
import pandas as pd
from rich import print
from date import handle_date


def export(selection, date):
    if not handle_date(date):
        print(
            f"[bold red]:thumbs_down: Het datatype voor deze parameter is niet juist. Dit moet een string zijn: YYYY-MM-DD\n:thumbs_down: The data type for this parameter is incorrect. This should be a string: YYYY-MM-DD[/bold red]"
        )
        return
    elif handle_date(date):
        date = pd.to_datetime(date)
    if selection == "expired":
        if not os.path.isfile("inventory.csv"):
            print(
                f"[bold red]Er zijn geen voorraadgegevens beschikbaar\nThere is no inventory data available[/bold red]"
            )
        elif os.path.isfile("inventory.csv"):
            inventory = pd.read_csv("inventory.csv")
            inventory["expiration_date"] = pd.to_datetime(
                inventory["expiration_date"], format="%Y-%m-%d"
            )
            inventory["expired"] = inventory["expiration_date"] < date
            inventory_selection = inventory[inventory["expired"] == True]
            if inventory_selection.empty:
                print(
                    f"[bold blue]Er zijn geen producten over de uiterste vervaldatum tot op heden.\nThere are no expired products to this date.[/bold blue]"
                )
            else:
                print(
                    f"[bold red]:exclamation_mark: Deze producten zijn over de datum:\n:exclamation_mark: These products are expired:[/bold red]\n{inventory_selection.to_string(index=False)}"
                )
                print(
                    f"Gegevens zijn geëxporteerd naar expired.csv.\nData is exported to expired.csv."
                )
                return inventory_selection.to_csv("expired.csv", index=False)
    if selection == "bought":
        if not os.path.isfile("bought.csv"):
            print(
                f"[bold magenta]Er is nog niets ingekocht!\nNothing bought yet![/bold magenta]"
            )
        elif os.path.isfile("inventory.csv"):
            bought = pd.read_csv("bought.csv")
            bought["buy_date"] = pd.to_datetime(bought["buy_date"])
            bought["bought"] = bought["buy_date"] <= date
            bought_selection = bought[bought["bought"] == True]
            if bought_selection.empty:
                print(
                    f"[bold blue]:prohibited: Er zijn geen producten gekocht tot op heden!\n:prohibited: There are products bought to this date![/bold blue]"
                )
            else:
                print(
                    f"[bold blue]:basket: Deze producten zijn gekocht:\n:basket: These products are bought:[/bold blue]\n{bought_selection.to_string(index=False)}"
                )
                print(
                    f"Gegevens zijn geëxporteerd naar bought.csv.\nData is exported to bought.csv."
                )
                return bought_selection.to_csv("bought.csv", index=False)
    if selection == "sold":
        if not os.path.isfile("sold.csv"):
            print(
                f"[bold magenta]Er is nog geen data voor verkocht!\nThere is no data for sold yet![/bold magenta]"
            )
        elif os.path.isfile("sold.csv"):
            sold = pd.read_csv("sold.csv")
            sold["sell_date"] = pd.to_datetime(sold["sell_date"])
            sold["sold"] = sold["sell_date"] <= date
            sold_selection = sold[sold["sold"] == True]
            if sold_selection.empty:
                print(
                    f"[bold blue]Er zijn geen producten verkocht tot op heden.\nThere are products sold to this date.[/bold blue]"
                )
            else:
                print(
                    f"[bold blue]Deze producten zijn verkocht:\nThese products are sold:[/bold blue]\n{sold_selection.to_string(index=False)}"
                )
                print(
                    f"Gegevens zijn geëxporteerd naar sold.csv.\nData is exported to sold.csv."
                )
                return sold_selection.to_csv("sold.csv", index=False)
