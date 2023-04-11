'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
import numpy as np

'''
    Section 2.1.1: Évolution de la relation entre le douleur et le nombre de visites 
'''

def getPainDetailsRelation(dataframe):
    
    pd.to_datetime(dataframe['DAY'])
    
    dataframe = dataframe[['PATIENT_ID','DAY','VISIT_COUNTS','HAS_PAIN_MENTION']].copy()
    
    return dataframe


'''
    Section 2.1.2:  Progression du niveau de complétion des activités par patient 
'''

def getAdlCompletionTimeline(dataframe):
    
    dataframe = dataframe[['PATIENT_ID','VISIT_COUNTS','ADL_COMPLETION_PERCENTAGE']].copy()
    
    return dataframe


'''
    Section 2.2.1: Nombre de chutes et d'hospitalisations
'''

def getFallsAndHospitalizationTimeline(dataframe):
    
    # create a new column that classifies each observation as 'fall', 'hospitalization', or 'nothing'
    conditions = [
        (dataframe['FALL_COUNT'] == 1),
        (dataframe['HOSPITALIZATION_COUNT'] == 1),
        (dataframe['FALL_COUNT'] == 0) & (dataframe['HOSPITALIZATION_COUNT'] == 0)
    ]
    choices = ['Chute', 'Hospitalisation', 'rien']
    dataframe['EVENT_TYPE'] = np.select(conditions, choices, default='unknown')

    dataframe = dataframe[['PATIENT_ID','DAY','EVENT_TYPE']].copy()
    
    return dataframe


'''
    Section 2.2.2 : Nombre de notes et d'hospitalisations
'''

def getGroupedBarHospitalizationCount(dataframe):
    
    dataframe = dataframe[['PATIENT_ID','NOTES_COUNT_TOTAL','HOSPITALIZATION_COUNT']].copy()
    dataframe = dataframe.groupby('PATIENT_ID', as_index=False).sum()
    
    return dataframe

def getGroupedBarFallCount(dataframe):
    
    dataframe = dataframe[['PATIENT_ID','NOTES_COUNT_TOTAL','FALL_COUNT']].copy()
    dataframe = dataframe.groupby('PATIENT_ID', as_index=False).sum()

    return dataframe


'''
    Section 2.3: Relations avec l'annulation de visites
'''

def getCancellationAndPainRelation(dataframe):
    
    dataframe = dataframe[['PATIENT_ID','CANCELLATION_COUNTS','HAS_PAIN_MENTION']].copy()
    dataframe = dataframe.groupby('PATIENT_ID', as_index=False).sum()
    
    return dataframe

def getCancellationAndAdlRelation(dataframe):
    
    dataframe = dataframe[['PATIENT_ID','CANCELLATION_COUNTS','ADL_COMPLETION_PERCENTAGE']].copy()
    dataframe = dataframe.groupby('PATIENT_ID', as_index=False).sum()

    new_adl = []
    for adl in dataframe['ADL_COMPLETION_PERCENTAGE']:
        new_adl.append(adl / 10)
    dataframe['ADL_COMPLETION_PERCENTAGE'] = new_adl
    
    return dataframe
