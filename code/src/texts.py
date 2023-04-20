'''
    Contains text strings that will population each section of the website.
'''


'''
    Home section of the website
'''


HOME_DESCRIPTION = "AlayaCare est une compagnie responsable par un logiciel de gestion des soins à domicile pour les agences du domaine. \n\n"\
"Les visualisations de données dans ce projet ont comme but d'outiller les utilisateurs du logiciel avec des comparaisons intuitives"\
"par rapport aux différents métriques enregistrées chez les patients. Cette vue d'ensemble a un potentiel pour identifier les"\
"tendences et comportements des patients ainsi que pour donner un aperçu général de la qualité des soins \n\n"\
"Les prochains onglets cherchent à répondre plusieurs questions réliées à cette thématique:\n\n"\
"1. Douleur et visites\n"\
"        - Est-ce que la douleur diminue chez les patients avec le nombre de visites?\n\n"\
"2. Progression du niveau de complétion\n"\
"        - Est-ce que le pourcentage de complétion d’activités de la vie quotidienne d’un patient augmente avec le nombre de visites durant les derniers 28 jours?\n\n"\
"3. Notes et hospitalisations\n"\
"        - Est-ce que le nombre de notes prises totale par patient est proportionnel au nombre d' hospitalisations?\n"\
"        - Est-ce que le nombre de notes prises totale par patient est proportionnel au nombre de chutes?\n\n"\
"4. Chutes et hospitalisations\n"\
"        - Est-ce que le nombre de chutes d’un patient augmente ou diminue au cours de ses visites durant les derniers 28 jours?\n"\
"        - Est-ce qu’il existe une corrélation entre les journées de chutes et d’hospitalisation des patients durant les derniers 28 jours?\n\n"\
"5. Annulation de visites\n"\
"        - Est-ce qu'il y a une corrélation de tendance entre les patients qui annulent des rendez-vous versus le niveau de douleur ressenti au dernier rendez-vous?\n"\
"        - Est-ce qu'il y a une corrélation de tendance entre les patients qui annulent des rendez-vous versus le pourcentage de complétions d'activités quotidiennes?\n\n\n"\
"Chaque visualisation est outillée d'info-bulles pour détailler les données présentés. Il suffit de passer la souris par-dessous les éléments des figures. "


'''
    Section 1.1: Évolution de la relation entre le douleur et le nombre de visites 
'''

SECTION_1_BUBBLE_CHART_HEADER = " Cette section présente la corrélation possible entre la douleur et le nombre de visites de patients sur une période de 28 jours \n"

SECTION_1_BUBBLE_CHART_DESCRIPTION = " Ce graphique permet de distinguer rapidement l'évolution de la douleur et le nombre de visites au cours des 28 jours "



'''
    Section 1.2:  Progression du niveau de complétion des activités par patient 
'''

SECTION_1_2_HEATMAP_1_HEADER = " Cette section présente le protrait des progressions des niveaux de complétion d'éactivité d'un patient \n"

SECTION_1_2_HEATMAP_1_DESCRIPTION = " Ce graphique a comme objectif de dresser le portrait"\
"des progressions des niveaux de complétion d'activités par patient, "\
"ce qui permet de faire le suivi visuel du progrès des patients par rapport aux activités complétés. "



'''
    Section 2.1: Nombre de chutes et d'hospitalisations
'''

SECTION_2_UNIVARIATE_SCATTER_PLOT_HEADER = " Cette section présente la corrélation possible entre le nombre de chutes et d'hospitalisation de tous les patients \n"

SECTION_2_UNIVARIATE_SCATTER_PLOT_DESCRIPTION = " Ce graphique permet de " \
"distinguer la possible corrélation entre les jours de chute et les jours " \
"d'hospitalisation vers le temps pendant les 28 derniers jours. \n" \
"En raison du manque de données et du petit nombre de personnes " \
"dont nous disposons d'informations, nous ne pouvons pas apprécier "\
"de corrélation entre les jours de chute et les jours d'hospitalisation."


'''
    Section 2.2 : Nombre de notes et d'hospitalisations
'''

SECTION_2_GROUPED_BAR_HEADER = " Cette section présente la corrélation possible entre les notes prises sur un patient comparées aux nombre de chutes et d'hospitalisation \n"

SECTION_2_GROUPED_BAR_1_DESCRIPTION = " Ce graphique à barres groupées permet de distinguer rapidement la disparité entre les notes prises et le nombre d'hospitalisations "

SECTION_2_GROUPED_BAR_2_DESCRIPTION = " Ce graphique à barres groupées permet de distinguer rapidement la disparité entre les notes prises et le nombre de chutes "


'''
    Section 3: Relations avec l'annulation de visites
'''

SECTION_3_GROUPED_BAR_HEADER = " Cette section présente la corrélation possible entre les annulations de visites d'un patient comparés aux mentions de douleurs et aux activités de la vie quotidienne complétées \n"

SECTION_3_GROUPED_BAR_1_DESCRIPTION = " Ce graphique à barres groupées permet de distinguer rapidement la disparité entre le pourcentage de visites annulées et le pourcentage de visites avec mention de douleur "

SECTION_3_GROUPED_BAR_2_DESCRIPTION = " Ce graphique à barres groupées permet de distinguer rapidement la disparité entre le nombre de visites annulées et le nombre total d'activités de la vie quotidienne complétées "







