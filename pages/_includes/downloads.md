# {{ page.title }}
{:.no_toc}

source pages/\_include/{{page.md_filename}}.md  file

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc' -->

* Do not remove this line (it will not be displayed)
{:toc}

## Validator Pack and Definitions:

The following file contains all the value sets, profiles, extensions, list of pages and urls in the IG, etc defined as part of the this Implementation Guide.:

- [Validator Pack](validator.pack)

In addition there are format specific definitions files.
- [XML](definitions.xml.zip)
- [JSON](definitions.json.zip)
- [TTL](definitions.ttl.zip)

These files should be the first choice whenever generating any implementation artifacts since they contain all of the rules about what makes these US-Core profiles valid. Implementers will still need to be familiar with the content of the specification and profiles that apply in order to make a conformant implementation.  See the overview on [validating FHIR profiles and resources]({{ site.data.fhir.path }}/validation.html)

## Schematrons:

Schematrons for the profiles defined in this guide are also available and listed below:

- [Schematrons](#)

## Examples:

All the examples that are used in this guide are available for download:

- [XML](examples.xml.zip)
- [JSON](examples.json.zip)
- [TTl](examples.ttl.zip)
