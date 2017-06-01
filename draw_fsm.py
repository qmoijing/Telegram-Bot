# -*- coding: utf-8 -*-
import pygraphviz as pgv

A=pgv.AGraph(strict=False,directed=True,layout='dot')

A.add_edge(0,1,label=u'天氣')
A.add_edge(1,0,label=u'Bot回覆天氣資訊')
A.add_edge(0,2,label=u'地鐵')
A.add_edge(2,3,label=u'起始站')
A.add_edge(3,4,label=u'終點站')
A.add_edge(4,0,label=u'Bot回覆乘車資訊')
A.add_edge(0,5,label=u'匯率')
A.add_edge(5,6,label=u'韓圜金額')
A.add_edge(6,0,label=u'Bot回覆對應台幣')

A.node_attr['shape']='circle'

A.write('fsm.dot') # write to simple.dot

B=pgv.AGraph('fsm.dot') # create a new graph from file
B.layout() # layout with default (neato)
B.draw('fsm.png') # draw png
