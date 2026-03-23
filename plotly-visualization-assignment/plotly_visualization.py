import pandas as pd
import plotly.express as px

# Step 1: Create dataset
epochs = list(range(1, 11))
training_loss = [0.95, 0.75, 0.60, 0.50, 0.42, 0.38, 0.36, 0.35, 0.34, 0.34]

# Step 2: Convert to DataFrame
df = pd.DataFrame({
    "Epoch": epochs,
    "Training Loss": training_loss
})

# Step 3: Create interactive line chart
fig = px.line(
    df,
    x="Epoch",
    y="Training Loss",
    title="Training Loss Over Epochs",
    labels={"Epoch": "Epoch", "Training Loss": "Loss"}
)

# Step 4: Add annotation (loss stabilizes around epoch 8)
fig.add_annotation(
    x=8,
    y=0.35,
    text="Loss stabilizes here",
    showarrow=True,
    arrowhead=2
)

# Step 5: Display chart
fig.show()
