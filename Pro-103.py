import pandas as pd
import plotly.express as px
df = pd.read_csv("data.csv")
fig = px.scatter(df, x='date', y='cases', color='country',title = 'Covid cases')
fig.show()

