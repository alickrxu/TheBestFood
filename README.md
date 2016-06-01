# TheBestFood
Uses information about restaurants on Yelp to predict which restuarants will eventually fail. A project by Alick Xu and Grant Apodaca.

We predict the failure rate for restuarants in Isla Vista, the college town next to UCSB. We use objective features of each restuarant (Has TV, Parking, etc.) by looking at their Yelp business pages. An 8-fold cross-validation is used on an SVM classifier fitted on a training set with 26 closed restuarants within the last 10 years and 20 currently open restuarants (as of June 1, 2016). 


# Dependencies
` pip install yelp `

` pip install scrapy `

` pip install sklearn `
