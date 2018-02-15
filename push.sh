#!/bin/bash
name="Argo-Scheduling"
while getopts s option
do
 case "${option}"
 in
 s) path1='../IG-Template2';;
 esac
done
echo "================================================================="
echo === Push $name IG!!! $(date -u) to github ===
echo see '/Users/ehaas/Documents/FHIR/IG-Template2/my_notes/local_workflow.mdlocal' file for how to use:
echo "================================================================="
if [[ $path1 ]]; then
  echo "================================================================="
  echo copy the locals docs directory from the $path1 directory
  echo to this directory before pushing so have a public version
  echo in GitHub Pages
  echo "================================================================="
  rm -r docs/*
  cp -r $path1/docs .
fi
git status
git add .
git status
git commit
git push
