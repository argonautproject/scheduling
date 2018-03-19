appointment-find2b.md

{: #scenario-2b}

**Scenario 2b:**

Use the operation to fetch all open appointments for dermatologists in Napa location for the next month.
**Request using `GET`**

`GET [base]/Appointment/$find?start=2017-07-15T20:00:00Z&end=2017-08-17T20:00:00Z&appt-type=http://hl7.org/fhir/v2/0276|ROUTINE&
     specialty=http://snomed.info/sct|394582007&location=Napa`

**Request using `POST`**

`POST [base]/Appointment/$find&_count=3`

**Request body**

~~~
{
  "resourceType": "Parameters",
  "id": "prefetch-derm-appts",
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
    "valueString": ["http://hl7.org/fhir/v2/0276|ROUTINE"]
  },
  {
    "name": "specialty",
    "valueString": ["http://snomed.info/sct|394582007"]
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
  "id": "prefetch-derm-appts",
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
    "fullUrl": "http://server/path/OperationOutcome/oo-for-derm-appts",
    "resource": {
      "resourceType": "OperationOutcome",
      "id": "oo-for-derm-appts",
      .. snip ...
    }
  ]
}
~~~
