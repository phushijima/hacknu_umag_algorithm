#Queue naive O(N) implementation
#INPUT: barcode, fromTime, toTime
#OUTPUT: barcode, quantity, revenue, netProfit
supplies = [
  {
    "id": 1,
    "barcode": 12334565,
    "price": 15,
    "quantity": 10,
    "supplyTime": "2022-12-02 09:00:00"
  },
  {
    "id": 2,
    "barcode": 12334565,
    "price": 20,
    "quantity": 5,
    "supplyTime": "2022-12-15 09:00:00"
  },
  {
    "id": 3,
    "barcode": 12334565,
    "price": 5,
    "quantity": 10,
    "supplyTime": "2022-12-26 09:00:00"
  }
]
sales = [
  {
    "id": 1,
    "barcode": 12334565,
    "price": 20,
    "quantity": 10,
    "saleTime": "2022-12-04 11:00:02"
  },
  {
    "id": 2,
    "barcode": 12334565,
    "price": 20,
    "quantity": 5,
    "saleTime": "2022-12-16 09:00:00"
  },
  {
    "id": 3,
    "barcode": 12334565,
    "price": 10,
    "quantity": 3,
    "saleTime": "2022-12-28 09:00:00"
  }
]

def calculate_revenue_and_profit(supplies, sales, barcode, fromTime, toTime):
    revenue = 0
    cost = 0

    # Iterate through supplies and calculate cost
    relevant_supplies = [supply for supply in supplies if supply['barcode'] == barcode and fromTime <= supply['supplyTime'] <= toTime]

    # Iterate through sales and calculate revenue
    relevant_sales = [sale for sale in sales if sale['barcode'] == barcode and fromTime <= sale['saleTime'] <= toTime]
        
    # Calculate cost using dictionary lookup
    cost = sum(supply['price'] * supply['quantity'] for supply in relevant_supplies)

    # Calculate revenue using dictionary lookup
    revenue = sum(sale['price'] * sale['quantity'] for sale in relevant_sales)

    
    # Calculate net profit
    net_profit = revenue - cost
    print(revenue, net_profit)
    return revenue, net_profit
print(type(sales))
#calculate_revenue_and_profit(supplies, sales, 12334565, "2022-12-01 09:00:00", "2022-12-05 11:00:02")