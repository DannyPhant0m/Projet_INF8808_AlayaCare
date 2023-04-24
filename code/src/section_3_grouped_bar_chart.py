'''
    Contains some functions related to the creation of the univariate scatter plot of the third section.
'''
import plotly.graph_objects as go
import hover_template

def get_figure_1(data):
    '''
        Args: data: The dataframe to display
            
        Returns: 
            The figure to be displayed
        
    '''
    
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=data['PATIENT_ID'],
        y=data['CANCELLATION_COUNTS'],
        name='Pourcentage de visites annulées',
        marker_color='#7786FA',
        hovertemplate=hover_template.get_grouped_bar_cancellations_percentage_hover_template()
    ))
    
    fig.add_trace(go.Bar(
        x=data['PATIENT_ID'],
        y=data['HAS_PAIN_MENTION'],
        name='Pourcentage de visites avec mention de douleur',
        marker_color='#FF6100',
        hovertemplate=hover_template.get_grouped_bar_pain_hover_template()
    ))
    
    fig.update_layout(
        xaxis=dict(title='Patient'),
        yaxis=dict(title='Nombre'),
        legend_title='Légende',
        title={
            'text': "<b>Pourcentage de visites annulées versus de visites<br> avec mentionde douleur au cours de 28 jours<b>",
            'font': {
                'size': 15,
            },
            'x': 0.34,
            'xanchor': 'center',
        },
    )
    
    fig.update_xaxes(
        tickangle = -45,
    )

    return fig

def get_figure_2(data):
    '''
        Args: data: The dataframe to display
            
        Returns: 
            The figure to be displayed
        
    # '''
    
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=data['PATIENT_ID'],
        y=data['CANCELLATION_COUNTS'],
        name='Nombre d\'annulations',
        marker_color='#7786FA',
        hovertemplate=hover_template.get_grouped_bar_cancellations_hover_template()
    ))
    
    fig.add_trace(go.Bar(
        x=data['PATIENT_ID'],
        y=data['TOTAL_COMPLETED_ADLS'],
        name='Nombre d’activités de la vie quotidienne complétées',
        marker_color='#FF6100',
        hovertemplate=hover_template.get_grouped_bar_activities_hover_template()
    ))

    fig.update_layout(
        xaxis=dict(title='Patient'),
        yaxis=dict(title='Nombre'),
        legend_title='Légende',
        title={
            'text': "<b>Nombre d'activités complétées versus d'annulations<br>de rendez-vous au cours de 28 jours<b>",
            'font': {
                'size': 15,
            },
            'x': 0.33,
            'xanchor': 'center',
        },
    )
    
    fig.update_xaxes(
        tickangle = -45,
    )

    return fig