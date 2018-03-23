

{: #scenario-1a}

**Scenario 1a:**

Use the operation to fetch a maximum of the soonest 3 open appointments available within the next 2 days for Dr Y at the Napa location.

**Request using `GET`**

`GET [base]/Appointment/$find?start=2017-07-15T20:00:00Z&end=2017-07-17T20:00:00Z&provider=Practitioner/dr-y&location=Napa&_count=3`

**Request using `POST`**

`POST [base]/Appointment/$find&_count=3`

**Request body**

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
        },
        {
          "name": "provider",
          "valueUri": ["Practitioner/dr-y"]
          }
        },
        {
          "name": "location",
          "valueString": ["Napa"]
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
      "id": "hal-dr-y-appts",
      "type": "searchset",
      "total": 3,
      "entry": [{
        "fullUrl": "http://server/path/Appointment/proposed-appt-1",
        "resource": {
          "resourceType": "Appointment",
          "id": "proposed-appt-1",
          .. snip ...
        },
        "fullUrl": "http://server/path/Appointment/proposed-appt-2",
        "resource": {
          "resourceType": "Appointment",
          "id": "proposed-appt-2",
          .. snip ...
        },
        "fullUrl": "http://server/path/Appointment/proposed-appt-3",
        "resource": {
          "resourceType": "Appointment",
          "id": "proposed-appt-3",
          .. snip ...
        },
        "fullUrl": "http://server/path/OperationOutcome/oo-for-dr-y-appts",
        "resource": {
          "resourceType": "OperationOutcome",
          "id": "oo-for-dr-y-appts",
          .. snip ...
        }
      ]
    }
~~~
