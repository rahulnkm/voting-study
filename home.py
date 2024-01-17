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



"""
query {
  votes (
    first: 1000
    skip: 0
    where: {
      proposal: "QmPvbwguLfcVryzBRrbY4Pb9bCtxURagdv1XjhtFLf3wHj"
    }
    orderBy: "created",
    orderDirection: desc
  ) {
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