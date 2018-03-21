## Examples

#### Patient Portal Search:

**Scenario:** Bruce has a rash and wants to make an appointment with his health-system

**Assumptions:** Using the Appointment$availability operation, an App searches for the next available open Dermatology Appointments near Bruce.

##### Request using POST Syntax

`POST [base]/Appointment/$availability{?_count=3&location.address=[Bruce's Zip Code]}`

**Operation's payload: the *Appointment* resource as an input parameter which is wrapped inside the *Parameters* resource**


      {
        "resourceType": "Parameters",
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


##### Response using *Bundle* containing 3 proposed appointments and an OperationOutcome with errors/warnings/information:

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
      ]
    }
