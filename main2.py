from tkinter import Label
from bokeh.plotting import figure, output_file,save, show, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
from bokeh.embed import components
import pandas as pd

df = pd.read_csv('topGoals.csv', delimiter=';', encoding='unicode_escape')
#print(df)
# Create a ColumnDataSource from DataFrame
source = ColumnDataSource(df)

car = df['Joueurs']
hp = df['Buts']


output_file('index2.html')

# Car list
car_list = source.data['Pays'].tolist()

# Add plot
p = figure(
    y_range=car_list,
    plot_width=1000,
    plot_height=600,
    title='Statistics of the Goals Scored by CAN 2021 Players',
    x_axis_label='Goals Scored',
    tools='pan,box_select,zoom_in,zoom_out,save,reset'
)

#citation = Label(text='Abdoulaye Leye')

# Render glyph
p.hbar(
    y = 'Pays',
    right='Buts',
    left=0,
    height=0.4,
    color='orange',
    fill_alpha=0.9,
    fill_color=factor_cmap(
        'Pays',
        palette=Blues8,
        factors=car_list
    ),
    source = source,
    legend_field='Joueurs'
)

# Add Legend
p.legend.orientation='vertical'
p.legend.location='top_right'
p.legend.label_text_font_size='10px'
p.title.align='center'
p.title.text_color='green'
p.title.text_font_size='100xp'
p.title.background_fill_color='#f9fd00'

# Add Tooltips
hover = HoverTool()
hover.tooltips = """
  <div>
    <h3>@Pays</h3>
    <div></strong><h3>@Joueurs</h3></div>
    <div><strong>Goals Scored: </strong>@Buts</div>
    <div><img src="@Images" alt="" width="200"/></div>
  </div>
"""
p.add_tools(hover)
#p.add_layout(citation)

# Show results

# show(p)

save(p)

# Print out div and scripts
# script, div = components(p)
# print(div)
# print(script)
 