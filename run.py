import pandas as pd
import streamlit as st


import plotly.express as px 
import pandas as pd
df = pd.read_csv(r"C:\Users\jsiu0002\Downloads\Only_once\PageUp-Org\Report about Organisation 2023-07-20T1525.csv")
df['Value'] = 1
# df = df[df['Organisational Unit Title'] != '']
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


st.set_page_config(page_title="The Monash Org Chart", layout="wide")
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 300px;

    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 300px;
        margin-left: -300px;

    }
     
    """,
    unsafe_allow_html=True,
)

fig2 = px.treemap(df_dict, 
                   path=['Faculty/Portfolio', 'School/Division' , 'Organisational Unit Title']
                   , values= 'Value'
                   , color='Faculty/Portfolio'
                   ,maxdepth=2
                   )

fig2.update_layout(
    # title_text="Monash Organisational Chart Diagram" 
     title=dict(
        text='<b><span style="font-family: Courier New, Monospace; font-size: 28pt">Monash Organisation Chart</span><br><br><span style="font-family: Courier New, Monospace;font-size: 15pt"> Faculty -> Division -> Org Unit</span></b>'
    )
                   
                   ,    font_family="Calibri"
                   ,font_size=25
                   ,grid= dict(columns=10, rows=4)
                   ,uniformtext=dict(minsize=35)
                   ,
autosize=True,
    width=500,
    height=1000,
)
# fig2.show()

st.plotly_chart(fig2, use_container_width=True)
