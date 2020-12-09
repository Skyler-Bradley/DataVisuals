import matplotlib.pyplot as plt
import json
scratch1 = json.loads('{"price": [600, 620, 2000, 370, 1900, 1700, 2100, 1200, 1800], "quantity": [10, 14, 20, 7, 30, 21, 40, 12, 32]}')
prices = scratch1["price"]
quantities = scratch1["quantity"]
scratch2 = json.loads('{"amount": [20, 30, 31, 40, 80], "date": [1940, 1950, 1960, 1980, 1990], "amount2": [20, 40, 43, 50, 72]}')
gdp = scratch2["amount"]
gdp2 = scratch2["amount2"]
year = scratch2["date"]
plt.title('Ginseng Transactions')
plt.scatter(quantities, prices)
plt.xlabel('Quantity in pounds')
plt.ylabel('Sale Price USD')
plt.show()
plt.title('Economies of Skylerlandia and Bradleystan')
plt.plot(year,gdp, label="Skylerlandia")
plt.plot(year,gdp2, label="Bradleystan")
plt.xlabel('Year')
plt.ylabel('GDP (in Billions USD)')
plt.legend()
plt.show()
