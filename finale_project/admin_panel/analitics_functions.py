import json
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class JSONReader:
    def __init__(self, customer_file_path, sales_file_path, donations_file_path, delivery_file_path):
        self.customer_file_path = customer_file_path
        self.sales_file_path = sales_file_path
        self.donations_file_path = donations_file_path
        self.delivery_file_path = delivery_file_path

    def read_customers(self):
        with open(self.customer_file_path, "r") as file:
            return json.load(file)

    def read_sales(self):
        with open(self.sales_file_path, "r") as file:
            return json.load(file)

    def read_donations(self):
        with open(self.donations_file_path, "r") as file:
            return json.load(file)

    def read_deliveries(self):
        with open(self.delivery_file_path, "r") as file:
            return json.load(file)


reader = JSONReader(
    "C:/Users/tornike/PycharmProjects/saba-phirtskhalaishvili/finale_project/data/customers_data.json",
    "C:/Users/tornike/PycharmProjects/saba-phirtskhalaishvili/finale_project/data/sales_data.json",
    "C:/Users/tornike/PycharmProjects/saba-phirtskhalaishvili/finale_project/data/donations_data.json",
    "C:/Users/tornike/PycharmProjects/saba-phirtskhalaishvili/finale_project/data/delivery_data.json"
)


def calculate_average_age():
    data = reader.read_customers()

    total_age = 0
    male_age_total = 0
    female_age_total = 0
    male_count = 0
    female_count = 0

    customer_count = len(data)

    for customer in data:
        total_age += customer['age']

        if customer['gender'].lower() == 'male':
            male_age_total += customer['age']
            male_count += 1
        elif customer['gender'].lower() == 'female':
            female_age_total += customer['age']
            female_count += 1

    if customer_count > 0:
        average_age = total_age / customer_count
        print(f"The Average Age is: {round(average_age, 2)}")
    else:
        print("No customers found")
        return "No customers found"

    if male_count > 0:
        male_average_age = male_age_total / male_count
        print(f"The Average Age of Males is: {round(male_average_age, 2)}")
    else:
        print("No male customers found")

    if female_count > 0:
        female_average_age = female_age_total / female_count
        print(f"The Average Age of Females is: {round(female_average_age, 2)}")
    else:
        print("No female customers found")

    return {
        "overall_average": round(average_age, 2) if customer_count > 0 else None,
        "male_average": round(male_average_age, 2) if male_count > 0 else None,
        "female_average": round(female_average_age, 2) if female_count > 0 else None
    }


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
    sales_data = reader.read_sales()

    city_count = {}
    city_revenue = {}

    for sale in sales_data:
        city = sale.get("city", "").lower()
        if city == "":
            city = "guests"
        if city:
            city_count[city] = city_count.get(city, 0) + sale["quantity"]
            city_revenue[city] = city_revenue.get(city, 0) + sale["totalPrice"]

    print("Sales in each city:")
    for city, count in city_count.items():
        print(f"\t-{city.capitalize()}: {count} units sold")

    print("\nSales Revenue from each city:")
    for city, sales_revenue in city_revenue.items():
        print(f"\t-{city.capitalize()}: ${sales_revenue:.2f}")

    if city_count:
        max_city_sales = max(city_count, key=city_count.get)
        max_sales = city_count[max_city_sales]
        print(f"\nThe highest number of units sold ({max_sales}) occurred in {max_city_sales.capitalize()}.")

        max_city_revenue = max(city_revenue, key=city_revenue.get)
        max_revenue = city_revenue[max_city_revenue]
        print(f"The highest sales revenue (${max_revenue:.2f}) came from {max_city_revenue.capitalize()}.")
    else:
        print("\nNo sales data found.")

    sorted_cities = sorted(city_count.items())
    cities, counts = zip(*sorted_cities)
    revenues = [city_revenue[city] for city in cities]

    city_sales_df = pd.DataFrame({"Units Sold": counts, "Revenue": revenues}, index=cities)

    # Normalize the data to use the same color scale
    normalized_sales = (city_sales_df["Units Sold"] - city_sales_df["Units Sold"].min()) / \
                       (city_sales_df["Units Sold"].max() - city_sales_df["Units Sold"].min())
    normalized_revenue = (city_sales_df["Revenue"] - city_sales_df["Revenue"].min()) / \
                         (city_sales_df["Revenue"].max() - city_sales_df["Revenue"].min())

    normalized_df = pd.DataFrame({"Units Sold": normalized_sales, "Revenue": normalized_revenue}, index=cities)

    plt.figure(figsize=(12, 6))
    sns.heatmap(
        normalized_df.T,
        annot=city_sales_df.T,
        cmap='YlGnBu',
        cbar=True,
        linewidths=0.5,
        fmt=".0f"
    )

    plt.title("City Distribution of Sales and Revenue (Heatmap)", fontsize=16)
    plt.xlabel("Cities", fontsize=12)
    plt.ylabel("Metrics", fontsize=12)
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
        if city == "":
            city = "guests"
        revenue = sale["totalPrice"]
        if city in revenue_by_city:
            revenue_by_city[city] += revenue
        else:
            revenue_by_city[city] = revenue

    total_revenue = sum(revenue_by_city.values())
    print(f"Total Sales Revenue Across All Cities: ${total_revenue:.2f}")

    # Prepare data for visualization
    cities = list(revenue_by_city.keys())
    revenues = list(revenue_by_city.values())

    revenue_array = np.array(revenues)
    color_threshold = np.percentile(revenue_array, 75)
    colors = ["lightblue" if revenue < color_threshold else "orange" for revenue in revenues]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(cities, revenues, color=colors, edgecolor="black")

    for bar, revenue in zip(bars, revenues):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                 f"${revenue:.2f}", ha='center', fontsize=10)

    plt.title("Total Sales Revenue by City", fontsize=16)
    plt.xlabel("City", fontsize=14)
    plt.ylabel("Revenue ($)", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.tight_layout()

    plt.show()


def donations_analyze():
    donations_data = reader.read_donations()

    total_donations = 0
    max_donation = 0

    for donation in donations_data:
        total_donations += donation["amount"]
        if donation["amount"] > max_donation:
            max_donation = donation["amount"]

    print(f"Total Donations: ${total_donations:.2f}")
    print(f"Maximum Donation: ${max_donation:.2f}")


def plot_revenue_by_city():
    data = reader.read_deliveries()

    total_revenue = 0
    city_revenue = {}

    for delivery in data:
        fee = delivery["deliveryFee"]
        city = delivery["deliveryAddress"]["city"]

        total_revenue += fee

        if city == "guest":
            city = ""

        if city in city_revenue:
            city_revenue[city] += fee
        else:
            city_revenue[city] = fee

    print(f"Total Deliveries Revenue: ${total_revenue}")
    print()
    print("Total Deliveries Revenue by City:")
    for city, revenue in city_revenue.items():
        print(f"\t-{city or 'guest'}: ${revenue}")

    sorted_cities = sorted(city_revenue.items())
    cities, revenues = zip(*sorted_cities)

    plt.bar(cities, revenues)
    plt.xlabel('City')
    plt.ylabel('Delivery Revenue')
    plt.title('Delivery Revenue by City')
    plt.xticks(rotation=90)
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
    print("-" * 5)
    donations_analyze()
    print("-" * 5)
    plot_revenue_by_city()


if __name__ == "__main__":
    main()
