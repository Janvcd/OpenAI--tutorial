

1.Creating Dummy data sets


!pip install pandas
!pip install numpy

import pandas as pd
import numpy as np
from random import choices

np.random.seed(10)

num_records = 1000
num_outlets = 10
num_products = 5

#quaters 2 (Jan-March)(apr-jun)
dates = pd.date_range(start = '2023-01-01', end= '2023-06-30')
dates = choices(dates, k=num_records)

len(dates)

dates

outlets = ['Outlet_'+str(i+1) for i in range(num_outlets)]
outlets = choices(outlets, k=num_records)

len(outlets)

products = ['products_'+str(i+1) for i in range(num_products)]
products = choices(products, k=num_records)

len(products)

units_Sold = np.random.randint(1,200, num_records)
price_per_unit = np.random.uniform(10,500, num_records)

total_sales= units_Sold * price_per_unit

len(total_sales)

"""Put this in Dataframe"""

df= pd.DataFrame({
    'Date': dates,
    'Outlets': outlets,
    'Products' : products,
    'Units_Solds': units_Sold,
    'Price_per_unit' : price_per_unit,
    'Total_Sales': total_sales

})

OPEN_API_KEY = "Your open-ai key"

pip install pandasai

from pandasai.llm.openai import OpenAI
from pandasai.smart_dataframe import SmartDataframe

llm = OpenAI(api_token=OPEN_API_KEY)
pandas_ai = SmartDataframe(df, config={"llm": llm})

df

response = pandas_ai.chat("Round price_per_unit and Total_sales to 2 decimal places.")
print(response)

response = pandas_ai.chat("Round price_per_unit and Total_sales to 2 decimal places.")
print(response)

df

"""Charting"""

response = pandas_ai.chat("Which product is most profitable?")
print(response)

response = pandas_ai.chat("Plot the bar chart of the product based on total_sales by arranign product ascending")
print(response)

response = pandas_ai.chat("can you name product_1 as apple?")
print(response)