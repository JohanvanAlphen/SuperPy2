# Imports

import pandas as pd
import os
from rich import print
from date import handle_date

pd.options.mode.chained_assignment = None  # default='warn'


# ---VERKOPEN PRODUCT EN EVT AANMAKEN CSV BESTAND / SELL PRODUCT AND IF NEEDED CREATE CSV FILE---

def sell_product(id, product_name, sell_price, sell_date, quantity):
    # Controleren of bestand al bestaat en anders aanmaken / Check if file exists and if not create the file
    if not os.path.isfile("sold.csv"):
        sold = pd.DataFrame(
            columns=[
                "product_id",
                "product_name",
                "sell_price",
                "sell_date",
                "quantity",
            ]
        )
        create_column = {
            "product_id": id,
            "product_name": product_name,
            "sell_price": sell_price,
            "sell_date": sell_date,
            "quantity": quantity,
        }
        sold = sold.append(create_column, ignore_index=True)
        print(
            f"[bold green]:thumbs_up: Product {product_name} is toegevoegd aan sold.csv bestand\n:thumbs_up: Product {product_name} added to sold.csv file[/bold green]")
        return sold.to_csv("sold.csv", index=False)
    elif os.path.isfile("sold.csv"):
        sold = pd.read_csv("sold.csv")
        create_column = {
            "product_id": id,
            "product_name": product_name,
            "sell_price": sell_price,
            "sell_date": sell_date,
            "quantity": quantity,
        }
        sold = sold.append(create_column, ignore_index=True)
        print(
            f"[bold green]:thumbs_up: Product {product_name} is toegevoegd aan sold.csv bestand\n:thumbs_up: Product {product_name} added to sold.csv file[/bold green]")
        return sold.to_csv("sold.csv", index=False)

# ---HAAL PRODUCT VAN DE VOORRAAD AF / REMOVE PRODUCT FROM INVENTORY---


def add_sell_product_to_inventory(product_name, sell_price, sell_date, quantity):
    # Controleren of juiste datum format wordt gehanteerd / heck if correct date format is used
    if not handle_date(sell_date):
        print(
            f"[bold red]:thumbs_down: Het datatype voor parameter buy_date is niet juist. Dit moet een string zijn: YYYY-MM-DD\n:thumbs_down: The data type for parameter buy_date is incorrect. This should be a string: YYYY-MM-DD[/bold red]"
        )
        return
    # Controleren of bestand al bestaat / Check if file exists
    if not os.path.isfile("inventory.csv"):
        print(
            f"[bold red]:thumbs_down: Er is momenteel geen voorraad van dit product\n:thumbs_down: At the moment there is no inventory of this product"
        )
    # Controleren of product_name al bestaat en of er genoeg voorraad is / Check if product_name exists and if there is enough stock in inventory
    elif os.path.isfile("inventory.csv"):
        inventory = pd.read_csv("inventory.csv")
        inventory["quantity"] = pd.to_numeric(inventory["quantity"])
        product_exists = (
            (inventory["product_name"] == product_name)
            & (inventory["quantity"] >= quantity)
        ).any()
        if not product_exists:
            print(
                f"[bold red]Er is van {product_name}niet genoeg in voorraad!\nThere is not enough in stock of {product_name}"
            )
        elif product_exists:
            product_index = inventory[
                (
                    (inventory["product_name"] == product_name)
                    & (inventory["quantity"] >= quantity)
                )
            ].index.tolist()
            # FIFO
            product_index = product_index[0]
            # Controleren of product over de datum is / check if product is expired
            if pd.to_datetime(
                inventory["expiration_date"].iloc[product_index], format="%Y-%m-%d"
            ) < pd.to_datetime(sell_date, format="%Y-%m-%d"):
                print(
                    f"[bold red]:prohibited: Het product is al over de uiterste verkoopdatum\n:prohibited: The product is already past its sell-by date"
                )
            # Als alles goed is kan product worden verkocht / If everything is okay product can be sold
            else:
                id = inventory["product_id"].iloc[product_index]
                sell_product(id, product_name, sell_price, sell_date, quantity)
                new_quantity = int(inventory["quantity"].iloc[product_index]) - int(
                    quantity
                )
                if new_quantity == 0:
                    inventory = inventory.drop(
                        inventory.index[product_index])
                    print(
                        f"Nieuwe voorraad: {inventory.to_string(index=False)}\nUpdated inventory: {inventory.to_string(index=False)}"
                    )
                    return inventory.to_csv("inventory.csv", index=False)
                else:
                    inventory["quantity"].iloc[product_index] = new_quantity
                    print(
                        f"Nieuwe voorraad: {inventory.to_string(index=False)}\nUpdated inventory: {inventory.to_string(index=False)}"
                    )
                    return inventory.to_csv("inventory.csv", index=False)
