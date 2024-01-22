import streamlit as st
import requests
import json

import requests
import json

@st.cache_data
def snapshot_voters_list():
    # Read all spaces from the file
    with open("spaces.txt", "r") as file:
        spaces = file.readlines()
    # Remove any newline characters from each space
    spaces = [space.strip() for space in spaces]
    # Initialize a list to collect voters from all spaces
    all_voters = []
    for space in spaces:
        # GraphQL query with variable
        graphql_query = """
        query GetVotes($spaceId: String!) {
            votes (
                first: 1000
                skip: 0
                where: {
                    space: $spaceId
                }
                orderBy: "created",
                orderDirection: desc
            ) {
                voter
            }        
        }
        """
        url = "https://hub.snapshot.org/graphql"
        headers = {
            "Content-Type": "application/json",
            # "Authorization": "Bearer YOUR_ACCESS_TOKEN" (Uncomment and use if you have a token)
        }
        # Structuring the payload with the query and variables
        payload = {
            "query": graphql_query,
            "variables": {
                "spaceId": space
            }
        }
        response = requests.post(url, headers=headers, json=payload)  # Note: using json=payload for proper formatting
        if response.status_code == 200:
            data = response.json()
            voters = data["data"]["votes"]
            all_voters.extend(voters)
        else:
            print(f"Error fetching data for space {space}: {response.status_code} {response.text}")
    return all_voters

@st.cache_data
def remove_duplicate_voters(voters_list):
    unique_voters = []
    seen_addresses = set()

    for voter in voters_list:
        if voter["voter"] not in seen_addresses:
            unique_voters.append(voter)
            seen_addresses.add(voter["voter"])

    return unique_voters

@st.cache_data
voters = snapshot_voters_list()

@st.cache_data
unique_voters = remove_duplicate_voters(voters)

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



st.write(remove_duplicate_voters(snapshot_voters_list()))
# st.write(check_farcaster_profile(voter))