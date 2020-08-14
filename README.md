# Donate-Direct
Donate Direct is a web service that provides an API for vendors, who pledge their proceeds to charity, to prove they reliability to their customers. It aims to remove the ambiguity of the trustworthiness of these third-party donation collectors, such as Instagram fundraisers and vendors who pledge their process to charities. Hopefully the guarantee that their money is being donated, will motivate more people to donate to worthy causes, such as the BLM movement.


## Objectives:
  - Create a web page for vendors to sign up and connect their PayPal accounts.
    - While signing up the vendor will give Donate Direct API access to their PayPal account associate with the pledged service
  - The web page will contain a database of all registered vendors
  - Build web service that can:
    - Monitor vendors PayPal accounts, through the PayPal API, for any changes
    - Transfers money to vendor's chosen charity
    - Notifies vendor of transfer and provides proof of donation
   
  
## Tools:
 - Google Cloud
 - PayPal API
 
## Stretch Goals:
 - User choice for percentage of proceeds donated


### Usage

To run the application locally navigate to the root directory and run:
```
python main.py
```

To refresh the google cloud instance of the web service run:
```
gcloud app deploy
```

---
### Duckhacks for Social Good
Team: Dan Pelis, Jessica Valenzuela
