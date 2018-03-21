{{page.uri}}

**Request using`POST` syntax**

`POST [base]/Slot/$prefetch`

**Request body**

~~~
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "practitioner",
      "valueDateTime" : "Practitioner/123"
    },
    {
      "name": "start",
      "valueDateTime" : "2017-07-15T00:00:00Z"
    },
    {
      "name": "end",
        "valueDateTime" : "2017-07-15T24:00:00Z"
    }
]}
~~~

**Response**

~~~
HTTP/1.1 200 OK
[other headers]
~~~

**Response body**

~~~
{
  "resourceType": "Bundle",
  "id": "prefetch-1",
  "type": "searchset",
  "total": 8,
  "entry": [{
    "fullUrl": "http://server/path/Slot/20170715240000-123",
    "resource": {
      "resourceType": "Slot",
      "id": "20170715240000-123",
      .. snip ...
      "status":"free"
      .. snip ...
    }
  ]}
~~~
