    appt-output-search.md file


[Syntax]({{site.data.fhir.uscore}}/guidance.html#readfetch-resource-notation)

**`GET [base]/Appointment?patient=[id]{&status=[status]}{&date=[date]{&date=[date]}}{&pracititioner=Practitioner/[id]}`**

*Support:* Mandatory

*Implementation Notes:*  Fetches all appointments for a patient. May include additional search parameters:

- filter by status such as 'booked'
- filter by a date or a date range ( including the date modifiers 'ge','le','gt','lt')
- filter by a practitioner

Examples:

Search for all appointments for a patient with Resource ID 1234: `GET [base]/Appointment?patient=1234`

Search for all booked appointments for this patient: `GET [base]/Appointment?patient=1234&status=booked`

Fetch all completed appointments for this patient since January: `GET [base]/Appointment?patient=1234&status=fulfilled&date=ge2017-01-01`

Fetch all completed appointments  with Dr Y for this patient since January : `GET [base]/Appointment?patient=1234&status=fulfilled&date=ge2017-01-01&practitioner=Practitioner/Dr+Y`
