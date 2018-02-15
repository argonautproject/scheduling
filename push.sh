#!/bin/bash
name="Argo-Scheduling"
path1 = "../IG-Template2"
echo "================================================================="
echo === Push $name IG!!! $(date -u) to github ===
echo see '/Users/ehaas/Documents/FHIR/IG-Template2/my_notes/local_workflow.mdlocal' file for how to use:
echo copy the locals docs directory from the $path1 directory
echo to this directory before pushing so have a public version
echo in GitHub Pages
echo "================================================================="
echo cp -r $path1/docs
git status
git add .
git status
git commit
git push
