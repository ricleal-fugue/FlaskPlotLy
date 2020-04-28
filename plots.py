import csv
import datetime
import glob
import logging
import os

import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objs as go
from plotly.offline import plot

logger = logging.getLogger(__name__)


def _get_data(path):
    ''' return headers, data '''

    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, 'data', path)

    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = np.array(list(reader))

    return headers, data


def plot_resources_drifted():

    headers, data = _get_data('resources_drifted.csv')

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

    headers, data = _get_data('new_rule_violations.csv')

    # Make the DS smaller
    data = data[-30:]

    x = data[:, 0]
    fig = go.Figure()
    for i, _ in enumerate(headers):
        if i > 0:
            fig.add_trace(go.Bar(x=x, y=data[:, i], text=data[:, i],
                                 textposition='auto'))

    fig.update_layout(
        title_text="New Rule Violations",
        height=800)

    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


def plot_new_rule_violations_burn_down():
    headers, data = _get_data('rule_violations_burn_down.csv')

    # Make the DS witgout the temp column
    data = data[:, :2]
    headers = headers[:2]

    x = data[:, 0]
    fig = go.Figure()
    for i, _ in enumerate(headers):
        if i > 0:
            fig.add_trace(go.Scatter(
                x=x, y=data[:, i],  mode='lines+markers', name=headers[i]))

    fig.update_layout(
        title_text="New Rule Violations",
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


def plot_compliance_summary():

    headers, data = _get_data('compliance_summary.csv')

    data_to_plot = data[:-1, 1:].astype(float)
    maximums = data[-1, 1:].astype(float)

    data_to_plot_relative = data_to_plot / maximums * 100

    # fig = go.Figure(
    #     data=go.Heatmap(
    #         z=data_to_plot_relative,
    #         x=headers[1:],
    #         y=data[:-1, 0],
    #         colorscale = 'RdYlGn',
    #     ),
    # )
    outer = []
    for row in data[:-1, 1:]:
        inner = []
        for elem, max in zip(row, maximums):
            inner.append("{}/{}".format(elem, int(max)))
        outer.append(inner)

    fig = ff.create_annotated_heatmap(
        data_to_plot_relative.tolist(),
        x=headers[1:],
        y=data[:-1, 0].tolist(),
        annotation_text=outer,
        colorscale='RdYlGn',
        showscale=True,
        colorbar=dict(title="%")
    )

    fig.update_layout(
        title_text="Compliance Summary Report - All Environments",
        height=800)

    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div
