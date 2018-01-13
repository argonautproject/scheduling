The Argonaut Appointment Bundle profile sets the minimum expectations for the Bundle resource which is returned as a result of the `$find` operation and when fetching appointments.

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

- [Operation$find Example 1a](Bundle-hal-dr-y-appts.html)
- [Operation$find Example 2b](Bundle-prefetch-derm-appts.html)
