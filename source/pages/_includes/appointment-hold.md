source file: pages/_includes/appointment-hold.md

The operation can be invoked as follows:

1.  `POST [base]/Appointment/[id]/$hold`  when using `appt-id` as an input parameter
1.  `POST [base]/Appointment/$hold`  when using `appt-resource` as an input parameter

#### Examples
{:.no_toc}

##### 1) Using `appt-id` as an input parameter

{% include appt-hold-id.md %}

##### 2) Using `appt-resource` as an input parameter

{% include appt-hold-resource.md %}
