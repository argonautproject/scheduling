## Examples

Using Both `GET` and `POST` Syntax

- [Scenario-1a](#scenario-1a)
- [Scenario-1b](#scenario-1b)
- [Scenario-2a](#scenario-2a)
- [Scenario-2b](#scenario-2b)

#### Scenario 1a: Use the operation to fetch a maximum of the soonest 3 open appointments available within the next 2 days for Dr Y at the Napa location.
{: #scenario-1a}

[Scenario Details](https://github.com/argonautproject/scheduling/wiki/Use-Cases#scenario-1a-existing-patient-schedules-directly-with-their-provider)

##### Request

**Using `GET`**

`GET [base]/Appointment/$find?start=2017-07-15T20:00:00Z&end=2017-07-17T20:00:00Z&max=3&provider=Practitioner/dr-y&location=Napa`

**Using `POST`**

`POST [base]/Appointment/$find`

    **payload:**

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
          "name": "max",
          "valuePositiveInt": 3
        },
        {
          "name": "provider",
          "valueUri": ["Practitioner/dr-y"]
          }
        },
        {
          "name": "location",
          "valueString": ["Napa"]
        }
    ]
    }

##### Response ([Operation$find Example 1a](Bundle-hal-dr-y-appts.html))


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

##### Request using `GET` Syntax

    GET  [base]/Appointment/$find?start=2017-07-15T20:00:00Z&end=2017-07-17T20:00:00Z&max=3&service-type=http://snomed.info/sct|708175003
    &appt-type=http://fhir.org/guides/argonaut-scheduling/CodeSystem/appt-types|urgent&location=Napa

##### Request using `POST` Syntax

`POST [base]/Appointment/$find`

    **payload:**

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
          "name": "max",
          "valuePositiveInt": 3
        },
        {
          "name": "appt-type",
          "valueString": ["http://fhir.org/guides/argonaut-scheduling/CodeSystem/appt-types|urgent"]
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

`GET [base]/Appointment/$find?start=2017-07-15T20:00:00Z&end=2017-08-17T20:00:00Z&
 provider=Practitioner/dr-y&location=Napa`

**Using `POST`**

`POST [base]/Appointment/$find`

    **payload:**

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
          "name": "provider",
          "valueUri": ["Practitioner/dr-y"]
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

##### Request using `GET` Syntax

    GET [base]/Appointment/$find?start=2017-07-15T20:00:00Z&end=2017-08-17T20:00:00Z&appt-type=http://hl7.org/fhir/v2/0276|ROUTINE&
     specialty=http://snomed.info/sct|394582007&location=Napa

##### Request using `POST` Syntax

`POST [base]/Appointment/$find`

    **payload:**

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

##### Response ([Operation$find Example 2b](Bundle-prefetch-derm-appts.html))

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
