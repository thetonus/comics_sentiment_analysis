''' Upload reddit posts that mention certain comics creators '''
from praw import Reddit
from helpers.upload import clean_text
from settings import mongo_connections, reddit_credentials
from queries import queries


def reddit_setup():
    ''' Create reddit instance 

    returns
        api: Reddit - Reddit instance'''

    api = Reddit(client_id=reddit_credentials.CLIENT_ID,
                 client_secret=reddit_credentials.CLIENT_SECRET,
                 user_agent=reddit_credentials.USER_AGENT,
                 username=reddit_credentials.USERNAME,
                 password=reddit_credentials.PASSWORD)
    return api


def criteria_top(conn, r_subreddit, query: str, limit: int) -> None:
    ''' Search the 'Top' criteria for top posts 

    args
        conn: MongoDB collection - collection for comic creator
        r_subreddit: Reddit subreddit instance - current subreddit
        limit: int - limit for posts to download, defaults for 1000 posts
    '''

    subreddit_in_question = r_subreddit.top(limit=limit)

    for submission in subreddit_in_question:
        # Clean text by removing links and special characters
        post = clean_text(submission.selftext)
        if query in post:
            conn.insert_one({'text': post})


def criteria_controversial(conn, r_subreddit, query: str, limit: int) -> None:
    ''' Search the 'Controversial' criteria for controversial posts 

    args
        conn: MongoDB collection - collection for comic creator
        r_subreddit: Reddit subreddit instance - current subreddit
        limit: int - limit for posts to download, defaults for 1000 posts
    '''

    subreddit_in_question = r_subreddit.controversial(limit=limit)

    for submission in subreddit_in_question:
        # Clean text by removing links and special characters
        post = clean_text(submission.selftext)
        if query in post:
            conn.insert_one({'text': post})


def criteria_hot(conn, r_subreddit, query: str, limit: int) -> None:
    ''' Search the 'Hot' criteria for hot posts 

    args
        conn: MongoDB collection - collection for comic creator
        r_subreddit: Reddit subreddit instance - current subreddit
        limit: int - limit for posts to download, defaults for 1000 posts
    '''

    subreddit_in_question = r_subreddit.hot(limit=limit)

    for submission in subreddit_in_question:
        # Clean text by removing links and special characters
        post = clean_text(submission.selftext)
        if query in post:
            conn.insert_one({'text': post})


def criteria_new(conn, r_subreddit, query: str, limit: int) -> None:
    ''' Search the 'New' criteria for new posts 

    args
        conn: MongoDB collection - collection for comic creator
        r_subreddit: Reddit subreddit instance - current subreddit
        limit: int - limit for posts to download, defaults for 1000 posts
    '''

    subreddit_in_question = r_subreddit.new(limit=limit)

    for submission in subreddit_in_question:
        # Clean text by removing links and special characters
        post = clean_text(submission.selftext)
        if query in post:
            conn.insert_one({'text': post})


def criteria_rising(conn, r_subreddit, query: str, limit: int) -> None:
    ''' Search the 'Rising' criteria for rising posts 

    args
        conn: MongoDB collection - collection for comic creator
        r_subreddit: Reddit subreddit instance - current subreddit
        limit: int - limit for posts to download, defaults for 1000 posts
    '''

    subreddit_in_question = r_subreddit.rising(limit=limit)

    for submission in subreddit_in_question:
        # Clean text by removing links and special characters
        post = clean_text(submission.selftext)
        if query in post:
            conn.insert_one({'text': post})


def upload_posts(api, subreddits, query: str, limit: int = 1000) -> None:
    ''' Upload posts to MongoDB 

    args
        api: praw.Reddit - Reddit instance
        subreddits: list - subreddits I want to search
        query: str - query parameter
        limit: int - limit for posts to download, defaults for 1000 posts
    '''

    conn = mongo_connections[query]

    for subreddit in subreddits:
        print(f'Searching {subreddit} for posts\n')
        r_subreddit = api.subreddit(subreddit)

        # Get posts according to topics
        print('Searching Top')
        criteria_top(conn, r_subreddit, query, limit)
        print('Searching Rising')
        criteria_rising(conn, r_subreddit, query, limit)
        print('Searching New')
        criteria_new(conn, r_subreddit, query, limit)
        print('Searching Hot')
        criteria_hot(conn, r_subreddit, query, limit)
        print('Searching Controversial')
        criteria_controversial(conn, r_subreddit, query, limit)


def reddit():
    api = reddit_setup()

    subreddits = ['comicbooks', 'DCcomics']
    limit = 10**5

    # Upload tweets
    print('Beginning Upload')
    for query in queries:
        print(f'\nPosts for {query}')
        upload_posts(api, subreddits, query, limit)

    print('Upload Complete')


# Run program
if __name__ == '__main__':
    reddit()
