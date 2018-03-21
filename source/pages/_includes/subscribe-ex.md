**Subscribe**

`POST [base]/Subscription`

**Request body**

~~~
    {
      "resourceType": "Subscription",
      "id": "example",
      "status": "active",
      "reason": "Notify subscriber of schedule changes to trigger the subscriber prefetch updated slots",
      "_criteria": {
        "extension": [
          {
            "url": "http://fhir.org/guides/argonaut-scheduling/StructureDefinition/extension-subscription-triggerevent",
            "valueString": "schedule where any slot that reference it has changed"
          },
          {
            "url": "http://fhir.org/guides/argonaut-scheduling/StructureDefinition/extension-subscription-eventfocus",
            "valueCode": "Schedule"
          }
        ]
      },
      "channel": {
        "extension": [
          {
            "url": "http://fhir.org/guides/argonaut-scheduling/StructureDefinition/extension-subscription-payloadprofile",
            "valueUri": "//fhir.org/guides/argonaut-scheduling/StructureDefinition/argo-sched-notif"
          }
        ],
        "type": "rest-hook",
        "endpoint": "https://feed-handler.com/notification",
        "payload": "application/fhir+json"
      }
    }
~~~

**Response**

~~~
HTTP/1.1 200 OK
[other headers]

~~~
