import os

import openai
from openai.embeddings_utils import get_embedding, cosine_similarity

# https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/chatgpt?pivots=programming-language-chat-completions#working-with-the-chatgpt-and-gpt-4-models

def chatgpt4(user_input):

    os.environ["AZURE_OPENAI_API_KEY"] = "d07b0e68cbe14c1e8390cce8bff03af1"
    os.environ["AZURE_OPENAI_ENDPOINT"] = "https://azwe-openai-dcoe-us.openai.azure.com/"

    API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    RESOURCE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

    openai.api_type = "azure"
    openai.api_key = API_KEY
    openai.api_base = RESOURCE_ENDPOINT

    openai.api_version = "2023-03-15-preview"

    model = 'gpt-4-32k'
    deployment_name = 'gpt-4-32k'
    
    url = openai.api_base+"openai/deployments/"+deployment_name+"/chat/completions?api-version="+openai.api_version

    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=[
        {"role":"system", "content":"Expert in sentiment analysis, topic modelling, and generating insights from text data."},
        {"role":"user", "content":user_input}
        ]
    )
    
    return response


prompt_1 = """Customers of a company are asked to rate their experience of being a customer of said company by giving a score (NPS score)
on a scale of 1 to 10, as well as leaving an optional comment to describe the primary reason for their score.
Given the comment: "{}", extract the sentiment from this comment to your best ability.
If the comment is too short or ambiguous, e.g., 'None', 'No Comment', 'Nothing', or some other similar word - return 'No Comment'.
If you're unsure about the sentiment of a comment, or you believe the comment is of neutral sentiment, return 'NEUTRAL'.
For anything else, the result should be either 'POSITIVE' or 'NEGATIVE'.
Give your answer as a single word/ phrase (i.e., 'POSITIVE', 'NEGATIVE', 'NEUTRAL', 'No Comment') without any additional commentary or padding.
"""

def sentiment_analysis_openai(dataframe, columns_list, prompt_n):
    
    sentiment_labels = []
    counter=0
    
    for score, comment in dataframe[columns_list].values:
        
        retries=0
        max_retries=5
        
        while True:
            try:
                print(f'Complaint {counter}: ', score, comment)
                
                prompt = prompt_n.format(comment)
                
                response = chatgpt4(prompt)['choices'][0]['message']['content']
                
                if response or retries>=max_retries:
                    break
                else:
                    retries+=1
            
            except:
                print(f'Request timeout for comment {counter}. Retrying...')
                retries+=1
                continue
                
        if response:
            sentiment_labels.append(response)
            print(f'Response {counter}: ', response)
            print('\n\n')
            counter+=1
            
        else:
            print(f'Failed to get response for comment {counter} after {max_retries} attempts.')
        
    return sentiment_labels