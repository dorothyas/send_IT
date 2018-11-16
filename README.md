[![Build Status](https://travis-ci.com/dorothyas/send_IT.svg?branch=API-feature)](https://travis-ci.com/dorothyas/send_IT)
[![Coverage Status](https://coveralls.io/repos/github/dorothyas/send_IT/badge.svg?branch=develop)](https://coveralls.io/github/dorothyas/send_IT?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/12bd3858a3bc8cdf3343/maintainability)](https://codeclimate.com/github/dorothyas/send_IT/maintainability)

SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.

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

• The UI folder houses the user interface. To access the user interface, open the index.html.
• The api folder contains the system backend services.

## Built with
- HTML
- Python 3
- CSS

## Prerequisites
- GIT

• to update and clone the repository
``` 
$ git clone
```

- IDE e.g Visual Studio Code
- Postman

### Activate virtual enviroment
``` 
$  venv venv
 source /env/bin/activate

```
### Install dependencies
``` 
$ pip install -r requirements.txt

```
### Running Tests
• To run tests, use the command below;
``` 
$ pytest

```
### Run server
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

## Project links:
•	Github Pages: https://dorothyas.github.io/send_IT/UI

• Heroku : https://stargal-dorothy.herokuapp.com/api/v1/parcels
## Author
- Dorothy Asiimwe
