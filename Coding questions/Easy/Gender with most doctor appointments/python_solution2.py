# Import your libraries
import pandas as pd

# Start writing code
medical_appointments["total"] = 1
count = pd.DataFrame(
    medical_appointments.groupby("gender").sum().reset_index()[["gender", "total"]]
)
max_count = max(count["total"][0], count["total"][1])
count[count["total"] == max_count]
