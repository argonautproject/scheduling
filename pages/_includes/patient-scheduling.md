## {{ page.title }}
{:.no_toc}

source pages/\_include/{{page.md_filename}}.md  file

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

### Introduction

The Argonaut Scheduling Implementation Guide defines a series of interactions which cover the basic appointment creation workflow which includes discovery of available appointments, booking the appointment, booking confirmation and updates to booked appointment. It also covers Patient and Provider access to their appointments. Below is an simple overview that summarizes the basic workflow steps for scenario 1 and 2 needed to schedule an appointment.  Note that the steps for both scenarios are the same except for where the *Registering or Fetching Patient* step occurs.

### Scenario 1: Patient Portal Scheduling for new or existing patient

Preconditions:

- Patient has relationship to health system
- Patient uses a "patient portal" - an application hosted by his provider.
- Login and trust
   - The app has been authorized by the health system
   - Uses *SMART on FHIR* authorization for apps that connect to EHR data.

##### Scenario 1a: **Existing Patient** schedules directly with their provider
{: .no_toc}
    Patient: Hal has been with his PCP for several years. Hal has some severe back pain
             and wants to see his PCP, Dr Y, as soon as possible (today, or tomorrow at the latest).

This simple scenario serves as an effective means to scale up the complexity toward subsequent scenarios

##### Scenario 1b: **Existing Patient** schedules a service directly with their health care service
{: .no_toc}

    Patient: Hal has been with his PCP for several years. Hal has some severe back pain and sees his PCP who
             ordered an imaging study.  Hal will be scheduling the study within the health care service.

This scenario is the same as 1a except a Service or Specialty instead of a specific Provider is being scheduled.

---

{% include img.html img="diagrams/Slide28.png" caption="Figure 1: Patient Portal Scheduling for new or existing patient" %}

#### 1. Patient login
{:.no_toc}

{% include img.html img="diagrams/Slide05.png" caption="Figure 1: Patient login" %}

