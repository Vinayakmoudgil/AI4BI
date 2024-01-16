import plotly.express as px

def bar_chart(df_data, x_axis,y_axis,kpi_name):
    fig = px.bar(df_data, x=x_axis, y=y_axis, title=kpi_name)
    return fig

def line_chart(df_data, x_axis,y_axis,kpi_name):
    fig = px.line(df_data, x=x_axis, y=y_axis, title=kpi_name)
    return fig

def scatter_chart(df_data, x_axis,y_axis,kpi_name):
    fig = px.scatter(df_data, x=x_axis, y=y_axis, title=kpi_name)
    return fig