**Request**

`POST [base]/Patient`

**Request body**

~~~
{
  "resourceType" : "Patient",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
    ]
  },
...snip...
  "active" : true,
  "name" : [
    {
      "family" : "Shaw",
      "given" : [
        "Amy",
        "V."
      ]
    }
  "gender" : "female",
  "birthDate" : "2007-02-20",
...snip...
}
~~~

**Response**

~~~
HTTP/1.1 201 Created
Location: [base]/Patient/server-id-123/_history/1
[other headers]
~~~
