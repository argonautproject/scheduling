# IG-Template  
Authors:  Eric Haas, Brett Marquard

A template for building an FHIR Implemenation Guide(IG) using the IG publisher and profile spreadsheets.  This is based on the design of the [Argonaut](http://www.fhir.org/guides/argonaut/r2/) and [US-Core](http://hl7.org/fhir/us/core/) IGs.    See the [FHIR IG publisher documentation](http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation)  for how to set up your local environment.  

### Rendered IG-Template at

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














