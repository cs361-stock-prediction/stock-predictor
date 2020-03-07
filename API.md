# API Documentation

### Get stock data

`GET:/api/stockdata/<ticker>`

Payload:
```json
{
	timeframe: "week"|"month"|"year"
}
```

Reply:
```json
{
	<ticker>: [
		[date, [$open, $close]], 
		[date, [$open, $close]], 
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
    timeframe: "week"|"month"|"year"
}
```

Reply:
```json
{
	<ticker>: [
		[date, [$open, $close]], 
		[date, [$open, $close]], 
		...
	]
}
```
(Date being in increments of one day for all timeframes)

### Get saved stocks for current user

`GET:/api/accountsaved/`

Payload:
```json
{
	session-id: ""
}
```

Reply:
```json
{
	saved: [
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
	session-id: ""
}
```

Reply:
```json
{
	history: [
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
	session-id: "",
	ticker: "<ticker>"
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
	session-id: "",
	ticker: "<ticker>"
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
	session-id: "",
	ticker: "<ticker>"
}
```

Reply:
```json
200 OK / 201 Created
```
(OR `401 Unauthorized` if account session has expired)


