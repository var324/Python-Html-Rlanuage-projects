import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. Load the stellar catalog
data = pd.read_csv("../data/stars_catalog.csv")
data = data.dropna()

# 2. Map physical spectral signatures to hexadecimal star colors
def assign_star_color(row):
    sc = str(row['spectral_class'])[0].upper()
    st = str(row['star_type']).lower()
    if 'white dwarf' in st: return '#e0f7fa'  
    elif sc == 'O': return '#3d5afe'  
    elif sc == 'B': return '#64b5f6'  
    elif sc == 'A': return '#ffffff'  
    elif sc == 'F': return '#fffde7'  
    elif sc == 'G': return '#ffff00'  
    elif sc == 'K': return '#ffb74d'  
    elif sc == 'M': return '#ff3d00'  
    return '#ffffff'

data['plot_color'] = data.apply(assign_star_color, axis=1)

# 3. Scale marker sizing elegantly based on stellar radius
data['marker_size'] = np.clip((data["radius"] * 4.5) + 4, 10, 50)

# 4. Generate the 3D Scatter Plot
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=data["temperature"],
    y=data["luminosity"],
    z=data["radius"],
    mode='markers+text',
    text=data["name"],
    textposition="top center",
    textfont=dict(color="#b0bec5", size=9.5),
    marker=dict(
        size=data['marker_size'],
        color=data['plot_color'],
        line=dict(width=1, color='white'),
        opacity=0.85
    ),
    hoverinfo="text",
    hovertemplate="<b>%{text}</b><br>" +
                  "Temperature: %{x} K<br>" +
                  "Luminosity: %{y} L/L☉<br>" +
                  "Radius: %{z} R/R☉<br>" +
                  "<extra></extra>"
))

# 5. Advanced 3D Axis and Layout Customizations
fig.update_layout(
    paper_bgcolor='#0a0a0a',
    plot_bgcolor='#0a0a0a',
    width=1200,
    height=850,
    scene=dict(
        # X-Axis: Beautiful clean numerical temperature ticks (Hot on left, Cold on right)
        xaxis=dict(
            title=dict(
                text="Effective Temperature T<sub>eff</sub> (Kelvin)",
                font=dict(color="#cfd8dc", size=12)
            ),
            type="log",
            autorange="reversed",
            tickvals=[40000, 30000, 20000, 10000, 7500, 6000, 5000, 3000, 2000],
            ticktext=["40,000 K", "30,000 K", "20,000 K", "10,000 K", "7,500 K", "6,000 K", "5,000 K", "3,000 K", "2,000 K"],
            tickfont=dict(color="#90a4ae", size=10),
            backgroundcolor="#050505",
            gridcolor="#263238",
            showbackground=True,
            zerolinecolor="#37474f"
        ),
        # Y-Axis: Logarithmic Solar Luminosity
        yaxis=dict(
            title=dict(
                text="Luminosity in Solar Units (L / L☉)",
                font=dict(color="#cfd8dc", size=12)
            ),
            type="log",
            tickvals=[1e-6, 1e-4, 1e-2, 1, 100, 10000, 1000000],
            ticktext=["10⁻⁶", "10⁻⁴", "10⁻²", "1 (Sun)", "10²", "10⁴", "10⁶"],
            tickfont=dict(color="#90a4ae", size=10),
            backgroundcolor="#050505",
            gridcolor="#263238",
            showbackground=True,
            zerolinecolor="#37474f"
        ),
        # Z-Axis: Logarithmic Stellar Radius
        zaxis=dict(
            title=dict(
                text="Stellar Radius (R / R☉)",
                font=dict(color="#cfd8dc", size=12)
            ),
            type="log",
            tickvals=[0.01, 0.1, 1, 10, 100, 1000],
            ticktext=["0.01 R☉", "0.1 R☉", "1 (Sun)", "10 R☉", "100 R☉", "1,000 R☉"],
            tickfont=dict(color="#90a4ae", size=10),
            backgroundcolor="#050505",
            gridcolor="#263238",
            showbackground=True,
            zerolinecolor="#37474f"
        ),
        camera=dict(
            eye=dict(x=1.6, y=1.6, z=1.2)
        )
    ),
    showlegend=False,
    margin=dict(l=0, r=0, b=0, t=20)
)

# 6. Save the standalone interactive 3D HTML file into your web directory
fig.write_html("../web/hr_interactive_3d.html", include_plotlyjs='cdn')
print("3D Interactive web element updated successfully with pristine axis lines inside web/ folder.")