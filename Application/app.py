import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import time
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)

import boto3
import pandas as pd
#from sagemaker import get_execution_role

#role = get_execution_role()
bucket='stocks-dump'
data_key = 'stocks-dump.json'
data_location = 's3://{}/{}'.format(bucket, data_key)

#pd.read_csv(data_location)

import json

s3 = boto3.resource('s3')
obj = s3.Object(bucket, data_key)
data = json.load(obj.get()['Body']) 

json_data = [] # your list with json objects (dicts)
df=pd.DataFrame(columns=['Company','Date_Time','Stock Price','Nasdaq','S&P 50','DowJones'])
for item in data:
    df.loc[len(df)]=[item['Company'],item['Date_Time'],item['Stock Price'],item['Nasdaq'], item['S&P 50'], item['DowJones']]



df['Date_Time']= pd.to_datetime(df['Date_Time'])
df = df.sort_values(by="Date_Time")

print(df.head(5))
fig = px.line(df, x="Date_Time", y="Stock Price", labels = {'x':'Date-Time', 'y':'Amazon Stock Price'},
                title="Amazon Stock Price")
fig1= px.line(df, x="Date_Time", y="Nasdaq")
fig2= px.line(df, x="Date_Time", y="S&P 50")

fig3= px.line(df, x="Date_Time", y="DowJones")
background_color="#003366"

fig.update_layout(title_x=0.5,
                paper_bgcolor=background_color,
                font_color="white",
                title_font_color="white")
                
                

                
fig1.update_layout(title_x=0.5,
                paper_bgcolor=background_color,
                font_color="white",
                title_font_color="white")
                

                
fig2.update_layout(title_x=0.5,
                paper_bgcolor=background_color,
                font_color="white",
                title_font_color="white")

fig3.update_layout(title_x=0.5,
                paper_bgcolor=background_color,
                font_color="white",
                title_font_color="white")
                
# ------------------------------------------------------------------------------
# App layout


button_style={ 'border': 'none','color':'black','padding':'15px 32px',
            'text-align': 'center','text-decoration':'none',
            'font-size': '24px','align':'center'}


app.layout = html.Div([

    html.H1("Stock Price Predictions", style={'text-align': 'center','color':'white'}),

    dcc.Graph(id='my_bee_map', figure=fig),
    
    html.Div([
    
    html.Button('Train the Model', id='btn-nclicks-1', n_clicks=0, 
    style=button_style),
    
    html.Button('Predict', id='btn-nclicks-2', n_clicks=0,
    style=button_style)
    ],
    style=button_style),

    html.Div(id='container-button-timestamp'),
    
    
    html.Div([
        dcc.Graph(id='my_bee_map1', figure=fig1),
        
        ], style={'width': '50%','display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(id='my_bee_map2', figure=fig2),
        
        ], style={'width': '50%', 
        'align': 'right',
        'display': 'inline-block'}),
    
    
        html.Div([
        dcc.Graph(id='my_bee_map3', figure=fig3),
        
        ], style={'width': '50%','display': 'inline-block'}),
    
 
    html.Div([
        dcc.Graph(id='my_bee_map4', figure=fig3),
        
        ], style={'width': '50%','align': 'right','display': 'inline-block'})
    
   
    
    

    ], style={
  'backgroundColor':background_color,
  'position':'absolute',
  'width':'100%',
  'height':'100%',
  'top':'0px',
  'left':'0px'
  
})



# ------------------------------------------------------------------------------

@app.callback(Output('container-button-timestamp', 'children'),
              [Input('btn-nclicks-1', 'n_clicks'),
               Input('btn-nclicks-2', 'n_clicks')])

def displayClick(btn1,btn2):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    print(changed_id)
    msg=str()

    if 'btn-nclicks-2.n_clicks' == changed_id:
        print("YES")
        msg = 'Button 2 was most recently clicked'
        print(msg)
    elif 'btn-nclicks-1.n_clicks' == changed_id:
        print("YES")
        
        time.sleep(10)
        msg=str(43)
        #msg = 'Button 2 was most recently clicked'
        print(msg)
    else:
        msg="Nothing Pressed"
    
    return html.Div(msg)

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8080,debug=True)
