# Cosmos DB - device API

## Python app to simulate streaming data from devices to CosmosDB using Mongo API.

### Installation
1. Clone repository.
2. Create docker image using command: docker build -t {name of image} .
3. Run container:
```docker run -e CONNECTION_STRING="CONNECTION STRING" -e DB_NAME="DATABASE" -e COLLECTION_NAME="Collection" -e BATCH_SIZE=10 -e DEVICE_ID="device_id"  image-name```
4. Check if data are in CosmosDB.
