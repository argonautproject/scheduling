Search for all appointments for a patient with Resource ID 1234: `GET [base]/Appointment?patient=1234`

Search for all booked appointments for this patient: `GET [base]/Appointment?patient=1234&status=booked`

Fetch all completed appointments for this patient since January: `GET [base]/Appointment?patient=1234&status=fulfilled&date=ge2017-01-01`

Fetch all completed appointments with Dr Y for this patient since January : `GET [base]/Appointment?patient=1234&status=fulfilled&date=ge2017-01-01&practitioner=Dr+Y`
