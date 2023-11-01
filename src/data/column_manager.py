import pandas as pd

def nps_label_based_on_score(wide_data):
    
    wide_data['NPS Label Based On Score'] = wide_data['Scale Score'].apply(lambda x: 'Detractor' if x<=6 else ('Passive' if x<=8 else 'Promoter'))
    
    return wide_data
