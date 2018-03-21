**Request to create Coverage resource for patients**

`POST [base]/Coverage`

**Request body**

~~~
{
  "resourceType" : "Coverage",
  "identifier" : [
    {
      "system" : "https://www.anthem.com/ca",
      "value" : "DZW9200000000"
    }
  ],
  "status" : "active",
  ...snip...
  "period" : {
    "start" : "2016-01-01"
  },
  "payor" : [
    {
      "display" : "Anthem Blue Cross of California"
    }
  ],
  "grouping" : {
    "plan" : "1FZQ",
    "planDisplay" : "Anthem Bronze 60 D HSA PPO"
  }
}
~~~

**Response**

~~~
HTTP/1.1 201 Created
Location: [base]/Coverage/argo-sch-1/_history/1
[other headers]
~~~

**Request to update Coverage to extend coverage period**

`PUT [base]/Coverage/argo-sch-1`

**Request body**

~~~
{
  "resourceType" : "Coverage",
  "id" : "argo-sch-1",
  "identifier" : [
    {
      "system" : "https://www.anthem.com/ca",
      "value" : "DZW9200000000"
    }
  ],
  "status" : "active",
  ...snip...
  "period" : {
    "start" : "2018-01-01"
  },
  "payor" : [
    {
      "display" : "Anthem Blue Cross of California"
    }
  ],
  "grouping" : {
    "plan" : "1FZQ",
    "planDisplay" : "Anthem Bronze 60 D HSA PPO"
  }
}
~~~

**Response**

~~~
HTTP/1.1 200 OK
Location: [base]/Coverage/argo-sch-1/_history/2
[other headers]
~~~
