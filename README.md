# Taxi Trip Data Analysis with OpenAI and pandas-ai

## **Project Overview**
This project leverages **OpenAI's API** and **pandas-ai** to analyze and visualize a taxi trip dataset. Using **Jupyter Notebook**, we explore data insights, create AI-driven queries, and generate meaningful visualizations.

## **Features**
- Load taxi trip data from a CSV file.
- Perform AI-powered data queries using **pandas-ai**.
- Generate various **chart visualizations** to explore trends.
- Identify correlations between fare amount, trip distance, and passenger count.
- Use **OpenAI API** for intelligent data interaction.


## **Usage**
1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/taxi-data-analysis.git
   cd taxi-data-analysis
   ```
2. **Open the Jupyter Notebook**:
   ```sh
   jupyter notebook Taxi_Trip_Analysis.ipynb
   ```
3. **Load your dataset** (`taxi_data.csv`) in the notebook.


## **Chart Visualizations You Can Generate**
You can ask OpenAI through pandas-ai to create the following visualizations:

## **Configuration**
Set up your **OpenAI API Key** inside the notebook before running queries:

```python
from pandasai.llm.openai import OpenAI

OPENAI_API_KEY = "your-api-key-here"
llm = OpenAI(api_token=OPENAI_API_KEY)
```

## **License**
This project is licensed under the **MIT License**.

## **Author**
Created by **janhavi jadhav** - Connect on [LinkedIn](https://www.linkedin.com/in/janhavi-jadhv/)
