# Import your libraries
import pandas as pd

# Start writing code
medical_appointments.head()

results = medical_appointments.groupby("gender")["appointmentid"].count().reset_index()

df = results[results["appointmentid"] == results["appointmentid"].max()]
