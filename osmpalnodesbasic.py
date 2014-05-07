#!/usr/bin/python
import sys
import os
sys.path.append('ENTER folder location for pyosm.py and geocoder.py here. e.g. /home/peter/osmnodes/lib/ or in Windows... C:\\osmnodes\\lib')
import pyosm
from geocoder import geocode_node
osm = pyosm.OSMXMLFile('ENTER location of your .osm data file here. e.g. /home/peter/osmnodes/new-york-small.osm, or in Windows... C:\\osmnodes\\new-york-small.osm')
import re

def dist(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def nearest_node_tagged(nodeID, qry):
    try:
        for Nid in osm.nodes:
            if osm.nodes[Nid]['id'] == nodeID:
                X1 = osm.nodes[Nid]['lon']
                Y1 = osm.nodes[Nid]['lat']
                originalNode = Nid
        #arbitrarily large starting distance for comparison
        nearestDist = 100
        for Nid in osm.nodes:
            match = re.search('\''+qry+'(.*)', str(osm.nodes[Nid].tags))
            newDist = dist(X1, Y1, osm.nodes[Nid]['lon'], osm.nodes[Nid]['lat'])
            if match and newDist < nearestDist and Nid is not originalNode:
                nearestDist = newDist
                nearestNode = Nid
                nearestTag = match.group(1)
        print 'Nearest Distance (not to scale) is: ', nearestDist
        print '\n Your starting node is http://www.openstreetmap.org/node/'+str(originalNode)
        print '\n Nearest tagged node for your query is http://www.openstreetmap.org/node/'+str(nearestNode)
        print '\n Nearest node\'s tagged info is:', nearestTag
    except:
        e = sys.exc_info()[0]
        l = sys.exc_traceback.tb_lineno
        print 'The following error ocurred: ', e, l

def farthest_node_tagged(nodeID, qry):
    try:
        for Nid in osm.nodes:
            if osm.nodes[Nid]['id'] == nodeID:
                X1 = osm.nodes[Nid]['lon']
                Y1 = osm.nodes[Nid]['lat']
                originalNode = Nid
        #arbitrarily small starting distance for comparison
        farthestDist = 0
        for Nid in osm.nodes:
            match = re.search('\''+qry+'(.*)', str(osm.nodes[Nid].tags))
            newDist = dist(X1, Y1, osm.nodes[Nid]['lon'], osm.nodes[Nid]['lat'])
            if match and newDist > farthestDist and Nid is not originalNode:
                farthestDist = newDist
                farthestNode = Nid
                farthestTag = match.group(1)
                XFAR = osm.nodes[farthestNode]['lon']
                YFAR = osm.nodes[farthestNode]['lat']
        print '\n Your starting node is http://www.openstreetmap.org/node/'+str(originalNode)        
        print '\n Farthest Node for your query is http://www.openstreetmap.org/node/'+str(farthestNode)
        print '\n Farthest node\'s tagged info: ', farthestTag
    except:
        e = sys.exc_info()[0]
        l = sys.exc_traceback.tb_lineno
        print 'The following error ocurred: ', e, l

def farthest_node(nodeID):
    #First loop through to get coordinates
    for nid in osm.nodes:
        if osm.nodes[nid]['id'] == nodeID:
            X1 = osm.nodes[nid]['lon']
            Y1 = osm.nodes[nid]['lat']
            originalNode = nid
            print '\n Your original node number is: ', originalNode
    #Arbitrarily small number that variable newDist will be bigger than in comparison below
    farthestDist = 0
    #Second loop through to calculate distance
    try:
        for Nid in osm.nodes:
            newDist = dist(X1, Y1, osm.nodes[Nid]['lon'], osm.nodes[Nid]['lat'])
            if newDist > farthestDist and Nid is not originalNode:
                farthestDist = newDist
                farthestNode = Nid
        if originalNode is not None:
            print '\n Your starting node is http://www.openstreetmap.org/node/'+str(originalNode)
            print '\n Farthest Node is http://www.openstreetmap.org/node/'+str(farthestNode)
            print '\n Farthest Distance calculated (not to scale) from your original node is : ', farthestDist
            XFAR = osm.nodes[farthestNode]['lon']
            YFAR = osm.nodes[farthestNode]['lat']
    except:
        e = sys.exc_info()[0]
        l = sys.exc_traceback.tb_lineno
        print 'The following error ocurred: ', e, l

def nearest_node(nodeID):
    #Need to loop through to get coordinates
    for nid in osm.nodes:
        if osm.nodes[nid]['id'] == nodeID:
            X1 = osm.nodes[nid]['lon']
            Y1 = osm.nodes[nid]['lat']
            originalNode = nid
            print '\n Your original node (starting node) number is :', originalNode
    # Start with arbitrarily large nearestDist and get smaller and smaller distance
    nearestDist = 10000
    try:
        for Nid in osm.nodes:
            newDist = dist(X1, Y1, osm.nodes[Nid]['lon'], osm.nodes[Nid]['lat'])
            if newDist < nearestDist and Nid is not originalNode:
                nearestDist = newDist
                nearestNode = Nid
        if originalNode is not None:
            print '\n Your starting node is http://www.openstreetmap.org/node/'+str(originalNode)
            print '\n Nearest Node is http://www.openstreetmap.org/node/'+str(nearestNode)
            print '\n Nearest Distance calculated (not to scale): ', nearestDist
            XNEAR = osm.nodes[nearestNode]['lon']
            YNEAR = osm.nodes[nearestNode]['lat']
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
