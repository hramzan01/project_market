import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
import plotly.graph_objects as go
import json
import numpy as np
from streamlit.components.v1 import html
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
import plotly.express as px
from PIL import Image
import numpy as np
from datetime import date, timedelta

st.set_page_config(page_title="Market", initial_sidebar_state="collapsed")


# Background and other custom styles
st.markdown(
    """
    <style>
    [data-testid="stHeader"] {
        background-color: #D16643;
    }
    </style>
    <style>
    [data-testid="stApp"] {
        background: linear-gradient(180deg, rgba(255,124,82,1) 0%, rgba(0,0,0) 47%, rgba(0,0,0) 100%);
        height:auto;
    }
    </style>
    <style>
    [data-testid="stSlider"] {
        background-color: #EEF0F4;
        border-radius: 5px;
        padding: 10px;
    }
    </style>
    <style>
        .stPlotlyChart {
            border-radius: 10px;
            overflow: hidden; /* This is important to ensure the border radius is applied properly */
        }
    </style>
    <style>
        .vp-center {
            width: 80%;
            margin: 0px 0px 0px 0px;
            background-color: #ffffff;
            opacity: .4;
        }
    </style>
    <style>
    .stForm {
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    # HOME: MARKET logo

    # Load in images
    logo = Image.open('app/assets/market_logo.png')
    what = Image.open('app/assets/market_what.png')
    
    st.image(logo, use_column_width=True)
    st.markdown('')  # Empty markdown line for spacing
    st.markdown('')  # Empty markdown line for spacing
    st.markdown('')  # Empty markdown line for spacing
    st.markdown('')  # Empty markdown line for spacing
    st.markdown('')  # Empty markdown line for spacing


    st.markdown('')
    st.write("""At Market©, we're revolutionizing energy ownership with our cutting-edge AI platform, powered by solar energy data.
Our technology provides insights on energy generation, consumption and cost, empowering individuals and communities to save money and invest in a more sustainable future.
☀️""")

    st.markdown('')  # Empty markdown line for spacing
    st.markdown('')  # Empty markdown line for spacing
    
    st.image(what, use_column_width=True)

    st.markdown('')  # Empty markdown line for spacing
    st.markdown('')  # Empty markdown line for spacing
    st.markdown('')  # Empty markdown line for spacing
    st.markdown('')  # Empty markdown line for spacing

    # PROFILE SECTION

    # Load in images and display them
    property_images = ['property_detached', 'property_bungalow', 'property_flat', 'property_terrace']
    battery_images = ['battery_small', 'battery_large', 'battery_car']
    panel_images = ['panel_3', 'panel_2', 'panel_1', 'panel_4']

    user_input = st.text_input("Username", "New User", key="user")
    postcode = st.text_input("Postcode", "E2 8DY", key="postcode")

    property_selection = st.selectbox('Select Property Type', property_images)
    battery_selection = st.selectbox('Select Battery Type', battery_images)
    panel_selection = st.selectbox('Select Panel Type', panel_images)

    col1, col2, col3 = st.columns([1, 1, 1])
    

    if property_selection:
        property_image = Image.open(f'app/assets/{property_selection}.png')
        col1.image(property_image, use_column_width=True)

    if battery_selection:
        battery_image = Image.open(f'app/assets/{battery_selection}.png')
        col2.image(battery_image, use_column_width=True)

    if panel_selection:
        panel_image = Image.open(f'app/assets/{panel_selection}.png')
        col3.image(panel_image, use_column_width=True)

    st.markdown('')  # Empty markdown line for spacing
    st.markdown('')  # Empty markdown line for spacing
    st.markdown('')  # Empty markdown line for spacing

# Return Lat & Lon from postcode
base_url = 'https://api.postcodes.io/postcodes'
response = requests.get(f'{base_url}/{postcode}').json()
lat = response['result']['latitude']
lon = response['result']['longitude']

# Generate Dashboard when submit is triggered
with st.form(key='params_for_api', border=False):
    if st.form_submit_button('CHARGE UP DASHBOARD ⚡️', use_container_width=True):
        with st.spinner('charging up your dashboard...'):

            # Call cached data
            cached = 'app/predict_cached.json'
            with open(cached, 'r') as file:
                data = json.load(file)
                
            weather = data['res_weather_code']
            saleprice = data['prediction_saleprice']
            buyprice = data['prediction_purchaseprice']
            power_gen = data['prediction_gen']
            power_cons = data['prediction_cons']
            res_opt_batt = data['res_opt_batt']['0']
            res_opt_buyprice = data['res_opt_buyprice']['0']
            res_opt_sellprice = data['res_opt_sellprice']['0']
            res_opt_baseprice = data['res_opt_baseprice']['0']
            x_sale, y_sale = zip(*saleprice.items()) # unpack a list of pairs into two tuples
            x_buy, y_buy = zip(*buyprice.items())
            #x_gen, y_gen = zip(*power_gen.items())
            x_cons, y_cons = zip(*power_cons.items())
            x_battopt, y_battopt = zip(*res_opt_batt.items())
            x_bpopt, y_bpopt = zip(*res_opt_buyprice.items())
            x_spopt, y_spopt = zip(*res_opt_sellprice.items())
            x_basep, y_basep = zip(*res_opt_baseprice.items())
            dates = pd.to_datetime(x_buy)


            # VISUALS
            # plotly map
            @st.cache_data
            def london_map(lat, lon):
                # Create a Plotly figure with Mapbox
                fig = go.Figure(go.Scattermapbox(
                    lat=[lat],
                    lon=[lon],
                    mode='markers',
                    marker=go.scattermapbox.Marker(
                        size=30,
                        color='orange',
                    ),
                    text=['London']
                ))
                fig.update_layout(
                    autosize=True,
                    margin=dict(l=0, r=0, t=0, b=0),
                    hovermode='closest',
                    mapbox=dict(
                        style='carto-positron',
                        bearing=0,
                        center=dict(
                            lat=lat,
                            lon=lon
                        ),
                        pitch=0,
                        zoom=16
                    )
                )
                return fig

            # Display the map using full container width
            st.plotly_chart(london_map(lat, lon), use_container_width=True)

            ### WEATHER
            # Initialize an empty list to store the weather codes at midday
            midday_weather_codes = []

            # Iterate over the hourly weather codes
            for index, weather_code in enumerate(weather):
                # Calculate the hour of the day using index (assuming index starts from 0)
                hour_of_day = index % 24

                # Check if the hour is midday (12:00 PM)
                if hour_of_day == 12:
                    # Add the weather code to the list
                    midday_weather_codes.append(weather_code)

            # Main optimised prohet graph
            st.divider()



            # Header
            st.subheader(f"{user_input}'s Energy Hub")
            st.divider()
            st.markdown('')  # Empty markdown line for spacing


            # Display images
            st.markdown('')  # Empty markdown line for spacing
            st.markdown('')  # Empty markdown line for spacing

            # Split the remaining space into three columns
            l, m, r = st.columns(3)
            
            image1 = Image.open('app/assets/icon_money.png')
            image2 = Image.open('app/assets/icon_energy.png')
            image3 = Image.open('app/assets/icon_charge.png')
            with l:
                st.image(image1, use_column_width=True)
                st.metric("Money Saved YTD", "£96.20", "£5.25 vs 2023")
            with m:
                st.image(image2, use_column_width=True)
                st.metric("Energy Saved YTD", "⌁568kWh", "0.46% vs 2023")
            with r:
                st.image(image3, use_column_width=True)
                st.metric("Energy Sold YTD", "⌁451kWh", "+4.87% vs 2023")

            # convert model price dictionary into numpy array and cumulative sum
            result = data['res_delta_buy_sell_price']['0'].items()
            graph_data = list(result)
            model = np.asarray(np.array(graph_data)[:,1], dtype=float).cumsum()/100
            # convert res_baseline_price_no_solar:  price dictionary into numpy array and cumulative sum
            result = data['res_baseline_price_no_solar']['0'].items()
            graph_data = list(result)
            baseline_no_solar = np.asarray(np.array(graph_data)[:,1], dtype=float).cumsum()/100
            # convert res_opt_baseprice:  price dictionary into numpy array and cumulative sum
            result = data['res_opt_baseprice']['0'].items()
            graph_data = list(result)
            baseline = np.asarray(np.array(graph_data)[:,1], dtype=float).cumsum()/100
            # Set up date range - will need to be imported from the streamlit
            today = date.today()
            first_date = today
            last_date = today + timedelta(days=7)
            date_range = pd.date_range(start = first_date, end=last_date, freq = 'h')
            date_range = date_range[:168]
            # Battery Output
            df = pd.DataFrame({'date': date_range ,'Solar plus Market': model, 'Solar': baseline, 'No Solar': baseline_no_solar})
            #fig_final = px.line(x=date_range, y=[model, baseline, baseline_no_solar], labels={'x': 'Date', 'y': 'Cumulative Cost', 'wide_variable_0': 'Solar plus Market', 'wide_variable_1': 'Solar', 'wide_variable_2': 'Baseline'}, title='Total Savings')
            fig_final = px.line(df, x='date', y=['No Solar', 'Solar', 'Solar plus Market'], title='Forcasted Weekly Cost') #Remove date and update y axis lable
            # Specify line styles
            fig_final.update_traces(line=dict(dash='dash'), selector=dict(name='No Solar'))
            fig_final.update_traces(line=dict(dash='dash'), selector=dict(name='Solar'))
            fig_final.update_traces(line=dict(dash='solid'), selector=dict(name='Solar plus Market'))
            fig_final.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', showlegend=False)
            fig_final.update_yaxes(title_text='Cumulative Cost')
            fig_final.update_xaxes(title_text='')
            st.plotly_chart(fig_final,use_container_width=True)

            # Split the remaining space into three columns
            st.divider()

            color = 'orange'
            # Buy vs Sell Price

            fig = px.line(x=date_range, y=y_sale, labels={'x': 'Date', 'y': 'Price (£)'}, title='FORECASTED ENERGY PRICE')
            fig.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            # width=600,
            # height=400,
            showlegend=False, # Hide legend
            yaxis_range=[0,25]
            )
            fig.add_scatter(x=date_range, y=y_buy, mode='lines', name='Buy Price')
            fig.add_scatter(x=date_range, y=y_sale, mode='lines', name='Sell Price')
            st.plotly_chart(fig, use_container_width=True)


            # Power gen vs power con
            fig_power = px.line(x=date_range, y=[power_gen, y_cons], labels={'x': 'Date'}, title='FORECASTED GEN & USE')
            fig_power.update_layout(
                plot_bgcolor='rgba(0, 0, 0, 0)',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                # width=600,
                # height=400,
                showlegend=False  # Hide legend
            )
            fig_power.add_scatter(x=date_range, y=power_gen, mode='lines', name='generated')
            fig_power.add_scatter(x=date_range, y=y_cons, mode='lines', name='consumed')
            fig_power.update_yaxes(title_text='Energy (kWh)')
            st.plotly_chart(fig_power, use_container_width=True)

            # Battery Output
            fig_battopt = px.area(x=date_range, y=y_battopt[1:], labels={'x': 'Date', 'y': 'Battery Charge (kWh)'}, title='BATTERY CHARGE')
            fig_battopt.update_layout(
                plot_bgcolor='rgba(0, 0, 0, 0)',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                # width=600,
                # height=400,
                showlegend=False  # Hide legend
            )
            st.plotly_chart(fig_battopt, use_container_width=True)

                            # Get definitiion for weather WMO codes
            wmo_url = 'https://gist.githubusercontent.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c/raw/76b0cb0ef0bfd8a2ec988aa54e30ecd1b483495d/descriptions.json'
            wmo_description = requests.get(wmo_url).json()

            # Forecast header
            st.subheader('7 Day Energy Forecast')
            st.markdown('')  # Empty markdown line for spacing
            st.markdown('')  # Empty markdown line for spacing

            # WEATHER
            daily_forecasts = np.array(weather).reshape(7, 24)
            # Define the range of daytime hours (for example, 7 AM to 7 PM)
            start_hour = 7
            end_hour = 19
            # Find the mode for daytime hours for each day
            daily_modes = []
            for day_data in daily_forecasts:
                daytime_data = day_data[start_hour:end_hour] # Slice for daytime hours
                mode = np.bincount(daytime_data).argmax()
                daily_modes.append(mode)
            weekly_forecast = {}
            for index, day in enumerate(daily_modes):
                image = wmo_description[f'{day}']['day']['image']
                description = wmo_description[f'{day}']['day']['description']
                weekly_forecast[index] = []
                weekly_forecast[index].append(image)
                weekly_forecast[index].append(description)

            days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            weather_description = [weekly_forecast[i][1] for i in range(7)]
            st.dataframe(pd.DataFrame({'Day': days_of_week, 'Weather': weather_description}), use_container_width=True)

        
            # FOOTER
            # Tracker cards
            st.divider()
            st.subheader('Model Performance')
            st.markdown('')  # Empty markdown line for spacing

            foot1, foot2, foot3 = st.columns(3)
            foot1.metric("Average User Annual Savings", "£230 💷")
            foot2.metric("Mean Absolute Error", "£0.64 📈")
            foot3.metric("R Squared:", "0.92 ✅")
            st.markdown('')  # Empty markdown line for spacing
            st.markdown("---")
            st.markdown('© 2024 Market Energy Ltd. All rights reserved.')   