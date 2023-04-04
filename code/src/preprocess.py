'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd


'''
    Section 2.1.1: Évolution de la relation entre le douleur et le nombre de visites 
'''

def getPainDetailsRelation(dataframe):
    
    #J'ai ajouter le pain_details, peut-etre que cela petu-etre pertinent pour toi
    
    dataframe = dataframe[['PATIENT_ID','VISIT_COUNTS','HAS_PAIN_MENTION','PAIN_DETAILS']].copy()
    
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
    
    dataframe = dataframe[['PATIENT_ID','FALL_COUNT','HOSPITALIZATION_COUNT']].copy()
    
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

    return dataframe

def getCancellationAndAdlRelation(dataframe):
    
    dataframe = dataframe[['PATIENT_ID','CANCELLATION_COUNTS','ADL_COMPLETION_PERCENTAGE']].copy()

    return dataframe