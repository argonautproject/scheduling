---
title: Provider based Scheduling Use Cases
layout: default
active: guidance
mycss: argo-sched.css
---

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

### Introduction

The Argonaut Scheduling Implementation Guide defines a series of interactions which cover the basic appointment creation workflow for provider based scheduling on behalf of a patient which includes: registration of patients and updating  coverage information, discovery of available appointments and booking the cancelling appointments. It also covers provider access to their appointments.  The basic workflow steps and Argonaut Scheduling APIs for two use cases are detailed below.  Note that the primary difference between these scenarios are the *registration steps*.


### Use Case 1: Scheduling across systems

This general use case accounts for both new and existing patients and the specific steps that are required depend upon more specific scenarios such as if the patient is known to the external system, and if and when patient coverage information is needed. Use Case 2 and Use Case 3 in the sections below are simplified variations of this use more general use case.

Preconditions:

- does not matter whether patient is known or unknown to external system.
- Login and trust
   - System level trust or
   - User level trust
- Work flow for clinic staff vs a call center to make appointment (in person vs over phone) is same

##### Scenario 1a Provider schedules an appointment with a patient's PCP on behalf of patient (Discharge follow-up):
{:.no_toc}
     Hospital A has treated patient B. Upon discharge, Hospital A schedules a follow-up appointment with patient B's PCP (primary care provider).

This is a basic referral scenario in which the patient is registered with the referral recipient.

##### Scenario 1b Provider schedules an appointment with a provider on behalf of patient (Dermatology referral):
{:.no_toc}
      Patient Y sees Doctor Z his PCP for a rash. After examining the patient, Doctor Z wants to Patient Y to see a dermatologist.  The clinic staff schedule Patient Y to see Doctor D for a dermatology consult.  Patient Y has never been to a dermatologist before.

This scenario is very similar to 1a above.  However, the patient is presumed to be a new patient to the referral recipient.

##### Scenario 1c Provider schedules a procedure on behalf of patient (Imaging referral):
{:.no_toc}
      Patient Y see Doctor X for a sore back. After examining the patient Doctor X recommends an MRI for Patient Y. The clinic staff schedule the MRI for Patient Y.  It is unknown whether the Patient Y has used the imaging service before.

This scenario is also very similar to 1a above, but is an appointment for a procedure instead of a direct referral.

---

{% include img.html img="diagrams/Slide36.png" caption="Figure 1: Provider Scheduling for a patient across systems" %}

----

1. Optional Patient Match

   - Optional Step
   - Fetch Patient ID(s) from other systems
   - Prevent overlapping appointments since Scheduler may not be aware

   Use $match operation as described in the [FHIR Specification](http://build.fhir.org/patient-operations.html#8.1.18.1)

1. Optional Patient Registration step

1. End user searches for available appointments

   -  Use the [Appointment Availability Search Operation](http://build.fhir.org/ig/argonautproject/scheduling/operations.html)
   - Same operation used for patient scheduling

1. Optional Conflict checking
    - Provider based - due to trust model - multiple system interaction
    - purpose is to avoid double booking a patient.
    - API - Appt search interaction before or after $find
    - Client Reconciliation prior to exposing to end user

1. End user selects from available appointments

   - Provider selects on behalf of patient
   - Patient instruct provider which appointment they want

1. Optional Conflict checking

1.  Optional $hold
    -  same as used for patient scheduling

1. Optional Patient Registration step

1. $book
   -  same as used for patient scheduling

1. Optional exchange patient information

   -  medical information
      - ccda exchange
         - document this
         - transactions out of scope - future
   -  patient registration
       - existing patient see patient match step
       - new patient registration prior to booking
   - coverage - optional

---

### Use Case 2: Scheduling for existing patient across systems

This use case is a simplified variation of this use more general use case 1 above. In this use case, the patient is an existing patient and either the patient ID can be retrieved via the Patient$match operation or by some other means.

Preconditions:

- External system knows patient
- Patient ID is known or retrieved
- Login and trust
   - System level trust or
   - User level trust
- Work flow for clinic staff vs a call center to make appointment (in person vs over phone) is same

##### Scenario 2a Provider schedules an appointment with a patient's PCP on behalf of patient (Discharge follow-up):
{:.no_toc}
     Hospital A has treated patient B. Upon discharge, Hospital A schedules a follow-up appointment with patient B's PCP (primary care provider).

This is a basic referral scenario in which the patient is registered with the referral recipient.

##### Scenario 2a Provider schedules a follow-up procedure on behalf of patient (Imaging referral):
{:.no_toc}
     Patient Y has been seeing Doctor X for a sore back. After examining the patient Doctor X recommends a follow-up MRI for Patient Y. The clinic staff schedule the MRI for Patient Y.

 This scenario is similar to 1a above, but is an appointment for a procedure instead of a direct referral with a practitioner.

---

{% include img.html img="diagrams/Slide35.png" caption="Figure 1: Provider Scheduling for existing patient across systemst" %}


----


### Use Case 3: Scheduling for existing patient within a system

This is the simplest variation of the more general use case 1 above. The patient and provider, service or procedure are all within the same system.  Note that this scenario is typically performed by in-practice system and therefore of limited use for this interoperability specification.

Preconditions:

- same patient, provider, service, insurance - etc

##### Scenario 3 Provider schedules an follow-up appointment with same provider on behalf of patient. (follow-up appointment):
{:.no_toc}      

       Patient Y sees Doctor Z for a rash. After examining and prescribing the appropriate treatment plan, Doctor Z wants to see Patient Y in two weeks for a follow-up visit to evaluate the response to treatment.  The clinic staff schedule Patient Y for a follow-up office call.

This simple use case is covered by steps 2, 3, and 4 in [Scenario 1](#scenario-1-scheduling-for-existing-patient-across-systems) above.

---

### Cancelling appointment

same as for Patient Use Cases

### Retrieving Patient appointments

same as for Patient Use Cases with Provider scope

A Provider data access search for all of her appointments and all of a patient's appointments:


[Draft Search requirements for appointment profile](http://build.fhir.org/ig/argonautproject/scheduling/StructureDefinition-appt-output.html#search)


required to support the:
- patient
- status
- date (+ modifiers supported in us core)
- practitioner
search parameters

Syntax:

`GET [base]\Appointment?practitioner=[id]{&status=[status]&date=[date]}`

For example, fetch all of a practitioner's appointments (all statuses):

`GET [base]\Appointment?practitioner=[id]`

fetch all open appointments:

`GET [base]\Appointment?practitioner=[id]&status=free`

fetch all completed appointments since October:

`GET [base]\Appointment?practitioner=[id]&status=fulfilled&date=ge2017-10-01`

fetch all completed appointments for a patient since October:

`GET [base]\Appointment?practitioner=[id]&patient=[id]&status=fulfilled&date=ge2017-10-01`

(see the patient facing search for additional examples)

Questions:

Support for multiple patients and practitioners (e.g. [id1, id2, id3])

More Useful to search provider Schedule?




### Retrieving Providers appointment/schedule

Discuss - what is in scope?
