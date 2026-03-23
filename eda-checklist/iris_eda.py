import pandas as pd
import plotly.express as px

df = pd.read_csv("iris.csv")

print(df.head())

print(df.shape)
# Observation: Confirms number of samples (150) and features (5).

print(df.info())
print(df.isnull().sum())
#Observation: Iris dataset typically has no missing values; all features are numeric except species


print(df['petal_length'].describe())
fig = px.histogram(df, x="petal_length", color="species", nbins=20)
fig.show()
#Observation: Petal length distribution differs across species; Setosa has distinctly smaller petal lengths.

fig = px.box(df, x="species", y="sepal_width")
fig.show()
#Observation: Boxplots highlight potential outliers (e.g., unusually wide sepals in Setosa).


fig = px.scatter(df, x="petal_length", y="petal_width", color="species")
fig.show()
#Observation: Strong correlation between petal length and width; Setosa is clearly separated, while Versicolor and Virginica overlap more.

print(df.groupby("species").mean())

#Observation:
#Setosa: Small petals, wider sepals.
#Versicolor: Intermediate measurements.
#Virginica: Largest petals overall.
#These differences suggest that petal measurements are highly discriminative for species classification.
