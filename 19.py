 my_branch
from datetime import datetime

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self):
        self.products = {}
        self.sales = {}

    def add_product(self, product):
        self.products[product.name] = product

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
        else:
            print("Product not found.")

    def add_sale(self, product_name, quantity, date):
        if product_name in self.products:
            if date in self.sales:
                self.sales[date].append((product_name, quantity))
            else:
                self.sales[date] = [(product_name, quantity)]
        else:
            print("Product not found.")

    def display_total_sales(self):
        total_sales = 0
        for date, sales in self.sales.items():
            for product_name, quantity in sales:
                total_sales += self.products[product_name].price * quantity
        print(f"Total sales: ${total_sales:.2f}")

    def display_average_daily_sales(self):
        total_sales = 0
        total_days = len(self.sales)
        for date, sales in self.sales.items():
            for product_name, quantity in sales:
                total_sales += self.products[product_name].price * quantity
        average_daily_sales = total_sales / total_days
        print(f"Average daily sales: ${average_daily_sales:.2f}")

    def display_monthly_sales(self, month):
        monthly_sales = 0
        for date, sales in self.sales.items():
            if date.startswith(month):
                for product_name, quantity in sales:
                    monthly_sales += self.products[product_name].price * quantity
        print(f"Monthly sales for {month}: ${monthly_sales:.2f}")

    def display_average_monthly_sales(self, month):
        monthly_sales = 0
        total_days = 0
        for date, sales in self.sales.items():
            if date.startswith(month):
                total_days += 1
                for product_name, quantity in sales:
                    monthly_sales += self.products[product_name].price * quantity
        average_monthly_sales = monthly_sales / total_days
        print(f"Average monthly sales for {month}: ${average_monthly_sales:.2f}")

    def display_yearly_sales(self, year):
        yearly_sales = 0
        for date, sales in self.sales.items():
            if date.startswith(year):
                for product_name, quantity in sales:
                    yearly_sales += self.products[product_name].price * quantity
        print(f"Yearly sales for {year}: ${yearly_sales:.2f}")

    def display_average_yearly_sales(self, year):
        yearly_sales = 0
        total_days = 0
        for date, sales in self.sales.items():
            if date.startswith(year):
                total_days += 1
                for product_name, quantity in sales:
                    yearly_sales += self.products[product_name].price * quantity
        average_yearly_sales = yearly_sales / total_days
        print(f"Average yearly sales for {year}: ${average_yearly_sales:.2f}")

def main():
    store = Store()
    while True:
        print("\n1. Add product")
        print("2. Remove product")
        print("3. Add sale")
        print("4. Display total sales")
        print("5. Display average daily sales")
        print("6. Display monthly sales")
        print("7. Display average monthly sales")
        print("8. Display yearly sales")
        print("9. Display average yearly sales")
        print("10. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            store.add_product(Product(name, price, quantity))
        elif choice == "2":
            name = input("Enter product name: ")
            store.remove_product(name)
        elif choice == "3":
            name = input("Enter product name: ")
            quantity = int(input("Enter sale quantity: "))
            date = input("Enter sale date (YYYY-MM-DD): ")
            store.add_sale(name, quantity, date)
        elif choice == "4":
            store.display_total_sales()
        elif choice == "5":
            store.display_average_daily_sales()
        elif choice == "6":
            month = input("Enter month (YYYY-MM): ")
            store.display_monthly_sales(month)
        elif choice == "7":
            month = input("Enter month (YYYY-MM): ")
            store.display_average_monthly_sales(month)
        elif choice == "8":
            year = input("Enter year (YYYY): ")
            store.display_yearly_sales(year)
        elif choice == "9":
            year = input("Enter year (YYYY): ")
            store.display_average_yearly_sales(year)
        elif choice == "10":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
=======
from datetime import datetime

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self):
        self.products = {}
        self.sales = {}

    def add_product(self, product):
        self.products[product.name] = product

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
        else:
            print("Product not found.")

    def add_sale(self, product_name, quantity, date):
        if product_name in self.products:
            if date in self.sales:
                self.sales[date].append((product_name, quantity))
            else:
                self.sales[date] = [(product_name, quantity)]
        else:
            print("Product not found.")

    def display_total_sales(self):
        total_sales = 0
        for date, sales in self.sales.items():
            for product_name, quantity in sales:
                total_sales += self.products[product_name].price * quantity
        print(f"Total sales: ${total_sales:.2f}")

    def display_average_daily_sales(self):
        total_sales = 0
        total_days = len(self.sales)
        for date, sales in self.sales.items():
            for product_name, quantity in sales:
                total_sales += self.products[product_name].price * quantity
        average_daily_sales = total_sales / total_days
        print(f"Average daily sales: ${average_daily_sales:.2f}")

    def display_monthly_sales(self, month):
        monthly_sales = 0
        for date, sales in self.sales.items():
            if date.startswith(month):
                for product_name, quantity in sales:
                    monthly_sales += self.products[product_name].price * quantity
        print(f"Monthly sales for {month}: ${monthly_sales:.2f}")

    def display_average_monthly_sales(self, month):
        monthly_sales = 0
        total_days = 0
        for date, sales in self.sales.items():
            if date.startswith(month):
                total_days += 1
                for product_name, quantity in sales:
                    monthly_sales += self.products[product_name].price * quantity
        average_monthly_sales = monthly_sales / total_days
        print(f"Average monthly sales for {month}: ${average_monthly_sales:.2f}")

    def display_yearly_sales(self, year):
        yearly_sales = 0
        for date, sales in self.sales.items():
            if date.startswith(year):
                for product_name, quantity in sales:
                    yearly_sales += self.products[product_name].price * quantity
        print(f"Yearly sales for {year}: ${yearly_sales:.2f}")

    def display_average_yearly_sales(self, year):
        yearly_sales = 0
        total_days = 0
        for date, sales in self.sales.items():
            if date.startswith(year):
                total_days += 1
                for product_name, quantity in sales:
                    yearly_sales += self.products[product_name].price * quantity
        average_yearly_sales = yearly_sales / total_days
        print(f"Average yearly sales for {year}: ${average_yearly_sales:.2f}")

def main():
    store = Store()
    while True:
        print("\n1. Add product")
        print("2. Remove product")
        print("3. Add sale")
        print("4. Display total sales")
        print("5. Display average daily sales")
        print("6. Display monthly sales")
        print("7. Display average monthly sales")
        print("8. Display yearly sales")
        print("9. Display average yearly sales")
        print("10. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            store.add_product(Product(name, price, quantity))
        elif choice == "2":
            name = input("Enter product name: ")
            store.remove_product(name)
        elif choice == "3":
            name = input("Enter product name: ")
            quantity = int(input("Enter sale quantity: "))
            date = input("Enter sale date (YYYY-MM-DD): ")
            store.add_sale(name, quantity, date)
        elif choice == "4":
            store.display_total_sales()
        elif choice == "5":
            store.display_average_daily_sales()
        elif choice == "6":
            month = input("Enter month (YYYY-MM): ")
            store.display_monthly_sales(month)
        elif choice == "7":
            month = input("Enter month (YYYY-MM): ")
            store.display_average_monthly_sales(month)
        elif choice == "8":
            year = input("Enter year (YYYY): ")
            store.display_yearly_sales(year)
        elif choice == "9":
            year = input("Enter year (YYYY): ")
            store.display_average_yearly_sales(year)
        elif choice == "10":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
  Osman--branch
    main()