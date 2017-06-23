## Examples

#### Patient Portal Search:

**Scenario:** Bruce has a rash and wants to make an appointment with his health-system

**Assumptions:** Using the Appointment$availability operation, an App searches for the next available open Dermatology Appointments near Bruce.

##### Request (using Parameters Resource in payload )

`POST [base]/Appointment/$availability{?_count&location.address=[Bruce's Zip Code]}`

**using *Parameters* Resource for payload:**


      {
        "resourceType": "Parameters",
        "id": "derm-appts",
        "parameter": [
          {
            "name": "appointment",
            "resource": {
              "resourceType": "Appointment",
              "id": "appt1",
              ...}
            }
        ]
      }


##### Response using *Bundle*:

    {
      "resourceType": "Bundle",
      "id": "bruce-derm-appts",
      "type": "searchset",
      "total": 4,
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
        "fullUrl": "http://server/path/OperationOutcome/proposed-appt-3",
        "resource": {
          "resourceType": "OperationOutcome",
          "id": "oo-for-derm-appts",
          .. snip ...
      ]
    }
