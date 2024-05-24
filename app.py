from js import Plotly, JSON, Uint8Array, File, URL
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pyodide.http import open_url
from pyscript import display, document
import warnings
warnings.filterwarnings("ignore")

url = "https://raw.githubusercontent.com/DisephD/Pyscript-Dashboad/main/data/water_data_processed%20(1).csv"

data = pd.read_csv(open_url(url), parse_dates=["Date"])
water_data = data

table_daily_total = None

def format_week_num(week_num): 
  return f"Week {week_num}"

#create a html representation of a plotly graph
def plotly_to_json (fig, target_id): 

    chart_json = fig.to_json()
    Plotly.newPlot (target_id, JSON.parse(chart_json))


def display_stats(variable, target):

    document.getElementById(target).innerHTML =''
    var = (f"{variable} ml")
    display (var, target = target)


#create statistics and parse to html
def monthly_stats(filtered_df):

    daily_total = filtered_df.groupby("Day")["Water(ml)"].sum().reset_index()
    total_water = int(daily_total["Water(ml)"].sum())
    avg_water = int(round((total_water/len(daily_total)),1))
    highest_water = int(daily_total["Water(ml)"].max())

    display_stats(total_water, "total_water")
    display_stats(avg_water, "avg_water")
    display_stats(highest_water, "highest_water")


#create total statistics for all the months 
def total_month_stats():

    daily_total = water_data.groupby("Day")["Water(ml)"].sum().reset_index()
    all_total = int(daily_total["Water(ml)"].sum())
    all_avg = int(round((all_total/len(daily_total)),1))
    all_highest = int(daily_total["Water(ml)"].max())

    display_stats(all_total, target= "all_total")
    display_stats(all_avg, target = "all_avg")
    display_stats(all_highest, target = "all_highest")


def circle_chart (filtered_df):

    total_water = int(filtered_df["Water(ml)"].sum())
    target= 62000

    fig=go.Figure(go.Indicator(
        align= "center", mode="gauge+number+delta", value=total_water, 
        title = {"text": "Monthly Goal: 62000ml", "font":{'size': 17, "color": "black"},"align": "center", },
        delta = {'reference': target, 'relative': True, 'increasing': {'color': 'green'}, 'font': {'size': 20} },
        number = {'suffix': "ml", "font": {'size': 19,}, 'valueformat': ":.2f", },
        gauge= {"bar": {"color": "#3C91E6"}, 'axis': {'range': [0, 62000]}, }
    ))

    fig.update_layout(width=300, height=300, showlegend=False, margin=dict(t=10,l=10,b=5,r=10),)
    plotly_to_json(fig, "circle_chart")
    

#create and format a line chart with plotly express 
def line_chart (filtered_df):

    daily_total = filtered_df.groupby("Day")["Water(ml)"].sum().reset_index()
    
    fig = px.line(daily_total, x="Day", y="Water(ml)", height=270, width= 670, markers=True)
    fig.update_traces (marker_size = 6, texttemplate='%{text:.2s}', line_color= "#4587D9")

    fig.update_layout(plot_bgcolor="rgb(254,254,254)", margin=dict(t=50,l=10,b=5,r=10), 
                      title= "Daily Trend", title_font_family ="Times New Roman Black", 
                      title_font_size = 17, title_x = 0.01, xaxis_tickfont_size=11,
                      yaxis=dict( title=None, titlefont_size=14, tickfont_size=11, tickfont_color= "#A9A9AB", ),
                      xaxis = dict(title=None, tickfont_size =11,  tickfont_color= "#A9A9AB"),
                      )
    
    fig.add_hline(y=2000, line_width=1,  line_dash="dash", line_color="#bbd9fe")
    plotly_to_json (fig, "line_chart")



#create and format a bar chart with plotly express 
def bar_chart (filtered_df): 

    bar_daily_total = filtered_df.groupby("Week")["Water(ml)"].sum().reset_index()

    fig = px.bar (bar_daily_total, x ="Week", y = "Water(ml)", title= "", labels ="", 
                  color_discrete_sequence=["#3C91E6"])
    fig.update_xaxes(tickvals= bar_daily_total["Week"].unique(),
                     ticktext=[format_week_num(week)for week in bar_daily_total['Week'].unique()])
    fig.update_layout(
        plot_bgcolor="rgb(254,254,254,0.7)", margin=dict(t=20,l=10,b=0,r=10), width=300, height = 300,
        xaxis_tickfont_size=14,yaxis=dict( title='', titlefont_size=14, tickfont_size=13),
        xaxis = dict(title="", tickfont_size =13), bargap=0.3, 
    )
    fig.update_traces(width=0.5)
    fig.add_hline(y=14000, line_width=2,  line_dash="dash", line_color="#E92022")

    plotly_to_json (fig, "bar_chart")


