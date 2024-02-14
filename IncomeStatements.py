import yfinance as yf
import pandas as pd
import StaticStrings
import numpy as np


def retrieve_Balance_data(ticker_symbol):
    """
    Retrieve financial data for a given ticker symbol using yfinance.
    """
    firm_data = yf.Ticker(ticker_symbol)
    return firm_data.balance_sheet.T

def retrieve_financial_data(ticker_symbol):
    """
    Retrieve financial data for a given ticker symbol using yfinance.
    """
    firm_data = yf.Ticker(ticker_symbol)
    return firm_data.financials.T




def retrieve_latest_income_statement(dataframe):
    """
    Retrieve the latest income statement from the financial data.
    """
    return dataframe.iloc[0]

def filter_excluded_fields(dataframe):
    """
    Filter out excluded fields from the income statement.
    """
    return dataframe.drop(StaticStrings.excluded_fields_Income)

def prepare_dataframe(filtered_income_statement):
    """
    Prepare a new DataFrame for the income statement.
    """
    new_dataframe = pd.DataFrame({
        StaticStrings.company_A: filtered_income_statement.index,
        'Income': filtered_income_statement.abs().astype('double').values / StaticStrings.currency_Normalizer
    })
    # Sort the DataFrame in descending order based on 'Income' column
    new_dataframe = new_dataframe.sort_values(by='Income', ascending=False)
    return new_dataframe

def construct_common_size_statements(dataframe):
    """
    Construct common size statements based on total revenue.
    """
    total_revenue = dataframe.loc[dataframe[StaticStrings.company_A] == 'Total Revenue', 'Income'].values[0]
    dataframe['Common-Size'] = ((dataframe['Income'] / total_revenue) * 100).round(3).astype(str) + '%'
    return dataframe



#main
# Retrieve financial data for Intel

def retriveIndexedIncomeSatement():
    
    income_statement = retrieve_financial_data(StaticStrings.company_A_ticker_symbol)
    income_statement.T.head()
    # Filter data for the past two years
    current_year = pd.Timestamp.now().year
    two_years_ago = current_year - 2

    income_statement_last_two_years = income_statement[income_statement.index.year >= two_years_ago]

    # Print the DataFrame for the past two years
    income_statement_last_two_years.T.head()
    income_statement_last_two_years=income_statement_last_two_years.T
    income_statement_last_two_years=filter_excluded_fields(income_statement_last_two_years)


    new_dataframe = pd.DataFrame({
        "Income Statement": income_statement_last_two_years.index,
        "2023": income_statement_last_two_years.iloc[:, 0].abs().astype('double').values / StaticStrings.currency_Normalizer,
        "2022": income_statement_last_two_years.iloc[:, 1].abs().astype('double').values / StaticStrings.currency_Normalizer
        # Assuming your columns have meaningful names and you want to keep them as they are
        # You can add more columns in a similar manner
    })

    print(new_dataframe.columns)


    # Print the head of the new DataFrame

    # Print the head of the new DataFrame
    print(new_dataframe.head())

    # Perform division while handling division by zero
    new_dataframe['Percentage Change '] = np.where(
        new_dataframe['2022'] != 0,  # Check if denominator is not zero
        ((new_dataframe['2023'] / new_dataframe['2022']) * 100).round(3).astype(str) + '%',  # Perform division
        np.nan  # Replace division by zero with NaN
    )
    new_dataframe_sorted = new_dataframe.sort_values(by='2023',ascending=False)
    return new_dataframe_sorted


def retriveIncomeCommonSizeSatement():
    
    income_statement = retrieve_financial_data(StaticStrings.company_A_ticker_symbol)
    latest_income_statement = retrieve_latest_income_statement(income_statement)
    filtered_income_statement = filter_excluded_fields(latest_income_statement)
    new_dataframe = prepare_dataframe(filtered_income_statement)
    common_size_df = construct_common_size_statements(new_dataframe)
    return common_size_df



# Balance Sheet

def retriveBalanceCommonSizeSatement():
    
    income_statement = retrieve_Balance_data(StaticStrings.company_A_ticker_symbol)
    income_statement=income_statement.iloc[1]
    new_dataframe = pd.DataFrame({
        StaticStrings.company_A: income_statement.index,
        'Income': income_statement.abs().astype('double').values / StaticStrings.currency_Normalizer
    })
    new_dataframe = new_dataframe.sort_values(by='Income', ascending=False)
    total_revenue = new_dataframe.loc[new_dataframe[StaticStrings.company_A] == 'Total Assets', 'Income'].values[0]
    new_dataframe['Common-Size'] = ((new_dataframe['Income'] / total_revenue) * 100).round(3).astype(str) + '%'
    new_dataframe_cleaned = new_dataframe.dropna()
    return new_dataframe_cleaned

def retriveIndexedBalanceSatement():
    
    income_statement = retrieve_Balance_data(StaticStrings.company_A_ticker_symbol)
    current_year = pd.Timestamp.now().year
    two_years_ago = current_year- 2

    income_statement_last_two_years = income_statement[income_statement.index.year >= two_years_ago].T
    income_statement_last_two_years.head()
    new_dataframe = pd.DataFrame({
        "Income Statement": income_statement_last_two_years.index,
        "2023": income_statement_last_two_years.iloc[:, 0].abs().astype('double').values / StaticStrings.currency_Normalizer,
        "2022": income_statement_last_two_years.iloc[:, 1].abs().astype('double').values / StaticStrings.currency_Normalizer
        # Assuming your columns have meaningful names and you want to keep them as they are
        # You can add more columns in a similar manner
        })

    new_dataframe.head()
    new_dataframe['Percentage Change '] = np.where(
        new_dataframe['2022'] != 0,  # Check if denominator is not zero
        ((new_dataframe['2023'] / new_dataframe['2022']) * 100).round(3).astype(str) + '%',  # Perform division
        np.nan  # Replace division by zero with NaN
    )
    new_dataframe_sorted = new_dataframe.sort_values(by='2023',ascending=False)
    return new_dataframe_sorted.dropna()