
import pandas as pd
import plotly.express as px
import preswald

# Load the weather dataset
df = pd.read_csv('data/weather.csv')

# Clean column names 
df.columns = [col.replace(' ', '_') for col in df.columns]

# Create a simple temperature visualization
fig = px.line(df, x='Formatted_Date', y='Temperature_(C)', 
              title='Temperature Over Time',
              labels={'Temperature_(C)': 'Temperature (°C)', 'Formatted_Date': 'Date'})

# Display the app
preswald.text("# Weather Data Analysis")
preswald.text("Simple weather data visualization.")
preswald.plotly(fig)
preswald.table(df.head(10), title="Weather Data Sample")
