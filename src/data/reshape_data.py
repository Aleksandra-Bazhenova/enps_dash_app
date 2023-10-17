import pandas as pd

#data = pd.read_excel("../../data/raw/global eNPS responses_June 2023.xlsx")

def make_wide_df(data):
    
    if ~data['Scale Score'].isnull()[0]:
        data['Score or Comment'] = ['Score', 'Comment']*int(len(data)/2)
        data_comments = data.loc[list(range(1, len(data), 2))].reset_index().rename(columns={'index':'Comment Original Index', 'Question Title':'Comment Question Title'})
        data_scores = data.loc[list(range(0, len(data), 2))].reset_index().rename(columns={'index':'Score Original Index', 'Question Title':'Score Question Title'})
            
    else:
        data['Score or Comment'] = ['Comment', 'Score']*int(len(data)/2)
        data_comments = data.loc[list(range(0, len(data), 2))].reset_index().rename(columns={'index':'Comment Original Index', 'Question Title':'Comment Question Title'})
        data_scores = data.loc[list(range(1, len(data), 2))].reset_index().rename(columns={'index':'Score Original Index', 'Question Title':'Score Question Title'})
    
    data_wide = pd.concat([data_scores[['Score Original Index', 'Score Question Title', 'Scale Score']], data_comments[[c for c in data_comments.columns if c not in ['Score Original Index', 'Score Question Title', 'Scale Score', 'Score or Comment']]]], axis=1)
        
    return data_wide

