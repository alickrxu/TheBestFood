from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

import pickle

with open('yelp_credentials.txt') as myfile:
    credentials = [line.strip() for line in myfile.readlines()]

auth = Oauth1Authenticator(credentials[0], credentials[1], credentials[2], credentials[3])

client = Client(auth)

def find_businesses(sw_lat, sw_long, ne_lat, ne_long):
    offset = 20
    count = 0
    while True:
        print 'searching for offset: ' + str(count * offset)

        params = {
                'category_filter': 'restaurants',
                'offset': count * offset
                }

        #edit the bounding box to search for different restuarants
        response = client.search_by_bounding_box(
                sw_lat,
                sw_long,
                ne_lat,
                ne_long,
                **params
                )

        results = []
        if len(response.businesses) == 0:
            print 'found all businesses'
            break

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

        with open('businesses.txt', 'a') as myfile:
            pickle.dump(results, myfile)
            '''
            for result in results:
                myfile.write(result['name'].encode('utf8') + ', ' + str(result['rating']).encode('utf8') + ', ' + str(result['count']).encode('utf8') +', ' + result['id'].encode('utf8') + ', ' + str(result['is_closed']).encode('utf8') + '\n')
                '''

        count = count + 1

def read_business_file():
    results = []
    with open('businesses.txt', 'r') as f:
        results = pickle.load(f)

    print results


#call methods here
find_businesses(34.409004, -119.870291, 34.417643, -119.853369)
read_business_file()
