import pandas as pd

# Step 1: Create your table data
data = {
    "Name": ["nicholas", "Matthew", "Conan", "Daniel"],
    "CGPA": [8.5, 7.9, 9.1, 8.2]
}

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Save as CSV
df.to_csv("students.csv", index=False)

# Step 4: Save as Excel
df.to_excel("students.xlsx", index=False)
pd.read_csv("C:\\Users\\Saanvi\\.ipython\\students.csv")
