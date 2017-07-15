## Examples

#### Scenario 1a Patient Portal Search:

**Scenario:**

**Assumptions:**

##### Request using `Get` Syntax

`GET [base]/Appointment/$find?end=2017-06-20&provider=Practitioner/123&max=3`

##### Request using `POST` Syntax and 'Parameters' resource in payload )

`POST [base]/Appointment/$find`

**payload:**

##### Response

#### Scenario 1b Patient Portal Search:

**Scenario:** Bruce has a rash and wants to make an appointment with his health-system

**Assumptions:** Using the Appointment$find operation, an App searches for the next 3 available open Dermatology Appointments near Bruce.

##### Request using `Get` Syntax

`GET [base]/Appointment/$find?end=2017-06-20&specialty=207N00000X&location=94559&max=3`

##### Request using `POST` Syntax and 'Parameters' resource in payload )

`POST [base]/Appointment/$find`

**payload:**

    {
      "resourceType": "Parameters",
      "id": "derm-appts",
      "parameter": [

        {
          "name": "end",
          ["valueDateTime": 2017-06-20"]
          },
          {
            "name": "max",
            "valuePositiveInt": 3
          },
          {
            "name": "specialty",
            "valueCodeableConcept": [{"system": "http://nucc.org/provider-taxonomy","code": "207N00000X","display": "Dermatology"}]
          },
          {
            "name": "location",
            "valueString": ["Napa"]
          },
            ...
      ]
    }

##### Response

    {
      "resourceType": "Bundle",
      "id": "bruce-derm-appts",
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
