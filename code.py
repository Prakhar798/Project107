import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(
    df,
    x= df.groupby(["student_id", "level"], as_index=False)["attempt"].mean(),
    y= ["Level 1", "Level 2", "Level 3", "Level 4"],
    size="attempt",
    color="attempt",
)
fig.show()
