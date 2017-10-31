## Examples

Using `POST` Syntax and *Parameters* resource in the payload

- [Scenario-1a](#scenario-1a)
- [Scenario-1b](#scenario-1b)
- [Scenario-2a](#scenario-2a)
- [Scenario-2b](#scenario-2b)

#### Scenario 1a: Use the operation to fetch a maximum of the soonest 3 open appointments available within the next 2 days for Dr Y at the Napa location.
{: #scenario-1a}

[Scenario Details](https://github.com/argonautproject/scheduling/wiki/Use-Cases#scenario-1a-existing-patient-schedules-directly-with-their-provider)



<!--
##### Request using `GET` Syntax

`GET [base]/Appointment/$find?...`
-->

##### Request


`POST [base]/Appointment/$find`

**payload:**

    {
      "resourceType": "Parameters",
      "id": "pcp-appts",
      "parameter": [
    {
      "name": "period",
      "valuePeriod": {
        "start" : "2017-07-15T20:00:00Z",
        "end" : "2017-07-17T20:00:00Z"
        }
     },
    {
        "name": "max",
        "valuePositiveInt": 3
      },
      {
        "name": "provider",
        "valueReference": [{
          "reference" : "Practitioner/dr-y",
          "display" : "Dr Y"
        }]
      },
      {
        "name": "location",
        "valueString": ["Napa"]
      }
    ]
    }

##### Response

    {
      "resourceType": "Bundle",
      "id": "hal-dr-y-appts",
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
        "fullUrl": "http://server/path/OperationOutcome/oo-for-dr-y-appts",
        "resource": {
          "resourceType": "OperationOutcome",
          "id": "oo-for-dr-y-appts",
          .. snip ...
        }
      ]
    }

#### Scenario 1b: Use the operation to fetch a maximum of the soonest 3 open appointments available within the next 2 days for the requested service at the Napa location.
{: #scenario-1b}
[Scenario Details](https://github.com/argonautproject/scheduling/wiki/Use-Cases#scenario-1b-existing-patient-schedules-a-service-directly-with-their-health-care-service)


<!--
##### Request using `Get` Syntax

`GET [base]/Appointment/$find?end=2017-06-20&specialty=207N00000X&location=94559&max=3`

-->

##### Request

`POST [base]/Appointment/$find`

**payload:**

    {
      "resourceType": "Parameters",
      "id": "imaging-appts",
      "parameter": [
    {
      "name": "period",
      "valuePeriod": {
        "start" : "2017-07-15T20:00:00Z",
        "end" : "2017-07-17T20:00:00Z"
        }
      },
      {
        "name": "max",
        "valuePositiveInt": 3
      },
      {
        "name": "service",
        "valueCoding": [{
            "system" : "http://fhir.org/guides/argonaut-scheduling/CodeSystem/appt-type",
            "code" : "urgent",
            "display" : "Urgent"
          },{         
              "system" : "http://snomed.info/sct",
              "code" : "708175003",
              "display" : "708175003	Diagnostic imaging service"
            }]
      },
      {
        "name": "location",
        "valueString": ["Napa"]
      }
    ]
    }

##### Response

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


#### Scenario 2a: Use the operation to 'prefetch' all of Dr Y's open appointments for the Napa location for the next month.
{: #scenario-2a}

[Scenario Details](https://github.com/argonautproject/scheduling/wiki/Use-Cases#scenario-2a-new-patient-schedules-an-appointment-with-a-provider-without-being-in-health-system)

<!--
##### Request using `GET` Syntax

`GET [base]/Appointment/$find?...`
-->

##### Request


`POST [base]/Appointment/$find`

**payload:**

    {
      "resourceType": "Parameters",
      "id": "prefetch-pcp-appts",
      "parameter": [
    {
      "name": "period",
      "valuePeriod": {
        "start" : "2017-07-15T20:00:00Z",
        "end" : "2017-08-15T20:00:00Z"
        }
      },
    {
        "name": "provider",
        "valueReference": [{
          "reference" : "Practitioner/dr-y",
          "display" : "Dr Y"
        }]
      },
    {
        "name": "location",
        "valueString": ["Napa"]
      }
    ]
    }

##### Response

    {
      "resourceType": "Bundle",
      "id": "prefetch-dr-y-appts",
      "type": "searchset",
      "total": <n>, // n = All the open Napa appts
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
        ... snip ...
        "fullUrl": "http://server/path/OperationOutcome/oo-for-dr-y-appts",
        "resource": {
          "resourceType": "OperationOutcome",
          "id": "oo-for-dr-y-appts",
         ... snip ...
        }
      ]
    }

#### Scenario 2b: Use the operation to 'prefetch' all open appointments for dermatologists in Napa location for the next month.
{: #scenario-2b}

[Scenario Details](https://github.com/argonautproject/scheduling/wiki/Use-Cases#scenario-2b-patient-discovers-and-schedules-a-service-without-being-in-a-health-system)

<!--
##### Request using `Get` Syntax

`GET [base]/Appointment/$find?end=2017-06-20&specialty=207N00000X&location=94559&max=3`

-->

##### Request

`POST [base]/Appointment/$find`

**payload:**

    {
      "resourceType": "Parameters",
      "id": "prefetch-derm-appts",
      "parameter": [
    {
      "name": "period",
      "valuePeriod": {
        "start" : "2017-07-15T20:00:00Z",
        "end" : "2017-08-17T20:00:00Z"
        }
      },
    {
          "name": "service",
          "valueCoding": [{
              "system" : "http://hl7.org/fhir/v2/0276",
              "code" : "ROUTINE",
              "display" : "Routine"
            }]
        },
      {
        "name": "specialty",
        "valueCoding": {         
            "system" : "http://snomed.info/sct",
            "code" : "394582007",
            "display" : "Dermatology"
          }
       },
      {
        "name": "location",
        "valueString": ["Napa"]
      }
    ]
    }

##### Response

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
