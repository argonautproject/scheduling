### Examples

#### 3rd party App Prefetch:

**Scenario:** 3rd Party App fetches open appointments from EHR.

**Assumptions:** Using the Appointment$find operation, an App searching for all open Dermatology Appointments within a particular zip code for the next two weeks.

##### Request (using GET syntax)

`GET [base]/Appointment/$find?duration=14&specialty=207N00000X&location=94559`

##### Response (using Parameter option)

    {
      "resourceType": "Parameters",
      "id": "prefetch",
      "parameter": [
        {
          "name": "available-appts",
          "resource": {
            "resourceType": "Appointment",
            "id": "prefetch-appt1",
            ...}
          },
          {
            "name": "available-appts",
            "resource": {
              "resourceType": "Appointment",
              "id": "prefetch-appt2",
              ...}
            },
            {
              "name": "available-appts",
              "resource": {
                "resourceType": "Appointment",
                "id": "prefetch-appt3",
                ...}
             }
             ...
      ]
    }
