
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
import section_3_grouped_bar_chart

import texts

import plotly.io as pio
pio.renderers.default = 'iframe'

import template


app = dash.Dash(__name__, assets_folder='assets')

server = app.server

app.config.suppress_callback_exceptions = True

app.title = 'AlayaCare'

dataframe = pd.read_csv('./assets/data/notes.csv')
dataframe2 = pd.read_csv('./assets/data/timeline_dataset.csv')

options = [{'label': name, 'value': name} for name in dataframe['PATIENT_ID'].unique()]


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
    html.Link(rel='stylesheet', href='/assets/style.css'),
    html.Header(className='header', children=[
        html.H1('AlayaCare'),
        html.H2("Relations entourant un patient et ses visites médicales")
    ]),
    html.Main(
        className='main', 
        children=[
            html.Aside(className='selecter', children=[
                html.Div(className='sideBarTitle', 
                                 children=[
                            html.P('Choix des patients: ')
                        ]),
                dcc.Checklist(
                    className='people-checkbox',
                    id='people-checkbox',
                    options=options,
                    value=[name for name in dataframe['PATIENT_ID'].unique()]
                )
            ]),
            html.Div(className='tabs', children=[
            dcc.Tabs(
                className='tabs-container',
                content_style={
                    'align-self': 'center',                    
                    'padding': '20px',
                    'justify-content': 'center',
                    'margin-top': '20px',
                },
                children = [
                    dcc.Tab(label='Accueil',
                            selected_className='tab-selected', 
                            children=[
                        html.Div(className='text', 
                                 children=[
                            html.P(texts.HOME_DESCRIPTION,
                                   style={
                                    'font-size': '17px',
                                    'text-align': 'justify',
                                    'white-space': 'pre-wrap',
                            })
                        ],
                        style={
                            'margin-top': '5%',
                            'display': 'flex',
                            'align-content': 'center',
                        }),
                ]),
                dcc.Tab(label='Douleur et visites',
                    selected_className='tab-selected',
                    children=[
                        html.Div(className='text', 
                            children=[
                                html.P(className='sectionHeader', children=[texts.SECTION_1_BUBBLE_CHART_HEADER])
                            ]),
                        html.Div([        
                            html.P(className='sectionDescription', children=[texts.SECTION_1_BUBBLE_CHART_DESCRIPTION]),
                            dcc.Graph(
                                id='bubble_chart_section_1',
                                className='graph',
                                figure=section_1_bubble_chart.get_figure(dataBubbleChart1),
                                config=dict(
                                    scrollZoom=False,
                                    showTips=False,
                                    showAxisDragHandles=False,
                                    doubleClick=False,
                                    displayModeBar=False
                                )
                            )],
                            style={
                                'display': 'flex'
                            })
                ]),
                dcc.Tab(label='Complétion des activités', 
                        selected_className='tab-selected',
                        children=[
                            html.Div(className='text',
                                children=[
                                    html.P(className='sectionHeader', children=[texts.SECTION_1_2_HEATMAP_1_HEADER])
                            ]),
                            html.Div([
                                html.P(className='sectionDescription', children=[texts.SECTION_1_BUBBLE_CHART_DESCRIPTION]),
                                dcc.Graph(
                                    id='heatmap_section_1',
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
                                        width='1100px'
                                    )
                                )
                            ],
                            style={
                                'display': 'flex',
                                'margin-left': '6%'
                            }),
                ])
                ,
                dcc.Tab(label='Notes et hospitalisations', 
                        selected_className='tab-selected',
                        children=[
                    html.Div(className='text', 
                             children=[
                        html.P(className='sectionHeader', children=[texts.SECTION_2_GROUPED_BAR_HEADER])
                    ]),
                    html.Div([
                        html.P(className='sectionDescription', children=[texts.SECTION_2_GROUPED_BAR_1_DESCRIPTION]),
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
                        )
                    ],
                    style={
                        'display': 'flex',
                        'margin-left': '6%'
                    }),
                    html.Div([
                        html.P(className='sectionDescription', children=[texts.SECTION_2_GROUPED_BAR_2_DESCRIPTION]),
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
                    ],
                    style={
                        'display': 'flex',
                        'margin-left': '6%'
                    }),
                ])
                ,
                dcc.Tab(label='Chutes et hospitalisations', 
                        selected_className='tab-selected',
                        children=[
                        html.Div(className='text', 
                             children=[
                                html.P(className='sectionHeader', children=[texts.SECTION_2_UNIVARIATE_SCATTER_PLOT_HEADER])
                        ]),
                        html.Div([
                            html.P(className='sectionDescription', children=[texts.SECTION_2_UNIVARIATE_SCATTER_PLOT_DESCRIPTION]),
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
                            ),
                        ],
                        style={
                            'display': 'flex',
                            'margin-left': '6%'
                        }),
                ]),
                dcc.Tab(label='Annulation de visites', children=[
                    html.Div([
                        html.P(className='sectionHeader', id='section3', children=[texts.SECTION_3_GROUPED_BAR_HEADER])
                    ]),
                    html.Div([
                        html.P(className='sectionDescription', children=[texts.SECTION_3_GROUPED_BAR_1_DESCRIPTION]),
                        dcc.Graph(
                            id='grouped_bar_chart_section_3_1',
                            className='graph',
                            figure=section_3_grouped_bar_chart.get_figure_1(dataUnivariateChart1),
                            config=dict(
                                scrollZoom=False,
                                showTips=False,
                                showAxisDragHandles=False,
                                doubleClick=False,
                                displayModeBar=False
                            ),
                            style=dict(
                                height='500px',
                                width='850px'
                            )
                        ),
                    ],
                    style={
                        'display': 'flex',
                        'margin-left': '8%'
                    }),
                    html.Div([
                        html.P(className='sectionDescription', children=[texts.SECTION_3_GROUPED_BAR_2_DESCRIPTION]),                        
                        dcc.Graph(
                            id='grouped_bar_chart_section_3_2',
                            className='graph',
                            figure=section_3_grouped_bar_chart.get_figure_2(dataUnivariateChart2),
                            config=dict(
                                scrollZoom=False,
                                showTips=False,
                                showAxisDragHandles=False,
                                doubleClick=False,
                                displayModeBar=False
                            ),
                            style=dict(
                                height='500px',
                                width='850px'
                            )
                        )
                    ],
                    style={
                        'display': 'flex',
                        'margin-left': '8%'
                    })
                ]),
            ])
        ])
    ])
])

