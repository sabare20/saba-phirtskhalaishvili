import json
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


class JSONReader:
    def __init__(self, customer_file_path, sales_file_path, donations_file_path, delivery_file_path, board_games_path):
        self.customer_file_path = os.path.join(os.getcwd(), customer_file_path)
        self.sales_file_path = os.path.join(os.getcwd(), sales_file_path)
        self.donations_file_path = os.path.join(os.getcwd(), donations_file_path)
        self.delivery_file_path = os.path.join(os.getcwd(), delivery_file_path)
        self.board_games_path = os.path.join(os.getcwd(), board_games_path)

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

    def read_board_games(self):
        with open(self.board_games_path, "r") as file:
            return json.load(file)


# Create an instance of the JSONReader class with relative file paths
reader = JSONReader(
    "data/customers_data.json",
    "data/sales_data.json",
    "data/donations_data.json",
    "data/delivery_data.json",
    "data/board_games_data.json"
)

# You can test reading data
try:
    customers_data = reader.read_customers()
    # Example usage
except FileNotFoundError as e:
    print(e)


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


def analyze_sold_games():
    sales_data = reader.read_sales()
    board_games_data = reader.read_board_games()

    # Convert the data into DataFrames for easier manipulation
    sales_df = pd.DataFrame(sales_data)
    games_df = pd.DataFrame(board_games_data)

    # Aggregate sales data to calculate the total quantity sold for each gameID
    sales_summary = sales_df.groupby("gameID")["quantity"].sum().reset_index()

    # Merge the aggregated sales data with the board games details to include game names
    merged_data = pd.merge(sales_summary, games_df, on="gameID")

    # Find the most sold game
    most_sold_game = merged_data.loc[merged_data["quantity"].idxmax()]

    plt.figure(figsize=(12, 6))
    plt.bar(merged_data["name"], merged_data["quantity"], color="skyblue", edgecolor="black")
    plt.title("Total Sales of Board Games", fontsize=16, weight="bold")
    plt.xlabel("Game Names", fontsize=14)
    plt.ylabel("Total Quantity Sold", fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

    most_sold_name = most_sold_game["name"]
    most_sold_quantity = most_sold_game["quantity"]

    print(f"Most Sold Game is: {most_sold_name} and Quantity Sold is: {most_sold_quantity}")
    return most_sold_name, most_sold_quantity


def total_generated_revenue():
    # Calculate Total Sales Revenue
    sales_data = reader.read_sales()
    total_sales_revenue = sum(sale["totalPrice"] for sale in sales_data)
    print(f"Total Sales Revenue: ${total_sales_revenue:.2f}")

    # Calculate Total Delivery Revenue
    deliveries_data = reader.read_deliveries()
    total_delivery_revenue = sum(delivery["deliveryFee"] for delivery in deliveries_data)
    print(f"Total Delivery Revenue: ${total_delivery_revenue:.2f}")

    # Calculate Total Donations Revenue
    donations_data = reader.read_donations()
    total_donations_revenue = sum(donation["amount"] for donation in donations_data)
    print(f"Total Donations Revenue: ${total_donations_revenue:.2f}")

    print("-" * 3)
    # Sum up all the revenue
    total_revenue = total_sales_revenue + total_delivery_revenue + total_donations_revenue
    print(f"Total Generated Revenue: ${total_revenue:.2f}")

    # Prepare data for the bar chart
    categories = ['Sales Revenue', 'Delivery Revenue', 'Donations Revenue']
    revenues = [total_sales_revenue, total_delivery_revenue, total_donations_revenue]
    total_revenue_bar = [total_revenue] * 1  # Total Revenue as a single bar

    # Plot the bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(categories, revenues, color=["skyblue", "lightgreen", "salmon"], edgecolor="black",
                  label="Individual Revenues")

    # Plot the total revenue bar (larger bar on top of individual ones)
    total_bar = ax.bar('Total Revenue', total_revenue, color='orange', edgecolor='black', alpha=0.7)

    # Add labels to individual bars
    for bar, revenue in zip(bars, revenues):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"${revenue:.2f}", ha='center', fontsize=10)

    # Add label to total revenue bar
    ax.text(total_bar[0].get_x() + total_bar[0].get_width() / 2, total_bar[0].get_height() + 1, f"${total_revenue:.2f}",
            ha='center', fontsize=12, fontweight='bold')

    # Add title and labels
    ax.set_title("Total Revenue Breakdown", fontsize=16, weight="bold")
    ax.set_xlabel("Revenue Categories", fontsize=14)
    ax.set_ylabel("Revenue ($)", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

    return total_revenue


def main_analytics_function():
    while True:
        print('1. Average age of customers')
        print('2. Gender distribution')
        print('3. Total Revenue Breakdown')
        print('4. Quantity sold distribution by cities')
        print('5. Sales Revenues by cities')
        print('6. Delivery Revenue by cities')
        print('7. Donations analyze')
        print('8. Sold Board Games')
        print('9. GO BACK')
        while True:
            try:
                input_data_number = int(input('enter number for command :'))
                if input_data_number == 1:
                    calculate_average_age()
                    print("-" * 5)
                    break
                elif input_data_number == 2:
                    gender_distribution()
                    print("-" * 5)
                    break
                elif input_data_number == 3:
                    total_generated_revenue()
                    print("-" * 5)
                    break
                elif input_data_number == 4:
                    city_distribution()
                    print("-" * 5)
                    break
                elif input_data_number == 5:
                    calculate_and_visualize_revenue()
                    print("-" * 5)
                    break
                elif input_data_number == 6:
                    plot_revenue_by_city()
                    print("-" * 5)
                    break
                elif input_data_number == 7:
                    donations_analyze()
                    print("-" * 5)
                    break
                elif input_data_number == 8:
                    analyze_sold_games()
                    print("-" * 5)
                    break
                elif input_data_number == 9:
                    break
                else:
                    raise ValueError('Error,you must enter number from 1 to 9 !.Please try again .')
            except ValueError as e:
                print(e)
        if input_data_number == 9:
            print('go back to admin panel ')
            break


if __name__ == '__main__':
    main_analytics_function()
