#### Summary of the input data elements

1. status:  MAY support one `Appointment.status` with a fixed value of "proposed"
1. serviceType:  MUST support one or more `Appointment.serviceType` which has an extensible binding  to the [Service Type](#) value set.
1. specialty:  MUST support one or more `Appointment.specialty` which has a **required** binding  to the [Specialty](#) value set.
1. appointmentType:  MUST support one `Appointment.appointmentType` which has an **example** binding  to the [Appointment Type](#) value set.
1. reason:  MUST support one or more `Appointment.reason` which has an extensible binding t to the [Reason Code](#) value set.
1. indication:  MUST support references to :
  - Condition
  - or Procedure

   using `Appointment.indication`
1. commment:  MUST support one `Appointment.comment`
1. participant:  MUST support at least one `Appointment.participant` where:
   1. participant.actor:  MUST support references to :
      - Patient
      - Practitioner
      - or HealthcareService

      using `Appointment.participant.actor`
   1. participant.status:  MAY support one `Appointment.participant.status` with a fixed value of "needs-action"
1. requestedPeriod:  MUST contain at least one `Appointment.requestedPeriod`
