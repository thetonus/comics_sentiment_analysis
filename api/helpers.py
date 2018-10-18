''' Helper functions for api '''
from api.queries import queries

def validate_creator(creator: str) -> bool:
    ''' Validate creator
    
    args
        str - creator twitter handle
        
    return 
        bool - if creator is in set of twitter handles '''
        
    if creator in queries:
        return True
    return False