'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    
    return ("<b>%{y}<br>"
            "<b>a complété</b> %{z} %<br>"
            "<b> des activités à la journée</b> %{x}<br>"
            '<extra></extra>')

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    hover_template = """
        <span style = 'font-family: Roboto Slab; font-weight: Bold;'>Date</span style = 'font-family: Roboto;'> : %{y}</span><br>
        <span style = 'font-family: Roboto Slab; font-weight: Bold;'>Trees</span style = 'font-family: Roboto;'> : %{x}</span>""" + "<extra></extra>"
        
    return hover_template


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips in the bubble chart.
        
        Contains three labels, followed by their corresponding
        value for the patient, the number of visits and the date.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''

    return ("<b>Nom du Patient</b>: %{y}<br>"
            "<b>Nombre de Visites</b>: %{marker.size:,}<br>"
            "<b>Date</b>: %{x}<br>"
            '<extra></extra>')
