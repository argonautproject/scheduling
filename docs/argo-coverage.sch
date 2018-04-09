<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2">
  <sch:ns prefix="f" uri="http://hl7.org/fhir"/>
  <sch:ns prefix="h" uri="http://www.w3.org/1999/xhtml"/>
  <!-- 
    This file contains just the constraints for the profile Coverage
    It includes the base constraints for the resource as well.
    Because of the way that schematrons and containment work, 
    you may need to use this schematron fragment to build a, 
    single schematron that validates contained resources (if you have any) 
  -->
  <sch:pattern>
    <sch:title>f:Coverage</sch:title>
    <sch:rule context="f:Coverage">
      <sch:assert test="count(f:status) &gt;= 1">status: minimum cardinality of 'status' is 1</sch:assert>
      <sch:assert test="count(f:payor) &gt;= 1">payor: minimum cardinality of 'payor' is 1</sch:assert>
      <sch:assert test="count(f:grouping) &gt;= 1">grouping: minimum cardinality of 'grouping' is 1</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>Coverage</sch:title>
    <sch:rule context="f:Coverage">
      <sch:assert test="not(parent::f:contained and f:contained)">If the resource is contained in another resource, it SHALL NOT contain nested Resources (inherited)</sch:assert>
      <sch:assert test="not(parent::f:contained and f:text)">If the resource is contained in another resource, it SHALL NOT contain any narrative (inherited)</sch:assert>
      <sch:assert test="not(exists(f:contained/*/f:meta/f:versionId)) and not(exists(f:contained/*/f:meta/f:lastUpdated))">If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (inherited)</sch:assert>
      <sch:assert test="not(exists(for $id in f:contained/*/@id return $id[not(ancestor::f:contained/parent::*/descendant::f:reference/@value=concat('#', $id))]))">If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>f:Coverage/f:grouping</sch:title>
    <sch:rule context="f:Coverage/f:grouping">
      <sch:assert test="count(f:plan) &gt;= 1">plan: minimum cardinality of 'plan' is 1</sch:assert>
      <sch:assert test="count(f:planDisplay) &gt;= 1">planDisplay: minimum cardinality of 'planDisplay' is 1</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>Coverage.grouping</sch:title>
    <sch:rule context="f:Coverage/f:grouping">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
</sch:schema>
