import streamlit as st

'''
1. Create an array of voters, social media posts, and votes
    - Find active Farcaster users that have been active on Snapshot ()
2.


For all the spaces on Snapshot,
Review all the proposals in each Space,
Collect the Ethereum addresses of each of the voters,
Collect a list of all Ethereum addresses on Snapshot

Search for Farcaster users that have same Ethereum address
Collect a list of Farcaster users that have been active on Snapshot

Rank the Farcaster and Snapshot users by their activity on Farcaster and Snapshot
- How many posts have they made? Over 10?
- How many proposals have they voted on? Over 10?

Collect social media posts of active Farcaster and Snapshot users
Collect votes of active Farcaster and Snapshot users
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
                    voter
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


def get_farcaster_from_eth_address(address_list):
    return None


if st.button("test"):
    st.write(get_all_voters_and_ids())