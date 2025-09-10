import pandas as pd
from dash import html, dcc, Input, Output, callback, register_page
import plotly.express as px
from pathlib import Path

register_page(__name__, path='/page2', name = 'Rising Sea Levels')

#AI used to brainstorm what types of non-interactive geographical maps are available in dash, and help with code syntax and layout improvements.

#Link for reference to data source: https://tidesandcurrents.noaa.gov/sltrends/sltrends_states.html?gid=1249

## Load in all of the csv files
data_path = Path(__file__).resolve().parent.parent / "CTBA_Team3_Final" / "data" / "Yorktown.csv"
yorktown = pd.read_csv(data_path, header= 4, index_col=False)
yorktown.head()
#rename Month column to yorktown_mean
yorktown = yorktown.rename(columns={' Monthly_MSL': 'yorktown_mean'})
yorktown.head()
#show last row of yorktown
yorktown.tail()
#alter dataframe to only include years between 2015 and 2024
yorktown = yorktown[yorktown['Year'] >= 2015]
yorktown = yorktown[yorktown['Year'] < 2025]
#check for any null values
yorktown.isnull().sum()
yorktown.head()

data_path1 = Path(__file__).resolve().parent.parent / "CTBA_Team3_Final" / "data" / "Windmill Point.csv"
WP = pd.read_csv(data_path1, header = 4, index_col=False)
WP.head()
#rename Month column to WP_mean
WP = WP.rename(columns={' Monthly_MSL': 'WP_mean'})
WP.head()
#show last row of WP
WP.tail()
#alter dataframe to only include years between 2015 and 2024
WP = WP[WP['Year'] >= 2015]
WP = WP[WP['Year'] < 2025]
#check for any null values
WP.isnull().sum()
WP.head()

data_path2 = Path(__file__).resolve().parent.parent / "CTBA_Team3_Final" / "data" / "Wachapreague.csv"
Wachapreague = pd.read_csv(data_path2, header = 4, index_col=False)
Wachapreague.head()
#rename Month column to Wachapreague_mean
Wachapreague = Wachapreague.rename(columns={' Monthly_MSL': 'Wachapreague_mean'})
Wachapreague.head()
#show last row of Wachapreague
Wachapreague.tail()
#alter dataframe to only include years between 2015 and 2024
Wachapreague = Wachapreague[Wachapreague['Year'] >= 2015]
Wachapreague = Wachapreague[Wachapreague['Year'] < 2025]
#check for any null values
Wachapreague.isnull().sum()
Wachapreague.head()

data_path3 = Path(__file__).resolve().parent.parent / "CTBA_Team3_Final" / "data" / "Sewells Point.csv"
SewellsPoint = pd.read_csv(data_path3, header = 4, index_col=False)
SewellsPoint.head()
#rename Month column to SewellsPoint_mean
SewellsPoint = SewellsPoint.rename(columns={' Monthly_MSL': 'SewellsPoint_mean'})
SewellsPoint.head()
#show last row of SewellsPoint
SewellsPoint.tail()
#alter dataframe to only include years between 2015 and 2024
SewellsPoint = SewellsPoint[SewellsPoint['Year'] >= 2015]
SewellsPoint = SewellsPoint[SewellsPoint['Year'] < 2025]
#check for any null values
SewellsPoint.isnull().sum()
SewellsPoint.head()

data_path4 = Path(__file__).resolve().parent.parent / "CTBA_Team3_Final" / "data" / "Lewisetta.csv"
Lewisetta = pd.read_csv(data_path4, header = 4, index_col=False)
Lewisetta.head()
#rename Month column to Lewisetta_mean
Lewisetta = Lewisetta.rename(columns={' Monthly_MSL': 'Lewisetta_mean'})
Lewisetta.head()
#show last row of Lewisetta
Lewisetta.tail()
#alter dataframe to only include years between 2015 and 2024
Lewisetta = Lewisetta[Lewisetta['Year'] >= 2015]
Lewisetta = Lewisetta[Lewisetta['Year'] < 2025]
#check for any null values
Lewisetta.isnull().sum()
Lewisetta.head()

data_path5 = Path(__file__).resolve().parent.parent / "CTBA_Team3_Final" / "data" / "Kiptopeke.csv"
Kiptopeke = pd.read_csv(data_path5, header = 4, index_col=False)
Kiptopeke.head()
#rename Month column to Kiptopeke_mean
Kiptopeke = Kiptopeke.rename(columns={' Monthly_MSL': 'Kiptopeke_mean'})
Kiptopeke.head()
#show last row of Kiptopeke
Kiptopeke.tail()
#alter dataframe to only include years between 2015 and 2024
Kiptopeke = Kiptopeke[Kiptopeke['Year'] >= 2015]
Kiptopeke = Kiptopeke[Kiptopeke['Year'] < 2025]
#Check for any null values
Kiptopeke.isnull().sum()
Kiptopeke.head()

data_path6 = Path(__file__).resolve().parent.parent / "CTBA_Team3_Final" / "data" / "Dahlgren.csv"
Dahlgren = pd.read_csv(data_path6, header = 4, index_col=False)
Dahlgren.head()
#rename Month column to Dahlgren_mean
Dahlgren = Dahlgren.rename(columns={' Monthly_MSL': 'Dahlgren_mean'})
Dahlgren.head()
#show last row of Dahlgren
Dahlgren.tail()
#alter dataframe to only include years between 2015 ane 2024
Dahlgren = Dahlgren[Dahlgren['Year'] >= 2015]
Dahlgren = Dahlgren[Dahlgren['Year'] < 2025]
#check for any null values
Dahlgren.isnull().sum()
Dahlgren.head()


