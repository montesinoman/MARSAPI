###############################################################################
# DEPENDENCIES
###############################################################################

import request
import json
import geojson

###############################################################################
# CONSTANTS
###############################################################################

###############################################################################
# FUNCTIONS
###############################################################################

def list_sectors():
    ''' Lists all the sectors
    :returns: DataFrame. Sector names.
    '''
    # Get the list
    sectors = request._request(request.URLIB.PLUMESECTOR)
    # Companies as data frame
    sectors = request._json_response_to_df(sectors)
    # Rename the column
    sectors.columns = ['Sectors']
    # Return the list
    return sectors

def list_satellites():
    ''' Lists all the satellites
    :returns: DataFrame. Satellite names.
    '''
    # Get the list
    satellites = request._request(request.URLIB.PLUMESAT)
    # Companies as data frame
    satellites = request._json_response_to_df(satellites)
    # Rename the column
    satellites.columns = ['Satellites']
    # Return the list
    return satellites

def list_sources():
    ''' Lists all the sources
    :returns: dict. Source list.
    '''
    # Get the list
    sources = request._request(request.URLIB.PLUMESOURCE)
    # Companies as data frame
    sources = request._json_response_to_df(sources)
    # Return the list
    return sources

def list_imagecoord_asgeojson():
    ''' Lists all the sources
    :returns: dict. Source list.
    '''
    # Get the list
    imgcoord = request._request(request.URLIB.PLUMEIMGCOORD)
    # Companies as data frame
    imgcoord = geojson.FeatureCollection([json.loads(imgcoord)])
    # Return the list
    return imgcoord

def list_plumes_asgeojson():
    ''' Lists all the sources
    :returns: dict. Source list.
    '''
    # Get the list
    plumes = request._request(request.URLIB.PLUMEGEOJSON)
    # Companies as data frame
    plumes = geojson.FeatureCollection([json.loads(plumes)])
    # Return the list
    return plumes

def list_centroids_asgeojson():
    ''' Lists all the sources
    :returns: dict. Source list.
    '''
    # Get the list
    centroids = request._request(request.URLIB.PLUMECENTROID)
    # Companies as data frame
    centroids = geojson.FeatureCollection([json.loads(centroids)])
    # Return the list
    return centroids

