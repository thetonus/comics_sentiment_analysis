''' Upload Content to MongoDB '''
from uploaders import twitter, reddit

# Upload Content
print('Upload Twitter Content')
twitter()
print('Upload Reddit Content')
reddit()
