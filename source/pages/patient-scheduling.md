---
title: Patient based Scheduling Use Cases
layout: default
active: quidance
mycss: argo-sched.css
---

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

## Introduction

The Argonaut Scheduling Implementation Guide defines a series of interactions which cover the basic appointment creation workflow for patient based scheduling which includes: registration of patients and updating  coverage information, discovery of available appointments and booking the canceling appointments. It also covers patient access to their appointments.  The basic workflow steps and Argonaut Scheduling APIs for three use cases are detailed below.

## Use Case 1: Patient Portal Scheduling for existing patients

This use case is focused on a patient scheduling through a healthcare organization's patient portal.  The patient may be trying to book an appointment to see a particular Practitioner or for a service to be performed.

Preconditions:

- Patient has relationship to health system
- Patient uses a "patient portal" - an application hosted by his provider.
- User level login and trust

#### Scenario 1a: **Existing Patient** schedules directly with their provider
{: .no_toc}



This simple scenario serves as an effective means to scale up the complexity toward subsequent scenarios

    Patient: Hal has been with his PCP for several years. Hal has some severe back pain
             and wants to see his PCP, Dr Y, as soon as possible (today, or tomorrow at the latest).



#### Scenario 1b: **Existing Patient** schedules a service directly with their health care service
{: .no_toc}

This scenario is the same as 1a except a Service or Specialty instead of a specific Provider is being scheduled.

    Patient: Hal has been with his PCP for several years. Hal has some severe back pain and sees his PCP who
             ordered an imaging study.  Hal will be scheduling the study within the health care service.

---

{% include img.html img="diagrams/Slide28.png" caption="Figure 1: Patient Portal Scheduling for new or existing patient" %}

###  Patient login
{:.no_toc}

Before a patient can begin, she must login in to the patient portal.  This step MAY include updating or confirmation of patient  and insurance coverage information.

{% include img.html img="diagrams/Slide05.png" caption="Figure 1: Patient login" %}

