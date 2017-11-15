#!/bin/bash
name="Argo-Scheduling"
path1=/Users/ehaas/Documents/FHIR/IG-Template/
path2=/Users/ehaas/Downloads/
path3=/Users/ehaas/Documents/FHIR/IG-tools/
echo "================================================================="
echo === Publish $name IG!!! $(date -u) ===
echo === run bash publish2.sh to update ig.json ===
echo === ig.json needs to be in ${path1} ===
echo "================================================================="
echo getting rid of .DS_Store files since they gum up the igpublisher....
find . -name '.DS_Store' -type f -delete
sleep 1
git status
sleep 3
python3.5 ${path3}definitions.py
sleep 3
git status
java -jar ${path2}org.hl7.fhir.igpublisher.jar -ig ${path1}ig.json -watch
