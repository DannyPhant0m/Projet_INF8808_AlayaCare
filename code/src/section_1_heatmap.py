'''
    Contains some functions related to the creation of the heatmap of the first section.
'''
import plotly.express as px
import hover_template

from template import THEME

def get_figure(data):
    '''
        This function generates the heatmap that depicts the percentage of
        activity completio for each patient over the dates from the dataframe imput

        Arg:
            data - a wide type dataframe
            
        Returns: 
            The figure to be displayed
        
    '''
    fig = px.imshow(
        data,
        labels=dict(
            x="Journée",
            y="Patient", 
            color="Taux de complétion d'activtiés (%)"
        ),
        color_continuous_scale=['#FFE3C0','#FFDFBA','#FFA73A','#F89213','#FF6100'],
        title='<b>Pourcentage de complétion des activités au long des visites</b>',
        width=1300
    )

    fig.update_layout(
        title_font_size=15,
        title_x=0.45,
        xaxis_nticks=len(data.columns),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    
    fig.update_xaxes(
        tickangle = -45,
        tickformat='%Y-%m-%d'
    )
    
    fig.update_traces(hovertemplate = hover_template.get_heatmap_hover_template())
    
    return fig