The patient ID is returned or known. See the [Login and Trust](index.html#login-and-trust) Section for details.

- Updates to patient demographic information MAY be included in the login step for some systems.  However the interactions to update this information are outside the scope of this specification
- Updates to patient insurance coverage information are detailed in [Use Case 2 Step 4](#patient-registration-option-b) below

###  Appointment Availability Discovery and Search
{:.no_toc}

This step is the key transaction for this scheduling Use case. It asks the questions: when to book?  It is dynamic and complex because of multiple dependencies.<!--(In contrast, a discovery operation - which is out of scope for this version - asks the question: what Service(/specialty/provider) to book?)-->

{% include img.html img="diagrams/Slide30.png" caption="Figure 1: Appointment Availability Discovery and Search" %}

Based on the set of input parameters supplied by the Client, the Server determines which schedulable "assets" are needed for the visit and returns a set of possible Appointment times where all required assets are available. The scope of this guide is limited to the available appointments based on the following "simple" inputs:

   - practitioner
   - available times
   - location
   - specialty
   - set of common [visit types](ValueSet-visit-type.html).

#### APIs
{:.no_toc}

The following Argonaut Scheduling artifacts are used in this transaction:

- **[Appointment Availability Operation](OperationDefinition-appointment-find.html)**.
- **[Argonaut Appointment Bundle Profile](StructureDefinition-avail-bundle.html)**.
- **[Argonaut Appointment Profile](StructureDefinition-argo-appt.html)**.

#### Usage
{:.no_toc}

Using Both `GET` and `POST` Syntax the operation can be invoked as follows:

`GET [base]/Appointment/$hold?{parameters}&?{_count}`

`POST [base]/Appointment/$hold?{_count}`

#### Example
{:.no_toc}

{% include appointment-find1a.md %}

<br />

###  Optional Hold Appointment Operation
{:.no_toc}
This operation puts to appointment in a hold status to temporarily prevent the appointment from being booked by another client.  This optional step may be needed to allow the end-user to complete additional steps such as end user data entry before the booking can be completed.


{% include img.html img="diagrams/Slide31.png" caption="Figure 4: Hold Appointment" %}

 The Client sends a hold request operation using the id of selected proposed appointment as the input parameter.  The Server determines if the appointment can be held and returns the Appointment resource with with an updated status. See the [Appointment State Diagram](state-diagram.html) for further details on statuses.

#### APIs
{:.no_toc}

The following Argonaut Scheduling artifacts are used in this transaction:

  - **[Appointment Hold Operation](OperationDefinition-appointment-hold.html)**.
  - **[Argonaut Appointment Bundle Profile](StructureDefinition-avail-bundle.html)**.
  - **[Argonaut Appointment Profile](StructureDefinition-argo-appt.html)**.

#### Usage
{:.no_toc}

{% include appointment-hold.md %}
<br />


###  Book Appointment
{:.no_toc}
The actual booking of the appointment is completed in this step and the scheduling step is completed.

{% include img.html img="diagrams/Slide32.png" caption="Figure 5: Book Appointment" %}

the Client sends a book operation using the id of selected proposed appointment, the patient(s) id and optionally any comments as the input parameters.  The Server determines if the appointment can be booked and returns the Appointment resource with with an updated status. See the [Appointment State Diagram](state-diagram.html) for further details on statuses.

#### APIs
{:.no_toc}

The following Argonaut Scheduling artifacts are used in this transaction:

  - **[Appointment Hold Operation](OperationDefinition-appointment-hold.html)**.
  - **[Argonaut Appointment Bundle Profile](StructureDefinition-avail-bundle.html)**.
  - **[Argonaut Appointment Profile](StructureDefinition-argo-appt.html)**.

#### Usage
{:.no_toc}

{% include appointment-book.md %}

<br />

## Use Case 2: Open Scheduling for new patient or existing patient

This use case is focused on scheduling through a third-party application where the patient is either a new or existing patient. In either case, the patient doesn’t need to be registered or logged in with the EHR to search for an open Appointment - which is defined as "Open scheduling" for this guide.  The patient may be trying to book an appointment to see a particular Practitioner or for a service to be performed. The primary difference between Use Case 2 and Use Case 1 above are the *registration steps*. The primary difference between Use Case 2 and Use Case 3 below is fetching data in *real time* in contrast to *prefetching* scheduling data

Preconditions:

- New or existing patient
- Patient uses a third-party application to schedule an appointment
- Open scheduling model
- User level Login and trust
- Fetching available appointments in real time

#### Scenario 2a. New Patient Schedules an Appointment with a Provider without being in health system
{:.no_toc}

    Patient: Bruce just moved to the area, has a rash.  He wants to set up an appointment with Dr X as soon as
             possible (within a week or so)

#### Scenario 2b. Patient Discovers and Schedules a Service without being in a health system
{:.no_toc}

    Patient: Bruce just moved to the area, has a rash.  He wants to set up an appointment with a local
            dermatologist as soon as possible (within a week or so).

In Scenario 2a and 2b we have introduced the complexities of a new patient and a consumer facing 3rd party application to schedule the appointment.  Scenario 2b is the same as 2a except a Service or Specialty instead of a specific Provider is being scheduled.


---

{% include img.html img="diagrams/Slide29.png" caption="Figure 1: Open Scheduling for new or existing patient" %}

###  Patient Registration Option A
{:.no_toc}

For this scenario a new patient will need to be registered or an existing patient fetched prior to booking.  This MAY occur at this step or prior to booking. This step is discussed in detail in [step 4](#patient-registration-option-b) below.


###  Appointment Availability Discovery and Search
{:.no_toc}

This step is the key transaction for this Scheduling Use Case. It asks the questions: when to book? It is dynamic and complex because of multiple dependencies.

{% include img.html img="diagrams/Slide03.png" caption="Figure 1: Appointment Availability Discovery and Search" %}

This step is the same as described in [Scenario-1](#appointment-availability-discovery-and-search).

###  Optional Hold Appointment Operation
{:.no_toc}

This operation puts to appointment in a hold status to temporarily prevent the appointment from being booked by another client. This step is not optional if the patient was not registered in step 1 above. It is needed in order to register the patient prior to booking the appointment.

{% include img.html img="diagrams/Slide04.png" caption="Figure 1: Optional Hold Appointment Operation" %}

The details of this step are the same as described in [Scenario-1](#optional-hold-appointment-operation).

###  Patient Registration Option B
{:.no_toc}

A new patient will need to be registered or an existing patient fetched prior to actually booking the appointment.   This MAY occur at this step prior to booking the appointment or at the beginning of the workflow in step 1.  This step MAY include updating or confirmation of patient and insurance coverage information as well.

{% include img.html img="diagrams/Slide12.png" caption="Figure 1: Patient Registration" %}

#### Registering or Fetching a Patient:
{:.no_toc}

##### Usage
{:.no_toc}

To register a new or existing patient, The Client SHALL use the standard FHIR RESTful [create API]({{site.data.fhir.path}}/http.html#create) as follows:

`POST [base]/Patient/[id]`

In response to this transaction, the server SHOULD create a new patient resource only if the patient resource does not already exist in the system.  If the patient is already registered within the system. The existing patient resource SHOULD be returned.  Note that the Client SHALL not use the 'If-None-Exist' header as described in FHIR [conditional create API]({{site.data.fhir.path}}/http.html#ccreate)).


##### Example
{:.no_toc}

~~~json
todo inline example
~~~
<br />

#### Updating or creating Patient Coverage Information:
{:.no_toc}

Updates to patient coverage information MAY be associated with the login and registration steps for some systems or as a distinct step following booking.

##### API
{:.no_toc}

The following Argonaut Scheduling artifacts are used in this transaction:

- **[Argonaut Coverage Profile](StructureDefinition-argo-coverage.html)**.

##### Usage
{:.no_toc}

To update the existing insurance information or create it if it is new, The Client uses the standard FHIR RESTful [update and create API]({{site.data.fhir.path}}http.html) as shown:

- update: `PUT [base]/Coverage/[id]`
- create: `PUT or POST [base]/Coverage`

​Note that the server MAY reject certain updates to the coverage information (for example, type of coverage) and SHOULD return an OperationOutcome explaining the reason. (see issue #47)

##### Example
{:.no_toc}

~~~
PUT [base]/Coverage/[id]....
~~~


<br />



###  Book Appointment
{:.no_toc}

After the patient is registered, the actual booking interaction can occur.

{% include img.html img="diagrams/Slide06.png" caption="Figure 1: Book Appointment" %}

This step is the same as described in [Scenario-1](#book-appointment).

###  Patient Coverage Update Option C
{:.no_toc}

For some systems, updating or confirmation of insurance coverage information MAY occur at this step after booking. The Coverage interaction is discussed in detail in [step 4](#patient-registration-option-b) above.


## Use Case 3 Prefetching Open Slots

As in Use Case 2 above, this use case is focused on scheduling through a third-party application where the patient is either a new or existing patient. The patient may be trying to book an appointment to see a particular Practitioner or for a service to be performed. In contrast to determining available appointments in real-time, in this use case: 1) the scheduling data is fetched *prior* to the end user request, 2) the appointment availability is based upon third party application business rules, and 3) a valid appointment resources created and exchanged with the scheduling server (EHR). This is defined as "prefetching" for this guide.

Preconditions:

- New or existing patient
- Patient uses a third-party application to schedule an appointment
- Open scheduling model
- User level Login and trust
- Third Party App able to acquire:
  - Scheduling business rules for target organization
  - At a minimum FHIR resource ids for Location and Practitioner
  - Accepts subscription notifications
- FHIR Scheduling Server:
  - Supports FHIR event based subscriptions
  - Allows writing of Appointments by 3rd party applications

#### Scenario 3a. New Patient Schedules an Appointment with a Provider without being in health system
{:.no_toc}

    Patient: Bruce just moved to the area, has a rash.  He wants to set up an appointment with Dr X as soon as
             possible (within a week or so)

#### Scenario 3b. Patient Discovers and Schedules a Service without being in a health system
{:.no_toc}

    Patient: Bruce just moved to the area, has a rash.  He wants to set up an appointment with a local
            dermatologist as soon as possible (within a week or so).

In Scenario 3a and 3b we have introduced the complexities of a new patient and a consumer facing 3rd party application to schedule the appointment.  Scenario 3b is the same as 3a except a Service or Specialty instead of a specific Provider is being scheduled.

---

{% include img.html img="diagrams/Slide37.png" caption="Figure 1: Prefetching Open Slots" %}

###  Share Business Rules
{:.no_toc}

The EHR/Hospital shares the business rules and logic for creating an appointment for a particular service with the third-party application. For example, which assets are needed. This is typically an "out of band" transaction. A FHIR based transaction is out of scope for this IG.

{% include img.html img="diagrams/Slide08.png" caption="Figure 1: Share Business Rules" %}

###  Initial Load
{:.no_toc}

The third-party application fetches the "initial load" of open slots to get all the data needed supporting the creation of new appointments. The query is made for the maximum date ranges for the available slots for each provider or service and is typically repeated daily to reset or to resynchronize its information with a scheduling server.  It may `_include` the relevant actor and schedule resources so the client application is able to apply its business rules to create valid FHIR Appointment resources for transacting with the FHIR Scheduler/EHR.  

{% include img.html img="diagrams/Slide14.png" caption="Figure 1: Initial Load" %}

#### API
{:.no_toc}

The following Argonaut Scheduling artifacts are used in this transaction:

- **[Argonaut Availability Prefetch Operation](OperationDefinition-slot-prefetch.html)**
- **[Argonaut Prefetch Slot Profile](StructureDefinition-prefetch-slot.html)**
- **[Argonaut Slot Bundle Profile](StructureDefinition-slot-bundle.html)**.

#### Usage
{:.no_toc}

Using Both `GET` and `POST` Syntax the operation can be invoked as follows to fetch all open slots for the maximum period of time for relevant Practitioners, Locations and Services:

`GET [base]/Slot/$prefetch?{parameters}`

`POST [base]/Slot/$prefetch`

{% include slot-prefetch1.md %}

###  Poll for updated slots
{:.no_toc}

After fetching the "initial load" in step 2, the third-party application periodically polls for updated slots to keep the list of open slots current.

Outline:  

1. Subscribe for notifications when the "lowest schedulable entity's" schedule changes  (i.e. a Practitioner's Schedule)
1. Nofifications (essentially a feed)  payload = stripped down schedule with an actor and period
  - "heartbeat" notification with no payload
1. Subscriber uses notification to fetch the slots for that actor and time period using the same operation as the initial load above.

Detailed Documentation pending....


<!--

{ % include img.html img="diagrams/Slide15.png" caption="Figure 1: Poll for updated slots" % }

#### API
{:.no_toc}

The following Argonaut Scheduling artifacts are used in this transaction:

- **[Argonaut Prefetch Slot Profile](StructureDefinition-prefetch-slot.html)**
- **[Argonaut Slot Bundle Profile](StructureDefinition-slot-bundle.html)**.

#### Usage
{:.no_toc}

To fetch all updated slots since the last update, the Client SHALL use:

- the standard FHIR RESTful [history API]({{site.data.fhir.path}}/http.html#history)
- the `_since` parameter to only include resource versions that were created at or after the last_update or initial load.

~~~
GET [base]/Slot/_history?_since=[last-update]
~~~

Note that this operation *does not* contain any search parameters. The client must to perform additional filtering on the returned slots (for example, `status`=active ) to match the search criteria used for initial load in step 2.

#### Example
{:.no_toc}

~~~json
todo inline example
~~~

-->

###  Patient Registration Option A
{:.no_toc}

This step is identical to [Scenario 2 Step 1.](#patient-registration-option-a) above.


###  Appointment Availability Discovery and Search
{:.no_toc}

Based on the shared business rules and user input, the client application server is able to create available appointments from the prefetched slot information and return them to the end user.  How this is done is application specific and out of scope for this guide.

{% include img.html img="diagrams/Slide10.png" caption="Figure 1: Appointment Availability Discovery and Search" %}

The FHIR RESTful based interactions are the same as described in [Scenario-1 Step 2.](#appointment-availability-discovery-and-search) with the key difference that the role of the FHIR Scheduler (EHR) is replaced by the Client Application Server.  Other non-FHIR based solutions are possible as well.

###  Optional Hold Appointment Operation
{:.no_toc}

After the end user selects a preferred appointment time.  There may be additional steps such as end user data entry prior to actually booking the appointment.  The Client Application may request FHIR Scheduler (EHR) to hold this appointment to prevent it from being taken by another user.

{% include img.html img="diagrams/Slide04.png" caption="Figure 1: Optional Hold Appointment Operation" %}

 This step is similar to [Scenario 2 Step 3](#optional-hold-appointment-operation-1) above and its detailed usage is described in [Scenario-1](#optional-hold-appointment-operation).  However, in this case the Client generates an Argonaut Appointment Profile resource and exchanges it with the FHIR Scheduler as is shown in the example below.

### Example
{:.no_toc}

~~~json
todo inline example
~~~


###  Patient Registration Option B
{:.no_toc}

This step is identical to [Scenario 2 Step 4](#patient-registration-option-b) above.

###  Book Appointment
{:.no_toc}

The Client is ready to actually book the appointment and the request to book the selected Appointment is made to the FHIR Scheduler (EHR).

{% include img.html img="diagrams/Slide06.png" caption="Figure 1: Optional Hold Appointment Operation" %}

This step is similar to [Scenario 2 Step 5](#book-appointment-1) above and its detailed usage is described in [Scenario-1](#book-appointment).  However, in this case the Client generates an Argonaut Appointment Profile resource and exchanges it with the FHIR Scheduler as is shown in the example below.

#### Example
{:.no_toc}

~~~json
todo inline example
~~~

###  Patient Coverage Update Option C
{:.no_toc}

For some systems, updating or confirmation of insurance coverage information MAY occur at this step after booking. The Coverage interaction is discussed in detail in [Scenario 2 Step 4](#patient-registration-option-b) above.

## Canceling/Rescheduling appointments

The end user may elect to cancel or reschedule an existing appointment.  Rescheduling is a two step process of canceling and rebooking a new appointment.

{% include img.html img="diagrams/Slide33.png" caption="Figure 1: Patient Canceling/Rescheduling appointments" %}

Canceling and Rescheduling has the potential to introduces complex failure states. The [best practices](index.html#best-practices) guidance discusses how failures should be handled. See the [Appointment State Diagram](state-diagram.html) for further details on statuses and state transitions.

### Usage
{:.no_toc}

To cancel an appointment the Client uses the standard FHIR [`PATCH`](http://build.fhir.org/http.html#patch) transaction as shown:

`PATCH [Base]/Appointment/[id]`

-  optional input parameter:

    1. cancel [reason code](#) or string

- Note the Server SHALL declare support for JSON, XML, or FHIRPath Patch in the [CapabilityStatement](server-capstatement.html)

### Examples
{:.no_toc}

{% include cancel-examples.md %}

## Releasing holds

The length of an appointment hold is determined by the scheduling service's business rules, after which the status of the Appointment may change.  However, the Client may also elect to cancel a hold on an appointment before it expires.

{% include img.html img="diagrams/Slide38.png" caption="Figure 1: Canceling Appointment Hold" %}

### Usage
{:.no_toc}

This transaction is identical to canceling an appointment as shown [above](patient-scheduling.html#usage-6).

### Examples
{:.no_toc}

~~~json
todo inline example
~~~


## Retrieving appointments

The patient searches for their appointments.

{% include img.html img="diagrams/Slide34.png" caption="Figure 1: Patient Retrieves Their Appointments" %}


Patient access to their scheduled appointments uses the standard FHIR [search API]({{site.data.fhir.path}}/search.html).

### APIs
{:.no_toc}

The following Argonaut Scheduling artifacts are used in this transaction:

- **[Argonaut Appointment Profile](StructureDefinition-argo-appt.html)**.

### Usage
{:.no_toc}

To fetch scheduled appointments for a patient the Client SHALL use the standard RESTful [search API]({{site.data.fhir.path}}/search.html) as shown along with these standard [search parameters]({{site.data.fhir.path}}/appointment.html#search):

- `patient` (required) filter by the patient
- `status` (optional) filter by status such as ‘booked’
- `date` (optional) filter by a date or a date range ( including the date modifiers ‘ge’,’le’,’gt’,’lt’)
- `practitioner` (optional) filter by a practitioner(s)

GET [base]/Appointment?patient=[id]{&status=[status]}{&date=[date]{&date=[date]}}{&practitioner=[id]}

### Examples
{:.no_toc}

Search for all appointments for a patient with Resource ID 1234: `GET [base]/Appointment?patient=1234`

Search for all booked appointments for this patient: `GET [base]/Appointment?patient=1234&status=booked`

Fetch all completed appointments for this patient since January: `GET [base]/Appointment?patient=1234&status=fulfilled&date=ge2017-01-01`

Fetch all completed appointments with Dr Y for this patient since January : `GET [base]/Appointment?patient=1234&status=fulfilled&date=ge2017-01-01&practitioner=Dr+Y`

<br />
