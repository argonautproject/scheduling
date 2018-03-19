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

## Introduction

The [Argonaut](http://argonautwiki.hl7.org/) Scheduling Project is a vendor agnostic specification providing FHIR RESTful APIs and guidance for access to and booking of appointments for patients by both patient and practitioner end users. This specification is based on [FHIR Version 3.0.1]({{site.data.fhir.path}}) and specifically the [Scheduling and Appointment resources]({{site.data.fhir.path}}/administration-module.html#sched).

These requirements were developed and defined by the Argonaut pilot implementations and through the HL7 Connectathons.

## Scope


### Patient Based Scheduling:
{:.no_toc}

   - Patient searches for available appointment times for a service or procedure through an organization's on-line service ("patient portal") or a third-party application.
      - Includes scenarios when patient is a new patient ("open-scheduling" through a third party application) or an existing patient (patient portal or third-party application).
      - Only those procedures/specialties/services based on the following inputs will be available:
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
      - Only those procedures/specialties/services based on the following inputs will be available:
         - practitioner
         - available times
         - location
         - specialty
         - set of common [visit types](ValueSet-visit-type.html)
      - books an appointment
      - cancels an appointment
      - Exchange of coverage and medical history
   - Provider retrieves their existing appointments for all patients


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

#### System level trust:
{:.no_toc}

  1. Supports the [use case 5](http://argonautwiki.hl7.org/images/4/4c/Argonaut_UseCasesV1.pdf) defined for Phase 1 of the Argonaut Project.
  1. One solution is to use access FHIR resources by requesting access tokens from OAuth 2.0 compliant authorization servers using [SMART Backend Services](http://docs.smarthealthit.org/authorization/backend-services/).
  1. it is assumed that consent is managed elsewhere.

#### User Level Trust:
{:.no_toc}

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

1. Rescheduling and appointment is a two step process of canceling and rebooking.

## Security

For general security consideration refer to the [Security section](http://hl7.org/fhir/us/core/security.html) in the US Core Implementation Guide.  See the [Assumptions](#login-and-trust) section above for a discussion of login and trust.

<!--
## Best Practices

[#29](https://github.com/argonautproject/scheduling/issues/29) add/document- prescribe best practices. + technical operations. ( check list of steps -e.g. Client SHALL verify successful cancellation prior to rebooking ) any outside resources (like a functional model)
 review :

...todo...
-->

## Future Scope

Throughout the development of the Argonaut Scheduling Guide several additional important items were reviewed for robust scheduling implementations. This page summarizes items under development, or things that should be considered for future efforts.

1. "Discovery Operation"
    - This operation would asks the key questions - What Service(/specialty/provider) are bookable?  Off-line exchanges (e.g., a spreadsheet) are typically used to exchange this information. This information is Static and is easy to prefetch Amending can be used as a filter when searching for appointment availability reducing the burden on server.  Consumer Facing apps can use this information to create appointments from slots.  In the future the Provider Directory (i.e., “common catalog”) can supply much of this key services information.  But in our initial scope, only those specialties/services based on the "simple" inputs - available times, location, specialty- will be available.

1. Additional input requirements
   - As stated above, in our initial scope, only those specialties/services based on a limited set of inputs are considered.  Additional patient input and more advanced conflict checking has been deferred.  Information like additional patient demographics, chief complaint/indication and other details can help with identifying the available appointments.

   -  For example an operation could precede the search for appointment availability to discover what inputs are needed for the service.  This operation would return a questionnaire to be filled out by the end user and submitted with the appointment availability operation.  Alternatively, an operation could return an OperationOutcome resource informing the client that information is needed and a questionnaire to be completed first.

1. Amending an appointment by an end user
   - Need to establish what if anything the consumer can update.

1. Scheduling Requests
   - Appointment Requests are “everything that is not covered by an appointment availability operation”
   - Patient scheduling scenario - where system could not find appointment and need to figure out what wanted or needed.  This may sometimes results in out of sync, out of band ( call-back) responses.
   - May need have a separate interaction that users can just submit the request.

1.  Best Practices

    - Add a section prescribing best practices for technical operations. Such as a check list of steps ( Client SHALL verify successful cancellation prior to rebooking ).

1. Prior approvals including preauthorizations
1. Scheduling physical (rooms, modalities, etc.) resources
1. Initiating Transitions of Care
1. Language support
1. Multimedia support
1. Estimated out of pocket patient costs
1. Provider based scheduling within an organization

Primary Authors: Eric Haas, Brett Marquard
