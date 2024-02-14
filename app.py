from shiny import render
from shiny.express import ui,input
from pathlib import Path
import pandas as pd
import IncomeStatements
import shinyswatch


shinyswatch.theme.journal()

here = Path(__file__).parent

with ui.sidebar(bg="#F0F8FF"):  
    with ui.card(fill=False): 
        @render.image
        def image_icon():
            img = {"src": here / "icon1.jpg", "width": "180px","height": "180px"}
            return img 
        ui.h3("Intel Corporation")
       
        
          

# Render the page
ui.page_opts(title="FINANCIAL ANALYTICS")



with ui.card():
    with ui.navset_bar(title="Income Statement"):
        with ui.nav_panel(title="Common Size -Income statement"):
            ui.h5("Common Size -Income statement")
            # Render the DataFrame
            @render.data_frame
            def show_income_common_size():
                return render.DataGrid(IncomeStatements.retriveIncomeCommonSizeSatement(), width='content.fit', height=500)
        with ui.nav_panel(title="Indexed - Income statement"):
            ui.h5("Indexed - Income statement")
            # Render the DataFrame
            @render.data_frame
            def show_indexed_income():
                return render.DataGrid(IncomeStatements.retriveIndexedIncomeSatement(), width='content.fit', height=500)
        with ui.nav_panel(title="Common size - Balance sheet"):
            ui.h5("Common size - Balance sheet")
            # Render the DataFrame
            @render.data_frame
            def show_common_size_balance():
                return render.DataGrid(IncomeStatements.retriveBalanceCommonSizeSatement(), width='content.fit', height=500)   
        with ui.nav_panel(title="Indexed- Balance sheet"):
            ui.h5("Indexed- Balance sheet")
            # Render the DataFrame
            @render.data_frame
            def show_indexed_balance():
                return render.DataGrid(IncomeStatements.retriveIndexedBalanceSatement(), width='content.fit', height=500)        
                