import streamlit as st
import requests
import json


def snapshot_voters_list():

    spaces = open("spaces.txt", "r").read()

    return spaces

    # For all spaces on Snapshot, get all voters
    # Collect Ethereum addresses for all voters

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


# snapshot_farcaster = farcaster_snapshot_list()
voter = "0x45CcFE16bC2AC8CEF704a7236fEf3E5f4222dE15" #snapshot_farcaster[0]

def check_farcaster_profile(id):

    # For all voters, check if they have a Farcaster account
    # Return all Ethereum addresses of voters with Farcaster accounts 

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

def farcaster_snapshot_list():

    # For all Ethereum addresses of voters with Farcaster accounts
    # Return all social media posts, count of social media posts, and count of votes on Snapshot
    # Rank the voters by cumulative activity

    voters = snapshot_voters_list()
    verified = []
    for voter in voters:
        id = voter["voter"]
        if check_farcaster_profile(id) != "No Farcaster profile associated with this Ethereum address.":
            verified.append(id)
    return verified

def rank_list():
    
    # Rank the Farcaster and Snapshot users by their activity on Farcaster and Snapshot
    # - How many posts have they made? Over 10?
    # - How many proposals have they voted on? Over 10?

    # Collect social media posts of active Farcaster and Snapshot users
    # Collect votes of active Farcaster and Snapshot users

    return ranked_list


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



st.write(snapshot_voters_list())
# st.write(check_farcaster_profile(voter))