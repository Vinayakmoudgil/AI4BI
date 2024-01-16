import google.generativeai as genai
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

genai.configure(api_key=config['AI API']['GEMINI_API_KEY'])

model = genai.GenerativeModel('gemini-pro')
no_of_kpi=10
def generate_kpi(df_columns):
    response = model.generate_content(f'''You are a retail Business intelligence Engineer.
                                      Provide the most important {no_of_kpi} KPI's and the column names
                                      from the below list of columns {','.join(df_columns)}.
                                      You should provide atleast 2 columns for 1 KPI.
                                      Please make sure you provide the output strictly in the below example json format, do not enter any new keys. Example:
                                      {{"KPIs": 
                                        [{{
                                            "KPI": "Total Sales", "Columns": ['SALES'] ['YEAR_ID']
                                            }}
                                         ],   
                                        }}
                                      ''')
    return response.text

def generate_chart(kpi_data):
    response = model.generate_content(f'''You are a retail Business intelligence Engineer.
                                      For the list of KPIs and columns {kpi_data},
                                      provide me the x-axis and y-axis for the columns and type of chart.
                                      You should provide atleast 1 chart for a KPI.
                                      Please make sure you provide the output strictly in the below example format only, do not add any new keys. Do not make any change in the format.
                                        Example: for KPI:Monthly Sales Trend and columns MONTH_ID,SALES:                                       
                                        {{"metrics": [
                                            {{
                                            "name": "Monthly Sales Trend",
                                            "x_axis": "MONTH_ID",
                                            "y_axis": "SALES",
                                            "x_label": "Months",
                                            "y_label": "Sales"
                                            "aggregation_column": "SALES"
                                            "aggregation_type": "SUM"
                                            "chart_type": "line"
                                            }}
                                            ]  
                                            }}                                             
                                      ''')
    return response.text




    
