##### A JSON example:
{:.no_toc}

Target Appointment:

    {
      "resourceType" : "Appointment",
      "id" : "proposed-appt1",
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

*Cancel using PATCH*

`PATCH [Base]/Appointment/[id]`

         **payload**

         [
         { "op": "replace", "path": "Appointment/status", "value": "cancelled" },
         ]

Resulting cancelled Appointment:

    {
      "resourceType" : "Appointment",
      "id" : "proposed-appt1",
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


##### An XML example:
{:.no_toc}

Target Appointment:

     <?xml version="1.0" encoding="UTF-8"?>
     <Appointment xmlns="http://hl7.org/fhir">
       <id value="proposed-appt1"/>
       <meta>
         <profile
                  value="http://fhir.org/guides/argonaut-scheduling/StructureDefinition/argo-appt"/>
       </meta>
       <text>
      ...snip
       </text>
       <status value="booked"/>
       <serviceType>
        ...snip...

*Cancel using PATCH*

`PATCH [Base]/Appointment/[id]`

     **payload**

     <?xml version="1.0" encoding="UTF-8"?>
     <diff xmlns="http://hl7.org/fhir">
       <replace sel="Appointment/status/@value">cancelled</replace>
     </diff>

Resulting cancelled Appointment:

     <?xml version="1.0" encoding="UTF-8"?>
     <Appointment xmlns="http://hl7.org/fhir">
       <id value="proposed-appt1"/>
       <meta>
         <profile
                  value="http://fhir.org/guides/argonaut-scheduling/StructureDefinition/argo-appt"/>
       </meta>
       <text>
      ...snip...
       </text>
       <status value="cancelled"/>
      ...snip...

##### A [FHIRPath](http://hl7.org/fhirpath/) example:
{:.no_toc}

Target Appointment:

    {
      "resourceType" : "Appointment",
      "id" : "proposed-appt1",
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

*Cancel using PATCH*

`PATCH [Base]/Appointment/[id]`

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


Resulting cancelled Appointment:

    {
      "resourceType" : "Appointment",
      "id" : "proposed-appt1",
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

<br />
