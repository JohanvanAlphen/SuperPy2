# Imports

from export import export
from buy_action import add_buy_product_to_inventory
from sell_action import add_sell_product_to_inventory
from calculate_profit import calculate_profit
from plot_data import plot_data
from remove_files import remove_files


def args_action(args):
    if args.command == "buy":
        add_buy_product_to_inventory(
            id=id,
            product_name=args.product_name,
            quantity=args.quantity,
            buy_price=args.buy_price,
            buy_date=args.buy_date,
            expiration_date=args.expiration_date,
        )
    elif args.command == "sell":
        add_sell_product_to_inventory(
            product_name=args.product_name,
            sell_price=args.sell_price,
            quantity=args.quantity,
            sell_date=args.sell_date,
        )
    elif args.command == "export":
        export(selection=args.file, date=args.date)
    elif args.command == "profit":
        calculate_profit(args.date)
    elif args.command == "plot":
        plot_data(args.file)
    elif args.command == "remove":
        remove_files(args.file)
