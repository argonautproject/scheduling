argo-coverage-intro.md file

This profile sets minimum expectations for Coverage resource to update or create patient coverage information for the use in scheduling appointments.

### Mandatory Data Elements

**Each Coverage must have:**

1. a status
1. a payor
1. a plan id and name

**The system [Must Support]({{site.data.fhir.uscore}}guidance.html#must-support) if available:**

1. a Coverage resource ID
1. a Subscriber ID
1. a Subscriber (in case of dependent)
1. type of coverage
1. coverage period

**Additional Profile specific implementation guidance:**

1. The `Coverage.subscriber` element references a Patient resource directly or indirectly through the RelatedPerson resource. If the Patient Id is unknown:

    - Option 1: Patient must be registered and Patient Id fetched before the Coverage interaction.
    - Option 2: Transmit Patient, Coverage and if needed RelatedPerson as a Bundle transaction following the Bundle [resource url rules]({{site.data.fhir.path}}/bundle.html#bundle-unique).
    - Option 3: Don't transmit the `subscriber` element when subscriber is the patient (in other words, `Coverage.relationship` = 'self'). When subscriber is not the patient (in other words, `Coverage.relationship` != 'self'), [contain]({{site.data.fhir.path}}/references.html#contained) the RelatedPerson resource and don't transmit the `RelatedPerson.patient` element.

#### Examples

- [Coverage Example 1](Coverage-argo-sch-1.html)
- [Coverage Example 2](Coverage-argo-sch-2.html)
