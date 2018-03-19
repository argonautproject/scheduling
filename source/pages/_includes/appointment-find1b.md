appointment-find1b.md

{: #scenario-1b}

**Scenario 1b:**

Use the operation to fetch a maximum of the soonest 3 open appointments available within the next 2 days for the requested service at the Napa location.

**Request using `GET`**

`[base]/Appointment/$find?start=2017-07-15T20:00:00Z&end=2017-07-17T20:00:00Z&service-type=http://snomed.info/sct|708175003
&appt-type=http://fhir.org/guides/argonaut-scheduling/CodeSystem/appt-type|urgent&location=Napa`

**Request using `POST`**

`POST [base]/Appointment/$find&_count=3`

**Request body**

~~~
{
  "resourceType": "Parameters",
  "id": "pcp-appts",
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
      "name": "appt-type",
      "valueString": ["http://fhir.org/guides/argonaut-scheduling/CodeSystem/appt-type|urgent"]
    },
    {
      "name": "service-type",
      "valueString": ["http://snomed.info/sct|708175003"]
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
  "id": "hal-imaging-appts",
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
    "fullUrl": "http://server/path/OperationOutcome/oo-for-imaging-appts",
    "resource": {
      "resourceType": "OperationOutcome",
      "id": "oo-for-imaging-appts",
      .. snip ...
    }
  ]
}
~~~
