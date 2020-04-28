import csv
import datetime
import glob
import logging
import os

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import plot

logger = logging.getLogger(__name__)


def plot_resources_drifted():

    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, 'data', 'resources_drifted.csv')

    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = np.array(list(reader))

    x = data[:, 0]
    fig = go.Figure()
    for i, _ in enumerate(headers):
        if i > 0:
            fig.add_trace(go.Bar(x=x, y=data[:, i], name=headers[i]))

    fig.update_layout(
        title_text="Resources Drifted",
        barmode='stack',
        xaxis={'categoryorder': 'category ascending'},
        height=800)


    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                        label="1d",
                        step="day",
                        stepmode="backward"),
                    dict(count=7,
                        label="7d",
                        step="day",
                        stepmode="backward"),
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                    dict(count=1,
                        label="1y",
                        step="year",
                        stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )

    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def plot_new_rule_violations():
    pass


def plot_new_rule_violations_burn_down():
    pass
