# Imports

import os
import pandas as pd
from matplotlib import pyplot as plt
from rich import print
from datetime import date

plt.rcParams["figure.figsize"] = [10, 6]


def plot_data(input):
    current_date = date.today()
    data = pd.read_csv("" + input + ".csv")
    df = pd.DataFrame(data)
    ax = df.plot(kind="bar", x="product_name", y="quantity")
    plt.xticks(rotation=0, horizontalalignment="center")
    plt.title(f"Voorraadoverzicht / Overview inventory {current_date}")
    plt.xlabel("Product")
    plt.ylabel("Aantal / Quantity")
    # Pdf bestand aanmaken / Create pdf file
    if not os.path.isfile("./" + input + ".pdf"):
        print(
            f"[bold blue]:writing_hand:  Bestand {input}.pdf wordt aangemaakt in huidige directory\n:writing_hand:  File {input}.pdf is created in current directory [/bold blue]"
        )
        ax.get_figure().savefig("./" + input + ".pdf", format="pdf")

    # Als pdf al bestaat: deze verwijderen en vervangen door nieuwe pdf / If .pdf file exists: remove existing file and replaced by new file
    elif os.path.isfile("./" + input + ".pdf"):
        os.remove("./" + input + ".pdf")
        print(
            f"[bold blue]:hourglass: Bestand {input}.pdf wordt geupdate\n:hourglass: File {input}.pdf is updated[bold blue]"
        )
        ax.get_figure().savefig("./" + input + ".pdf", format="pdf")
