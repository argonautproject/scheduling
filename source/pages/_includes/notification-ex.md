##### Notification of schedule change:
{:.no_toc}

`POST https://feed-handler.com/notification`

**Notification body**

~~~
{
  "resourceType" : "Schedule",
  "id" : "example1",
  "actor" : [
    {
      "reference" : "Practitioner/1",
      "display" : "Crusher, Beverly"
    }
  ],
  "planningHorizon" : {
    "start" : "2018-02-13",
    "end" : "2018-02-13"
  }
}
~~~

##### "Heartbeat" Notification:
{:.no_toc}
~~~
POST https://feed-handler.com/notification

**** No notification body****
~~~