@app.callback(
    Output('bubble_chart_section_1', 'figure'),
    Output('heatmap_section_1', 'figure'),
    Output('grouped_bar_chart_1_section_2', 'figure'),
    Output('grouped_bar_chart_2_section_2', 'figure'),
    Output('univariate_scatter_plot_section_2', 'figure'),
    Output('grouped_bar_chart_section_3_1', 'figure'),
    Output('grouped_bar_chart_section_3_2', 'figure'), # Add the output component with different ids
    Input('people-checkbox', 'value')
)
def update_graph(people):
    # Filter the dataset based on the selected people
    df_filtered = dataframe2[dataframe2['PATIENT_ID'].isin(people)]
    
    dataFrameGroupedBarChart1 = preprocess.getGroupedBarHospitalizationCount(df_filtered)
    dataFrameGroupedBarChart2 = preprocess.getGroupedBarFallCount(df_filtered)

    dataBubbleChart1 = preprocess.getPainDetailsRelation(df_filtered)
    dataHeatmapChart1 = preprocess.getAdlCompletionTimeline(df_filtered)

    dataUnivariateChart = preprocess.getFallsAndHospitalizationTimeline(df_filtered)

    dataUnivariateChart1 = preprocess.getCancellationAndPainRelation(df_filtered)
    dataUnivariateChart2 = preprocess.getCancellationAndAdlRelation(df_filtered) 
    
    return [section_1_bubble_chart.get_figure(dataBubbleChart1),
           section_1_heatmap.get_figure(dataHeatmapChart1),
           section_2_grouped_bar_chart.get_figure_hospitalization(dataFrameGroupedBarChart1),
           section_2_grouped_bar_chart.get_figure_falls(dataFrameGroupedBarChart2),
           section_2_univariate_scatter_plot.get_figure(dataUnivariateChart),
           section_3_grouped_bar_chart.get_figure_1(dataUnivariateChart1),
           section_3_grouped_bar_chart.get_figure_2(dataUnivariateChart2)]
    
if __name__ == '__main__':
    app.run_server(debug=True)