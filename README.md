# IG-Template
A template for building IG based on the Argonaut and US-Core IG

Here some screenshots:

1. **index.html (home) page:**

![index.html page](ss1.png)

2. **profile list page:**

![profile list page](ss2.png)

3. **individual profile page:**

![profile page](ss3.png)

4. **example page:**

![example](ss4.png)




See FHIR [IG publsiher documentation](http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation)  for how to set up your local environment.   

You will also need to have the following directories in the same path:

- `temp`
- `output`
- `qa`

There is a python file that will create the ig.json and ig.xnl file based on the content in the `resources` and `example` directories.  The bash scripts to run the ig publisher with or withoutthe python script.

Authors:  Eric Haas, Brett Marquard


-----

GitHub will automatically trigger a new build whenever you commit changes.
(To manually trigger a build, just `POST` to the Webhook URL yourself, for example via:
`curl -X POST "https://2rxzc1u4ji.execute-api.us-east-1.amazonaws.com/prod/publish?Healthedata1/IG-Template"`)

*Note: a build takes 2-3 minutes to complete. Then you can...*

### Find your rendered IG automatically available at

http://build.fhir.org/ig/Healthedata1/IG-Template

### Find debugging info about the build

http://build.fhir.org/ig/Healthedata1/IG-Template/debug.tgz
