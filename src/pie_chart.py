import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from io import BytesIO
import base64

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%".format(pct, absolute)

def fig_to_uri(in_fig, close_all=True, **save_args):
    # type: (plt.Figure) -> str
    """
    Save a figure as a URI
    :param in_fig:
    :return:
    """
    out_img = BytesIO()
    in_fig.savefig(out_img, format='png', **save_args)
    if close_all:
        in_fig.clf()
        plt.close('all')
    out_img.seek(0)  # rewind file
    encoded = base64.b64encode(out_img.read()).decode("ascii").replace("\n", "")
    return "data:image/png;base64,{}".format(encoded)

def draw_pie_chart(name, year):
    '''
    Function to draw the pie chart of players of different PlayType.
    Just input the player name and the year you want to know.
    :param name: Player name, string
    :param year: year
    :return:
    '''

    assert isinstance(name, str)
    assert 2015 <= year <= 2019
    path = "data/data_cleaned/pca_data/" + str(year) + "_pca_table.csv"
    df = pd.read_csv(path)
    new_df = df[df['PLAYER_NAME'] == name]
    data = new_df[["iso_freq", "tr_freq", "prb_freq", "prr_freq", "pu_freq", "su_freq", "ho_freq", "cut_freq", "os_freq",
                  "putback_freq", "misc_freq"]]
    data = data.values.tolist()
    data = np.array(data)[0]
    data = data / np.sum(data)
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    recipe = ["Isolation",
              "Transition",
              "PRBallHandler",
              "PRRollMan",
              "Postup",
              "Spotup",
              "Handoff",
              "Cut",
              "Offscreen",
              "OffRebound",
              "Misc"]
    ingredients = [x.split()[-1] for x in recipe]
    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                      textprops=dict(color="w"), shadow=False,
                                      colors=["cornflowerblue", "mediumseagreen", "gray", "salmon", "burlywood", "plum",
                                              "peru", "sandybrown", "teal", "darkkhaki", "pink"])
    ax.legend(wedges, ingredients,
              title="Freq of PlayTypes",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title(name + "  " + str(year))

    our_url= fig_to_uri(fig)
    return our_url
