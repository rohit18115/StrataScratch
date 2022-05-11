SELECT gender , count(appointmentid) AS n_appointments 
FROM medical_appointments
GROUP BY gender
ORDER BY n_appointments DESC
LIMIT 1