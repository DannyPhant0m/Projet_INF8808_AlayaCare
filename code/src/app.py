
# -*- coding: utf-8 -*-

'''
    File name: app.py
    Author: Équipe 14
    Course: INF8808
    Python Version: 3.8

    This file is the entry point for our dash app.
'''

import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

import pandas as pd

import preprocess
import section_1_heatmap
import section_1_bubble_chart
import section_2_grouped_bar_chart
import section_2_univariate_scatter_plot
import section_3_univariate_scatter_plot
import template


app = dash.Dash(__name__)
app.title = 'AlayaCare'

dataframe = pd.read_csv('./assets/data/notes.csv')
dataframe2 = pd.read_csv('./assets/data/timeline_dataset.csv')


dataFrameGroupedBarChart1 = preprocess.getGroupedBarHospitalizationCount(dataframe2)
dataFrameGroupedBarChart2 = preprocess.getGroupedBarFallCount(dataframe2)

dataBubbleChart1 = preprocess.getPainDetailsRelation(dataframe2)
dataHeatmapChart1 = preprocess.getAdlCompletionTimeline(dataframe2)

dataUnivariateChart = preprocess.getFallsAndHospitalizationTimeline(dataframe2)

dataUnivariateChart1 = preprocess.getCancellationAndPainRelation(dataframe2)
dataUnivariateChart2 = preprocess.getCancellationAndAdlRelation(dataframe2) 

# We need to add template

# template.create_custom_theme()
# template.set_default_theme()

app.layout = html.Div(className='content', children=[
    html.Header(children=[
        html.H1('AlayaCare'),
        html.H2("Relations entourant un patient et ses visites médicales")
    ]),
    html.Main(
        className='viz-container', 
        style={ 
            'display': 'table',
        }, 
        children=[
            dcc.Tabs(
                style={
                    'height': '100%',
                    'width': '100%',
                    'display': 'flex',
                    'justifyContent': 'flex-start',
                    'alignItems': 'center',
                }, 
                content_style={
                    'display': 'flex',
                    'padding': '20px',
                    'justify-content': 'center'
                },
                children = [
                dcc.Tab(label='Douleur et visites', children=[
                    dcc.Graph(
                        id='heatmap_section_1',
                        className='graph',
                        figure=section_1_bubble_chart.get_figure(dataBubbleChart1),
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False
                        ),
                        style=dict(
                            height='500px',
                        )
                    )
                ]),
                dcc.Tab(label='Progression du niveau de complétion', children=[
                    dcc.Graph(
                        id='bubble_chart_section_1',
                        className='graph',
                        figure=section_1_heatmap.get_figure(dataHeatmapChart1),
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False
                        ),
                        style=dict(
                            height='500px',
                            width='1300px'
                        )
                    )
                ])
                ,
                dcc.Tab(label='Notes et hospitalisations', children=[
                    dcc.Graph(
                        id='grouped_bar_chart_1_section_2',
                        className='graph',
                        figure=section_2_grouped_bar_chart.get_figure_hospitalization(dataFrameGroupedBarChart1),
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False
                        ),
                        style=dict(
                            height='500px',
                            width='800px'
                        )
                    ),
                    dcc.Graph(
                        id='grouped_bar_chart_2_section_2',
                        className='graph',
                        figure=section_2_grouped_bar_chart.get_figure_falls(dataFrameGroupedBarChart2),
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False
                        ),
                        style=dict(
                            height='500px',
                            width='800px'
                        )
                    )
                ])
                ,
                dcc.Tab(label='Chutes et hospitalisations', children=[
                    dcc.Graph(
                        id='univariate_scatter_plot_section_2',
                        className='graph',
                        figure=section_2_univariate_scatter_plot.get_figure(dataUnivariateChart),
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False
                        )
                    )
                ])
                ,
                dcc.Tab(label='Annulation de visites', children=[
                    dcc.Graph(
                        id='univariate_scatter_plot_section_3_1',
                        className='graph',
                        figure=section_3_univariate_scatter_plot.get_figure_1(dataUnivariateChart1),
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False
                        ),
                        style=dict(
                            height='500px',
                            width='800px'
                        )
                    ),
                    dcc.Graph(
                        id='univariate_scatter_plot_section_3_2',
                        className='graph',
                        figure=section_3_univariate_scatter_plot.get_figure_2(dataUnivariateChart2),
                        config=dict(
                            scrollZoom=False,
                            showTips=False,
                            showAxisDragHandles=False,
                            doubleClick=False,
                            displayModeBar=False
                        ),
                        style=dict(
                            height='500px',
                            width='800px'
                        )
                    )
                ])
                ,
            ])
    ])
])
