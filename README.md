# TheBestFood
Uses information about restaurants on Yelp to predict which restuarants will eventually fail. A project by Alick Xu and Grant Apodaca.

We predict the failure rate for restuarants in Isla Vista, the college town next to UCSB. We use objective features of each restuarant (Has TV, Parking, etc.) by looking at their Yelp business pages. An 8-fold cross-validation is used on an SVM classifier fitted on a training set with 26 closed restuarants within the last 10 years and 20 currently open restuarants (as of June 1, 2016). 

# Structure

Scripts:
` classify_restaurants.py ` classifies a restuarant as closed in 3 years or not. Input is svmlight style data file ( `<label> <feature_name>:<value> <feature_name><value> ... `) 
` date_convert.py ` helper to calculate length of time between two dates, and pickle dump to `test_dates_dictionary.py`
` make_feature_dict.py ` helper that, given `features.txt` which contains all of our features, creates a python dictionary with all of our features and possible values
` get_restuarants.py ` uses the Yelp API to return a file containing a list of all restuarants in a geographic bounding box
` make_svm_test_data.py ` given the testing (restaurants currently open) data, creates an svmlight data file with each restaurant labelled and features properly assigned
` make_svm_training_data.py ` given the training (restaurants already closed) data, creates an svmlight data file with each restaurant labelled and features properly assigned. Can clean this up later to make one svm creation script
` scrape_yelp.py` uses Scrapy to scrape yelp pages of given restuarants for newest/oldest review, price range, cuisine type, and business info ('Has TV', 'Ambience', etc). run with `scrapy runspider scrape_yelp.py`
` scrape_closed.py` uses Scrapy to scrape yelp pages of given closed restuarants. Can clean this up later to make one scrape script 


Files:
` labels_features.txt` maps every english label ('Mexican', 'Has TV') to a number
` reverse_feature_labels.txt` maps from number to english label, for result analysis
` test_dates_dictionary.txt` maps restuarant to length of existence for test restuarants (in years)
` training_dates_dictionary.txt` maps restuarant to length of existence for training restuarants


# Dependencies
` pip install yelp `

` pip install scrapy `

` pip install sklearn `
