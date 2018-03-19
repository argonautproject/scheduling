**Request**

`POST [base]/Appointment/proposed-appt2a-1/$book`

**Request body**

~~~
    {
      "resourceType": "Parameters",
      "id": "pcp-appts",
      "parameter": [
        {
          "name": "appt-id",
          "valueUrl" : "Appointment/proposed-appt2a-1"
        },
        {
          "name": "patient-id",
            "valueDateTime" : "Patient/1234"
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
          "id": "derm-booked",
          "type": "searchset",
          "total": 2,
          "entry": [{
            "fullUrl": "http://server/path/Appointment/booked-derm-appt",
            "resource": {
              "resourceType": "Appointment",
              "id": "booked-derm-appt",
              ...snip...
                "status" : "booked",
                "serviceType" : [
              ...snip...
            "fullUrl": "http://server/path/OperationOutcome/oo-booked-derm-appt",
            "resource": {
              "resourceType": "OperationOutcome",
              "id": "oo-booked-derm-appt",
              .. snip ...
            }
          ]
        }
~~~
