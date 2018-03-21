---
title: Provider based Scheduling Use Cases
layout: default
active: guidance
mycss: argo-sched.css
---

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

## Introduction

The Argonaut Scheduling Implementation Guide defines a series of interactions which cover the basic appointment creation workflow for provider based scheduling on behalf of a patient which includes: registration of patients and updating  coverage information, discovery of available appointments and booking the canceling appointments. It also covers provider access to their appointments.  The basic workflow steps and Argonaut Scheduling APIs for three use cases are detailed below.  Note that the primary difference between these scenarios are the *registration steps*.


## Use Case 1: Scheduling across systems

This use case accounts for both new and existing patients.  The actual required steps depend upon factors such as if the patient is known to the external system, and if and when patient coverage information is needed. Use Case 2 and Use Case 3 in the sections below are simplified variations of this more generalized use case.

Preconditions:

- Does not matter whether patient is known or unknown to external system.
- Login and trust
   - System level trust or
   - User level trust
- Work flow for clinic staff vs a call center to make appointment (in person vs over phone) is same

#### Scenario 1a Provider schedules an appointment with a patient's PCP on behalf of patient (Discharge follow-up):
{:.no_toc}
     Hospital A has treated patient B. Upon discharge, Hospital A schedules a follow-up appointment with patient B's PCP (primary care provider).

This is a basic referral scenario in which the patient is registered with the referral recipient.

#### Scenario 1b Provider schedules an appointment with a provider on behalf of patient (Dermatology referral):
{:.no_toc}
      Patient Y sees Doctor Z his PCP for a rash. After examining the patient, Doctor Z wants to Patient Y to see a dermatologist.  The clinic staff schedule Patient Y to see Doctor D for a dermatology consult.  Patient Y has never been to a dermatologist before.

This scenario is very similar to 1a above.  However, the patient is presumed to be a new patient to the referral recipient.

#### Scenario 1c Provider schedules a procedure on behalf of patient (Imaging referral):
{:.no_toc}

      Patient Y see Doctor X for a sore back. After examining the patient Doctor X recommends an MRI for Patient Y. The clinic staff schedule the MRI for Patient Y.  It is unknown whether the Patient Y has used the imaging service before.

This scenario is also very similar to 1a above, but is an appointment for a procedure instead of a direct referral.

---

{% include img.html img="diagrams/Slide36.png" caption="Figure 1: Provider Scheduling for a patient across systems" %}


### Optional Find Patient
{:.no_toc}

Prior to booking an appointment with a FHIR Scheduler, the Client can search across the systems for an existing FHIR Patient resource ID for the patient.  If there is an existing FHIR Patient resource, finding it helps avoid double booking a patient.

{% include img.html img="diagrams/Slide20.png" caption="Figure 1: Optional Find Patient" %}

#### Usage
{:.no_toc}

