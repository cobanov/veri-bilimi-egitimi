import pandas as pd
import umap
from vispy.scene import visuals
import vispy.scene
import sys

# Read dataset
df = pd.read_csv("./penguins_scaled.csv")

# UMAP
reducer = umap.UMAP(
    n_neighbors=5,
    n_components=3,
)
embeddings = reducer.fit_transform(df.iloc[:, :-1])

# Visualization preprocessing
classes = {0: [0, 0, 1], 1: [1, 0, 0], 2: [0, 1, 0]}
colors = pd.DataFrame(df["target"].map(classes).tolist(), columns=["v1", "v2", "v3"])

# VisPy Visualization
canvas = vispy.scene.SceneCanvas(keys="interactive", show=True)
view = canvas.central_widget.add_view()

scatter = visuals.Markers()
scatter.set_data(
    embeddings,
    edge_color=None,
    face_color=colors,
    size=5,
    symbol="o",
    edge_width=1,
)

view.add(scatter)

view.camera = "arcball"  # or try 'arcball'
axis = visuals.XYZAxis(parent=view.scene)

if sys.flags.interactive != 1:
    vispy.app.run()
