

#api credentials
api_key = "NcuUQxybP4d3dfz2NZ87CtdCbk0EmDyx"
ticker_symbol='INTC'
api_endpoint_incomestatement = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker_symbol}?period=annual&apikey={api_key}"


# Define the fields to exclude from the income statement
excluded_fields_Income = [
    'Tax Effect Of Unusual Items',
    'Tax Rate For Calcs',
    'Normalized EBITDA',
    'Operating Revenue',
    'Basic EPS',
    'Diluted EPS',
    'Minority Interests',
    'Gain On Sale Of Business',
    'Other Non Operating Income Expenses',
    'Reconciled Cost Of Revenue',
    'Other Special Charges',
    'Total Other Finance Cost',
    'Special Income Charges',
    'Operating Income',
    'Other Income Expense',
    'Total Unusual Items Excluding Goodwill',
    'Total Unusual Items',
    'Restructuring And Mergern Acquisition',
    'Gain On Sale Of Security',
    'Write Off',
    'Net Non Operating Interest Income Expense',
    'Interest Expense Non Operating',
    'Interest Income Non Operating',
    'Net Income Including Noncontrolling Interests',
    'Diluted NI Availto Com Stockholders',
    'Net Income From Continuing Operation Net Minority Interest',
    'Net Income From Continuing And Discontinued Operation'

    # Add other fields you want to exclude here
]   


#Values are in dollars
currency = 'USD'
currency_Normalizer = 1000000   # Normalize values by dividing each value by this number



#Company Creds
company_A = "Intel Corporation"
company_A_ticker_symbol='INTC'