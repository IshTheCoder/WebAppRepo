import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
from plotly.tools import mpl_to_plotly
from pie_chart import fig_to_uri

playtypes = ['cut', 'ho', 'iso', 'misc',
             'os', 'prb', 'prr', 'pu',
             'putback', 'su', 'tr']

playtype_shortcut = {'iso': 'Isolation', 'tr': 'Transition', 'prb': 'PRBallHandler',
                     'prr': 'PRRollMan', 'pu': 'Postup', 'su': 'Spotup',
                     'ho': 'Handoff', 'cut': 'Cut', 'os': 'Offscreen',
                     'putback': 'OffRebound', 'misc': 'Misc'}


def get_plot_data(aggr_data=None):
    """
    param: aggr_data, str, where the yearly aggregated data is
    param: outdir, str, folder to store output figures
    return: plot_data, dictionary = {year: data list of the year}
    """

    assert aggr_data, "Input directory is invalid."

    files = os.listdir(aggr_data)
    plot_data = defaultdict(list)
    for f in files:
        df = pd.read_csv(
            os.path.join(aggr_data, f)
        )
        year = "".join(
            [c for c in f if '0' <= c <= '9']
        )
        year = int(year)

        for col in playtypes:
            df[col + "_pts"] = df[col + "_ppp"] * df[col + "_poss"]
        df_sum = df.sum()
        for col in playtypes:
            plot_data[year].append(
                df_sum[col + "_pts"] / df_sum[col + "_poss"]
            )
    return plot_data


def plot_most_effi_figure(aggr_data, outdir=None):
    """
    param: aggr_data, str, where the yearly aggregated data is
    param: outdir, str, folder to store output figures
    return: save figures in the outdir
    """
    if outdir and not os.path.exists(outdir):
        os.mkdir(outdir)

    plot_data = get_plot_data(aggr_data)
    x = np.arange(11, dtype=np.float64)
    bar_width, start = 0.15, x
    colors = ["#823935", "#89BEB2", "#C9BA83", "#DED38C", "#DE9C53"]

    fig=plt.figure(figsize=(10, 5))
    for year in range(2015, 2020):
        plt.bar(
            start,
            plot_data[year],
            bar_width,
            color=colors[year - 2015],
            label=str(year)
        )
        start += bar_width

    plt.legend(loc="upper center")
    plt.xticks(
        x - 5.5 * bar_width / 2, [playtype_shortcut[x] for x in playtypes]
    )
    plt.xticks(rotation=45s)
    plt.ylabel("Efficiency / PPP")
    # plotly_fig = mpl_to_plotly(fig)
    uri = fig_to_uri(fig)
    return uri



# plot_most_effi_figure("data/data_cleaned/poss_ppp_data")