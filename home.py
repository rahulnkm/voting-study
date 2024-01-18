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


def snapshot_voters_list():
    # GraphQL query
    graphql_query = """
    query {
        votes (
            first: 100
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
        return data["data"]["votes"]
    else:
        # Handle errors
        return f"Error: {response.status_code} {response.text}"

def farcaster_lookup(id):
    # Farcaster API endpoint for profiles
    api_endpoint = "https://searchcaster.xyz/api/profiles"

    # Parameters for the API call
    params = {
        "connected_address": id
    }

    # Make the GET request
    response = requests.get(api_endpoint, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        profiles = response.json()

        # Check if a profile is associated with the Ethereum address
        if profiles:
            return "Farcaster profile found:", profiles
        else:
            return "No Farcaster profile associated with this Ethereum address."
    else:
        # Handle errors
        return f"Error: {response.status_code}"

def farcaster_snapshot_list(address_list):

    farcaster_snapshot_list = []

    for voter_id in address_list:
        if farcaster_lookup(voter_id) != False:
            farcaster_snapshot_list.append(voter_id)
    
    return farcaster_snapshot_list

if st.button("test"):
    # st.write(snapshot_voters_list())
    st.write(farcaster_lookup())