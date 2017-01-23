# RSAL API

## endpoints
### request publication of dataset
`host/release` : `POST`, JSON encoded with parameters:

 - `datasetIdentifier` : local identifier for dataset
 - other parameters as necessary

return values: HTTP code 200 and 'ok', or *HTTP error code TDB*

## messages
*TBD - dataverse endpoint for these messages*

### dataset released
Whatever operations have happened to make the dataset accessable to users have finished.

