#!/usr/bin/python
import sys
import os
sys.path.append('ENTER folder location for pyosm.py and geocoder.py here. e.g. /home/peter/osmnodes/lib/ or in Windows...C:\\osmnodes\\lib')
import pyosm
import re
osm = pyosm.OSMXMLFile('ENTER location of your .osm data file here. e.g. /home/peter/osmnodes/new-york-small.osm, or in Windows...C:\\osmnodes\\new-york-small.osm')

'''Geocodes a user entered address and returns a node for processing by osmpalnodesgraph.py
or by osmpalnodesbasic.py. Geocoder will match for query in the following priority: 1. house number and street name '''
'''2. zip code/postal code and city  3. Last option is matching for site name'''

'''Checks to see if the query string entered by user matches valid house number and street in the .osm file'''
'''It returns the first house number and street node that matches the user's query string'''
def check_house_number_and_street(queryString):
    for Nid in osm.nodes:
        checkHouseTag = re.search(('addr:housenumber'),str(osm.nodes[Nid].tags).lower())
        houseTagContents = re.search('addr:housenumber\': u\'(.*?)\'', str(osm.nodes[Nid].tags).lower())
        if houseTagContents:
            houseQuery = re.search(str(houseTagContents.group(1)), queryString)
            if checkHouseTag and houseTagContents and houseQuery:
                checkStreetTag = re.search(('addr:street'),str(osm.nodes[Nid].tags).lower())
                streetTagContents = re.search('addr:street\': u\'(.*?)\'', str(osm.nodes[Nid].tags).lower())
                if streetTagContents:
                    streetQuery = re.search(str(streetTagContents.group(1)), queryString)
                    if checkStreetTag and streetTagContents and streetQuery:
                        #return osm.nodes[Nid]['id']
                        return osm.nodes[Nid]['id']


'''Checks to see if the query string entered by user matches a valid zip code/postal code city name in the .osm file'''
'''It returns the first zip code/postal code and city combination that matches the user's query string'''
def check_postcode_and_city(queryString):
    for Nid in osm.nodes:
        checkPostcodeTag = re.search(('addr:postcode'),str(osm.nodes[Nid].tags).lower())
        postcodeTagContents = re.search('addr:postcode\': u\'(.*?)\'', str(osm.nodes[Nid].tags).lower())
        if postcodeTagContents:
            postcodeQuery = re.search(str(postcodeTagContents.group(1)), queryString)
            if checkPostcodeTag and postcodeTagContents and postcodeQuery:
                checkCityTag = re.search(('addr:city'),str(osm.nodes[Nid].tags).lower())
                cityTagContents = re.search('addr:city\': u\'(.*?)\'', str(osm.nodes[Nid].tags).lower())
                if cityTagContents:
                    streetQuery = re.search(str(cityTagContents.group(1)), queryString)
                    if checkCityTag and cityTagContents and streetQuery:
                        #return osm.nodes[Nid]['id']
                        return osm.nodes[Nid]['id']

'''Finds a site name that is in any tag in .osm file and has more than one word, e.g. Union Squre'''
def check_site_name(queryString):
    for Nid in osm.nodes:
        checkSiteName = re.search((queryString.lower()),str(osm.nodes[Nid].tags).lower())
        if checkSiteName:
            return osm.nodes[Nid]['id']

'''Takes string input and returns node number '''
'''Geocoder will match for query in the following priority: 1. house number and street name '''
'''2. zip code/postal code and city  3. Last option is matching for site name'''
'''geocoder will only run if there is more than one word entered in the query. '''
def geocode_node(queryString):
    try:
        if ' ' in queryString:  #if query string has space then do geocoding
            node = check_house_number_and_street(queryString)
            if node is None:
                node = check_postcode_and_city(queryString)
                if node is None:
                    node = check_site_name(queryString)
        else:
        #just match one word against first result in .osm file
            for Nid in osm.nodes:
                match = re.search((queryString.lower()+'?'), str(osm.nodes[Nid].tags).lower())
                if match:
                    node = osm.nodes[Nid]['id']
        return node
    except:
        e = sys.exc_info()[0]
        l = sys.exc_traceback.tb_lineno
        print 'The following error ocurred: ', e, l
