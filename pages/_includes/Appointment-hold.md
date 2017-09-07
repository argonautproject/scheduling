## Example

#### Scenario 1a: Use the operation to book the appointment.
{: #scenario-1}

[Scenario Details](https://github.com/argonautproject/scheduling/wiki/Use-Cases#scenario-1a-existing-patient-schedules-directly-with-their-provider)

##### Request

`POST [base]/Appointment/$hold`

    **payload:**

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


##### Response ([Operation$hold Example 1a](Bundle-hal-dr-y-held.html))

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
          .. snip ...
        "fullUrl": "http://server/path/OperationOutcome/oo-held-appt1a",
        "resource": {
          "resourceType": "OperationOutcome",
          "id": "oo-held-appt1a-appt1a",
          .. snip ...
        }
      ]
    }
