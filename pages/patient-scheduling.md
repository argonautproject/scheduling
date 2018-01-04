---
title: Patient based Scheduling Use Cases
layout: default
active: quidance
---

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

### Introduction

The Argonaut Scheduling Implementation Guide defines a series of interactions which cover the basic appointment creation workflow for patient base scheduling which includes: registration of patients and updating  coverage information, discovery of available appointments and booking the cancelling appointments. It also covers patient access to their appointments.  The basic workflow steps and Argonaut Scheduling APIs for three use cases are detailed below.

### Use Case 1: Patient Portal Scheduling for existing patients

This use case is focused on a patient scheduling through a healthcare organization's patient portal.  The patient may be trying to book an appointment to see a particular Practitioner or for a service to be performed.

Preconditions:

- Patient has relationship to health system
- Patient uses a "patient portal" - an application hosted by his provider.
- User level lgoin and trust

##### Scenario 1a: **Existing Patient** schedules directly with their provider
{: .no_toc}



This simple scenario serves as an effective means to scale up the complexity toward subsequent scenarios

    Patient: Hal has been with his PCP for several years. Hal has some severe back pain
             and wants to see his PCP, Dr Y, as soon as possible (today, or tomorrow at the latest).



##### Scenario 1b: **Existing Patient** schedules a service directly with their health care service
{: .no_toc}

This scenario is the same as 1a except a Service or Specialty instead of a specific Provider is being scheduled.

    Patient: Hal has been with his PCP for several years. Hal has some severe back pain and sees his PCP who
             ordered an imaging study.  Hal will be scheduling the study within the health care service.

---

{% include img.html img="diagrams/Slide28.png" caption="Figure 1: Patient Portal Scheduling for new or existing patient" %}

#### 1. Patient login
{:.no_toc}

Before a patient can begin, she must login in to the patient portal.  This step MAY include updating or confirmation of patient  and insurance coverage information.

{% include img.html img="diagrams/Slide05.png" caption="Figure 1: Patient login" %}

