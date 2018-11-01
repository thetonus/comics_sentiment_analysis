''' Upload Content to MongoDB '''
from uploaders import twitter, reddit
from helpers.reset_db import reset_db
from stats import upload_stats
from queries import queries

# Upload statistics data
# for query in queries:
#     upload_stats(query)

# Delete Previous data
# reset_db()

# Upload Content

# print('Upload Twitter Content')
# twitter()

# print('Upload Reddit Content')
# reddit()
