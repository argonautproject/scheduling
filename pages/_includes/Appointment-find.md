## Examples

#### Patient Portal Search:

**Scenario:** Bruce has a rash and wants to make an appointment with his health-system

**Assumptions:** Using the Appointment$find operation, an App searches for the next 3 available open Dermatology Appointments near Bruce.

##### Request ( using Parameters Resource in payload )

`POST [base]/Appointment/$find`

**payload:**

    {
      "resourceType": "Parameters",
      "id": "derm-appts",
      "parameter": [

        {
          "name": "period",
          "valuePeriod": [{"start": "2017-06-20"}]
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
          {
            "name": "patient",
            "resource": [{
              "resourceType": "Patient",
              "id": "bruce",
              "identifier":[{"value": "id-for-bruce"}],
              "name":{"given":["Bruce"]}
              ...}]
            }
            ...
      ]
    }

##### Response (using bundle option

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
        }
      ]
    }
