---
title: Contents
layout: default
active: toc
topofpage: true
---

## [Argonaut Implementation Guide HomePage](index.html)
- [Introduction](index.html#introduction)
- [Scope](index.html#scope)
    - [Patient Based Scheduling](index.html#patient-based-scheduling)
    - [Provider based Scheduling](index.html#provider-based-scheduling)
- [Actors](index.html#actors)
- [Assumptions and Preconditions](index.html#assumptions-and-preconditions)
- [Security](index.html#security)
- [Future Scope](index.html#future-scope)

### [Patient Based Scheduling](patient-scheduling.html)
- [Introduction](patient-scheduling.html#introduction)
- [Use Case 1: Patient Portal Scheduling for existing patients](patient-scheduling.html#use-case-1-patient-portal-scheduling-for-existing-patients)
    - [Patient login](patient-scheduling.html#patient-login)
    - [Appointment Availability Discovery and Search](patient-scheduling.html#appointment-availability-discovery-and-search)
    - [Optional Hold Appointment Operation](patient-scheduling.html#optional-hold-appointment-operation)
    - [Book Appointment](patient-scheduling.html#book-appointment)

- [Use Case 2: Open Scheduling for new patient or existing patient](patient-scheduling.html#use-case-2-open-scheduling-for-new-patient-or-existing-patient)
    - [Patient Registration Option A](patient-scheduling.html#patient-registration-option-a)
    - [Appointment Availability Discovery and Search](patient-scheduling.html#appointment-availability-discovery-and-search-1)
    - [Optional Hold Appointment Operation](patient-scheduling.html#optional-hold-appointment-operation-1)
    - [Patient Registration Option B](patient-scheduling.html#patient-registration-option-b)
    - [Book Appointment](patient-scheduling.html#book-appointment-1)
    - [Patient Coverage Update Option C](patient-scheduling.html#patient-coverage-update-option-c)

- [Use Case 3 Prefetching Open Slots](patient-scheduling.html#use-case-3-prefetching-open-slots)
    - [Share Business Rules](patient-scheduling.html#share-business-rules)
    - [Subscribe for Schedule Change Notifications](patient-scheduling.html#subscribe-for-schedule-change-notifications)
    - [Initial Load](patient-scheduling.html#initial-load)
    - [Notification of schedule changes](patient-scheduling.html#notification-of-schedule-changes)
    - [“Smart Polling” for Updated Slots](patient-scheduling.html#smart-polling-for-updated-slots)
    - [Patient Registration Option A](patient-scheduling.html#patient-registration-option-a-1)
    - [Appointment Availability Discovery and Search](patient-scheduling.html#appointment-availability-discovery-and-search-2)
    - [Optional Hold Appointment Operation](patient-scheduling.html#optional-hold-appointment-operation-2)
    - [Patient Registration Option B](patient-scheduling.html#patient-registration-option-b-1)
    - [Book Appointment](patient-scheduling.html#book-appointment-2)
    - [Patient Coverage Update Option C](patient-scheduling.html#patient-coverage-update-option-c-1)

- [Canceling/Rescheduling Appointments](patient-scheduling.html#cancelingrescheduling-appointments)
    - [Usage](patient-scheduling.html#usage)

- [Releasing Holds](patient-scheduling.html#releasing-holds)
    - [Usage](patient-scheduling.html#usage-1)

- [Retrieving appointments](patient-scheduling.html#retrieving-appointments)
    - [Usage](patient-scheduling.html#usage-2)

### [Provider Based Scheduling](provider-scheduling.html)
- [Introduction](provider-scheduling.html#introduction)
- [Use Case 1: Scheduling across systems](provider-scheduling.html#use-case-1-scheduling-across-systems)
    - [Optional Find Patient](provider-scheduling.html#optional-find-patient)
    - [New Patient Registration/Coverage Information Option A](provider-scheduling.html#new-patient-registrationcoverage-information-option-a)
    - [Appointment Availability Discovery and Search](provider-scheduling.html#appointment-availability-discovery-and-search)
    - [Optional hold appointment operation](provider-scheduling.html#optional-hold-appointment-operation)
    - [New Patient Registration/Coverage Information Option B](provider-scheduling.html#new-patient-registrationcoverage-information-option-b)
    - [Book appointment](provider-scheduling.html#book-appointment)
    - [Optional exchange of patient information](provider-scheduling.html#optional-exchange-of-patient-information)

- [Use Case 2: Scheduling for existing patient across systems](provider-scheduling.html#use-case-2-scheduling-for-existing-patient-across-systems)
- [Use Case 3: Scheduling for existing patient <em>within</em> a system](provider-scheduling.html#use-case-3-scheduling-for-existing-patient-within-a-system)
- [Canceling/Rescheduling appointments](provider-scheduling.html#cancelingrescheduling-appointments)
- [Releasing holds](provider-scheduling.html#releasing-holds)
- [Retrieving Patient appointments](provider-scheduling.html#retrieving-patient-appointments)


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
- [ImplemenationGuide Resource](downloads.html#implemenationguide-resource)
- [Validator Pack and Definitions](downloads.html#validator-pack-and-definitions)
- [Schematrons](downloads.html#schematrons)
- [Examples](downloads.html#examples)
