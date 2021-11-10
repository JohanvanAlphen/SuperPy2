# Imports

import argparse
from arg_action import args_action
from date import create_date_txt

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.


def main():
    # begin met het eerste niveau van de parser / start with the first level of the parser
    parser = argparse.ArgumentParser(
        prog="main.py", description="Voorraad check / Inventory check"
    )
    subparsers = parser.add_subparsers(
        help="Welke actie / Type of action", dest="command")
    subparsers.required = True

    # creëer de koop-parser / create the buy-parser:
    buy_parser = subparsers.add_parser(
        "buy", help="Voeg product toe aan de voorraad / Add product to inventory")
    buy_parser.add_argument(
        "--product-name",
        dest="product_name",
        type=str,
        help="Productnaam toevoegen / Insert product name",
        required=True
    )
    buy_parser.add_argument(
        "--buy-price",
        type=float,
        dest="buy_price",
        help="Voeg inkoopprijs toe / Insert buying price",
        required=True,
    )
    buy_parser.add_argument(
        "--quantity",
        type=int,
        dest="quantity",
        help="Voeg aantal toe / Insert quantity",
        default=1,
    )
    buy_parser.add_argument(
        "--buy-date",
        type=str,
        dest="buy_date",
        help="Voeg datum van koop toe / Insert date of purchase: format YYYY-MM-DD",
        required=True,
    )
    buy_parser.add_argument(
        "--expiration-date",
        type=str,
        dest="expiration_date",
        help="Voeg vervaldatum toe / Insert expire date: YYYY-MM-DD",
        required=True,
    )

    # creëer de verkoop-parser / create the sell parser:
    sell_parser = subparsers.add_parser(
        "sell", help="Verkoop product / Sell product")
    sell_parser.add_argument(
        "--product-name",
        type=str,
        dest="product_name",
        help="Productnaam toevoegen / Insert product name",
        required=True
    )
    sell_parser.add_argument(
        "--sell-price",
        type=float,
        dest="sell_price",
        help="Voeg verkoopprijs toe / Insert selling price",
        required=True,
    )
    sell_parser.add_argument(
        "--quantity",
        type=int,
        dest="quantity",
        help="Voeg aantal toe / Insert quantity",
        default=1,
    )

    sell_parser.add_argument(
        "--sell-date",
        type=str,
        dest="sell_date",
        help="Voeg datum van verkoop toe / Insert date of sale: format YYYY-MM-DD",
        required=True,
    )

    # creëer de rapport-parser / create the report parser:
    profit_parser = subparsers.add_parser(
        "profit",
        help="Rapporteer opbrengst van specifieke datum / Report revenue specific date",
    )
    profit_parser.add_argument(
        "--date",
        type=str,
        dest="date",
        help="Kies de gewenste datum / Choose date of interest(format YYYY-MM-DD)",
        required=True,
    )

    # creëer de exporteer-parser / create the export parser:
    export_parser = subparsers.add_parser(
        "export",
        help="Exporteer uw voorraad / Export your inventory",
    )
    export_parser.add_argument(
        "--file",
        type=str,
        dest="file",
        help="Exporteert voorraad naar .csv file / Exports the inventory to a .csv file",
        choices=["expired", "bought", "sold"],
        required=True,
    )
    export_parser.add_argument(
        "--date",
        type=str,
        dest="date",
        help="Kies de gewenste datum / Choose date of interest(format YYYY-MM-DD)",
        required=True,
    )

    # creëer de pdf-parser / create the pdf parser:
    plot_parser = subparsers.add_parser(
        "plot",
        help="Maak een staafdiagram van producten in de inventaris, gekochte of verkochte lijst / Plot bar graph of products in inventory, bought or sold list",
    )
    plot_parser.add_argument(
        "--file",
        type=str,
        dest="file",
        help="Bestand dat moet worden uitgezet / File to be plotted",
        choices=["bought", "sold", "inventory"],
        required=True,
    )

    # creëer de remove-parser / create remove parser:
    remove_parser = subparsers.add_parser(
        "remove",
        help="Verwijder bestanden of alle bestanden / Remove file or all files",
    )
    remove_parser.add_argument(
        "--file",
        type=str,
        dest="file",
        help="Bestanden die moeten worden verwijderd / Files to be removed",
        choices=["bought", "sold", "inventory", "all"],
        default="all",
    )

    args = parser.parse_args()
    return args_action(args)


if __name__ == "__main__":
    main()
    create_date_txt()
