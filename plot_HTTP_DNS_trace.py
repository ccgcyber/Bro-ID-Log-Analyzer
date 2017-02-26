global connection
from plotly.graph_objs import *
import plotly.offline  as py
import os
import networkx as nx
from datetime import datetime as time


def plot_dns_http (connection):
    connection.DBquery.exec_("select ts,uid,uri from http")
    while connection.DBquery.next():
        print(connection.DBquery.value(0),connection.DBquery.value(1),connection.DBquery.value(2))
        # connection.DBquery.exec_("select answer from dns_answers where answer='resp_h' ")

    #
    #
    #
    # ("select orig_h from dns")
    # ("select resp_h from dns")
    # "select query from dns"
    # "select "
    # if resp_id not in dns answers:
    #     show warning with red edge possible dns injection
    # else:
    #     normal edge from source to distenation
    #
    #
