The Slot Bundle profile sets the minimum expectations for the Bundle resource which is returned as a result of the prefetch ‘initial load’ and polling update interactions when prefetching slots.

### Mandatory Data Elements

**Each Bundle must have:**

1. a bundle type
1. a total number of matches

**The system [Must Support]({{site.data.fhir.uscore}}guidance.html#must-support) if available:**

1. Appointment entries
1. OperationOutcome entry

**Additional Profile specific implementation guidance:**

- None

#### Examples

- [Prefetch Slot Bundle Example](Bundle-slot-bundle-example.html)
