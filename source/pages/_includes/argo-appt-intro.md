source file: _includes/argo-appt-intro.md


This profile sets minimum expectations for the Appointment resource to record, search and fetch basic information about an individual appointment. It identifies which core elements, extensions, vocabularies and value sets SHALL be present in the resource when using this profile.

This profile is defined for:

- Use in the Bundle resource as a result of the $find, $hold, and $ book operations.
- Patient searching for their appointments.
- Provider searching for their appointments.

##### Mandatory Data Elements and Terminology

The following data-elements are mandatory (i.e data MUST be present).

**Each Appointment must have:**

1. a status (e.g., 'proposed')
1. a start and end time
1. a list of participants and their individual statuses (e.g., the patient will be there)
1. the times that were requested for this appointment

**The system [Must Support]({{site.data.fhir.uscore}}guidance.html#must-support) if available:**

1. An Appointment resource ID
1. A visit type
1. Specialty
1. Appointment type
1. Status reason

**Additional Profile specific implementation guidance:**

 - The [Appointment State Diagram](state-diagram.html) SHOULD be referenced to when considering the statuses of the scheduling resources during the scheduling workflow.
 - The Specialty codes are bound to the [Argonaut Scheduling Specialties](ValueSet-specialty.html) valueset which is based upon SNOMED CT.  There are other provider specialty code systems that implementers should be aware of including *NUCC* codes, and *CMS Provider* types.  More information on them can be found [here](https://www.cms.gov/Medicare/Provider-Enrollment-and-Certification/MedicareProviderSupEnroll/Taxonomy.html).

#### Examples

- [Proposed Appt 1](Appointment-proposed-appt1.html)
- [Proposed Appt 2](Appointment-proposed-appt2.html)
- [Proposed Appt 3](Appointment-proposed-appt3.html)
