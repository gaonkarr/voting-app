### Votingapp

This is a simple API service built for various tests purposes. This application is a scaled down version of (and it's been inspired by) [Yelb](https://github.com/mreferre/yelb/).

The application puts and stores "votes" in an Amazon DynamoDB table. You can vote by just CURLing (or similar) to 4 APIs: 
```
/api/restaurant-1
/api/restaurant-2
/api/restaurant-3
/api/restaurant-4
```
In addition to vote, you can query the status by CURLing (or similar) the `/api/getvotes` API. 

If you hit the `/` path of the service a summary of the various APIs available is provided. This path only serves static content and does not test DynamoDB connectivity. 
