**Target Appointment:**

~~~
{
  "resourceType" : "Appointment",
  "id" : "argo-appt1",
  "meta" : {
    "profile" : [
      "http://fhir.org/guides/argonaut-scheduling/StructureDefinition/argo-appt"
    ]
  },
  "text" : {
  ...snip...
  },
  "status" : "booked",
  "serviceType" : [
  ...snip...
~~~

**Cancel using JSON PATCH**

`PATCH [Base]/Appointment/argo-appt1`

**Patch body**

~~~
 [
 { "op": "replace", "path": "Appointment/status", "value": "cancelled" },
 ]
~~~

**Cancel using XML PATCH**

`PATCH [Base]/Appointment/argo-appt1`

**Patch body**

~~~
 <?xml version="1.0" encoding="UTF-8"?>
 <diff xmlns="http://hl7.org/fhir">
   <replace sel="Appointment/status/@value">cancelled</replace>
 </diff>
~~~


**Cancel using FHIRPath PATCH**

`PATCH [Base]/Appointment/argo-appt1`

**Patch body**

~~~
 **payload**
 <?xml version="1.0" encoding="UTF-8"?>
 <Parameters xmlns="http://hl7.org/fhir">
   <parameter>
     <name value="operation"/>
     <part>
       <name value="type"/>
       <valueCode value="replace"/>
     </part>
     <part>
       <name value="path"/>
       <valueString value="status"/>
     </part>
     <part>
       <name value="value"/>
       <valueCode value="cancelled"/>
     </part>
   </parameter>
 </Parameters>
~~~

*Response*

~~~
HTTP/1.1 200 OK
Location: [base]/Appointment/argo-appt1/_history/3
[other headers]
~~~


**Resulting cancelled Appointment:**

~~~
{
  "resourceType" : "Appointment",
  "id" : "argo-appt1",
  "meta" : {
    "profile" : [
      "http://fhir.org/guides/argonaut-scheduling/StructureDefinition/argo-appt"
    ]
  },
  "text" : {
  ...snip...
  },
  "status" : "cancelled",
  "serviceType" : [
  ...snip...
~~~

<br />
