###############################################################################
# DEPENDENCIES
###############################################################################

import json
from ..request import request

###############################################################################
# CONSTANTS
###############################################################################

###############################################################################
# FUNCTIONS
###############################################################################

def list_all():
    ''' Lists all the OGMP companies
    :returns: DataFrame. Company IDs and names.
    '''
    # Get the list
    companies = request._request(request.URLIB.COMPANY)
    # Companies as data frame
    companies = request._json_response_to_df(companies)
    # Return the list
    return companies

def find_id(companyname):
    ''' Tries to find the company ID
    :param companyname: str. Name of the company.
    :returns: str. Company ID.
    '''
    # List all companies
    all_companies = list_all()
    # Find the company name
    this_company = all_companies[
        all_companies['name'].str.contains(companyname, case=False, na=False)]
    # Return the ID
    return this_company['idCompany'].iloc[0]

def get_info(companyid, year):
    ''' Get information of a company for a given year
    :param companyid: str. IMEO company ID.
    :param year: int. Information on that year.
    :returns: dict. Company information on methane emissions.
    '''
    # Build URL
    this_url = request.URLIB.COMPANYFACT % (companyid, str(year))
    # Request the information
    company_facts = request._request(this_url)
    # Turn into a data frame
    company_facts = json.loads(company_facts)
    # Return
    return company_facts