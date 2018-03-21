**Request**

`POST [base]/Appointment/$book`

**Appointment resource as request body**

~~~
{
  "resourceType" : "Appointment",
...snip...
  "status" : "pending",
  "serviceType" : [
...snip...
  "start" : "2017-07-17T01:00:00Z",
  "end" : "2017-07-17T01:15:00Z",
  "participant" : [
    {
      "actor" : {
        "reference" : "Practitioner/dr-y",
        "display" : "Dr Y"
...snip...
}

~~~

**Parameter format as request body**

~~~  
      {
        "resourceType": "Parameters",
        "parameter": [
          {
            "name": "appt-resource",
            "resource":{
                        "resourceType" : "Appointment",
                        "id" : "proposed-appt2",
                      ...snip...
                        "status" : "pending",
                        "serviceType" : [
                      ...snip...
                        "start" : "2017-07-17T01:00:00Z",
                        "end" : "2017-07-17T01:15:00Z",
                        "participant" : [
                          {
                            "actor" : {
                              "reference" : "Practitioner/dr-y",
                              "display" : "Dr Y"
                      ...snip...
            }

          }
        ]
      }

~~~

**Response**

~~~
HTTP/1.1 201 Created
Location: [base]/Appointment/argo-appt-1/_history/1
[other headers]
~~~

**Response body**

~~~

    {
      "resourceType": "Bundle",
      "id": "argo-appt-1",
      "type": "searchset",
      "total": 2,
      "entry": [{
        "fullUrl": "http://server/path/Appointment/scheduled-appt2a",
        "resource": {
          "resourceType": "Appointment",
          "id": "held-appt2a",
          ...snip...
            "status" : "booked",
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
