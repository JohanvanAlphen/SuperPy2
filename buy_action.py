# Imports

import pandas as pd
import os
from rich import print
from date import handle_date

pd.options.mode.chained_assignment = None  # default='warn'

# ---TOEVOEGEN PRODUCT EN EVT AANMAKEN CSV BESTAND / ADD PRODUCT AND IF NEEDED CREATE CSV FILE---


def buy_product(id, product_name, buy_price, buy_date, quantity, expiration_date):
    # Controleren of bestand al bestaat en anders aanmaken / Check if file exists and if not create the file
    if not os.path.isfile("bought.csv"):
        bought = pd.DataFrame(
            columns=[
                "product_id",
                "product_name",
                "buy_price",
                "buy_date",
                "quantity",
                "expiration_date",
            ]
        )
        create_column = {
            "product_id": id,
            "product_name": product_name,
            "buy_price": buy_price,
            "buy_date": buy_date,
            "quantity": quantity,
            "expiration_date": expiration_date,
        }
        bought = bought.append(create_column, ignore_index=True)
        print(
            f"[bold green]:thumbs_up: Product {product_name} is toegevoegd aan bought.csv bestand\n:thumbs_up: Product {product_name} added to bought.csv file[/bold green]")
        return bought.to_csv("bought.csv", index=False)
    elif os.path.isfile("bought.csv"):
        bought = pd.read_csv("bought.csv")
        create_column = {
            "product_id": id,
            "product_name": product_name,
            "buy_price": buy_price,
            "buy_date": buy_date,
            "quantity": quantity,
            "expiration_date": expiration_date,
        }
        bought = bought.append(create_column, ignore_index=True)
        print(
            f"[bold green]:thumbs_up: Product {product_name} is toegevoegd aan bought.csv bestand\n:thumbs_up: Product {product_name} added to bought.csv file[/bold green]")
        return bought.to_csv("bought.csv", index=False)


# ---VOEG PRODUCT TOE AAN DE VOORRAAD / ADD PRODUCT TO INVENTORY---


def add_buy_product_to_inventory(id, product_name, buy_price, quantity, buy_date, expiration_date):
    # Controleren of juiste datum format wordt gehanteerd / heck if correct date format is used
    if (handle_date(expiration_date) == False) | (handle_date(buy_date) == False):
        print(
            f"[bold red]:thumbs_down: Het datatype voor parameter buy_date is niet juist. Dit moet een string zijn: YYYY-MM-DD\n:thumbs_down: The data type for parameter buy_date is incorrect. This should be a string: YYYY-MM-DD[/bold red]"
        )
        return
    # Controleren of bestand al bestaat en anders aanmaken / Check if file exists and if not create the file
    if not os.path.isfile("inventory.csv"):
        inventory = pd.DataFrame(
            columns=[
                "product_id",
                "product_name",
                "quantity",
                "expiration_date",
            ]
        )
        count_column = inventory.shape[0]
        id = count_column + 1
        create_column = {
            "product_id": id,
            "product_name": product_name,
            "quantity": quantity,
            "expiration_date": expiration_date,
        }
        inventory = inventory.append(create_column, ignore_index=True)
        print(
            f"[bold green]:thumbs_up: Product {product_name} is toegevoegd aan de voorraad:\n:thumbs_up: Product {product_name} added to inventory:[/bold green]")
        print(
            f"{inventory.to_string(index=False)}"
        )

        buy_product(id, product_name, buy_price,
                    buy_date, quantity, expiration_date)
        return inventory.to_csv("inventory.csv", index=False)
    # Indien bestand al bestaat controleren of product_name en expriration_date al voorkomen / If file exist check if product_name and expiration_date are in file
    elif os.path.isfile("inventory.csv"):
        inventory = pd.read_csv("inventory.csv")
        product_exists = (
            (inventory["product_name"] == product_name)
            & ((inventory["expiration_date"] == expiration_date))
        ).any()
        if not product_exists:
            count_column = inventory.shape[0]
            id = count_column + 1
            create_column = {
                "product_id": id,
                "product_name": product_name,
                "quantity": quantity,
                "expiration_date": expiration_date,
            }
            inventory = inventory.append(create_column, ignore_index=True)
            print(
                f"[bold green]:thumbs_up: Product {product_name} is toegevoegd aan de voorraad.\n:thumbs_up: Product {product_name} added to inventory.[/bold green]")
            print(
                f"Nieuwe voorraad: {inventory.to_string(index=False)}\nUpdated inventory: {inventory.to_string(index=False)}"
            )
            buy_product(id, product_name, buy_price,
                        buy_date, quantity, expiration_date)
            return inventory.to_csv("inventory.csv", index=False)
        elif product_exists:
            product_index = inventory[
                (
                    (inventory["product_name"] == product_name)
                    & ((inventory["expiration_date"] == expiration_date))
                )
            ].index.tolist()
            product_index = product_index[0]
            id = int(inventory["product_id"].iloc[product_index])
            current_quantity = inventory["quantity"].iloc[product_index]
            new_quantity = int(current_quantity) + int(quantity)
            inventory["quantity"].iloc[product_index] = new_quantity
            print(
                f"{product_name} is al op voorraad, aantal is verhoogd en is nu {new_quantity}.\n{product_name} is already in invetory, quantity is update to {new_quantity}"
            )
            print(
                f"Nieuwe voorraad: {inventory.to_string(index=False)}\nUpdated inventory: {inventory.to_string(index=False)}"
            )
            buy_product(id, product_name, buy_price,
                        buy_date, quantity, expiration_date)
            return inventory.to_csv("inventory.csv", index=False)
