---
title: Appointment State Diagram
layout: default
active: state
---

### Introduction

It is important to understand the state transitions during the scheduling process and the typical flow of statuses for an Appointment and associated Slot resources.  This State Diagram should be referenced to when considering the statuses of the scheduling resources.


{% include img.html img="appt-state.png" caption="Figure 1: Appointment State Diagram based on the Appointment.status codes" %}



Typical flow of statuses for an appointment from appointment availability to booking including the [Slot](http://build.fhir.org/slot.html) resource from context of the scheduling service.  (modified from the [Appointment](http://build.fhir.org/appointment.html) resource notes)

|Step|Activity Description (Role: Scheduler)|Slot|Appointment|
|---|---|---|---|
|1|The schedule is created/published |status = free||
|2|An appointment availability request is processed to locate available slots for all participants |status = free||
|3|An appointment availability request is processed and available appointments created ||status = proposed, participant.status = needs-action|
|4|*Optional: The hold request for an available appointment is processed and the slot status updated for all participants*|status = busy-tentative||
|5|*Optional: An appointment hold request is processed and the appointment updated.*||status = pending, participant.status = tentative|
|6|The appointment request is processed and the slot status updated for all participants |status = busy-tentative||
|7|*Optional: The patient is registered within the system. I.e., create Patient resource for patient and appointment is accepted by patient*||patient participant.status = accepted|
|8|The appointment is confirmed as accepted by all participants |status = busy|status = booked, participant.status = accepted|
{: .grid}

Flow for the rejection of an appointment request by scheduler beginning from steps 4 or 6.

|Step|Activity Description (Role: Scheduler)|Slot|Appointment|
|---|---|---|---
|4r or 6r|The appointment request is processed and unable to update slot status for all participants. (i.e., slot status != free)|status varies||
|6r|The appointment is cancelled. Update participant status|status varies|status = cancelled, participant.status = declined (may be other statuses too)||
{: .grid}

Flow for the cancellation of an appointment by patient following step 8.

|Step|Activity Description (Role: Scheduler)|Slot|Appointment|
|---|---|---|---|
|8|The appointment is confirmed as accepted by all participants |status = busy|status = booked, participant.status = accepted|
|9c|An appointment cancel request is processed. The appointment is declined by patient||patient participant.status = declined|
|10c|The appointment is cancelled|status = free|status = cancelled, participant.status = declined||
{: .grid}
