from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

import pickle

with open('yelp_credentials.txt') as myfile:
    credentials = [line.strip() for line in myfile.readlines()]

auth = Oauth1Authenticator(credentials[0], credentials[1], credentials[2], credentials[3])

client = Client(auth)

params = {
        'category_filter': 'restaurants',
        'offset': 20
        }

#edit the bounding box to search for different restuarants
response = client.search_by_bounding_box(
        34.409004,
        -119.870291,
        34.417643,
        -119.853369,
        **params
        )

results = []
for b in response.businesses:
    # find business of all search results
    info = client.get_business(b.id)
    results.append({
        'name' : info.business.name, 
        'id' : info.business.id,
        'rating' : info.business.rating,
        'count' : info.business.review_count,
        'location' : info.business.location,
        'categories' : info.business.categories,
        'is_closed' : info.business.is_closed
        })
    print info.business.categories

with open('businesses.txt', 'w') as myfile:
    pickle.dump(results, myfile)
    '''
    for result in results:
        myfile.write(result['name'].encode('utf8') + ', ' + str(result['rating']).encode('utf8') + ', ' + str(result['count']).encode('utf8') +', ' + result['id'].encode('utf8') + ', ' + str(result['is_closed']).encode('utf8') + '\n')
        '''
