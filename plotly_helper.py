# Utility functions to make plotly figures look like matplotlib
# and use Matlab-style plotting commands
#
# import with import plotly_helper as ph
# and plot with ph.plot(fig,x=x,y=y)

from plotly.subplots import make_subplots

import plotly.graph_objs as go
import plotly.io as pio
pio.renderers.default='browser'

def matplotlibstyle(fig):
    #copied and adjusted from:
    #https://medium.com/swlh/formatting-a-plotly-figure-with-matplotlib-style-fa56ddd97539

    # choose the figure font
    font_dict=dict(family='Arial',
               size=16,
               color='black'
               )
    # general figure formatting
    fig.update_layout(font=font_dict,  # font formatting
                  plot_bgcolor='white',  # background color
                  width=800,  # figure width
                  height=400,  # figure height
                  margin=dict(r=0,t=90,b=10)  # remove white space 
                  )
    
    # x and y-axis formatting
    fig.update_yaxes(
                 showline=True,  # add line at x=0
                 linecolor='black',  # line color
                 linewidth=2.4, # line size
                 ticks='inside',  # ticks outside axis
                 tickfont=font_dict, # tick label font
                 mirror='allticks',  # add ticks to top/right axes
                 tickwidth=2.4,  # tick width
                 tickcolor='black',  # tick color
                 title_standoff=0,
                 #tickformat='.1r',
                 )
    fig.update_xaxes(
                 showline=True,
                 showticklabels=True,
                 linecolor='black',
                 linewidth=2.4,
                 ticks='inside',
                 tickfont=font_dict,
                 mirror='allticks',
                 tickwidth=2.4,
                 tickcolor='black',
                 title_standoff=10,
                 #tickformat='.1r',
                 )
    fig.layout.legend.orientation='h'
    
    ##This needs adjustment if there are many curves plotted
    fig.update_layout(legend_xanchor='center')
    fig.update_layout(legend_x=0.5)
    fig.update_layout(legend_y=1.2)
    fig.update_layout(title_y=0.98)
    
    fig.update_traces(hoverlabel=dict(namelength=-1))
    
    return fig


def figure(params=None, title=None):
    fig=go.Figure()
    fig.update_layout(title_text=title)
    return f

def subplot(rows=1, cols=1,titles=None):
    fig = make_subplots(rows, cols,subplot_titles=titles)
    return fig

def plot_scatter(fig=None,x=[],y=[],name=None,row=None,col=None,color=None,size=None):
    fig=plot_both('markers',fig,x,y,name,row,col,color,size)
    return fig

def plot_line(fig=None,x=[],y=[],name=None,row=None,col=None,color=None):
    fig=plot_both('lines',fig,x,y,name,row,col,color,0)
    return fig

def plot_dash(fig=None,x=[],y=[],name=None,row=None,col=None,color=None):
    fig=plot_both('dash',fig,x,y,name,row,col,color,0)
    return fig

def plot_line_markers(fig=None,x=[],y=[],name=None,row=None,col=None,color=None,size=None):
    fig=plot_both('lines+markers',fig,x,y,name,row,col,color,size)
    return fig

def plot_both(mode,fig,x,y,name,row,col,color,size):

    if fig == None:
        fig=figure()
    if mode=='dash':
        fig.add_trace(go.Scatter(x=x,y=y,mode='lines',name=name,line=dict(dash='dash',color=color)),row=row,col=col)
    elif mode=='markers':
        fig.add_trace(go.Scatter(x=x,y=y,mode='markers',name=name,marker=dict(color=color,size=size)),row=row,col=col)
    elif mode=='lines':
        fig.add_trace(go.Scatter(x=x,y=y,mode='lines',name=name,line=dict(color=color)),row=row,col=col)
    elif mode=='lines+markers':
        fig.add_trace(go.Scatter(x=x,y=y,mode='lines+markers',name=name,
            line=dict(color=color),marker=dict(color=color,size=size)),row=row,col=col)

         
    return fig

def xlim(fig,limits,row=None,col=None):
    fig.update_xaxes(range=limits,row=row,col=col)
    return fig

def ylim(fig,limits,row=None,col=None):
    fig.update_yaxes(range=limits,row=row,col=col)
    return fig

def xlabel(fig,title,row=None,col=None):
    fig.update_xaxes(title=title,row=row,col=col)
    return fig

def ylabel(fig,title,row=None,col=None):
    fig.update_yaxes(title=title,row=row,col=col)
    return

def title(fig,title,row=None,col=None):
    fig.update_layout(title_text=title)
    return fig

def legend(fig,legs=None,title=None):
    if legs is not None:
        for i in range(len(legs)):
            fig.data[i].name=legs[i]
    fig.layout.legend.title.text=title

    return fig

def set_figsize(fig,width=None,height=None):
    fig.update_layout(width=width,  
                      height=height,  
                  )

def contour():
    #TODO
    pass

    return

def contourf():
    #TODO
    pass

    return

### aliases
plot = plot_line

