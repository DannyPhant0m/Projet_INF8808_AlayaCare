
# -*- coding: utf-8 -*-

'''
    File name: app.py
    Author: Équipe 14
    Course: INF8808
    Python Version: 3.8

    This file is the entry point for our dash app.
'''

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import pandas as pd

import preprocess
import heatmap_section_1
import bubble_chart_section_1
import grouped_bar_chart_section_2
import univariate_scatter_plot_section_2
import univariate_scatter_plot_section_3
import template


app = dash.Dash(__name__)
app.title = 'AlayaCare...'

dataframe = pd.read_csv('./assets/data/notes.csv')
dataframe2 = pd.read_csv('./assets/data/timeline_dataset.csv')

# we also need to add the second data frame
#the next is all not working yet

dataframe = preprocess.convert_dates(dataframe)
dataframe = preprocess.filter_years(dataframe, 2010, 2020)
yearly_df = preprocess.summarize_yearly_counts(dataframe)
data = preprocess.restructure_df(yearly_df)

template.create_custom_theme()
template.set_default_theme()

app.layout = html.Div(className='content', children=[
    html.Header(children=[
        html.H1('AlayaCare'),
        html.H2('Fun test')
    ]),
    html.Main(className='viz-container', children=[
        dcc.Graph(
            id='heatmap_section_1',
            className='graph',
            figure=heatmap_section_1.get_figure(data),
            config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
            )
        )
        ,
        dcc.Graph(
            id='bubble_chart_section_1',
            className='graph',
            figure=bubble_chart_section_1.get_figure(),
            config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
            )
        )
        ,
        dcc.Graph(
            id='grouped_bar_chart_section_2',
            className='graph',
            figure=grouped_bar_chart_section_2.get_figure(),
            config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
            )
        )
        ,
        dcc.Graph(
            id='univariate_scatter_plot_section_2',
            className='graph',
            figure=univariate_scatter_plot_section_2.get_figure(),
            config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
            )
        )
        ,
        dcc.Graph(
            id='univariate_scatter_plot_section_3',
            className='graph',
            figure=univariate_scatter_plot_section_3.get_figure(),
            config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
            )
        )
        ,
    ])
])