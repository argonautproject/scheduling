This profile sets the minimum expectations for the Slot resource to record, search and fetch basic information about an individual slot when prefetching slots. It identifies which core elements, extensions, vocabularies and value sets SHALL be present in the resource when using this profile.

This profile is defined for:

- Use in the Bundle resource as a result of the prefetch 'initial load' and polling update interactions.

### Mandatory Data Elements

**Each Slot must have:**

1. an id
1. a status
1. a location or practitioner schedule
1. a start and end time

**The system [Must Support]({{site.data.fhir.uscore}}guidance.html#must-support) if available:**

1. a visit type
1. comments to describe any extended information

**Additional Profile specific implementation guidance:**

- For additional implementation or site specific context os constraints (For example qualification on visit types such as age restrictions for well child visits.) use `Slot.comment`. The example below demonstrates is usage.

#### Examples

- [Slot Example 1](Slot-2017-09-07T154500-arg-s-6.html)
