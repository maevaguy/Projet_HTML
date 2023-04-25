import pandas as pd
import plotly.express as px

# Load data into a pandas DataFrame
data = pd.read_csv('data.csv')

# Create a violin plot with Plotly
fig = px.violin(data, x='Group', y='Coverage',box=True,color='Group',title='Violin Plot du coverage en fonction des OG groups',points="all")

# Show the plot
fig.show()
