## {{ page.title }}
{:.no_toc}

source pages/\_include/{{page.md_filename}}.md  file

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

### Introduction

### Scenario 1: Scheduling for existing patient across systems

Preconditions:

- External system knows patient
- Login and trust ( todo: confirm this)
   - The referring provider application has been authorized by the referral recipients health system
   - Uses *SMART on FHIR* authorization for applications that connect to EHR data.
- Work flow for clinic staff vs a call center to make appointment (in person vs over phone) is same

##### Scenario 1a Provider schedules an appointment with a patient's PCP on behalf of patient (Discharge follow-up):
{:.no_toc}
     Hospital A has treated patient B. Upon discharge, Hospital A schedules a follow-up appointment with patient B's PCP (primary care provider).

This is a basic referral scenario in which the patient is registered with the referral recipient.

##### Scenario 2a Provider schedules a follow-up procedure on behalf of patient (Imaging referral):
{:.no_toc}
     Patient Y has been seeing Doctor X for a sore back. After examining the patient Doctor X recommends a follow-up MRI for Patient Y. The clinic staff schedule the MRI for Patient Y.

 This scenario is similar to 1a above, but is an appointment for a procedure instead of a direct referral with a practitioner.

---

{% include img.html img="diagrams/Slide35.png" caption="Figure 1: Provider Scheduling for existing patient across systemst" %}


1. Patient Match



   - Optional Step
   - Fetch Patient ID(s) from other systems
   - Prevent overlapping appointments since Scheduler may not be aware

   Use $match operation as described in the [FHIR Specification](http://build.fhir.org/patient-operations.html#8.1.18.1)

1. End user searches for available appointments

   -  Use the [Appointment Availability Search Operation](http://build.fhir.org/ig/argonautproject/scheduling/operations.html)
   - Same operation used for patient scheduling

1. End user selects from available appointments

   - Provider selects on behalf of patient
   - Patient instruct provider which appointment they want.
   - $hold and $book operations same as used for patient scheduling

1. exchange patient information

   -  medical information
      - ccda exchange
         - document this
         - transactions out of scope - future
   -  patient registration
       - existing patient see patient match step
       - new patient registration prior to booking
   - coverage - optional

---

### Scenario 2: Scheduling for new patient across systems

Preconditions:

- The patient is presumed to be unknown to external system.
- Login and trust ( todo: confirm this)
   - The referring provider application has been authorized by the referral recipients health system
   - Uses *SMART on FHIR* authorization for applications that connect to EHR data.
- Work flow for clinic staff vs a call center to make appointment (in person vs over phone) is same

##### Scenario 2a Provider schedules an appointment with a provider on behalf of patient (Dermatology referral):
{:.no_toc}
      Patient Y sees Doctor Z his PCP for a rash. After examining the patient, Doctor Z wants to Patient Y to see a dermatologist.  The clinic staff schedule Patient Y to see Doctor D for a dermatology consult.  Patient Y has never been to a dermatologist before.

This basic referral scenario is the same as [Scenario-1a][#] above except that the patient is presumed to be a new patient to the referral recipient. An alternative but equivalent scenario would be a hospital scheduling at discharge and follow-up with a patient's PCP (primary care provider).

##### Scenario 2b Provider schedules a procedure on behalf of patient (Imaging referral):
{:.no_toc}
      Patient Y see Doctor X for a sore back. After examining the patient Doctor X recommends an MRI for Patient Y. The clinic staff schedule the MRI for Patient Y.  This is first MRI for patient Y.

This basic referral scenario is the same as [Scenario-1b][#] above except that the patient is presumed to be a new patient to the referral recipient.  This is very similar to 2a above but is an appointment for a procedure instead of a direct referral.

---

{% include img.html img="diagrams/Slide36.png" caption="Figure 1: Provider Scheduling for existing patient across systemst" %}

----

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
