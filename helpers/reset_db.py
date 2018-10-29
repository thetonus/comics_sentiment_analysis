''' Delete MongoDB connections to start new collections in the future '''

from settings import mongo_connections
from queries import queries


def reset_db() -> None:
    ''' Reset MongoDB '''
    for query in queries:
        print(f'Delete {query} collection.')
        mongo_connections[query].drop()

reset_db()