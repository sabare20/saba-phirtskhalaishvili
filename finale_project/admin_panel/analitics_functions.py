import json
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class JSONReader:
    def __init__(self, customer_file_path, sales_file_path):
        self.customer_file_path = customer_file_path
        self.sales_file_path = sales_file_path

    def read_customers(self):
        with open(self.customer_file_path, "r") as file:
            return json.load(file)

    def read_sales(self):
        with open(self.sales_file_path, "r") as file:
            return json.load(file)


reader = JSONReader(
    "C:/Users/tornike/PycharmProjects/saba-phirtskhalaishvili/finale_project/data/customers_data.json",
    "C:/Users/tornike/PycharmProjects/saba-phirtskhalaishvili/finale_project/data/sales_data.json"
)


def calculate_average_age():
    data = reader.read_customers()

    total_age = 0
    customer_count = len(data)

    for customer in data:
        total_age += customer['age']

    if customer_count > 0:
        average_age = total_age / customer_count
        print(f"The Average Age is: {round(average_age, 2)}")
        return average_age
    else:
        print("No customers found")
        return "No customers found"


def gender_distribution():
    data = reader.read_customers()

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
    data = reader.read_customers()

    city_count = {}

    for customer in data:
        city = customer.get("city", "").lower()
        if city:
            city_count[city] = city_count.get(city, 0) + 1

    # Print the sales in each city
    print("Sales in each city:")
    for city, count in city_count.items():
        print(f"\t-{city.capitalize()}: {count} sales")

    # Find the city with the maximum sales
    max_city = max(city_count, key=city_count.get)
    max_sales = city_count[max_city]
    print(f"\nThe highest number of sales ({max_sales} sales) occurred in {max_city.capitalize()}.")

    # Visualization
    sorted_cities = sorted(city_count.items())
    cities, counts = zip(*sorted_cities)

    city_df = pd.DataFrame(counts, index=cities, columns=["Sales"])

    plt.figure(figsize=(12, 6))
    sns.heatmap(city_df.T, annot=True, cmap='YlGnBu', cbar=True, fmt="d", linewidths=0.5)

    plt.title("City Distribution of Customers (Heatmap)", fontsize=16)
    plt.xlabel("Cities", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def calculate_and_visualize_revenue():
    sales_data = reader.read_sales()

    total_quantity = 0

    for i in sales_data:
        total_quantity += i["quantity"]
    print(f"Total Quantity of Sold Board_Games: {total_quantity}")

    revenue_by_city = {}
    for sale in sales_data:
        city = sale["city"]
        revenue = sale["totalPrice"]
        if city in revenue_by_city:
            revenue_by_city[city] += revenue
        else:
            revenue_by_city[city] = revenue

    total_revenue = sum(revenue_by_city.values())
    print(f"Total Revenue Across All Cities: ${total_revenue:.2f}")

    # Print revenue by each city
    print("\nCity-wise Revenue:")
    for city, revenue in revenue_by_city.items():
        print(f"\t-{city}: ${revenue:.2f}")

    # Prepare data for visualization
    cities = list(revenue_by_city.keys())
    revenues = list(revenue_by_city.values())

    revenue_array = np.array(revenues)
    color_threshold = np.percentile(revenue_array, 75)  # Define a threshold for "much higher revenue"
    colors = ["lightblue" if revenue < color_threshold else "orange" for revenue in revenues]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(cities, revenues, color=colors, edgecolor="black")

    for bar, revenue in zip(bars, revenues):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                 f"${revenue:.2f}", ha='center', fontsize=10)

    plt.title("Total Revenue by City", fontsize=16)
    plt.xlabel("City", fontsize=14)
    plt.ylabel("Revenue ($)", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.tight_layout()

    plt.show()


def main():
    calculate_average_age()
    print("-" * 5)
    gender_distribution()
    print("-" * 5)
    city_distribution()
    print("-" * 5)
    calculate_and_visualize_revenue()


if __name__ == "__main__":
    main()