If the patient is logged into an EHR’s patient portal, the patient ID is returned or known. See the [Login and Trust](index.html#login-and-trust) Section for details.  However, the server MAY allow for [updates](http://build.fhir.org/http.html#update) to the basic demographic and insurance information.  Additional patient input and more advanced conflict checking has been deferred to future scope.

   - The interactions to update demographic information is outside the scope of this specification
   - To update the existing insurance information, The Argonaut Coverage Profile is used by the Client application to update the existing Coverage with the new information as shown:

      `PUT [base]/Coverage/[id]`

      - **[Coverage Profile API](StructureDefinition-argo-coverage.html)**.

       Note that the server MAY reject certain updates to the coverage information (for example, type of coverage) and SHOULD return an [OperationOutcome]({{site.data.fhir.path}}/operationoutcome.html) explaining the reason.[Issue #47](../issues/47)

~~~json
todo inline example
~~~

#### 2. Appointment Availability Discovery and Search
{:.no_toc}

{% include img.html img="diagrams/Slide30.png" caption="Figure 1: Appointment Availability Discovery and Search" %}

The Appointment Availability Search Operation asks the key questions: when to book?  It is
dynamic and complex because of multiple dependencies.  (In contrast, a discovery operation - which is out of scope for this version - asks the key question: what Service(/specialty/provider) to book?) The scope of this guide is limited to the available appointments based on the following "simple" inputs:

   - practitioner
   - available times
   - location
   - specialty
   - set of common [visit types](ValueSet-visit-type.html).

The Server determines which schedulable resources are needed for the visit and provides appointment times where all required resources are available.


The following Argonaut Scheduling artifacts are used in this transaction:

- **[Appointment Hold Operation API](OperationDefinition-appointment-hold.html)**.
- **[Argonaut Availability Output Profile API](StructureDefinition-avail-bundle.html)**.
- **[Argonaut Appointment Output Profile](StructureDefinition-appt-output.html)**.

- The operation can be invoked in 2 ways depending on the inputs:

   `GET [base]/Appointment/$find?{simple parameters}`

   and

   `POST [base]/Appointment/$find&{_count=[integer]}`



~~~json
todo inline example
~~~

#### 3. Optional Hold Appointment Operation
{:.no_toc}

{% include img.html img="diagrams/Slide31.png" caption="Figure 4: Hold Appointment" %}

This step may be needed to allow the end-user to complete some additional steps such as end user data entry.  The Client sends a hold request operation using the id of selected proposed appointment as the input parameter.  The Server determines if the appointment can be held and returns the Appointment resource with with an updated status. See the [Scheduling State Diagram](state-diagram.html) for further details on statuses.

The following Argonaut Scheduling artifacts are used in this transaction:

  - **[Appointment Hold Operation API](OperationDefinition-appointment-hold.html)**.
  - **[Argonaut Availability Output Profile API](StructureDefinition-avail-bundle.html)**.
  - **[Argonaut Appointment Output Profile](StructureDefinition-appt-output.html)**.

- The operation can be invoked as follows:

   `POST [base]/Appointment/$hold`



~~~json
todo inline example
~~~

#### 4. Book appointment
{:.no_toc}

{% include img.html img="diagrams/Slide32.png" caption="Figure 5: Book Appointment" %}

The actual booking of the appointment is completed in this step.  the Client sends a book operation using the id of selected proposed appointment, the patient(s) id and optionally any comments as the input parameters.  The Server determines if the appointment can be booked and returns the Appointment resource with with an updated status. See the [Scheduling State Diagram](state-diagram.html) for further details on statuses.

The following Argonaut Scheduling artifacts are used in this transaction:

  - **[Appointment Book Operation API](OperationDefinition-appointment-book.html)**.
  - **[Argonaut Availability Output Profile API](StructureDefinition-avail-bundle.html)**.
  - **[Argonaut Appointment Output Profile](StructureDefinition-appt-output.html)**.


- The operation can be invoked as follows:

   `POST [base]/Appointment/$book`

~~~json
todo inline example
~~~

### Scenario 2: Open Scheduling for new patient

Preconditions:

- New Patient
- Open scheduling model” where the patient doesn’t need to be registered with the EHR to search for an open Appointment.
- Login and trust
  - The app has been authorized by the health system
  - Uses *SMART on FHIR* authorization for apps that connect to EHR data.
    - The authorized App does availability search without Server having to “know” the patient.
    - A “patient level authorization” step is required at some point in the workflow in order to create a new account and complete the appointment.  The technical details for this are out of scope.
- The application server **MAY** "pre-fetch" available slots from the EHR.

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

For this scenario a new patient will need to be registered or an existing patient fetched prior to booking.  This MAY occur at this step or prior to booking.  This step is discussed in detail in [step 4](#patient-registration-option-b) below.


#### 2. Appointment Availability Discovery and Search
{:.no_toc}

{% include img.html img="diagrams/Slide03.png" caption="Figure 1: Appointment Availability Discovery and Search" %}

This step is the same as described in [Scenario-1](#appointment-availability-discovery-and-search).

#### 3. Optional Hold Appointment Operation
{:.no_toc}

{% include img.html img="diagrams/Slide04.png" caption="Figure 1: Optional Hold Appointment Operation" %}

If the patient is not registered in step 1 above, the hold step is required in order to register the patient in step 4.  The end user needs to complete the information needed to complete the booking.  The details of this step are the same as described in [Scenario-1](#pptional-hold-appointment-operation).

#### 4. Patient Registration Option B
{:.no_toc}

{% include img.html img="diagrams/Slide12.png" caption="Figure 1: Patient Registration" %}

In this scheduling scenario a patient will need to be registered or an existing patient fetched prior to actually booking the appointment.  The server SHOULD perform a conditional create for these interactions as is documented below.

  Client - Create a new patients as shown:

  `POST [base]/Patient`

  NOTE : **The client will not supply a FHIR search query using an HL7 defined extension header "If-None-Exist" in the `POST` transaction as described described for the [Conditional create](http://build.fhir.org/http.html#create) transaction in the FHIR specification**

  Server - Conditionally create a new patient in response to a RESTful `POST` operation.

  - This operation creates a new patient resource if the patient resource does not already exist in the system
  - If the the patient is already registered within the system. The existing patient resource is returned.
  - The payload is a [US-Core profile](http://hl7.org/fhir/us/core/StructureDefinition-us-core-patient.html) on the Patient resource that includes demographics and patient preferences.
  - The server behavior is the same as described for [Conditional create](http://build.fhir.org/http.html#create).

  After fetching the Patient resource Id, the Client application may create or update existing insurance coverage information. the Argonaut Coverage Profile is used by the Client application to update the existing Coverage with the new information as shown:

  `PUT [base]/Coverage/[id]`

  - **[Coverage Profile API](StructureDefinition-argo-coverage.html)**.

   Note that the server MAY reject certain updates to the coverage information (for example, type of coverage) and SHOULD return an [OperationOutcome]({{site.data.fhir.path}}/operationoutcome.html) explaining the reason.[Issue #47](../issues/47)

~~~json
todo inline example
~~~

#### 4. Book Appointment
{:.no_toc}

{% include img.html img="diagrams/Slide06.png" caption="Figure 1: Book Appointment" %}

After the patient is registered the actual booking interaction can occur.  This step is the same as described in [Scenario-1](#book-appointment).

### Scenario 3: Prefetching Open Slots for Scheduling patient



### Cancelling appointment

{% include img.html img="diagrams/Slide33.png" caption="Figure 1: Patient Cancel" %}

In this scenario the end user wishes to cancels or cancel/reschedule an appointment.

CLIENT: send cancel request using a RESTful [`PATCH`](http://build.fhir.org/http.html#patch) transaction as shown

`PATCH [Base]/Appointment/[id]`


-  optional input parameter:

    1. cancel reason code or string

SERVER:
- Return OperationOutcome and defined in the FHIR specification.
- Note the Server SHALL declare support for JSON, XML, or FHIRPath Patch in the [CapabilityStatement](server-capstatement.html)
- not sure what server options are - discuss?  [#30](../issues/30)

~~~json
todo inline example
~~~


### Retrieving appointments

{% include img.html img="diagrams/Slide34.png" caption="Figure 1: Patient Cancel" %}


Patient access for their scheduled appointments

[Draft Search requirements for appointment profile](http://build.fhir.org/ig/argonautproject/scheduling/StructureDefinition-appt-output.html#search)

A patient data access use case for searching their appointments. The search criteria for this transaction isdescribed in:

- **[Appointment Hold Operation API](OperationDefinition-appointment-hold.html)**

Syntax:

`GET [base]\Appointment?patient=[id]{&status=[status]&date=[date]}`

For example, fetch all appointments (all statuses):

`GET [base]\Appointment?patient=[id]`

fetch all booked appointments:

`GET [base]\Appointment?patient=[id]&status=booked`

fetch all completed appointments since January:

`GET [base]\Appointment?patient=[id]&status=fulfilled&date=ge2017-01-01`

~~~json
todo inline example
~~~
<br />
