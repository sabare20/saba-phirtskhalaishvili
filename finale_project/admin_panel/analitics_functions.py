import json
import matplotlib.pyplot as plt


def calculate_average_age(file_path="C:/Users/tornike/PycharmProjects/saba-phirtskhalaishvili/finale_project/customers_data.json"):
    with open(file_path, "r") as file:
        data = json.load(file)

    total_age = 0
    customer_count = len(data)

    for customer in data:
        total_age += customer['age']

    if customer_count > 0:
        average_age = total_age / customer_count
        print(f"The average age is: {average_age}")
        return average_age
    else:
        print("No customers found")
        return "No customers found"


def analyze_gender_distribution(file_path="C:/Users/tornike/PycharmProjects/saba-phirtskhalaishvili/finale_project/customers_data.json"):
    with open(file_path, "r") as file:
        data = json.load(file)

    gender_count = {"male": 0, "female": 0}

    for customer in data:
        gender = customer.get("gender", "").lower()
        if gender in gender_count:
            gender_count[gender] += 1

    sizes = gender_count.values()

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, autopct='%1.1f%%', startangle=90, colors=["#66b3ff", "#ff69b4"])
    plt.title("Gender Distribution of Customers")
    plt.axis("equal")
    plt.show()

    print("Gender Distribution:", gender_count)


def main():
    average_age = calculate_average_age()
    analyze_gender_distribution()


if __name__ == "__main__":
    main()
