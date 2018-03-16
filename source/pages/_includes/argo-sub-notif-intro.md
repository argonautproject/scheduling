The Argonaut Scheduling Subscription Profile is defined for sending notifications to a subscriber as described in the updating slots step in [Use Case 3 Prefetching Open Slots](patient-scheduling.html#use-case-3-prefetching-open-slots). This profile identifies which core elements, extensions, vocabularies and fixed values SHALL be present in the resource when using this profile.

### Mandatory Data Elements

**Each Subscription must have:**

1. Trigger event description(s)
1. A Trigger event focus on Schedule
1. A notification endpoint
1. A notification payload profile of [Argonaut Scheduling Schedule Notification Profile](StructureDefinition-argo-sched-notif.html)


**Additional Profile specific implementation guidance:**

- The *Trigger Event Description*, *fhirPath Expression*, *Trigger Event Focus*, and *Notification Payload Profile* are all FHIR extensions defined for this Profile.
- The Subscription's criteria is based upon the Slot resource triggering events.
- The *Trigger Event Description* extension SHALL contain natural language description for the following triggers:

  1.  Slots that are open to prefetching have a change of status
  1.  Slots that are open to prefetching have a change of visit type
  1.  Slots that were previously open to prefetching are no longer open to prefetching

   and MAY include additional triggers.

- The *Trigger Event Description* extension may also include a formal expression such as SQL or a reference to a named expression.  A [FHIRPath](http://hl7.org/fhirpath/) expression may be represented using the *fhirPath Expression* extension.
- The Server is not obligated to implement the formal expressions if present and may use their own business logic to evaluate the changes defined in the event descriptions.
-  The *Notification Payload Profile* extension defines subscription's notification payload as the [Schedule](StructureDefinition-argo-sched-notif.html) instance that the triggering Slot references in the `schedule` element.
- A "hearbeat" notification should be sent with a site specific frequency and should not contain a payload.


- [Example 1](Subscription-example.html)
