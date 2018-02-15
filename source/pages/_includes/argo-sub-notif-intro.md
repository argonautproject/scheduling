The Argonaut Scheduling Subscription Profile is defined for sending notifications to a subscriber as described in the updating slots step in [Use Case 3 Prefetching Open Slots](patient-scheduling.html#use-case-3-prefetching-open-slots).  It identifies which core elements, extensions, vocabularies and fixed values SHALL be present in the resource when using this profile.

### Mandatory Data Elements

**Each Subscription must have:**

1. Trigger event description(s)
1. A Trigger event focus on Schedule
1. A notification endpoint
1. A notification payload profile of [Argonaut Scheduling Schedule Notification Profile](StructureDefinition-argo-sched-notif.html)


**Additional Profile specific implementation guidance:**

- The trigger event description, Trigger event focus. and notification payload profile are all FHIR extensions defined for this Profile.
- There SHALL be a trigger event descriptions which SHALL contain the following natural language description - "schedules that are open to prefetching and where any slots that reference the schedule have changed" - and MAY include a formal expression such as SQL a [FHIRPath](http://hl7.org/fhirpath/) expression, or a reference to a named expression.
- There SHALL be a trigger event descriptions which SHALL contain the following natural language description - "schedules that are no longer open to prefetching" - and MAY include a formal expression such as SQL a [FHIRPath](http://hl7.org/fhirpath/) expression, or a reference to a named expression.
- The Server is not obligated to implement the formal expressions if present and may use their own business logic to evaluate the schedules for the changes defined in the event descriptions.

- [Example 1](Subscription-example.html)
