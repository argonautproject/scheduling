Fetch all of a practitioner's appointments (all statuses):
`GET [base]\Appointment?practitioner=[id]`

Fetch all open appointments:
`GET [base]\Appointment?practitioner=[id]&status=free`

Fetch all completed appointments since October:
`GET [base]\Appointment?practitioner=[id]&status=fulfilled&date=ge2017-10-01`

Fetch all completed appointments for a patient since October:
`GET [base]\Appointment?practitioner=[id]&patient=[id]&status=fulfilled&date=ge2017-10-01`
