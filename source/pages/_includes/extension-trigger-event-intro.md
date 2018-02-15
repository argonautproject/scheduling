A brief, natural language description of a particular event identified by the implementation environment. When this event is evaluated as true, it triggers a notification to the subscriber.

A formal expression, or a reference to a named expression may also be inlined. If the expression is a [FHIRPath](http://hl7.org/fhirpath/) expression, it evaluates in the context of a resource of one of the types identified in the [Subscription Event Focus Extension](StructureDefinition-extension-event-focus.html), and may also refer to the variable `%previous` for delta comparisons on the same type.

**Context of Use** {{site.data.structuredefinitions.[page.id].contextType}}: {{site.data.structuredefinitions.[page.id].contexts}}
