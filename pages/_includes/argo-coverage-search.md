
\argo-coverage-search.md file

To update the existing insurance information (or create it if it is new), The Client uses the standard FHIR RESTful [update API]({{site.data.fhir.path}}/http.html#update) as shown:

   `PUT [base]/Coverage/[id]`

- Note that the server MAY reject certain updates to the coverage information (for example, type of coverage) and SHOULD return an [OperationOutcome]({{site.data.fhir.path}}/operationoutcome.html) explaining the reason.[Issue #47](../issues/47)

##### Example

~~~
PUT [base]/Coverage/[id]....

~~~
<br />
