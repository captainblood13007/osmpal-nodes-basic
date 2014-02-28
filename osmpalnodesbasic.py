#!/usr/bin/python
# Tool to read OpenStreetMap .osm files and find nearest and farthest nodes. 
import sys
import os
PYOSM_DIR = os.path.join(os.path.dirname(__file__), ' INSERT THE PATH OF YOUR PYOSM FILE, e.g. /home/peter/osmpal/lib/')
sys.path.append(PYOSM_DIR)
import pyosm
osm = pyosm.OSMXMLFile('INSERT THE PAHT OF YOUR OSM FILE HERE, e.g. /home/peter/osmpal/new-york.osm')

def dist(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5


def farthest_node(nodeID):
    #Need to loop through to get coordinates
    for nid in osm.nodes:
        if osm.nodes[nid]['id'] == nodeID:
            X1 = osm.nodes[nid]['lon']
            Y1 = osm.nodes[nid]['lat']
            originalNode = nid
            print 'X1:', X1
            print '\n Y1: ', Y1
            print '\n Your original node number is: ', originalNode
    #Arbitrarily small number that variable newDist will be bigger than in comparison below
    farthestDist = 0.000000000000000000000001
    try:
        for Nid in osm.nodes:
            newDist = dist(X1, Y1, osm.nodes[Nid]['lon'], osm.nodes[Nid]['lat'])
            if newDist > farthestDist and Nid is not originalNode:
                farthestDist = newDist
                farthestNode = Nid
        if originalNode is not None:
            print '\n Farthest Node is no: ', farthestNode
            print '\n Farthest Distance calculated from your original node is : ', farthestDist
            XFAR = osm.nodes[farthestNode]['lon']
            YFAR = osm.nodes[farthestNode]['lat']
    except:
        e = sys.exc_info()[0]
        print 'The following error ocurred: ', e

def nearest_node(nodeID):
    #Need to loop through to get coordinates
    for nid in osm.nodes:
        if osm.nodes[nid]['id'] == nodeID:
            X1 = osm.nodes[nid]['lon']
            Y1 = osm.nodes[nid]['lat']
            originalNode = nid
            print 'X1:', X1
            print '\n Y1: ', Y1
            print '\n Your original node (starting node) number is :', originalNode
    # Start with arbitrarily large nearestDist and get smaller and smaller distance
    nearestDist = 100
    try:
        for Nid in osm.nodes:
            newDist = dist(X1, Y1, osm.nodes[Nid]['lon'], osm.nodes[Nid]['lat'])
            if newDist < nearestDist and Nid is not originalNode:
                nearestDist = newDist
                nearestNode = Nid
        if originalNode is not None:
            print '\n Nearest Node is no: ', nearestNode
            print '\n Nearest Distance calculated: ', nearestDist
            XNEAR = osm.nodes[nearestNode]['lon']
            YNEAR = osm.nodes[nearestNode]['lat']
    except:
        e = sys.exc_info()[0]
        print 'The following error ocurred: ', e