#aggregate data by year and take the mean of each year for each location 
yorktown_aggregated = yorktown.groupby('Year')['yorktown_mean'].mean().reset_index()
WP_aggregated = WP.groupby('Year')['WP_mean'].mean().reset_index()
SewellsPoint_aggregated = SewellsPoint.groupby('Year')['SewellsPoint_mean'].mean().reset_index()
Wachapreague_aggregated = Wachapreague.groupby('Year')['Wachapreague_mean'].mean().reset_index()
Lewisetta_aggregated = Lewisetta.groupby('Year')['Lewisetta_mean'].mean().reset_index()
Kiptopeke_aggregated = Kiptopeke.groupby('Year')['Kiptopeke_mean'].mean().reset_index()
Dahlgren_aggregated = Dahlgren.groupby('Year')['Dahlgren_mean'].mean().reset_index()

#merge all dataframes together on Year column
merged_df = pd.merge(yorktown_aggregated, WP_aggregated, on='Year', how='inner')
merged_df = pd.merge(merged_df, SewellsPoint_aggregated, on='Year', how='inner')
merged_df = pd.merge(merged_df, Wachapreague_aggregated, on='Year', how='inner')
merged_df = pd.merge(merged_df, Lewisetta_aggregated, on='Year', how='inner')
merged_df = pd.merge(merged_df, Kiptopeke_aggregated, on='Year', how='inner')
merged_df = pd.merge(merged_df, Dahlgren_aggregated, on='Year', how='inner')

merged_df.head()
len(merged_df)

merged_df

print(merged_df.dtypes)


# Add Lat/Lon columns to your dataframe

# Add Lat/Lon columns to your dataframe
locations_data = {
    'yorktown_mean': {'lat': 37.227, 'lon': -76.495, 'name': 'Yorktown'},
    'WP_mean': {'lat': 37.615, 'lon': -76.290, 'name': 'Windmill Point'},
    'SewellsPoint_mean': {'lat': 36.947, 'lon': -76.330, 'name': 'Sewells Point'},
    'Wachapreague_mean': {'lat': 37.608, 'lon': -75.686, 'name': 'Wachapreague'},
    'Lewisetta_mean': {'lat': 37.995, 'lon': -76.465, 'name': 'Lewisetta'},
    'Kiptopeke_mean': {'lat': 37.165, 'lon': -75.988, 'name': 'Kiptopeke'},
    'Dahlgren_mean': {'lat': 38.319, 'lon': -77.036, 'name': 'Dahlgren'},
}

# Restructure the dataframe from wide to long format
df_long = pd.melt(
    merged_df,
    id_vars=['Year'],
    value_vars=['yorktown_mean', 'WP_mean', 'SewellsPoint_mean', 'Wachapreague_mean', 'Lewisetta_mean', 'Kiptopeke_mean', 'Dahlgren_mean'],
    var_name='Location_Key',
    value_name='Mean_Increase'
)

# Map the lat/lon values and location names to the new dataframe
df_long['Location'] = df_long['Location_Key'].map(lambda x: locations_data[x]['name'])
df_long['Lat'] = df_long['Location_Key'].map(lambda x: locations_data[x]['lat'])
df_long['Lon'] = df_long['Location_Key'].map(lambda x: locations_data[x]['lon'])
df_long.head()
 


fig = px.scatter_map(
    df_long,
    lat="Lat",
    lon="Lon",
    hover_name="Location",
    zoom=7,
    center={"lat": 37.75, "lon": -76.5},  
    height=600,
    color_discrete_sequence=['red']
)

layout = html.Div(
    children=[
        html.H1('Virginia Sea Level Rise'),
        html.P("This dashboard shows the average sea level rise in meters for various locations in Virginia from 2015 to 2024, utilizing data from NOAA. The map below shows the coordinates of NOAA's Tides and Currents Stations in Virginia, where they track changes in sea level rise based on monthly mean sea level data. "),
        html.Div([ html.P([ "For more information on the data source, visit ", html.A("NOAA Tides and Currents", href="https://tidesandcurrents.noaa.gov/sltrends/sltrends_states.html?gid=1249", target="_blank")])]),
        html.Br(),
        html.H2("Map of NOAA's Tides & Currents Stations in Virginia"),
        html.Div([
        dcc.Graph(figure=fig)], style={"width": "85%", "height": "600px", "margin": "auto"}),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

                html.Div(
            children=[
                html.H2('Sea Level Rise Trends', style={'color': "#FFFFFF", 'textAlign': 'center'}),
                html.P('Select a location from the dropdown to view its historical sea level trend between 2015 and 2024.', style={'color': "#FFFFFF", 'textAlign': 'center'}),
                dcc.Dropdown(
                    id='location-dropdown',
                    options=[{'label': loc, 'value': loc} for loc in sorted(df_long['Location'].unique())],
                    value='Yorktown',  # Default value
                    clearable=False,
                    style={'backgroundColor': 'white',
                           'color': '#293831',
                           'fontSize': '16px',
                           'textAlign': 'center',
                           'margin': 'auto'}
                ),
                dcc.Graph(id='trend-line-chart'),
            ]
        )
    ]
)
 

@callback(
    Output('trend-line-chart', 'figure'),
    Input('location-dropdown', 'value')
)

def update_line_chart(selected_location):
    d = df_long[df_long['Location'] == selected_location]
    
    fig = px.line(
        d,
        x='Year',
        y='Mean_Increase',
        title=f'Sea Level Rise Trend at {selected_location}',
        markers=True
    )


    
    fig.update_layout(
        #paper_bgcolor='#32453C',
        #plot_bgcolor='#293831',
        font_color= 'Black',
        xaxis_title='Year',
        xaxis=dict(dtick=1),
        yaxis_title='Mean Sea Level (Meters)',
        margin=dict(l=10, r=10, t=50, b=10),
    )

    

    return fig


