###############################################################################
# DEPENDENCIES
###############################################################################

import subprocess
import json
import pandas

###############################################################################
# CONSTANTS
###############################################################################

class URLIB:
    # HEALTH block
    HEALTH = 'https://methanedata.unep.org/api/healthcheck'
    # COUNTRY block
    COUNTRIES = 'https://methanedata.unep.org/api/countries'
    COUNTRYSTATS = 'https://methanedata.unep.org/api/countries/%s/keystats'
    COUNTRYFACTS = 'https://methanedata.unep.org/api/factsheets/country/%s/year/%s'
    # PLUME block
    PLUMES = 'https://methanedata.unep.org/api/plumes'
    PLUMEGEOJSON = 'https://methanedata.unep.org/api/plumes/geojson'
    PLUMECENTROID ='https://methanedata.unep.org/api/plumes/centroids/geojson'
    PLUMEIMGCOORD = 'https://methanedata.unep.org/api/plumes/images-coordinates'
    PLUMESAT = 'https://methanedata.unep.org/api/plumes/satellites'
    PLUMESECTOR = 'https://methanedata.unep.org/api/sector'
    PLUMESOURCE = 'https://methanedata.unep.org/api/plumes/sources'
    # COMPANY block
    COMPANY = 'https://methanedata.unep.org/api/companies'
    COMPANYFACT = 'https://methanedata.unep.org/api/factsheets/company/%s/year/%s'

###############################################################################
# FUNCTIONS
###############################################################################

def _request(url):
    ''' Sends the request and captures the response
    :param url: str. URL for the request
    :returns: str. Response
    '''
    # Send the request
    response = subprocess.run(['curl', url],
                              capture_output=True,
                              text=True)
    # Check all good
    if response.returncode == 0:
        # Get the response 
        out =  response.stdout
    # Otherwise
    else:
        # Warn
        sys.exit(f"Error: {response.returncode} with {url}")
    # Return the response
    return out

def _healthcheck():
    ''' Checks that API is running
    '''
    # Check the health of the API
    vitals = _request(URLIB.HEALTH)
    # All goo if response is ''
    ishealthy = ('MethaneData public API' == vitals)
    # Retrun
    return ishealthy

def _json_response_to_df(response):
    ''' Convert a request response to data frame
    :param response: str. Request reponse.
    '''
    # Load the JSON
    json_response = json.loads(response)
    # Coercing to DataFrame
    df_response = pandas.DataFrame(json_response)
    # Return the dataframe
    return df_response
    