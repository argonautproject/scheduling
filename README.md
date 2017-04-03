# Welcome to the [Argonaut](http://argonautwiki.hl7.org/index.php?title=Main_Page) Scheduling Implementation Guide

Project Lead: [Micky Tripathi](mtripathi@maehc.org)

Project Coordinator: [Jennifer Monahan](jmonahan@maehc.org)

FHIR SME and Facilitator: [Eric Haas](ehaas@healthedatainc.com)

FHIR SME and Facilitator: [Brett Marquard](brett@riverrockassociates.com)


## Scope of Work

Support basic patient and provider access to a provider's calendar and appointment requests including APIs and guidance.

## Timeline

![timeline](https://github.com/argonautproject/scheduling/blob/master/meeting-notes/Screen%20Shot%202017-04-03%20at%2011.08.16%20AM.png)

## Meetings Notes

Meeting agenda and notes are archived [here](https://github.com/argonautproject/scheduling/tree/master/meeting-notes)

## Issues

Issues will be listed and tracked on this Github repository site [here](https://github.com/argonautproject/scheduling/issues).

### Rendered Scheduling Implementation Guide at

http://build.fhir.org/ig/Healthedata1/IG-Template

(GitHub will automatically trigger a new build whenever you commit changes.)

Debugging info about the build: http://build.fhir.org/ig/Healthedata1/IG-Template/debug.tgz)

## Setup instructions

You will also need to add the following directories to the same path:

- `temp`
- `output`
- `qa`

There is a python file that will create the ig.json and ig.xnl file based on the content in the `resources` and `example` directories.  See the inline comments for how to use.  The bash scripts to run the ig publisher with or without the python script.  

Some screenshots...

1. **index.html (home) page:**

![index.html page](ss1.png)

2. **profile list page:**

![profile list page](ss2.png)

3. **individual profile page:**

![profile page](ss3.png)

4. **example page:**

![example](ss4.png)














