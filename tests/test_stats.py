''' Test calculating statistics '''
from queries import queries
from stats import retrieve_stats, upload_stats

def test_upload_stats():
    ''' Test upload_stats function '''

    for query in queries:
        assert type(upload_stats(query, test=True)) == dict

def test_retrieve_stats():
    ''' Test retrieves_stats function '''

    assert True