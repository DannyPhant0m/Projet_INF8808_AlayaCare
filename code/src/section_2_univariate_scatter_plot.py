'''
    Contains some functions related to the creation of the univariate scatter plot of the second section.
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
        y=[data['CANCELLATION_COUNTS'], data['ADL_COMPLETION_PERCENTAGE']],
        barmode='group',
        title="Pourcentage de complétion d'activités versus nombre d'annulation<br>d'un rendez-vous d'un patient au cours de 28 jours",
    )

    fig.update_layout(
        xaxis=dict(title='Patient'),
        yaxis=dict(title='Nombre'),
        legend_title='Légende',
        title={
            'text': "<b>Pourcentage de complétion d'activités versus nombre d'annulation<br>d'un rendez-vous d'un patient au cours de 28 jours<b>",
            'font': {
                'size': 15,
            },
            'x': 0.4,
            'xanchor': 'center',
        },
    )
    
    fig.data[0].name = 'Nombre d\'annulations'
    fig.data[1].name = 'Pourcentage de complétion d\'activité'

    return fig