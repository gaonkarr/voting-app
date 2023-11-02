### Voting-app

This is a simple API service built for various tests purposes. This application is a scaled down version of (and it's been inspired by) [Yelb](https://github.com/mreferre/yelb/).

The application puts and stores "votes" in an Amazon DynamoDB table - `restaurants-voting-app`. You can vote by just CURLing (or similar) to 4 APIs: 
```
/api/restaurant-1
/api/restaurant-2
/api/restaurant-3
/api/restaurant-4
```
In addition to vote, you can query the status by CURLing (or similar) the `/api/getvotes` API. 

If you hit the `/` path of the service a summary of the various APIs available is provided. This path only serves static content and does not test DynamoDB connectivity. 

#### Variables

- `DDB_AWS_REGION` this variable is required and needs to be set to the region of the DynamoDB table.
- `DDB_TABLE_NAME` this variable is optional and contains the DynamoDB table name (default: `restaurants-voting-app`)


#### Deploying the application with other services and platforms  

The application comes with its `requirements.txt` file and SAM `template.yaml`. It also provides`prepare.sh` that can help you set the variables, create the DynamoDB table and add some sample votes.
To deploy this application, run `sam build` and `sam deploy --guided`. Note the URL in output to access the application.


#### Licensing

This application is made available under the [MIT license](./LICENSE). The Python prerequisite required to run this application and their licensing are as follows:
```
Flask - BSD License 
Flask-Cors - MIT License
Boto3 - Apache License 2.0
Botocore - Apache License 2.0
Simplejson - Academic Free License (AFL), MIT License (MIT License)