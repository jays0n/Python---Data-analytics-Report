###############################################################################################################################################################
#
# Módulo de Classe: ENG Classe Charts (gráficos)                 Data de Criação: 03/06/2022
#
# Objetivo: Representação de uma série de valores através de um Gráfico
#
# Ultimas alterações: Criação
#
# Data da ultima alteração: 03/06/2022
#
# Desenvolvedor: Francisco J. E. de Sousa
#
# Contato: e-mail: francisco.sousa1993@outlook.com      tel: (21) 96965-6759
#
###############################################################################################################################################################

# Imports:

import matplotlib as mp
from matplotlib import pyplot as plt
from EngConstants import *

# Class #1:

class EngClsCharts(object):
    def __init__(self,title_shart=None,x_points=None,y_points=None,point_marker=ENG_MARKER_POINT,line_color=ENG_COLOR_RED,line_style=ENG_LINESTYLE_SOLID,marker_size=0,
                 marker_edge_color=ENG_COLOR_RED,marker_face_color=ENG_COLOR_RED,line_width=0.8,x_title=None,y_title=None,title_font=None,axis_font=None,title_location=ENG_LOCATION_CENTER,
                 grid_style=ENG_GRID_NONE,chart_labels=None,show_legend=False):
        self.title=title_shart
        self.xPoints=x_points
        self.yPoints=y_points
        self.marker=point_marker
        self.lineColor=line_color
        self.lineStyle=line_style
        self.markerSize=marker_size
        self.markerEdgeColor=marker_edge_color
        self.markerFaceColor=marker_face_color
        self.lineWidth=line_width
        self.xTitle=x_title
        self.yTitle=y_title
        self.titleFont=title_font
        self.axisFont=axis_font
        self.titleLocation=title_location
        self.grid=grid_style
        self.labels=chart_labels
        if show_legend==True:
            plt.legend()
        plt.xlabel(self.xTitle,self.axisFont)
        plt.ylabel(self.yTitle,self.axisFont)
        plt.title(self.title,self.titleFont,self.titleLocation)
        if not self.grid==ENG_GRID_NONE:
            plt.grid(axis=self.grid)

    def PlotLine(self):        
        plt.plot(self.xPoints,self.yPoints,marker=self.marker,ms=self.markerSize,mec=self.markerEdgeColor,mfc=self.markerFaceColor,ls=self.lineStyle,color=self.lineColor,linewidth=self.lineWidth)
        plt.show()

    def PlotScatter(self):
        plt.scatter(self.xPoints,self.yPoints,c=self.lineColor)
        plt.show()

    def PlotBarsVertical(self):
        plt.bar(self.xPoints,self.yPoints,color=self.lineColor,width=self.lineWidth)
        plt.show()

    def PlotBarsHorizontal(self):
        plt.bar(self.xPoints,self.yPoints,color=self.lineColor,height=self.lineWidth)
        plt.show()

    def PlotHistogram(self):
        plt.hist(self.xPoints,color=self.lineColor)
        plt.show()

    def PlotPizza(self):
        if self.lineColor!=ENG_COLOR_RED:
            plt.pie(self.xPoints,colors=self.lineColor,labels=self.labels)
        else:
            plt.pie(self.xPoints,labels=self.labels)
        plt.show()




