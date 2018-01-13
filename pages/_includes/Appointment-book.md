source file:  _includes/appointment-book.md

The operation can be invoked as follows:

   `POST [base]/Appointment/$book`

##### Examples
{:.no_toc}
<!--
- [Scenario-1](#scenario-1)
- [Scenario-2](#scenario-2)

#### Scenario 1a: Use the operation to book the appointment.
{: #scenario-1}

[Scenario Details](https://github.com/argonautproject/scheduling/wiki/Use-Cases#scenario-1a-existing-patient-schedules-directly-with-their-provider)

##### Request

`POST [base]/Appointment/$book`

    **payload:**

    {
      "resourceType": "Parameters",
      "id": "pcp-book",
      "parameter": [
        {
          "name": "appt-id",
          "valueUrl" : "Appointment/proposed-appt1a-1"
        },
        {
          "name": "comment",
          "valueString" : "this is an appointment comment how long can it be?"
        }

      ]
    }


##### Response ([Operation$book Example 1a](Bundle-hal-dr-y-book.html))

    {
      "resourceType": "Bundle",
      "id": "hal-dr-y-booked",
      "type": "searchset",
      "total": 2,
      "entry": [{
        "fullUrl": "http://server/path/Appointment/booked-appt1a",
        "resource": {
          "resourceType": "Appointment",
          "id": "booked-appt1a",
          .. snip ...
        "fullUrl": "http://server/path/OperationOutcome/oo-booked-appt1a",
        "resource": {
          "resourceType": "OperationOutcome",
          "id": "oo-booked-appt1a",
          .. snip ...
        }
      ]
    }
-->
~~~
#### Request

`POST [base]/Appointment/$book`

    **payload:**

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

##### Response ([Operation$book Example 2a](Bundle-derm-book.html))

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
              .. snip ...
            "fullUrl": "http://server/path/OperationOutcome/oo-booked-derm-appt",
            "resource": {
              "resourceType": "OperationOutcome",
              "id": "oo-booked-derm-appt",
              .. snip ...
            }
          ]
        }
~~~