To search and fetch the FHIR Patient reasource Id, use the [`$match` operation](http://build.fhir.org/patient-operations.html#8.1.18.1) as described in the FHIR Specification. It can be invoked as follows:

`POST [base]/Patient/$match`

#### Example
{:.no_toc}

~~~json
todo inline example
~~~

---

### New Patient Registration/Coverage Information Option A
{:.no_toc}

New patients need to be registered and existing patients discovered prior to booking.  This registration step MAY occur at this step or  as a distinct step just prior to booking (step 5).  Additional coverage information for *both* new and existing patients MAY be associated with this step or as a distinct step prior to (step 5) or following booking (step 7).  The information is supplied by the patient or on behalf of the patient.

#### Registering or Fetching a Patient:
{:.no_toc}

{% include img.html img="diagrams/Slide21.png" caption="Figure 1: New Patient Registration" %}

Usage and examples for this step are described in the [Patient Use Cases](patient-scheduling.html#registering-or-fetching-a-patient).

#### Updating or creating Patient Coverage Information:
{:.no_toc}

{% include img.html img="diagrams/Slide22.png" caption="Figure 1: Update Coverage information" %}

Usage and examples for this step are described in the [Patient Use Cases](patient-scheduling.html#updating-or-creating-patient-coverage-information).

---

### Appointment Availability Discovery and Search
{:.no_toc}

The Client searches for available appointments across system(s) based on simple search criteria provided by the patient or on behalf of the patient. This step is the key transaction for this Scheduling Use Case. It asks the questions: when to book? It is dynamic and complex because of multiple dependencies.

{% include img.html img="diagrams/Slide23.png" caption="Figure 1: Appointment Availability Discovery and Search" %}

This step uses the Appointment Availability Search Operation and its usage and examples
are described in the [Patient Use Cases](patient-scheduling.html#appointment-availability-discovery-and-search).


### Optional hold appointment operation
{:.no_toc}

After the patient or the provider on behalf of the patient selects from the available appointments returned in step 3 above, the Client requests a hold on the appointment to prevent the appointment from being booked by another client.  This optional interaction may be needed to allow the patient or provider to complete additional steps such as end user data entry before the booking can be completed.

{% include img.html img="diagrams/Slide24.png" caption="Figure 1: Hold Appointment" %}

Usage and examples for this step are described in the [Patient Use Cases](patient-scheduling.html#optional-hold-appointment-operation).

### New Patient Registration/Coverage Information Option B
{:.no_toc}

This registration step MAY occur here or as a distinct step prior to the availability search [step 2](provider-scheduling.html#new-patient-registrationcoverage-information-option-a) where it is discussed in detail

### Book appointment
{:.no_toc}

 After the patient or the provider selects from the available appointments returned in step 3 and the patient registration is complete, the appointment is booked.  

{% include img.html img="diagrams/Slide41.png" caption="Figure 1: Book Appointment" %}

Usage and examples for this step are described in the [Patient Use Cases](patient-scheduling.html#book-appointment).

### Optional exchange of patient information
{:.no_toc}

Additional information MAY be exchange following the booking of the appointment.  For example the exchange of CCD, other clinical documents or, if not transacted during the prior registration steps, coverage information.  This exchange of clinical documents is covered by a [separate standard](https://wiki.ihe.net/index.php/Cross-Enterprise_Document_Sharing) and is currently out of scope for this guide.   The details for the exchange of coverage information are described [above](provider-scheduling.html#new-patient-registrationcoverage-information-option-a).

---

## Use Case 2: Scheduling for existing patient across systems

This use case is a simplified variation of this use more general use case 1 above.  In this use case, the patient is an existing patient and either the patient ID can be retrieved via the Patient $match operation or by some other means.

Preconditions:

- External system knows patient
- Patient ID is known or retrieved
- Login and trust
   - System level trust or
   - User level trust
- Work flow for clinic staff vs a call center to make appointment (in person vs over phone) is same

#### Scenario 2a Provider schedules an appointment with a patient's PCP on behalf of patient (Discharge follow-up):
{:.no_toc}
     Hospital A has treated patient B. Upon discharge, Hospital A schedules a follow-up appointment with patient B's PCP (primary care provider).

This is a basic referral scenario in which the patient is registered with the referral recipient.

#### Scenario 2a Provider schedules a follow-up procedure on behalf of patient (Imaging referral):
{:.no_toc}
     Patient Y has been seeing Doctor X for a sore back. After examining the patient Doctor X recommends a follow-up MRI for Patient Y. The clinic staff schedule the MRI for Patient Y.

 This scenario is similar to 2a above, but is an appointment for a procedure instead of a direct referral with a practitioner.

---

{% include img.html img="diagrams/Slide35.png" caption="Figure 1: Provider Scheduling for existing patient across systems" %}


This use case is discussed in detail in steps 1, 3, 4, 6, 7 in [Scenario 1](#use-case-1-scheduling-across-systems) above.

---

## Use Case 3: Scheduling for existing patient *within* a system

This is the simplest variation of the more general use case 1 above. The patient and provider, service or procedure are all within the same system.  Note that this scenario is typically performed by in-practice system and therefore of limited use for this interoperability specification.

Preconditions:

- same patient, provider, service, insurance

#### Scenario 3 Provider schedules an follow-up appointment with same provider on behalf of patient. (follow-up appointment):
{:.no_toc}      

       Patient Y sees Doctor Z for a rash. After examining and prescribing the appropriate treatment plan, Doctor Z wants to see Patient Y in two weeks for a follow-up visit to evaluate the response to treatment.  The clinic staff schedule Patient Y for a follow-up office call.

{% include img.html img="diagrams/Slide40.png" caption="Figure 1: Provider Scheduling for Existing Patient *within* system" %}

This simple use case is covered by steps 2, 3, and 4 in [Scenario 1](#use-case-1-scheduling-across-systems) above.

---

## Canceling/Rescheduling appointments

Usage and examples are described in the [Patient Use Cases](patient-scheduling.html#cancelingrescheduling-appointments).

## Releasing holds

Usage and examples are described in the [Patient Use Cases](patient-scheduling.html#releasing-holds).

## Retrieving Patient appointments

The provider searches for appointments on behalf of a patient or the provider.

{% include img.html img="diagrams/Slide39.png" caption="Figure 1: Retrieving Patient appointments" %}

Provider access to their scheduled appointments uses the standard FHIR [search API]({{site.data.fhir.path}}/search.html).

#### APIs
{:.no_toc}

The following Argonaut Scheduling artifacts are used in this transaction:

- **[Argonaut Appointment Profile](StructureDefinition-argo-appt.html)**.

#### Usage
{:.no_toc}

To fetch scheduled appointments for a patient the Client SHALL use the standard RESTful [search API]({{site.data.fhir.path}}/search.html) as shown along with these standard [search parameters]({{site.data.fhir.path}}/appointment.html#search):

- `patient` (optional) filter by the patient
- `status` (optional) filter by status such as ‘booked’
- `date` (optional) filter by a date or a date range ( including the date modifiers ‘ge’,’le’,’gt’,’lt’)
- `practitioner` (optional) filter by a practitioner(s)

`GET [base]\Appointment?practitioner=[id]{&status=[status]&date=[date]}`

### Examples
{:.no_toc}

Fetch all of a practitioner's appointments (all statuses):
`GET [base]\Appointment?practitioner=[id]`

Fetch all open appointments:
`GET [base]\Appointment?practitioner=[id]&status=free`

Fetch all completed appointments since October:
`GET [base]\Appointment?practitioner=[id]&status=fulfilled&date=ge2017-10-01`

Fetch all completed appointments for a patient since October:
`GET [base]\Appointment?practitioner=[id]&patient=[id]&status=fulfilled&date=ge2017-10-01`
