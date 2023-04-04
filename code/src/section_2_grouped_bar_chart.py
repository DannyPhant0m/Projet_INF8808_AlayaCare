'''
    Contains some functions related to the creation of the grouped bar chart.
'''
import plotly.express as px
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
    
    fig = px.bar(
        data,
        x='PATIENT_ID',
        y=['NOTES_COUNT_TOTAL', 'HOSPITALIZATION_COUNT'],
        barmode='group',
        title="Nombre de notes versus nombre d'hospitalisations d'un patient au cours de 28 jours",
    )

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
    
    fig.data[0].name = 'Nombre de notes'
    fig.data[1].name = 'Nombre d\'hospitalisations'

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
    
    fig = px.bar(
        data,
        x='PATIENT_ID',
        y=['NOTES_COUNT_TOTAL', 'FALL_COUNT'],
        barmode='group',
        title="Nombre de notes versus nombre de chutes d'un patient au cours de 28 jours"
    )

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
    
    fig.data[0].name = 'Nombre de notes'
    fig.data[1].name = 'Nombre de chutes'

    return fig