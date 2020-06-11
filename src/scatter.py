import pandas as pd
import plotly.graph_objs as go

flist = ['data/data_cleaned/poss_ppp_data/poss2015.csv', 'data/data_cleaned/poss_ppp_data/poss2016.csv', 'data/data_cleaned/poss_ppp_data/poss2017.csv',
             'data/data_cleaned/poss_ppp_data/poss2018.csv', 'data/data_cleaned/poss_ppp_data/poss2019.csv']
def scatter_plot_in(fname):
    '''
    Function that outputs total poss, ppp, and name of each player through 3 lists
    fname is expected directory path
    fname must use data in ./poss_ppp_data

    '''
    pt_abrv = ['iso', 'tr', 'prb', 'prr', 'pu', 'su', 'ho', 'cut', 'os', 'putback', 'misc']
    df = pd.read_csv(fname)
    df_calc = pd.DataFrame()
    for i in pt_abrv:
        df_poss = df[i + '_poss']
        df_ppp = df[i + '_ppp']
        df_points = df_ppp * df_poss
        df_calc[i + '_points'] = df_points
    ppp = df_calc.sum(axis=1) / df['total_poss']
    return df['total_poss'].tolist(), ppp.tolist(), df['PLAYER_NAME'].tolist()


def create_slider_scatter(fname_list, title_graph, yaxis_label, x_axis_label):
        """
        get xy should take in the list of filenames for each year and output the x values, i.e. total possessions for the year vs total PPP.
        PPP should be weighted according to the number of possessions right, like a players season PPP, is PPP_i * Poss_i, where i is the playtype
        """
        fig = go.Figure()
        colorscale_curr = [[0.0, "rgb(165,0,38)"], [0.1111111111111111, "rgb(215,48,39)"],
                           [0.2222222222222222, "rgb(244,109,67)"], [0.3333333333333333, "rgb(253,174,97)"],
                           [0.4444444444444444, "rgb(254,224,144)"], [0.5555555555555556, "rgb(224,243,248)"],
                           [0.6666666666666666, "rgb(171,217,233)"], [0.7777777777777778, "rgb(116,173,209)"],
                           [0.8888888888888888, "rgb(69,117,180)"], [1.0, "rgb(49,54,149)"]]
        colorscale_curr.reverse()
        # just going to use global variable list of path strings;
        for i in range(len(flist)):
            x_1, y_1, names = scatter_plot_in(flist[i])
            fig.add_trace(
                go.Scatter(x=x_1, y=y_1, text=names, hoverinfo='text', mode='markers',
                           marker=dict(color=y_1, colorscale=colorscale_curr, size=12,
                                       line=dict(width=2, color='DarkSlateGrey')), visible=False,
                           name="Points Per Possession vs Possessions " + str(i)
                           ))
        fig.data[0].visible = True
        steps = []
        for i in range(len(fig.data)):
            step = dict(
                method="restyle",
                args=["visible", [False] * len(fig.data)],
                label='Year ' + str(i + 2015)

            )
            step["args"][1][i] = True  # Toggle i'th trace to "visible"
            steps.append(step)

        sliders = [dict(
            active=5,
            currentvalue={"prefix": "Year: "},
            pad={"t": 5},
            steps=steps
        )]
        start_index = 2015
        fig.update_layout(
            sliders=sliders,
            # title = "9 Cluster classification of players based on Scoring Styles"
            title={"text": title_graph},
            xaxis_title=x_axis_label,
            yaxis_title=yaxis_label,
        )
        return fig