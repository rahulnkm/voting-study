import streamlit as st
import requests
import json

'''
For all the spaces on Snapshot,
Review all the proposals in each Space,
Collect the Ethereum addresses of each of the voters,
Collect a list of all Ethereum addresses on Snapshot
'''

def voters_list():
    graphql_query = """
    query {
        votes (
            first: 20
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
    url = "https://hub.snapshot.org/graphql"
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    }
    payload = json.dumps({"query": graphql_query})
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["votes"]
    else:
        return f"Error: {response.status_code} {response.text}"

'''
Search for Farcaster users that have same Ethereum address
Collect the associated usernames for the addresses
Collect a list of Farcaster users that have been active on Snapshot
'''

def check_farcaster_profile(id):
    api_endpoint = "https://searchcaster.xyz/api/profiles"
    params = {
        "connected_address": id
    }
    response = requests.get(api_endpoint, params=params)
    if response.status_code == 200:
        profiles = response.json()
        if profiles:
            return "Farcaster profile found:", profiles
        else:
            return "No Farcaster profile associated with this Ethereum address."
    else:
        return f"Error: {response.status_code}"

def users():
    voters = snapshot_voters_list()
    verified = []
    for voter in voters:
        id = voter["voter"]
        if check_farcaster_profile(id) != "No Farcaster profile associated with this Ethereum address.":
            verified.append(id)
    return verified


snapshot_farcaster = users()
voter = "0x45CcFE16bC2AC8CEF704a7236fEf3E5f4222dE15" #snapshot_farcaster[0]

'''
Rank the Farcaster and Snapshot users by their activity on Farcaster and Snapshot
- How many posts have they made? Over 10?
- How many proposals have they voted on? Over 10?

Collect social media posts of active Farcaster and Snapshot users
Collect votes of active Farcaster and Snapshot users
'''


def get_farcaster_posts(id):
    # Farcaster API endpoint for profiles
    api_endpoint = "https://searchcaster.xyz/api/search"

    # Parameters for the API call
    params = {
        "username": id
    }

    # Make the GET request
    response = requests.get(api_endpoint, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        profiles = response.json()
        return profiles



# st.write(snapshot_voters_list())
st.write(check_farcaster_profile(voter))