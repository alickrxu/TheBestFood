from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

with open('yelp_credentials.txt') as myfile:
    credentials = [line.strip() for line in myfile.readlines()]

auth = Oauth1Authenticator(credentials[0], credentials[1], credentials[2], credentials[3])

client = Client(auth)

params = {
        'term': 'restaurants'
        }

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
        'location' : info.business.location
        })

with open('businesses.txt', 'w') as myfile:
    for result in results:
        myfile.write(result['name'] + ', ' + str(result['rating']) + ', ' + str(result['count']) +', ' + result['id'] + '\n')
