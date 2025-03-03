import json
import random
import os
from faker import Faker

# Initialize Faker
fake = Faker()

# Lists of Georgian first names (split by gender)
georgian_male_names = [
    "Giorgi", "Davit", "Levan", "Luka", "Tornike", "Nika", "Vakhtang", "Irakli", "Zurab", "Shota"
]
georgian_female_names = [
    "Nino", "Mariam", "Ana", "Tamar", "Natia", "Ketevan", "Maia", "Salome", "Eka", "Nana"
]

# Expanded list of Georgian last names
georgian_last_names = [
    "Abashidze", "Abuladze", "Adamia", "Amirejibi", "Antidze", "Arabidze", "Arveladze", "Asatiani",
    "Babunashvili", "Bagrationi", "Bakradze", "Baratashvili", "Beridze", "Bolkvadze", "Chavchavadze",
    "Chichua", "Chkheidze", "Chkoidze", "Dadiani", "Davitashvili", "Dolidze", "Eristavi", "Gabashvili",
    "Gamkrelidze", "Gelashvili", "Gogoladze", "Gogoberidze", "Gurgenidze", "Javakhishvili", "Kalandadze",
    "Kapanadze", "Kavtaradze", "Kereselidze", "Kiknadze", "Kipiani", "Kobakhidze", "Kvaratskhelia",
    "Lortkipanidze", "Machavariani", "Maisuradze", "Mamardashvili", "Mchedlidze", "Meskhidze",
    "Mgeladze", "Mikadze", "Mkheidze", "Nadiradze", "Nakashidze", "Nizharadze", "Okropiridze",
    "Pavlenishvili", "Petviashvili", "Qipshidze", "Rurua", "Sakandelidze", "Samkharadze", "Sanaia",
    "Sharikadze", "Shengelia", "Shervashidze", "Shubladze", "Svanidze", "Taktakishvili", "Tsereteli",
    "Tsiklauri", "Tsintsadze", "Tskhvediani", "Tusishvili", "Vachnadze", "Vasadze", "Zedginidze",
    "Zurabashvili", "Zviadadze"
]

# List of Georgian cities (mostly Tbilisi)
georgian_cities = ["Tbilisi"] * 80 + ["Batumi", "Kutaisi", "Rustavi", "Gori", "Zugdidi", "Poti", "Telavi",
                                      "Akhaltsikhe"]

# Counter for customerID
customer_counter = 1


# Function to generate a single customer
def generate_customer():
    global customer_counter  # Use the global counter

    # Randomly choose gender first
    gender = random.choice(["Male", "Female"])

    # Select a first name based on gender
    if gender == "Male":
        first_name = random.choice(georgian_male_names)
    else:
        first_name = random.choice(georgian_female_names)

    # Select a last name
    last_name = random.choice(georgian_last_names)

    # Generate username, password, and email
    username = (first_name.lower() + last_name.lower()).replace(" ", "")
    password = fake.password()
    name = f"{first_name} {last_name}"
    email = f"{username}@{fake.free_email_domain()}"

    # Select city and age
    city = random.choice(georgian_cities)

    # Fix the weights to match the population length
    population = list(range(16, 61))  # Ages from 16 to 60 (45 values)
    weights = (
            [1] * 4 +  # Ages 16-19 (4 values)
            [5] * 20 +  # Ages 20-39 (20 values)
            [3] * 20 +  # Ages 40-59 (20 values)
            [1] * 1  # Age 60 (1 value)
    )

    age = random.choices(population, weights=weights, k=1)[0]

    # Create customer dictionary
    customer = {
        "customerID": customer_counter,
        "username": username,
        "password": password,
        "name": name,
        "email": email,
        "city": city.lower(),
        "age": age,
        "gender": gender
    }

    # Increment the counter for the next customer
    customer_counter += 1

    return customer


# Generate 1000 customers
customers = [generate_customer() for _ in range(20000)]

# Define the directory and file path
data_directory = "data"  # Directory name
file_path = r"C:\Users\HOME\PycharmProjects\saba-phirtskhalaishvili\finale_project\data\customers_data.json"  # Full file path

# Save to JSON file in the specified directory
with open(file_path, "w") as f:
    json.dump(customers, f, indent=4)

print(f"customers_data.json file generated successfully in the '{data_directory}' directory!")