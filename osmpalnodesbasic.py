#!/usr/bin/python
# Program created by Peter Chin, May, 2014. peter.chin@redcross.ca, Open Source license pending
import sys
import os
sys.path.append('C:\\osmcleanup\\lib')
import pyosm
from geocoder import geocode_node
osm = pyosm.OSMXMLFile('c:\\osmcleanup\\new-york-small.osm')
import re

def distance_nodes(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
	
def nearest_node_tagged(nodeID, qry):
    try:
        #arbitrarily large starting distance for comparison
        nearestDist = 100000000
        for node in osm.nodes:
            match = re.search('\''+qry+'(.*)', str(osm.nodes[node].tags))
            newDist = distance_nodes(osm.nodes[nodeID]['lon'], osm.nodes[nodeID]['lat'], osm.nodes[node]['lon'], osm.nodes[node]['lat'])
            if match and newDist < nearestDist and node != nodeID:
                nearestDist = newDist
                nearestNode = node
                nearestTag = match.group(1)
        print '\n Your starting node is http://www.openstreetmap.org/node/'+str(nodeID)
        print '\n Nearest tagged node for your query is http://www.openstreetmap.org/node/'+str(nearestNode)
        print '\n Nearest node\'s tagged info is:'+str(nearestTag)
    except:
        e = sys.exc_info()[0]
        l = sys.exc_traceback.tb_lineno
        print 'The following error ocurred: ', e, l

def farthest_node_tagged(nodeID, qry):
    try:
        #arbitrarily small starting distance for comparison
        farthestDist = 0
        for node in osm.nodes:
            match = re.search('\''+qry+'(.*)', str(osm.nodes[node].tags))
            newDist = distance_nodes(osm.nodes[nodeID]['lon'], osm.nodes[nodeID]['lat'], osm.nodes[node]['lon'], osm.nodes[node]['lat'])
            if match and newDist > farthestDist and node != nodeID:
                farthestDist = newDist
                farthestNode = node
                farthestTag = match.group(1)
        print '\n Your starting node is http://www.openstreetmap.org/node/'+str(nodeID)
        print '\n Farthest Node for your query is http://www.openstreetmap.org/node/'+str(farthestNode)
        print '\n Farthest node\'s tagged info: '+str(farthestTag)
    except:
        e = sys.exc_info()[0]
        l = sys.exc_traceback.tb_lineno
        print 'The following error ocurred: ', e, l

def farthest_node(nodeID):
    farthestDist = 0
    try:
        for node in osm.nodes:
            newDist = distance_nodes(osm.nodes[nodeID]['lon'], osm.nodes[nodeID]['lat'], osm.nodes[node]['lon'], osm.nodes[node]['lat'])
            if newDist > farthestDist and node != nodeID:
                farthestDist = newDist
                farthestNode = node
        print '\n Your starting node is http://www.openstreetmap.org/node/'+str(nodeID)
        print '\n Farthest Node is http://www.openstreetmap.org/node/'+str(farthestNode)
    except:
        e = sys.exc_info()[0]
        l = sys.exc_traceback.tb_lineno
        print 'The following error ocurred: ', e, l

def nearest_node(nodeID):
    # Start with arbitrarily large nearestDist and get smaller and smaller distance
    nearestDist = 100000000
    try:
        for node in osm.nodes:
            newDist = distance_nodes(osm.nodes[nodeID]['lon'], osm.nodes[nodeID]['lat'], osm.nodes[node]['lon'], osm.nodes[node]['lat'])
            if newDist < nearestDist and node != nodeID:
                nearestDist = newDist
                nearestNode = node
        print '\n Your starting node is http://www.openstreetmap.org/node/'+str(nodeID)
        print '\n Nearest Node is http://www.openstreetmap.org/node/'+str(nearestNode)
    except:
        e = sys.exc_info()[0]
        l = sys.exc_traceback.tb_lineno
        print 'The following error ocurred: ', e, l

#Allow user to choose the function in command line
# e.g. python osmpalnodesgraph.py nearest_node_tagged 26301254 $'amenity\': u\'cafe'
if __name__ == "__main__":
    #If user input is not a digit, run geocoder function
    if not sys.argv[2].isdigit():
        node = geocode_node(sys.argv[2])
    #Take user entered node number and run one of the functions below
    else:
        node = int(sys.argv[2])
    if sys.argv[1] == 'nearest_node_tagged':
        nearest_node_tagged(node, sys.argv[3])
    elif sys.argv[1] == 'farthest_node_tagged':
        farthest_node_tagged(node, sys.argv[3])
    elif sys.argv[1] == 'nearest_node':
        nearest_node(node)
    elif sys.argv[1] == 'farthest_node':
        farthest_node(node)
