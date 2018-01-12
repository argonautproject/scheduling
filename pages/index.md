---
title: Argonaut Scheduling IG HomePage
layout: default
active: home
mycss: argo-sched.css
---

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}


<!-- end TOC -->


source pages/\_include/{{page.md_filename}}.md  file

## Introduction

The [Argonaut](http://argonautwiki.hl7.org/) Scheduling Project(#.html) is a vendor agnostic specification providing FHIR RESTful APIs and guidance for access to and booking of appointments for patients by both patient and practitioner end users. This specification is based on [FHIR Version 3.0.1]({{site.data.fhir.path}}) and specifically the [Scheduling and Appointment resources]({{site.data.fhir.path}}/administration-module.html#sched).

These requirements were developed and defined by the [Argonaut](http://argonautwiki.hl7.org) pilot implementations.

## Scope


### Patient Based Scheduling:
{:.no_toc}

   - Patient searches for available appointment times for a service or procedure through an organization's on-line service ("patient portal") or a third-party application.
      - Includes scenarios when patient is a new patient ("open-scheduling" through a third party application) or an existing patient (patient portal or third-party application).
      - Only those procedures/specialties/services based on the following "simple" inputs will be available:
         - practitioner
         - available times
         - location
         - specialty
         - set of common [visit types](ValueSet-visit-type.html).
   - Patient registers and provides coverage information through a patient portal or a third-party application.
   - Patient books an appointment through a patient portal or a third-party application.
   - Patient cancels an appointment through a patient portal or a third-party application.
   - Patient retrieves their scheduled appointments through a patient portal or a third-party application.

### Provider based Scheduling:
{:.no_toc}
 Note that in this guide "provider"  =  individual, organization or healthcare service.

   - Provider scheduling between organizations on behalf of a patient
      - searches for available appointment times for a service or procedure
        - Includes scenarios when patient is a new patient or an existing patient.
        - Only those procedures/specialties/services based on the following "simple" inputs will be available:
           - practitioner
           - available times
           - location
           - specialty
           - set of common [visit types](ValueSet-visit-type.html)
      - books an appointment
      - cancels an appointment
      - Exchange of coeverage and medical history ( document only )
   - Provider retrieves their existing appointments for all patients

## Future Scope

Throughout the development of the Argonaut Scheduling Guide several additional important items were reviewed for robust scheduling implementations. This page summarizes items under development, or things that should be considered for future efforts.

1. "Discovery Operation"
    - Asks the key questions - What Service(/specialty/provider) are bookable?
        - This information is Static and is easy to prefetch.
        - It can be used as a filter when searching for appointment availability reducing the burden on server.
        - Consumer Facing apps can use this information to create appointments from slots.
        - in the future the Provider Directory (i.e., “common catalog”) can supply much of this key services information
        - In our initial scope, only those specialties/services based on the "simple inputs" - available times, location, specialty- will be available. Instead of a separate FHIR operation will document the need for an off-line exchange to coordinate the services/per provider (e.g. a spreadsheet)

1. Additional input requirements Operation
   - As stated above, in our initial scope, only those specialties/services based on the "simple inputs" - available times, location, specialty- will be available. Additional patient input and more advanced conflict checking which has been deferred to future scope.  Information like additional patient demographics, chief complaint/indication and other details to help with identifying the available appointments.   
   - for example an *Appointment$input operation* could precede the Appointment Availability Operation to discover what inputs are needed for the service.  This operation would return a questionnaire to be filled out by the End User and submitted with the Appointment Availability Operation.  Alternatively the Operation#find operation could return an OperationOutcome informing the client that information is needed and a questionnaire to be completed first.

1. Amending an appointment
   - Need to establish what if anything the consumer can update.
1. Scheduling Requests
   - Requests are “everything that is not covered by Appointment$find”
   - Patient scheduling scenario - where system could not find appointment and need to figure out what want.. sometimes out of sync, out of band ( call-back)
   - May need have a separate interaction that users can just submit the request.


1. Prior approvals including preauthorizations
  - Who has the authority to get pre-auth?
    - call center ( third party )
    - referring
    - referred-to Organization.
  - When is it needed

1. Scheduling physical (rooms, modalities, etc.) resources
1. Initiating Transitions of Care
1. Language support
1. Multimedia support
1. Estimated out of pocket patient costs
1. Provider based scheduling within an organization

## Actors

In FHIR, booking an appointment typically includes two main actors: the FHIR Server serving as the EHR scheduler and a Client as a scheduling application. For the patient based scheduling, the actors are depicted in figure 1 below.  Note that for the 3rd Party Application the scheduling application is both server for the end user application and a client of the FHIR Server.  In the patient portal use case the the end user application interacts directly with the FHIR Server.


{% include img.html img="diagrams/Slide27.png" caption="Figure 1: Actors for Patient Based Scheduling" %}

For the provider based scheduling, the actors are depicted in figure 2 below.  The referring provider's scheduling application is the client and may schedule with or without patient input.

{% include img.html img="diagrams/Slide19.png" caption="Figure 2: Actors for Provider Based Scheduling" %}

## Assumptions

### Third Party applications
{:.no_toc}
1. A third party patient scheduling application may 'pre-fetch' open slots and create appointments or it may fetch open appointments in real time.


### Login and Trust
{:.no_toc}
1. System level trust (more on this?)
1. User Level Trust:
    1. An client application has been authorized by the health system.
    1. Uses [SMART on FHIR](http://docs.smarthealthit.org/authorization/ ) authorization for apps that connect to EHR data.
    1. If the patient is successfully registered via a third-party application or logged into an EHR's patient portal, the patient ID is returned or known.
    1. 'Open-scheduling':  Authorized applications can search for available appointments without Server having to “know” the patient.
       - Later on in interaction a “patient level authorization” in order to create a new account and complete the appointment will be required.  The technical details for this are out of scope for this project.
       - Alternate approaches are out of scope for this project.

### Dependencies
{:.no_toc}

1. [US Core Profiles](http://hl7.org/fhir/us/core/index.html) are supported
1. [US Core General Guidance](http://hl7.org/fhir/us/core/guidance.html) and conventions apply to this guide.

### Rescheduling
{:.no_toc}

1. Rescheduling and appointment is a two step process of cancelling and rebooking.

## Security

For general security consideration refer to the [Security section](http://hl7.org/fhir/us/core/security.html) in the US Core Implementation Guide.  See the [Assumptions](#login-and-trust) section above for a discussion of login and trust.

## Best Practices

[#29](https://github.com/argonautproject/scheduling/issues/29) add/document- prescribe best practices. + technical operations. ( check list of steps -e.g. Client SHALL verify successful cancellation prior to rebooking ) any outside resources (like a functional model)??

...todo...


## Jekyll Site Variables(remove prior to publishing)

igName : Title of the implementation Guide (defined in ig.xml) -  {% raw %} {{site.data.fhir.igName}} {% endraw %}= {{site.data.fhir.igName}}

path : path to the main FHIR specification (defined in ig.json)-  {% raw %} {{site.data.fhir.path}} {% endraw %}= {{site.data.fhir.path}}

canonical : canonical path to this specification (defined in ig.json)-  {% raw %} {{site.data.fhir.canonical}} {% endraw %} = {{site.data.fhir.canonical}}

dependency url -  “uscore” : Base url of a dependency implementation Guide (defined in ig.json) - {% raw %}{{site.data.fhir.uscore}}{% endraw %} = {{site.data.fhir.uscore}}

errorCount : number of errors in the build file (not including HTML validation errors) -  {% raw %} {{site.data.fhir.errorCount}} {% endraw %} = {{site.data.fhir.errorCount}}

version : version of FHIR -  {% raw %} {{site.data.fhir.version}} {% endraw %} = {{site.data.fhir.version}}

revision : revision of FHIR -  {% raw %} {{site.data.fhir.revision}} {% endraw %} = {{site.data.fhir.revision}}

versionFull : version-revision -  {% raw %} {{site.data.fhir.versionFull}} {% endraw %} = {{site.data.fhir.versionFull}}

totalFiles : total number of files found by the build -  {% raw %} {{site.data.fhir.totalFiles}} {% endraw %} = {{site.data.fhir.totalFiles}}

processedFiles : number of files genrated by the build -  {% raw %} {{site.data.fhir.processedFiles}} {% endraw %} = {{site.data.fhir.processedFiles}}

genDate : date of generation (so date stamps in the pages can match those in the conformance resources) -  {% raw %} {{site.data.fhir.genDate}} {% endraw %} = {{site.data.fhir.genDate}}

----

Primary Authors: Eric Haas, Brett Marquard
