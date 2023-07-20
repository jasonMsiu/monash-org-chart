import pandas as pd
import streamlit as st


import plotly.express as px 
import pandas as pd
df = pd.read_csv("Report about Organisation 2023-07-20T1525.csv")
df['Value'] = 1
df = df[df['Organisational Unit Title'] != '']
df['Organisational Unit Title'] = df['Organisational Unit Title'].astype(str)

df_dict = df.to_dict()

# fig2 = px.sunburst(df_dict, 
#                    path=['Faculty/Portfolio', 'School/Division' , 'Organisational Unit Title'], 
#                    values= 'Value', color='Faculty/Portfolio')
# fig2.update_layout(title_text="Two-level Sunburst Diagram", font_size=10,
#                    grid= dict(columns=2, rows=1),
#     )
# fig2.show()

fig2 = px.treemap(df_dict, 
                   path=['Faculty/Portfolio', 'School/Division' , 'Organisational Unit Title'], 
                   values= 'Value', color='Faculty/Portfolio')
fig2.update_layout(title_text="Three-level Sunburst Diagram", font_size=10,
                   grid= dict(columns=1, rows=1),
    )
fig2.show()

st.plotly_chart(fig2, use_container_width=True)
