# TASK-27-API-CLIENT# API Response Example

## Raw JSON response (trimmed)

```json
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "city": "Gwenborough",
    "zipcode": "92998-3874"
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona"
  }
}
```

## Formatted output from `api_client.py`

```
========================================
  User #1
========================================
  Name    : Leanne Graham
  Email   : Sincere@april.biz
  Phone   : 1-770-736-8031 x56442
  City    : Gwenborough
  Company : Romaguera-Crona
  Website : hildegard.org
========================================
```

## Error-handling examples

| Situation | Output |
|---|---|
| User doesn't exist (`python api_client.py 999`) | `Error 404: user 999 was not found.` |
| No internet | `Error: could not connect. Check your internet connection.` |
| Slow server | `Error: the request timed out. Try again later.` |

## Interview questions (short answers)

- **What is a REST API?** An interface that lets programs communicate over HTTP using URLs as resources and methods like GET, POST, PUT, DELETE, usually exchanging JSON.
- **What is HTTP status code 200?** "OK": the request succeeded and the response contains the data.
- **GET vs POST?** GET retrieves data and puts parameters in the URL; it should not change anything on the server. POST sends data in the request body to create or submit something, and does change server state.
