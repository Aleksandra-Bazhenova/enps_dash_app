import pandas as pd

#data = pd.read_excel("../../data/raw/global eNPS responses_June 2023.xlsx")

def make_wide_df(df):
    
    if ~df['Scale Score'].isnull()[0]:
        df['Score or Comment'] = ['Score', 'Comment']*int(len(df)/2)
        data_comments = df.loc[list(range(1, len(df), 2))].reset_index().rename(columns={'index':'Comment Original Index', 'Question Title':'Comment Question Title'})
        data_scores = df.loc[list(range(0, len(df), 2))].reset_index().rename(columns={'index':'Score Original Index', 'Question Title':'Score Question Title'})
            
    else:
        df['Score or Comment'] = ['Comment', 'Score']*int(len(df)/2)
        data_comments = df.loc[list(range(0, len(df), 2))].reset_index().rename(columns={'index':'Comment Original Index', 'Question Title':'Comment Question Title'})
        data_scores = df.loc[list(range(1, len(df), 2))].reset_index().rename(columns={'index':'Score Original Index', 'Question Title':'Score Question Title'})
    
    data_wide = pd.concat([data_scores[['Score Original Index', 'Score Question Title', 'Scale Score']], data_comments[[c for c in data_comments.columns if c not in ['Score Original Index', 'Score Question Title', 'Scale Score', 'Score or Comment']]]], axis=1)
        
    return data_wide

