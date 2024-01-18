import streamlit as st

'''
1. Create an array of voters, social media posts, and votes
    - Find active Farcaster users that have been active on Snapshot ()
2.


For all the spaces on Snapshot,
Review all the proposals in each Space,
Collect the Ethereum addresses of each of the voters,

For all active Farcaster users,
Collect the active Farcaster user eth addresses,
Compare the voters addresses to active Farcaster eth addresses,
Collect a list of Farcaster users with 

Collect social media posts of Farcaster and Snapshot users,

Return a list of Farcaster eth addresses, the social media posts they made, and the votes they made 

'''

import requests
import json


def get_all_voters_and_ids():
    # GraphQL query
    graphql_query = """
    query {
        votes (
            first: 10
            skip: 0
            where: {
                space: "lido-snapshot.eth"
                }
                orderBy: "created",
                orderDirection: desc
                )
                {
                    id
                    voter
                    vp
                    vp_by_strategy
                    vp_state
                    created
                    proposal {
                    id
                    }
                    choice
                    space {
                    id
                }
            }
        }
    """

    # GraphQL endpoint URL
    url = "https://hub.snapshot.org/graphql"

    # Request headers
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    }

    # Request payload
    payload = json.dumps({"query": graphql_query})

    # Send the request
    response = requests.post(url, headers=headers, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Process successful response
        data = response.json()
        return data
    else:
        # Handle errors
        return f"Error: {response.status_code} {response.text}"


if st.button("test"):
    st.write(get_all_voters_and_ids())