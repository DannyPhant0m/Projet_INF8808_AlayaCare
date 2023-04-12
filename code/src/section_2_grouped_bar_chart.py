'''
    Contains some functions related to the creation of the grouped bar chart.
'''
import plotly.express as px
import plotly.graph_objects as go

import hover_template

from template import THEME

def get_figure_hospitalization(data):
    '''
        Generates the grouped chart using the given data.

        Args: 
            data: The data to display in the
            grouped chart
        Returns: 
            The figure to be displayed
        
    '''
    
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=data['PATIENT_ID'],
        y=data['NOTES_COUNT_TOTAL'],
        name='Nombre de notes',
        marker_color='#7786FA',
        hovertemplate=hover_template.get_grouped_bar_notes_hover_template()
    ))

    fig.add_trace(go.Bar(
        x=data['PATIENT_ID'],
        y=data['HOSPITALIZATION_COUNT'],
        name='Nombre d\'hospitalisations',
        marker_color='#FF6100',
        hovertemplate=hover_template.get_grouped_bar_hospitalization_hover_template()
    ))

    fig.update_layout(
        xaxis=dict(title='Patient'),
        yaxis=dict(title='Nombre'),
        legend_title='Légende',
        title={
            'text': "<b>Nombre de notes versus nombre d'hospitalisations d'un patient <br> au cours de 28 jours<b>",
            'font': {
                'size': 15,
            },
            'x': 0.4,
            'xanchor': 'center',
        },
    )
    
    fig.update_xaxes(
        tickangle = -45,
    )

    return fig


def get_figure_falls(data):
    '''
        Generates the grouped chart using the given data.

        Args: 
            data: The data to display in the
            grouped chart
        Returns: 
            The figure to be displayed
        
    '''
    
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=data['PATIENT_ID'],
        y=data['NOTES_COUNT_TOTAL'],
        name='Nombre de notes',
        marker_color='#7786FA',
        hovertemplate=hover_template.get_grouped_bar_notes_hover_template()
    ))

    fig.add_trace(go.Bar(
        x=data['PATIENT_ID'],
        y=data['FALL_COUNT'],
        name='Nombre de chutes',
        marker_color='#FF6100',
                hovertemplate=hover_template.get_grouped_bar_falls_hover_template()
    ))

    fig.update_layout(
        xaxis=dict(title='Patient'),
        yaxis=dict(title='Nombre'),
        legend_title='Légende',
        title={
            'text': "<b>Nombre de notes versus nombre de chutes d'un patient <br> au cours de 28 jours<b>",
            'font': {
                'size': 15,
            },
            'x': 0.4,
            'xanchor': 'center',
        },
    )
    
    fig.update_xaxes(
        tickangle = -45,
    )

    return fig