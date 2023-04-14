'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
import numpy as np

'''
    Section 1.1: Évolution de la relation entre le douleur et le nombre de visites 
'''

def getPainDetailsRelation(dataframe):
    
    pd.to_datetime(dataframe['DAY'])    
     
    dataframe = dataframe[['PATIENT_ID','DAY','VISIT_COUNTS','HAS_PAIN_MENTION']].copy()
    
    dataframe['HAS_PAIN_MENTION']=dataframe['HAS_PAIN_MENTION'].map({True:'Oui',False:'Non'})
    
    return dataframe


'''
    Section 1.2:  Progression du niveau de complétion des activités par patient 
'''

def getAdlCompletionTimeline(dataframe):
    
    pd.to_datetime(dataframe['DAY'])
    
    dataframe = dataframe[['PATIENT_ID','DAY','ADL_COMPLETION_PERCENTAGE']].copy()
    
    dataframe=dataframe.pivot(index='PATIENT_ID',columns='DAY',values='ADL_COMPLETION_PERCENTAGE')

    dataframe=dataframe.replace(0, np.nan)
    
    return dataframe


'''
    Section 2.1: Nombre de chutes et d'hospitalisations
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
    Section 2.2 : Nombre de notes et d'hospitalisations
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
    Section 3: Relations avec l'annulation de visites
'''

def getCancellationAndPainRelation(dataframe):
    
    dataframe = dataframe[['PATIENT_ID','CANCELLATION_COUNTS','HAS_PAIN_MENTION','VISIT_COUNTS']].copy()
    dataframe = dataframe.groupby('PATIENT_ID', as_index=False).sum()
    
    pain_percentage = []
    for index, pain in enumerate(dataframe['HAS_PAIN_MENTION']):
        cancellations_count = dataframe['CANCELLATION_COUNTS'][index]
        visits_count = dataframe['VISIT_COUNTS'][index]
        pain_percentage.append(pain / (visits_count - cancellations_count) * 100)
    dataframe['HAS_PAIN_MENTION'] = pain_percentage
    
    cancellations_percentage = []
    for index, cancellation in enumerate(dataframe['CANCELLATION_COUNTS']):
        cancellations_percentage.append(cancellation / dataframe['VISIT_COUNTS'][index] * 100)
    dataframe['CANCELLATION_COUNTS'] = cancellations_percentage
    
    return dataframe

def getCancellationAndAdlRelation(dataframe):
    
    dataframe = dataframe[['PATIENT_ID','CANCELLATION_COUNTS','TOTAL_COMPLETED_ADLS']].copy()
    dataframe = dataframe.groupby('PATIENT_ID', as_index=False).sum()
    
    return dataframe
