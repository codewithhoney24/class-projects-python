import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Student Data Generator", layout="wide")
st.title("Student CSV File Generator")

# Male & Female Names
male_names = ["Waqas", "Zai", "Aamir", "Abid", "Thair", "Sajid", "Nazim", "Moosa", "Anas"]
female_names = ["Sara", "Nadia", "Alishba", "Ayesha", "Benish", "Saba", "Sadia"]

cities = ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar", "Multan"]
states = ["Sindh", "Punjab", "KPK", "Balochistan", "Gilgit", "AJK"]

students = []

# Sample unique names (8 males + 7 females = 15 total)
selected_male_names = random.sample(male_names, 8)
selected_female_names = random.sample(female_names, 7)
all_names = [(name, "Male") for name in selected_male_names] + [(name, "Female") for name in selected_female_names]
random.shuffle(all_names)  # Mix the genders

# Grade based on marks
def get_grade(marks):
    if marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"

# GPA based on marks
def get_gpa(marks):
    if marks >= 85:
        return round(random.uniform(3.6, 4.0), 2)
    elif marks >= 70:
        return round(random.uniform(3.0, 3.5), 2)
    elif marks >= 60:
        return round(random.uniform(2.5, 2.9), 2)
    elif marks >= 50:
        return round(random.uniform(2.0, 2.4), 2)
    elif marks >= 40:
        return round(random.uniform(1.5, 1.9), 2)
    else:
        return round(random.uniform(0.0, 1.4), 2)

for i, (name, gender) in enumerate(all_names, start=1):
    age = random.randint(18, 25)
    attendance = f"{random.randint(70, 100)}%"
    marks = random.randint(0, 100)
    grade = get_grade(marks)
    gpa = get_gpa(marks)

    contact_number = f"03{random.randint(0, 9)}-{random.randint(10000000, 99999999)}"
    email = f"{name.lower()}{i}@example.com"

    # Address variations
    city = random.choice(cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    street = f"{random.randint(1, 1000)} Street"
    house_no = f"House #{random.randint(10, 999)}"

    address_formats = [
        f"{street}",
        f"{house_no}, {city}",
        f"{city}, {state}",
        f"{zip_code}",
        f"{street}, {city}, {state}",
        f"{house_no}, {zip_code}",
        f"{house_no}, {street}, {state}",
        f"{street}, {zip_code}",
    ]
    address = random.choice(address_formats)

    student = {
        "ID": i,
        "Name": name,
        "Gender": gender,
        "Age": age,
        "Attendance": attendance,
        "Marks": marks,
        "Grade": grade,
        "GPA": gpa,
        "Contact Number": contact_number,
        "Email": email,
        "Address": address
    }

    students.append(student)

# Create DataFrame
df = pd.DataFrame(students)

# Display
st.subheader("Generated Students Data")
st.dataframe(df)

# CSV download
csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV File", csv_file, "students.csv", "text/csv")

st.success("Students Record Generated Successfully!")
