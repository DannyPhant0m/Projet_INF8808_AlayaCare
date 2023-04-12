'''
    Contains some functions related to the creation of the bubble chart.
'''
import plotly.express as px
import hover_template

from template import THEME

def get_figure(data):
    '''
        Generates the bubble plot.
        
        Day in axe X, patient in axe Y, 
        number of visits in marker size
        and pain indicator in marker color

        Args: 
            data: The dataframe to display
            
        Returns: 
            The figure to be displayed
        
    '''

    fig = px.scatter(
        data, 
        y='PATIENT_ID', 
        x='DAY', 
        color='HAS_PAIN_MENTION', 
        size='VISIT_COUNTS', 
        size_max=10, width=1200, 
        height=600,
        title='<b>Douleur chez les patients vs nombre de visites</b>',
        color_discrete_sequence=['#7786FA','#FF6100'],
        labels=dict(
            PATIENT_ID='<b>Nom du Patient</b>', 
            DAY='<b>Jour</b>', 
            HAS_PAIN_MENTION='Douleur'
        )      
    )
    
    fig.update_layout(
        title_font_size=15,
        title_x=0.5 #center title
    )
    
    fig.update_xaxes(
        tickangle = -45,
        nticks=28,
        tickformat='%Y-%m-%d'
    )
    
    fig.update_traces(
        hovertemplate=hover_template.get_bubble_hover_template()
    )

    return fig
