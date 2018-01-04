argo-coverage-intro.md file

    This is the introduction markdown file that gets inserted into the sd.html template.

    This profile sets minimum expectations for blah blah blah

    ##### Mandatory Data Elements and Terminology

    The following data-elements are mandatory (i.e data MUST be present). blah blah blah

    **must have:**

    1. blah
    1. blah
    1. blah

**Additional Profile specific implementation guidance:**

1. The `Coverage.subscriber` element references a Patient resource directly or indirectly through the RelatedPerson resource. When the Patient Id is unknown:

    - Option 1: Patient must be registered and Patient Id fetched before the Coverage interaction.
    - Option 2: Transmit Patient, Coverage and if needed RelatedPerson as a Bundle transaction following the Bundle [resource url rules]({{site.data.fhir.path}}/bundle.html#bundle-unique).
    - Option 3: Don't transmit the `subscriber` element when subscriber is the patient (in other words, `Coverage.relationship` = 'self'). When subscriber is not the patient (in other words, `Coverage.relationship` != 'self'), [contain]({{site.data.fhir.path}}/references.html#contained) the RelatedPerson resource and don't transmit the `RelatedPerson.patient` element.

#### Examples

- [Coverage Example 1](Coverage-argo-sch-1.html)
- [Coverage Example 2](Coverage-argo-sch-2.html)
