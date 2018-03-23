Prefetch open slots from July 15,2017 to August 17,2017

**Request using `GET` Syntax**

`GET  [base]/Slot/$prefetch?start=2017-07-15T20:00:00Z&end=2017-07-17T20:00:00Z`

**Request using `POST` Syntax**

`POST [base]/Slot/$prefetch`

**Post request body**

~~~
    {
      "resourceType": "Parameters",
      "parameter": [
        {
          "name": "start",
          "valueDateTime" : "2017-07-15T20:00:00Z"
        },
        {
          "name": "end",
            "valueDateTime" : "2017-07-17T20:00:00Z"
        }
    ]
    }
~~~

**Response**

~~~
HTTP/1.1 200 OK
[other headers]
~~~

**Response body**

~~~
    {
      "resourceType": "Bundle",
      "id": "prefetch-1",
      "type": "searchset",
      "total": 1000,
      "entry": [{
        "fullUrl": "http://server/path/Slot/1",
        "resource": {
          "resourceType": "Slot",
          "id": "1",
          .. snip ...
          "status":"free"
          .. snip ...
        },
        "fullUrl": "http://server/path/Slot/2",
        "resource": {
          "resourceType": "Slot",
          "id": "2",
          .. snip ...
          "status":"free"
          .. snip ...
        },
        "fullUrl": "http://server/path/Slot/3",
        "resource": {
          "resourceType": "Slot",
          "id": "3",
          .. snip ...
          "status":"free"
          .. snip ...
        },
        "fullUrl": "http://server/path/OperationOutcome/oo-for-prefetch",
        "resource": {
          "resourceType": "OperationOutcome",
          "id": "oo-for-prefetch",
          .. snip ...
        }
      ]
    }
~~~
