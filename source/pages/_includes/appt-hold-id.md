**Request**

`POST [base]/Appointment/proposed-appt1a-1/$hold`

**Request body**

~~~
    {
      "resourceType": "Parameters",
      "id": "pcp-hold",
      "parameter": [
        {
          "name": "appt-id",
          "valueUrl" : "Appointment/proposed-appt1a-1"
        }
      ]
    }
~~~

**Response**

~~~
HTTP/1.1 200 OK
Expires: Wed, 21 March 2018 07:28:00 GMT
[other headers]
~~~

**Response body**

~~~
    {
      "resourceType": "Bundle",
      "id": "hal-dr-y-held",
      "type": "searchset",
      "total": 2,
      "entry": [{
        "fullUrl": "http://server/path/Appointment/booked-appt1a",
        "resource": {
          "resourceType": "Appointment",
          "id": "held-appt1a",
          ...snip...
            "status" : "pending",
            "serviceType" : [
          ...snip...
        "fullUrl": "http://server/path/OperationOutcome/oo-held-appt1a",
        "resource": {
          "resourceType": "OperationOutcome",
          "id": "oo-held-appt1a-appt1a",
          .. snip ...
        }
      ]
    }
~~~
