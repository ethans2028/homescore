"""
Module containing helper functions to interact with the Seattle housing permits API
"""

from typing import Dict, List, Optional

import requests

PERMIT_API_URL = "https://data.seattle.gov/resource/76t5-zqzr.json"
ISSUED_PERMITS_STATUS = "Issued"
MAX_PAGE_SIZE = 1000


def request_permit_data(
    address: str,
    permit_type: Optional[str] = "Building",
    exclude_unissued_permits: Optional[bool] = True,
    partial_search: Optional[bool] = False,
    app_token: Optional[str] = "",
) -> List[Dict[str, str]]:
    """
    Requests permit data for a particular address.

    Params:
        - address: The street name and number of the property i.e 5102 SW PRITCHARD ST

        - exclude_unissued_permits: Excludes all permits that do not have the 'Issued' status

        - partial_search: Searches for permits that partially match the `address`

        - permit_type: The permit type by category, such as building, demolition,
                       roofing, grading, and environmentally critical areas.

        - app_token: Application token to authenticate with the Socrata API.
                     See: https://dev.socrata.com/foundry/data.seattle.gov/76t5-zqzr
                          https://dev.socrata.com/docs/app-tokens.html
    """
    params = {}
    headers = {}

    if partial_search:
        params["$where"] = f"originaladdress1 like '{address}'"
    else:
        params["originaladdress1"] = address

    if exclude_unissued_permits:
        params["statuscurrent"] = ISSUED_PERMITS_STATUS

    params["permittypemapped"] = permit_type

    if app_token:
        headers["X-App-Token"] = app_token

    resp = requests.get(PERMIT_API_URL, headers=headers, params=params)

    return resp.json()
