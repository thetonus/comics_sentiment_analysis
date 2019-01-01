''' Upload stats to MongoDB '''
import datetime

from analysis import app
from queries import queries
from settings import mongo_connections_stats
from typing import Dict

'''
|--------------------------------------------------------------------------
| Upload Stats to MongoDB
|--------------------------------------------------------------------------
|
| In order to study the popularity of a comics creator, it is important to
| gather stats on how people perceive these creators. In order to use
| multi-chain Monte Carlo to predict the posterior probability (which I feel
| will lead to a more accurate prediction of how people think than just a 
| rolling average.) In order to calculate a reasonable prior, I need to find
| the mean and std of each type of sentiment.
|
'''

def upload_stats(query: str, test: bool = False) -> Dict[str, str]:
    ''' Upload stats to MongoDB

    args
        str (query) - name you want to query
        bool (test) - If in test mode, it does not submit 
            new stats data to MongoDB
    '''
    # Retrieve current time
    now = datetime.datetime.now()
    current = now.strftime("%Y-%m-%d %H: %M")

    # Begin upload of statistics
    print(f'Begin Upload of {query} stats')
    data = app(query)

    result = {
        'time': current,
        'creator': data[0],
        'total tweets': data[1],
        'postive_mean': data[2],
        'postive_std': data[3],
        'neutral_mean': data[4],
        'neutral_std': data[5],
        'negative_mean': data[6],
        'negative_std': data[7],
    }

    # Upload stats
    print(f'Upload stats for {query}')

    if test == True:
        # Bypasses uploaded data to MongoDB
        return result

    conn = mongo_connections_stats[query]
    conn.insert_one(result)
    
    print('End Upload')

def retrieve_stats(query: str) -> Dict[str, str]:
    ''' Retrieve stats on creators 
    
    args
        str (query) - name you want to query

    returns
        dict - stats from mongo
    '''

    conn = mongo_connections_stats[query]
    return conn.find_one()

