'''
    Contains some functions related to the creation of the univariate scatter plot of the second section.
'''
import plotly.express as px
import hover_template

from template import THEME

def get_figure(data):
    '''
        Args: data: The dataframe to display
            
        Returns: 
            The figure to be displayed
        
    '''

    # We create a scatter plot with the data
    fig = px.scatter(
        data[data['EVENT_TYPE'] != 'rien'], 
        x='PATIENT_ID', 
        y='DAY', 
        width=1000,
        height=600,
        color='EVENT_TYPE', 
        hover_data={'PATIENT_ID','DAY','EVENT_TYPE'},
        color_discrete_sequence=['#7786FA','#FF6100'],
    )

    # We update the layout of the figure
    fig.update_traces(marker={'size': 11})

    # We update the hover template
    fig.update_traces(
        hovertemplate="<br>".join([
            "<b>Nom du Patient</b>: %{x}",
            "<b>Date</b>: %{y}",
            "<b>Type d'événement</b>: %{customdata[0]}",
            "<extra></extra>"
        ])
    )

    # We update the x axis
    fig.update_xaxes(
        title_text="<b>Nom du Patient</b>",
        tickangle = -45
    )

    # We update the y axis
    fig.update_yaxes(
        title_text="<b>Jour</b>",
        nticks=15, 
        tickformat='%Y-%m-%d'
    )
    
    # We update the legend and the title
    fig.update_layout(
        legend=dict(
            orientation='h',
            yanchor='top',
            y=1.1,
            xanchor='center',
            x=0.5,
            title=None,
            font=dict(
                family='Arial',
                size=12,
            ),
        ),
        title=dict(
            text = "<b>Nombre de notes versus nombre d'hospitalisations d'un patient au cours de 28 jours<b>",
            font = {
                'size': 15,
            },
            x=0.5,
            y=1.0,
        ),
        margin=dict(t=20),
    )

    # We update the background color
    fig.update_layout(plot_bgcolor='white')
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

    return fig