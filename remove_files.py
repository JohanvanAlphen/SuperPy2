# Imports

import os
from rich import print


def remove_files(input):
    create_print = f"[bold]:cross_mark: Het {input}-bestand is verwijderd.\n:cross_mark: The {input}-file has been removed.[/bold]"
    create_print_all = f"[bold]:cross_mark: Alle bestanden zijn verwijderd.\n:cross_mark: All files have been removed.[/bold]"
    if input == "bought":
        if os.path.isfile("./bought.csv"):
            os.remove("./bought.csv")
            print(
                create_print
            )
        if os.path.isfile("./bought.pdf"):
            os.remove("./bought.pdf")
            print(
                create_print
            )
    elif input == "sold":
        if os.path.isfile("./sold.csv"):
            os.remove("./sold.csv")
            print(
                create_print
            )
        if os.path.isfile("./sold.pdf"):
            os.remove("./sold.pdf")
            print(
                create_print
            )
    elif input == "inventory":
        if os.path.isfile("./inventory.csv"):
            os.remove("./inventory.csv")
            print(
                create_print
            )
        if os.path.isfile("./inventory.pdf"):
            os.remove("./inventory.pdf")
            print(
                create_print
            )
    else:
        if os.path.isfile("./bought.csv"):
            os.remove("./bought.csv")
        if os.path.isfile("./bought.pdf"):
            os.remove("./bought.pdf")

        if os.path.isfile("./sold.csv"):
            os.remove("./sold.csv")
        if os.path.isfile("./sold.pdf"):
            os.remove("./sold.pdf")

        if os.path.isfile("./inventory.csv"):
            os.remove("./inventory.csv")
        if os.path.isfile("./inventory.pdf"):
            os.remove("./inventory.pdf")

        if os.path.isfile("./expired.csv"):
            os.remove("./expired.csv")

        print(
            create_print_all
        )
