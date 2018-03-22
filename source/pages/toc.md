---
title: Contents
layout: default
active: toc
---

### [Home](index.html)

- [Introduction](index.html#introduction)
- [Scope](index.html#scope)
  * [Patient Based Scheduling:](index.html#patient-based-scheduling)
  * [Provider based Scheduling:](index.html#provider-based-scheduling)
- [Actors](index.html#actors)
- [Assumptions](index.html#assumptions-and-preconditions)
  * [Third Party applications](index.html#third-party-applications)
  * [Login and Trust](index.html#login-and-trust)
    + [System level trust:](index.html#assumptions-and-preconditions)
    + [User Level Trust:](index.html#assumptions-and-preconditions)
  * [Dependencies](index.html#dependencies)
  * [Rescheduling](index.html#rescheduling)
- [Security](index.html#security)
- [Best Practices](index.html#best-practices)
- [Future Scope](index.html#future-scope)

### [Use Cases: Patient Based Scheduling](patient-scheduling.html)

- [Introduction](patient-scheduling.html#introduction)
- [Use Case 1: Patient Portal Scheduling for existing patients](patient-scheduling.html#use-case-1-patient-portal-scheduling-for-existing-patients)
    + [Scenario 1a: **Existing Patient** schedules directly with their provider](patient-scheduling.html#scenario-1a-existing-patient-schedules-directly-with-their-provider)
    + [Scenario 1b: **Existing Patient** schedules a service directly with their health care service](patient-scheduling.html#scenario-1b-existing-patient-schedules-a-service-directly-with-their-health-care-service)
  * [Patient login](patient-scheduling.html#patient-login)
  * [Appointment Availability Discovery and Search](patient-scheduling.html#appointment-availability-discovery-and-search)
    + [APIs](patient-scheduling.html#apis)
    + [Usage](patient-scheduling.html#usage)
    + [Example](patient-scheduling.html#example)
  * [Optional Hold Appointment Operation](patient-scheduling.html#optional-hold-appointment-operation)
    + [APIs](patient-scheduling.html#apis-1)
    + [Usage](patient-scheduling.html#usage-1)
  * [Book Appointment](patient-scheduling.html#book-appointment)
    + [APIs](patient-scheduling.html#apis-2)
    + [Usage](patient-scheduling.html#usage-2)
- [Use Case 2: Open Scheduling for new patient or existing patient](patient-scheduling.html#use-case-2-open-scheduling-for-new-patient-or-existing-patient)
    + [Scenario 2a. New Patient Schedules an Appointment with a Provider without being in health system](patient-scheduling.html#scenario-2a-new-patient-schedules-an-appointment-with-a-provider-without-being-in-health-system)
    + [Scenario 2b. Patient Discovers and Schedules a Service without being in a health system](patient-scheduling.html#scenario-2b-patient-discovers-and-schedules-a-service-without-being-in-a-health-system)
  * [Patient Registration Option A](patient-scheduling.html#patient-registration-option-a)
  * [Appointment Availability Discovery and Search](patient-scheduling.html#appointment-availability-discovery-and-search-1)
  * [Optional Hold Appointment Operation](patient-scheduling.html#optional-hold-appointment-operation-1)
  * [Patient Registration Option B](patient-scheduling.html#patient-registration-option-b)
    + [Registering or Fetching a Patient:](patient-scheduling.html#registering-or-fetching-a-patient)
      - [Usage](patient-scheduling.html#usage-3)
      - [Example](patient-scheduling.html#example-1)
    + [Updating or creating Patient Coverage Information:](patient-scheduling.html#updating-or-creating-patient-coverage-information)
      - [API](patient-scheduling.html#api)
      - [Usage](patient-scheduling.html#usage-4)
      - [Example](patient-scheduling.html#example-2)
  * [Book Appointment](patient-scheduling.html#book-appointment-1)
  * [Patient Coverage Update Option C](patient-scheduling.html#patient-coverage-update-option-c)
- [Use Case 3 Prefetching Open Slots](patient-scheduling.html#use-case-3-prefetching-open-slots)
    + [Scenario 3a. New Patient Schedules an Appointment with a Provider without being in health system](patient-scheduling.html#scenario-3a-new-patient-schedules-an-appointment-with-a-provider-without-being-in-health-system)
    + [Scenario 3b. Patient Discovers and Schedules a Service without being in a health system](patient-scheduling.html#scenario-3b-patient-discovers-and-schedules-a-service-without-being-in-a-health-system)
  * [Share Business Rules](patient-scheduling.html#share-business-rules)
  * [Initial Load](patient-scheduling.html#initial-load)
    + [Usage](patient-scheduling.html#usage-5)
    + [Example](patient-scheduling.html#example-3)
  * [Poll for updated slots](patient-scheduling.html#smart-polling-for-updated-slots)
    + [Usage](patient-scheduling.html#usage-6)
    + [Example](patient-scheduling.html#example-4)
  * [Patient Registration Option A](patient-scheduling.html#patient-registration-option-a-1)
  * [Appointment Availability Discovery and Search](patient-scheduling.html#appointment-availability-discovery-and-search-2)
  * [Optional Hold Appointment Operation](patient-scheduling.html#optional-hold-appointment-operation-2)
  * [Example](patient-scheduling.html#example-5)
  * [Patient Registration Option B](patient-scheduling.html#patient-registration-option-b-1)
  * [Book Appointment](patient-scheduling.html#book-appointment-2)
    + [Example](patient-scheduling.html#example-6)
  * [Patient Coverage Update Option C](patient-scheduling.html#patient-coverage-update-option-c-1)
- [Canceling/Rescheduling appointments](patient-scheduling.html#cancelingrescheduling-appointments)
  * [Usage](patient-scheduling.html#usage-7)
  * [Examples](patient-scheduling.html#examples)
- [Releasing holds](patient-scheduling.html#releasing-holds)
  * [Usage](patient-scheduling.html#usage-8)
  * [Examples](patient-scheduling.html#examples-1)
- [Retrieving appointments](patient-scheduling.html#retrieving-appointments)
  * [APIs](patient-scheduling.html#apis-3)
  * [Usage](patient-scheduling.html#usage-9)
  * [Examples](patient-scheduling.html#examples-2)


### [Use Cases: Provider based Scheduling](provider-scheduling.html)
{:.no_toc}

- [Introduction](provider-scheduling.html#introduction)
- [Use Case 1: Scheduling across systems](provider-scheduling.html#use-case-1-scheduling-across-systems)
    + [Scenario 1a Provider schedules an appointment with a patient's PCP on behalf of patient (Discharge follow-up):](provider-scheduling.html#scenario-1a-provider-schedules-an-appointment-with-a-patient-s-pcp-on-behalf-of-patient-discharge-follow-up)
    + [Scenario 1b Provider schedules an appointment with a provider on behalf of patient (Dermatology referral):](provider-scheduling.html#scenario-1b-provider-schedules-an-appointment-with-a-provider-on-behalf-of-patient--dermatology-referral)
    + [Scenario 1c Provider schedules a procedure on behalf of patient (Imaging referral):](provider-scheduling.html#scenario-1c-provider-schedules-a-procedure-on-behalf-of-patient--imaging-referral)
  * [Optional Find Patient](provider-scheduling.html#optional-find-patient)
    + [Usage](provider-scheduling.html#usage)
    + [Example](provider-scheduling.html#example)
  * [New Patient Registration/Coverage Information Option A](provider-scheduling.html#new-patient-registrationcoverage-information-option-a)
    + [Registering or Fetching a Patient:](provider-scheduling.html#registering-or-fetching-a-patient)
    + [Updating or creating Patient Coverage Information:](provider-scheduling.html#updating-or-creating-patient-coverage-information)
  * [Appointment Availability Discovery and Search](provider-scheduling.html#appointment-availability-discovery-and-search)
  * [Optional hold appointment operation](provider-scheduling.html#optional-hold-appointment-operation)
  * [New Patient Registration/Coverage Information Option B](provider-scheduling.html#new-patient-registrationcoverage-information-option-b)
  * [Book appointment](provider-scheduling.html#book-appointment)
  * [Optional exchange of patient information](provider-scheduling.html#optional-exchange-of-patient-information)
- [Use Case 2: Scheduling for existing patient across systems](provider-scheduling.html#use-case-2--scheduling-for-existing-patient-across-systems)
    + [Scenario 2a Provider schedules an appointment with a patient's PCP on behalf of patient (Discharge follow-up):](provider-scheduling.html#scenario-2a-provider-schedules-an-appointment-with-a-patient-s-pcp-on-behalf-of-patient-discharge-follow-up)
    + [Scenario 2a Provider schedules a follow-up procedure on behalf of patient (Imaging referral):](provider-scheduling.html#scenario-2a-provider-schedules-a-follow-up-procedure-on-behalf-of-patient--imaging-referral)
- [Use Case 3: Scheduling for existing patient *within* a system](provider-scheduling.html#use-case-3--scheduling-for-existing-patient--within--a-system)
    + [Scenario 3 Provider schedules an follow-up appointment with same provider on behalf of patient. (follow-up appointment):](provider-scheduling.html#scenario-3-provider-schedules-an-follow-up-appointment-with-same-provider-on-behalf-of-patient--follow-up-appointment)
- [Canceling/Rescheduling appointments](provider-scheduling.html#cancelingrescheduling-appointments)
- [Releasing holds](provider-scheduling.html#releasing-holds)
- [Retrieving Patient appointments](provider-scheduling.html#retrieving-patient-appointments)
    + [APIs](provider-scheduling.html#apis)
    + [Usage](provider-scheduling.html#usage-1)



### [Operations](operations.html)

{% include list-simple-operationdefinitions.xhtml %}

### [Profiles/Extensions](profiles.html)

{% include list-simple-profiles.xhtml %}

### [Terminology](terminology.html)

**Value Sets**

{% include list-simple-valuesets.xhtml %}

**Code Systems**

{% include list-simple-codesystems.xhtml %}

**Concept Maps**

{% include list-simple-conceptmaps.xhtml %}

### [Conformance requirements for Server](CapabilityStatement-server.html)

### [Conformance requirements for Client](CapabilityStatement-client.html)

### [Downloads](downloads.html)

- [Validator Pack and Definitions:](downloads.html#validator-pack-and-definitions)
- [Schematrons:](downloads.html#schematrons)
- [Examples:](downloads.html#examples)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>
