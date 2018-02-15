|State|Activity Description|Slot|Appointment|
|---|---|---|---|
||The schedule is created/published |status = free||
||An appointment availability request is processed to locate available slots for all participants |status = free||
|1.|An appointment availability request is processed and available appointments created ||status = proposed, participant.status = needs-action|
||*Optional: The hold request for an available appointment is processed and the slot status updated *|status = busy-tentative||
||*Optional: The appointment hold is accepted as described – by all participants*||participant.status = tentative|
|2.|*Optional: An appointment hold request is processed and the appointment updated. *||status = pending, participant.status = tentative|
||The appointment request is processed and the slot status updated |status = busy-tentative||
|2.|An appointment request is processed and the appointment updated ||status = pending, participant.status = needs-action/tentative|
||The appointment is accepted as described – by all participants ||participant.status = accepted|
||*Optional: The patient is registered within the system. I.e., create Patient resource for patient and appointment is accepted by patient*||patient participant.status = accepted|
|3.|The appointment is confirmed as accepted by all participants |status = busy|status = booked, participant.status = accepted|
