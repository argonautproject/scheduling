# Welcome to the [Argonaut](http://argonautwiki.hl7.org/index.php?title=Main_Page) Scheduling Implementation Guide

Argonaut Lead: [Micky Tripathi](mtripathi@maehc.org)

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

https://argonautproject.github.io/scheduling/

(GitHub will automatically trigger a new build whenever you commit changes.)

## Setup instructions

See the [FHIR IG publisher documentation](http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation)  for how to set up your local environment.

You will also need to import these modules

- [IG-Template](https://github.com/Healthedata1/IG-Template): a module containing all the static template and pages and build files for FHIR IG Publishing

- If using the bash scripts `publish2.sh` you will also need the file. [IG-FileBuilder](https://github.com/Healthedata1/FHIR-IGPub-filebuilder): A python script that will create the ig.json and ig.xnl file based on the content in the `resources` and `example` directories.  See the inline comments for how to use.

#### To run the igpublisher from directly from the command line:

1. copy the ig.json file to the IG-Template folder
1. run the command line from this cloned (source) directory:

    java -jar ${path1}org.hl7.fhir.igpublisher.jar -ig ${path2}ig.json -watch

where:
- ${path1} = relative or absolute path to the jar file
- ${path2} = relative or absolute path to the IG-Template folder

####  To run the igpublisher using the bash scripts

- update the path and title in the script to local names and paths.  The scripts run from the source directory.
- If using the bash scripts:  `publish2.sh` the relative locations of the two modules above need to updated in The `definitions.csv` file.
- To update the ig.json and ig.xml files using the IG-Filebuilder prior to running the ig publisher

     bash publish2.sh

- To run the ig publisher

     bash publish.sh















Some screenshots....
