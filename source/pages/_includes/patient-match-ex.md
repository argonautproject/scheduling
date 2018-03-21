**Request**

POST [base]/Patient/$match

**Request body**

~~~
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "resource",
      "resource": {
        "resourceType": "Patient",
        "identifier": [
          {
            "use": "usual",
            "type": {
              "coding": [
                {
                  "system": "http://hl7.org/fhir/v2/0203",
                  "code": "MR"
                }
              ]
            },
            "system": "urn:oid:1.2.36.146.595.217.0.1",
            "value": "12345"
          }
        ],
        "name": [
          {
            "family": [
              "Chalmers"
            ],
            "given": [
              "Peter"
            ]
          }
        ],
        "gender": "male",
        "birthDate": "1974-12-25"
      }
    },
    {
      "name": "count",
      "valueInteger": "3"
    },
    {
      "name": "onlyCertainMatches",
      "valueBoolean": "false"
    }
  ]
}
~~~

**ResponseResults from imaginary MPI algorithm:**

~~~
HTTP/1.1 200 OK
[other headers]
~~~

**Response body**

~~~
{
  "resourceType": "Bundle",
  "id": "26419249-18b3-45de-b10e-dca0b2e72b",
  "meta": {
    "lastUpdated": "2016-03-18T03:28:49Z"
  },
  "type": "searchset",
  "total": 2,
  "entry": [{
    "fullUrl": "http://server/path/Patient/example",
    "resource": {
      "resourceType": "Patient",
      "id": "example",
      .. snip ...
    },
    "search": {
      "extension": [{
        "url": "http://hl7.org/fhir/StructureDefinition/match-grade",
        "valueCode": "certain"
      }],
      "mode": "match",
      "score": 0.9
    }
  },{
    "fullUrl": "http://server/path/Patient/292",
    "resource": {
      "resourceType": "Patient",
      "id": "292",
      .. snip ...
    },
    "search": {
      "extension": [{
        "url": "http://hl7.org/fhir/StructureDefinition/match-grade",
        "valueCode": "possible"
      }],
      "mode": "match",
      "score": 0.2
    }
  }]
}
~~~
