'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd


def getGroupedBarSums(dataframe):
    
    dataframe = dataframe[['PATIENT_ID','NOTES_COUNT_TOTAL','HOSPITALIZATION_COUNT']].copy()
    
    dataframe = dataframe.groupby('PATIENT_ID', as_index=False).sum()
    
    print(dataframe)
    return dataframe


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    
    
    return dataframe