The patient ID is returned or known. See the [Login and Trust](index.html#login-and-trust) Section for details.

- Updates to patient demographic information MAY be included in the login step for some systems.  However the interactions to update this information are outside the scope of this specification
- Updates to patient insurance coverage information are detailed in the [section](#.html) below

#### 2. Appointment Availability Discovery and Search
{:.no_toc}

This step is the key transaction for this scheduling Use case. It asks the questions: when to book?  It is dynamic and complex because of multiple dependencies.<!--(In contrast, a discovery operation - which is out of scope for this version - asks the question: what Service(/specialty/provider) to book?)-->

{% include img.html img="diagrams/Slide30.png" caption="Figure 1: Appointment Availability Discovery and Search" %}

Based on the set of input parameters supplied by the Client, the Server determines which schedulable "assets" are needed for the visit and returns a set of possible Appointment times where all required assets are available. The scope of this guide is limited to the available appointments based on the following "simple" inputs:

   - practitioner
   - available times
   - location
   - specialty
   - set of common [visit types](ValueSet-visit-type.html).

##### APIs
{:.no_toc}

The following Argonaut Scheduling artifacts are used in this transaction:

- **[Appointment Availability Operation API](OperationDefinition-appointment-find.html)**.
- **[Argonaut Availability Output Profile API](StructureDefinition-avail-bundle.html)**.
- **[Argonaut Appointment Output Profile](StructureDefinition-appt-output.html)**.

##### Usage
{:.no_toc}

Using Both `GET` and `POST` Syntax the operation can be invoked as follows:

`GET [base]/Appointment/$hold?{parameters}&?{_count}`

`POST [base]/Appointment/$hold?{_count}`

##### Example
{:.no_toc}

{% capture my-include %}{% include appointment-find1a.md %}{% endcapture %}{{ my-include | markdownify }}
<br />

#### 3. Optional Hold Appointment Operation
{:.no_toc}
This operation puts to appointment in a hold status to temporarily prevent the appointment from being booked by another client.  This optional step may be needed to allow the end-user to complete additional steps such as end user data entry before the booking can be completed.


{% include img.html img="diagrams/Slide31.png" caption="Figure 4: Hold Appointment" %}

 The Client sends a hold request operation using the id of selected proposed appointment as the input parameter.  The Server determines if the appointment can be held and returns the Appointment resource with with an updated status. See the [Scheduling State Diagram](state-diagram.html) for further details on statuses.

##### APIs
{:.no_toc}

The following Argonaut Scheduling artifacts are used in this transaction:

  - **[Appointment Hold Operation API](OperationDefinition-appointment-hold.html)**.
  - **[Argonaut Availability Output Profile API](StructureDefinition-avail-bundle.html)**.
  - **[Argonaut Appointment Output Profile](StructureDefinition-appt-output.html)**.

##### Usage
{:.no_toc}

{% capture my-include %}{% include appointment-hold.md %}{% endcapture %}{{ my-include | markdownify }}
<br />


#### 4. Book appointment
{:.no_toc}
The actual booking of the appointment is completed in this step and the scheduling step is completed.

{% include img.html img="diagrams/Slide32.png" caption="Figure 5: Book Appointment" %}

the Client sends a book operation using the id of selected proposed appointment, the patient(s) id and optionally any comments as the input parameters.  The Server determines if the appointment can be booked and returns the Appointment resource with with an updated status. See the [Scheduling State Diagram](state-diagram.html) for further details on statuses.

##### APIs
{:.no_toc}

The following Argonaut Scheduling artifacts are used in this transaction:

  - **[Appointment Hold Operation API](OperationDefinition-appointment-hold.html)**.
  - **[Argonaut Availability Output Profile API](StructureDefinition-avail-bundle.html)**.
  - **[Argonaut Appointment Output Profile](StructureDefinition-appt-output.html)**.

##### Usage
{:.no_toc}

{% capture my-include %}{% include appointment-book.md %}{% endcapture %}{{ my-include | markdownify }}
<br />

### Use Case 2: Open Scheduling for new patient or existing patient

This use case is focused on scheduling through a third-party application where the patient is either a new or existing patient. In either case, the patient doesn’t need to be registered or logged in with the EHR to search for an open Appointment - which is defined as "Open scheduling" for this guide.  The patient may be trying to book an appointment to see a particular Practitioner or for a service to be performed. The primary difference between Use Case 2 and Use Case 1 above are the *registration steps*. The primary difference between Use Case 2 and Use Case 3 below is fetching data in *real time* in contrast to *prefetching* scheduling data

Preconditions:

- New or existing patient
- Patient uses a third-party application to schedule an appointment
- Open scheduling model
- User level Login and trust
- Fetching available appointments in real time

##### Scenario 2a. New Patient Schedules an Appointment with a Provider without being in health system
{:.no_toc}

    Patient: Bruce just moved to the area, has a rash.  He wants to set up an appointment with Dr X as soon as
             possible (within a week or so)

##### Scenario 2b. Patient Discovers and Schedules a Service without being in a health system
{:.no_toc}

    Patient: Bruce just moved to the area, has a rash.  He wants to set up an appointment with a local
            dermatologist as soon as possible (within a week or so).

In Scenario 2a and 2b we have introduced the complexities of a new patient and a consumer facing 3rd party application to schedule the appointment.  Scenario 2b is the same as 2a except a Service or Specialty instead of a specific Provider is being scheduled.


---

{% include img.html img="diagrams/Slide29.png" caption="Figure 1: Open Scheduling for new or existing patient" %}

#### 1. Patient Registration Option A
{:.no_toc}

For this scenario a new patient will need to be registered or an existing patient fetched prior to booking.  This MAY occur at this step or prior to booking. This step is discussed in detail in [step 4](#patient-registration-option-b) below.


#### 2. Appointment Availability Discovery and Search
{:.no_toc}

This step is the key transaction for this Scheduling Use Case. It asks the questions: when to book? It is dynamic and complex because of multiple dependencies.

{% include img.html img="diagrams/Slide03.png" caption="Figure 1: Appointment Availability Discovery and Search" %}

This step is the same as described in [Scenario-1](#appointment-availability-discovery-and-search).

#### 3. Optional Hold Appointment Operation
{:.no_toc}

This operation puts to appointment in a hold status to temporarily prevent the appointment from being booked by another client. This step is not optional if the patient was not registered in step 1 above. It is needed in order to register the patient prior to booking the appointment.

{% include img.html img="diagrams/Slide04.png" caption="Figure 1: Optional Hold Appointment Operation" %}

The details of this step are the same as described in [Scenario-1](#pptional-hold-appointment-operation).

#### 4. Patient Registration Option B
{:.no_toc}

A new patient will need to be registered or an existing patient fetched prior to actually booking the appointment.   This MAY occur at this step prior to booking the appointment or at the beginning of the workflow in step 1.  This step MAY include updating or confirmation of patient and insurance coverage information as well.

{% include img.html img="diagrams/Slide12.png" caption="Figure 1: Patient Registration" %}

**Registering or Fetching a Patient:**

##### Usage
{:.no_toc}

To register a new or existing patient, The Client SHALL use the standard FHIR RESTful [create API]({{site.data.fhir.path}}/http.html#create) as shown ( and SHALL not use the 'If-None-Exist' header as described in FHIR [conditional create API]({{site.data.fhir.path}}/http.html#ccreate))

POST [base]/Patient/[id]

In response to this transaction, the server SHOULD create a new patient resource only if the patient resource does not already exist in the system.  If the patient is already registered within the system. The existing patient resource SHOULD be returned.


##### Example
{:.no_toc}

~~~json
todo inline example
~~~
<br />

**Updating or creating Patient Coverage Information:**

Updates to patient coverage information MAY be associated with the login and registration steps for some systems or as a distinct step following booking.

**API**

The following Argonaut Scheduling artifacts are used in this transaction:

- **[Argonaut Coverage Profile](StructureDefinition-argo-coverage.html)**.

**Usage**

{% capture my-include %}{% include argo-coverage-search.md %}{% endcapture %}{{ my-include | markdownify }}


<br />



#### 5. Book Appointment
{:.no_toc}

After the patient is registered the actual booking interaction can occur.

{% include img.html img="diagrams/Slide06.png" caption="Figure 1: Book Appointment" %}

After the patient is registered the actual booking interaction can occur.  This step is the same as described in [Scenario-1](#book-appointment).

#### 6. Patient Coverage Update Option C
{:.no_toc}

For some systems, updating or confirmation of insurance coverage information MAY occur at this step after booking. The Coverage interaction is discussed in detail in [step 4](#patient-registration-option-b) above.


### Use Case 3 Prefetching Open Slots

This use case is the same as [Use Case 2](#use-case-2-open-scheduling-for-new-patient-or-existing-patient) above except data for available appointments are gathered in advance of end user login instead of determining available appointments in real-time. Therefore, in this use case open slots are queried and scheduling business rules need to be shared between the third-party app and EHR scheduler in order to determine appointment availability and create valid appointments.

Preconditions:

- New or existing patient
- Patient uses a third-party application to schedule an appointment
- Open scheduling model
- User level Login and trust
- Prefetching available open slots
- Third Party App able to aquire:
  - Scheduling business rules for target organization
  - At a minimum FHIR resource ids for Location and Practitioner
- FHIR Server maintain a version history

##### Scenario 3a. New Patient Schedules an Appointment with a Provider without being in health system
{:.no_toc}

    Patient: Bruce just moved to the area, has a rash.  He wants to set up an appointment with Dr X as soon as
             possible (within a week or so)

##### Scenario 3b. Patient Discovers and Schedules a Service without being in a health system
{:.no_toc}

    Patient: Bruce just moved to the area, has a rash.  He wants to set up an appointment with a local
            dermatologist as soon as possible (within a week or so).

In Scenario 3a and 3b we have introduced the complexities of a new patient and a consumer facing 3rd party application to schedule the appointment.  Scenario 3b is the same as 3a except a Service or Specialty instead of a specific Provider is being scheduled.

---

{% include img.html img="diagrams/Slide37.png" caption="Figure 1: Prefetching Open Slots" %}

#### 1. Share Business Rules
{:.no_toc}

The EHR/Hospital shares the business rules and logic for creating an appointment for a particular service with the third-party application. For example, which assets are needed. This is typically an "out of band" transaction. A FHIR based transaction is out of scope for this IG.

{% include img.html img="diagrams/Slide08.png" caption="Figure 1: Share Business Rules" %}

#### 2. Initial Load
{:.no_toc}

The third-party application fetches the 'initial load' of open slots.  It may be repeated to periodically refresh the data. This query may `_include` the relevant actors and and schedules so the client application is able to apply its business rules to create valid FHIR Appointment resources for transacting with the FHIR Scheduler/EHR.  Occasionally the Client server may need to repeat this step to reset its information.

{% include img.html img="diagrams/Slide14.png" caption="Figure 1: Initial Load" %}

**Fetching the 'intial load' of open slots:**

##### Usage
{:.no_toc}

To fetch all open slots for a period of time and include relevant Practitioners, Locations and Schedules, the Client SHALL use the standard FHIR RESTful [search API]({{site.data.fhir.path}}/search.html) as shown along with these standard [search parameters]({{site.data.fhir.path}}/slot.html#search):

- status (required = "free")
- start (required)
- slot-type (optional)
- the [chained]({{site.data.fhir.path}}/search.html#chaining) schedule.actor parameter to limit to Practitioner or Location actor(s) (optional)

~~~
GET [base]/Slot?status=free&start=ge[date]&start=le[date]{&slot-type=[type1]{,[type2]...}&schedule.actor=Practitioner/[id1],
{Location/[id1],Practitioner/[id2],Location/[id2]...}}
~~~

In addition, Clients may use the `_include` parameter and `:recurse` modifier to fetch the Schedule and the actor (i.e., Practitioner or Location) resources related to the slot search results.

~~~
GET [base]/Slot?status=free&start=ge[date]&start=le[date]{&schedule.actor=Practitioner/[id1]_include=Slot:schedule&_include:recurse=Schedule:actor}
~~~


##### Example
{:.no_toc}

~~~json
todo inline example
~~~

#### 3. Poll for updated slots
{:.no_toc}

After fetching the 'initial load' in step 2, the third-party application periodically polls for updated slots to keep the list of open slots current. The query would use the `_history` interaction to fetch only the slots that were either updated, deleted or created since the last query.  By reconciling the query results with its list of open slots, the Client application is able to synchronize its slots information with the FHIR Server.

{% include img.html img="diagrams/Slide15.png" caption="Figure 1: Poll for updated slots" %}

**Fetching open slot updates:**

##### Usage
{:.no_toc}

To fetch all updated slots since the last update, the Client SHALL use:

- the standard FHIR RESTful [history API]({{site.data.fhir.path}}/http.html#history)
- the `_since` parameter
- the standard search parameters listed in step 2 above

~~~
GET [base]/Slot/_history?_since=[last-update]&status=free&start=ge[date]&start=le[date]{&slot-type=[type1]{,[type2]...}
&schedule.actor=Practitioner/[id1],{Location/[id1],Practitioner/[id2],Location/[id2]...}}
~~~

##### Example
{:.no_toc}

~~~json
todo inline example
~~~

#### 4. Patient Registration Option A
{:.no_toc}

This step is identical to [Scenario 2 Step 1.](#patient-registration-option-a) above.


#### 5. Appointment Availability Discovery and Search
{:.no_toc}

Based on the shared business rules and user input, the client application server is able to create available appointments from the prefetched slot information (How this is done is out of scope) and return them to the end user.

{% include img.html img="diagrams/Slide10.png" caption="Figure 1: Appointment Availability Discovery and Search" %}

The FHIR RESTful based interactions are the same as described in [Scenario-1](#appointment-availability-discovery-and-search) noting that the role of the FHIR Scheduler (EHR) is replaced by the Client Application Server.  Other non-FHIR based solutions are possible as well.

#### 3. Optional Hold Appointment Operation
{:.no_toc}

This operation puts to appointment in a hold status to temporarily prevent the appointment from being booked by another client. This step is not optional if the patient is not registered. It is needed in order to register the patient prior to booking the appointment.

{% include img.html img="diagrams/Slide11.png" caption="Figure 1: Optional Hold Appointment Operation" %}

The details of this step are the same as described in [Scenario-1](#optional-hold-appointment-operation).

#### 7. Patient Registration Option B
{:.no_toc}

This step is identical to [Scenario 2 Step 4.](#patient-registration-option-a) above.

#### 5. Book Appointment
{:.no_toc}

After the patient is registered the actual booking interaction can occur.

{% include img.html img="diagrams/Slide06.png" caption="Figure 1: Book Appointment" %}

After the patient is registered the actual booking interaction can occur.  This step is the same as described in [Scenario-1](#book-appointment).

#### 6. Patient Coverage Update Option C
{:.no_toc}

For some systems, updating or confirmation of insurance coverage information MAY occur at this step after booking. The Coverage interaction is discussed in detail in [step 4](#patient-registration-option-b) above.



|Step|Title|Description|
|---|---|---|
|A|Share Business Rules|EHR/Hospital shares with client application the business rules and logic for creating an appointment for a particular service.  For example, which assets are needed.   This is typically an "out of band" transaction. A FHIR based Transaction is out of scope for this this IG.|
|AA|Initial Load|Client application fetches the 'intial load' of open slots.  This is needed for options 2 and 3 listed above. It may be repeated to periodically refresh the data. The query would have to `_include` the relevant actors and and schedules so the client application could apply its business rules to create appointments to transact with the FHIR Scheduler/EHR.|
|B|Poll for updated slots| With this option need to get an "initial load".  The query results updates the previous one to keep the list of open slots current.  The query would use the `_history` interaction to retrieve the slots that were updated, deleted or created since the last query.  See the [Issue #44](https://github.com/argonautproject/scheduling/issues/44) for more details. The query would have to `_include` the relevant actors and and schedules so the client application could apply its business rules to create appointments to transact with the FHIR Scheduler/EHR.|
|C|End user search for available appointments| This is this same as for all other scenarios. The End User provides basic input data like preferred dates, location, basic demographic data and possibley insurance information|
|D|Client App Returns available appointments| Based on the shared business rules the client application is able to create and return available appointments to the end user
|E|End user selects from available appointments||
|F|Holds Appointment|Client Application PUT/POST the created Appointment to the FHIR Server|
|G|Returns BookingConfirmation or Rejection|FHIR Scheduler, (EHR) returns confirmation or rejection of tentative appointment using the OperationOutcome to indicate the reason for rejection.|
|H|booking on hold until completed by End User|
|I|End user enters  patient information| *Optional step* Provide needed additional information. For example, to register the patient.|
|J|Fetch or Register Patient|*Optional step* The client application sends patient registration information to the FHIR Server|
|K|Returns Patient Id|*Optional step*  The FHIR Server returns the Patient ID|
|L|Book Appointment|Client Application PUTs the updated Appointment to the FHIR Server.|
|M|Returns BookingConfirmation or Rejection| The FHIR Server returns confirmation or rejection of booked appointment using the OperationOutcome to indicate the reason for rejection.|


#### TODO
{:.no_toc}

~~~json
todo inline example
~~~
<br />


### Cancelling appointments

{% include img.html img="diagrams/Slide33.png" caption="Figure 1: Patient Cancel" %}

In this scenario the end user wishes to cancels or cancel/reschedule an appointment. A cancelation is done using the standard FHIR  [`PATCH`](http://build.fhir.org/http.html#patch) transaction as shown:

`PATCH [Base]/Appointment/[id]`

-  optional input parameter:

    1. cancel [reason code](#) or string


- Note the Server SHALL declare support for JSON, XML, or FHIRPath Patch in the [CapabilityStatement](server-capstatement.html)
- not sure what server options are - discuss?  [#30](../issues/30)

~~~json
todo inline example
~~~
<br />

### Retrieving appointments

{% include img.html img="diagrams/Slide34.png" caption="Figure 1: Patient Cancel" %}


Patient access to their scheduled appointments uses the standard FHIR search API.  The supported search criteria for this transaction are described in:

- **[Argonaut Appointment Output Profile](StructureDefinition-appt-output.html)**.


~~~json
todo inline example
~~~
<br />
