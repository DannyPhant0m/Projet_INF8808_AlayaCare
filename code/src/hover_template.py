'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

    '''
    
    return ("<b>%{y}<br>"
            "<b>a complété</b> %{z} %<br>"
            "<b> des activités à la journée</b> %{x}<br>"
            '<extra></extra>')


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips in the bubble chart.
        
        Contains three labels, followed by their corresponding
        value for the patient, the number of visits and the date.

        The labels font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''

    return ("<b>Nom du Patient</b>: %{y}<br>"
            "<b>Nombre de Visites</b>: %{marker.size:,}<br>"
            "<b>Date</b>: %{x}<br>"
            '<extra></extra>')
    
def get_grouped_bar_notes_hover_template():
    '''
        Sets the template for the hover tooltips in the grouped bar charts.

        Contains three labels, followed by their corresponding
        value, separated by a colon : Patient name, and the number associated.

    '''

    return ("<b>Nom du Patient</b>: %{x}<br>" +
            '<b>Nombre de notes:</b>' + "<b> %{y}<br>"
            '<extra></extra>')
    
    
def get_grouped_bar_falls_hover_template():
    '''
        Sets the template for the hover tooltips in the grouped bar charts.

        Contains three labels, followed by their corresponding
        value, separated by a colon : Patient name, and the number associated.

    '''

    return ("<b>Nom du Patient</b>: %{x}<br>" +
            '<b>Nombre de chutes:</b>' + "<b> %{y}<br>"
            '<extra></extra>')

def get_grouped_bar_hospitalization_hover_template():
    '''
        Sets the template for the hover tooltips in the grouped bar charts.

        Contains three labels, followed by their corresponding
        value, separated by a colon : Patient name, and the number associated.

    '''

    return ("<b>Nom du Patient</b>: %{x}<br>" +
            '<b>Nombre d\'hospitalisations:</b>' + "<b> %{y}<br>"
            '<extra></extra>')