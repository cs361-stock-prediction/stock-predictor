# API Documentation

## General methods:

### Stock search

```
GET:/search?query=<ticker>
```

```
POST:/search
	session-id: ""
	query: <ticker>
```

Reply:
Search result webpage, not JSON


This request uses HTML form requests to send querys. 
See [the MDN documentation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data#On_the_server_side_retrieving_the_data) for how the payload is structured.

### Get stock data

`GET:/api/stockdata/<ticker>`

Payload:
```json
{
	'timeframe': "week"|"month"|"year"
}
```

Reply:
```json
{
	'<ticker>': [
		["date", [$open, $close]], 
		["date", [$open, $close]], 
		...
	] 
}
```
(Date being in increments of one day for all timeframes)

### Get stock prediction

`GET:/api/stockpredict/<ticker>`

Payload:
```json
{
	'timeframe': "week"|"month"|"year"
}
```

Reply:
```json
{
	'<ticker>': [
		["date", [$open, $close]], 
		["date", [$open, $close]], 
		...
	]
}
```
(Date being in increments of one day for all timeframes)

## Account methods:

### Get saved stocks for current user

`GET:/api/accountsaved/`

Payload:
```json
{
	'session-id': ""
}
```

Reply:
```json
{
	'saved': [
		"ticker",
		"ticker",
		...
	]
}
```
(OR `401 Unauthorized` if account session has expired)

### Get view history for current user

`GET:/api/accounthist/`

Payload:
```json
{
	'session-id': ""
}
```

Reply:
```json
{
	'history': [
		"ticker",
		"ticker",
		...
	]
}
```
(OR `401 Unauthorized` if account session has expired)

### Save stock to current user account

`POST:/api/accountsaved/`

Payload:
```json
{
	'session-id': "",
	'ticker': "<ticker>"
}
```

Reply:
```json
200 OK
```
(OR `401 Unauthorized` if account session has expired)

### Remove saved stock from current user account

`DELETE:/api/accountsaved/`

Payload:
```json
{
	'session-id': "",
	'ticker': "<ticker>"
}
```

Reply:
```json
200 OK
```
(OR `401 Unauthorized` if account session has expired)

### Add stock to view history for current user

`PUT:/api/accounthist/`

Payload:
```json
{
	'session-id': "",
	'ticker': "<ticker>"
}
```

Reply:
```json
200 OK
```
(OR `401 Unauthorized` if account session has expired)