#create and format a table with plotly graph objects
def table_chart (filtered_df):

    global table_daily_total
    table_daily_total = filtered_df.groupby("Date")["Water(ml)"].sum().reset_index()
    table_daily_total["Daily_Change"] = table_daily_total["Water(ml)"].pct_change().mul(100).round(1).fillna(0).apply(lambda x: f"+{x}" if x > 0 else str(x)) + "%"
    table_daily_total["Daily_Change"] = table_daily_total["Daily_Change"].astype("category")
    
    font_color = ["#333131", "#333131",
                  ["#8DE28D" if "+" in x else "#FE5555" if "-" in x else "#333131" for x in list(table_daily_total["Daily_Change"])]]

    table_daily_total["Date"] = table_daily_total["Date"].astype("str")
    fig= go.Figure(data=[go.Table (columnwidth = [12, 10, 10],
                                    header=dict(values=list(table_daily_total.columns, ),
                                                 fill_color='white', align=['left', "left", "left"], 
                                                height=45,font=dict(size=17, color= "black"),
                                                line_color= "rgb(231, 239, 250)",), 
                                    cells=dict(values=[table_daily_total["Date"], table_daily_total["Water(ml)"],
                                                        table_daily_total["Daily_Change"]],
                                                fill_color='white', line_color= "rgb(231, 239, 250)", 
                                                align=['left',"left","left"],
                                                height=45, font=dict(size=15, color= font_color)))
                                    ])
    fig.layout.width= 670
    fig.update_layout(plot_bgcolor="rgb(254,254,254)",height= 270, margin=dict(t=5,l=10,b=10,r=10),)
    plotly_to_json (fig, "table")

    return table_daily_total


#create and format a heatmap with plotly express
def heat_chart (filtered_df): 

    heatmap_data = filtered_df.groupby(['Weekday_name', 'Time_of_day'])["Water(ml)"].sum().reset_index()
    custom_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun', ]
    heatmap_data['Weekday_name'] = pd.Categorical(heatmap_data['Weekday_name'], categories=custom_order, ordered=True)
    day_order = ["Morning", "Noon", "Evening", "Night"]
    heatmap_data['Time_of_day'] = pd.Categorical(heatmap_data['Time_of_day'], categories=day_order, ordered=True)

    heatmap_pivot= heatmap_data.pivot_table(index="Time_of_day", columns= "Weekday_name", values= "Water(ml)", aggfunc="sum", fill_value= 0)

    fig= px.imshow(heatmap_pivot, color_continuous_scale='Blues', height=300, width = 240)
    fig.update_traces(showscale=False, coloraxis=None,colorscale= "Blues")
    fig.update_layout(plot_bgcolor="rgb(254,254,254)", title='',margin=dict(t=10,l=0,b=80,r=20), 
        xaxis_tickfont_size=14,
        yaxis=dict( title=None, titlefont_size=14, tickfont_size=13),
        xaxis = dict(title=None, tickfont_size =13, side="top", tickangle=90),
    )
    plotly_to_json (fig, "heatmap")


#return all the different chart functions
def plot_charts(selected_month):  
   filtered_df = water_data[water_data["Month"]==selected_month]
   all_stats = total_month_stats()
   kpis = monthly_stats(filtered_df)
   line = line_chart(filtered_df)
   table = table_chart(filtered_df)
   circle = circle_chart(filtered_df)
   bar = bar_chart(filtered_df)
   heatmap = heat_chart(filtered_df)
   return all_stats, kpis, line, table, circle, bar, heatmap


#create a dropdown event catcher
def dropdown_event(event):
    selected_month = document.getElementById("dropdown_menu").value
    plot_charts(selected_month)


def download_file(*args):
    filename = "waterdata.csv"
    table_daily_total.to_csv(filename, index=False)

    with open (filename, "rb") as data:
        my_stream = data.read()
        js_array = Uint8Array.new(len(my_stream))
        js_array.assign(my_stream)
        file = File.new ([js_array], "unused.csv", {type: "text/csv"})
        url = URL.createObjectURL(file)
        hidden_link = document.createElement("a")
        hidden_link.setAttribute("download", "waterdata.csv")
        hidden_link.setAttribute("href", url)
        hidden_link.click()

plot_charts("January")