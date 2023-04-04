'''
    Contains some functions related to the creation of the grouped bar chart.
'''
import plotly.express as px
import hover_template

from template import THEME

def get_figure(data):
    '''
        !!!!!!!!!!!!Add description here!!!!!!!!!

        Args: !!!!!!add arguments!!!!!!!!!!!
            
        Returns: 
            The figure to be displayed
        
    '''
    
    fig = px.bar(
        data,
        x='PATIENT_ID',
        y=['NOTES_COUNT_TOTAL', 'HOSPITALIZATION_COUNT'],
        barmode='group',
        title='Patient Notes and Hospitalizations'
    )

    # Update the axis labels
    fig.update_layout(
        xaxis=dict(title='Patient ID'),
        yaxis=dict(title='Count')
    )

    # Show the plot

    return fig