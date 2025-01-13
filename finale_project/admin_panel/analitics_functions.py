import json
import matplotlib.pyplot as plt

# Define the file path globally
file_path = "C:/Users/tornike/PycharmProjects/saba-phirtskhalaishvili/finale_project/data/customers_data.json"


def read_json_file():
    with open(file_path, "r") as file:
        return json.load(file)


def calculate_average_age():
    data = read_json_file()

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


def gender_distribution():
    data = read_json_file()

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


def city_distribution():
    data = read_json_file()

    city_count = {}

    for customer in data:
        city = customer.get("city", "").lower()
        if city:
            city_count[city] = city_count.get(city, 0) + 1

    # Print sales in each city
    print("Sales in each city:")
    for city, count in city_count.items():
        print(f"\t-{city.capitalize()}: {count} sales")

    # Find the city with the maximum sales
    max_city = max(city_count, key=city_count.get)
    max_sales = city_count[max_city]
    print(f"\nThe highest number of sales ({max_sales} sales) occurred in {max_city.capitalize()}.")

    sorted_cities = sorted(city_count.items())
    cities, counts = zip(*sorted_cities)

    colors = ["#66b3ff", "#ffcc00", "#ff6347", "#98fb98", "#ff1493", "#f0e68c", "#dda0dd", "#00fa9a"]

    plt.figure(figsize=(10, 6))
    plt.plot(cities, counts, marker='o', color='blue', linestyle='-', markersize=8)

    plt.title("City Distribution of Customers", fontsize=14)
    plt.xlabel("Cities", fontsize=12)
    plt.ylabel("Quantity of Products Sold", fontsize=12)

    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    calculate_average_age()
    print("-" * 5)
    gender_distribution()
    print("-" * 5)
    city_distribution()


if __name__ == "__main__":
    main()
