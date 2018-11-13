[![Build Status](https://travis-ci.com/dorothyas/send_IT.svg?branch=API-feature)](https://travis-ci.com/dorothyas/send_IT)
[![Coverage Status](https://coveralls.io/repos/github/dorothyas/send_IT/badge.svg?branch=develop)](https://coveralls.io/github/dorothyas/send_IT?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/12bd3858a3bc8cdf3343/maintainability)](https://codeclimate.com/github/dorothyas/send_IT/maintainability)

SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.
## Project links:
•	Github Pages: https://dorothyas.github.io/send_IT/UI

## Project Functionality
### User Interface
- Users can create an account and log in.
- Users can create a parcel delivery order.
- Users can change the destination of a parcel delivery order.
- Users can cancel a parcel delivery order.
- Users can see the details of a delivery order.
- Admin can change the status and present location of a parcel delivery order.

### API endpoints

- Fetch all parcel delivery orders
- Fetch a specific parcel delivery order
- Fetch all parcel delivery orders by a specific user
- Cancel the specific parcel delivery order
- Create a parcel delivery order

## Prerequisites
- GIT
- IDE e.g Visual Studio Code
- Postman
- HTML5

## installed packages
- python 3.7
``` 
$ pip install -r requirements.txt
```
## run server
``` 
$ python run.py
```

## Endpoints

|Endpoint |Functionality |
|---------|:------------:|
|GET /parcels|Fetch all parcel delivery orders| 
|GET /parcels/<parcelId>|Fetch a specific parcel delivery order|
|GET /users/<userId>/parcels |Fetch all parcel delivery orders by a specific user |
|PUT /parcels/<parcelId>/cancel|Cancel the specific parcel delivery order|
|POST /parcels| Create a parcel delivery order| 

## Author
- Dorothy Asiimwe
