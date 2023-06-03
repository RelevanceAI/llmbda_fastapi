import os

RELEVANCE_API_KEY = os.getenv("RELEVANCE_API_KEY")
RELEVANCE_REGION = os.getenv("RELEVANCE_REGION")
RELEVANCE_PROJECT = os.getenv("RELEVANCE_PROJECT")

if not RELEVANCE_API_KEY:
    raise KeyError(
        "'RELEVANCE_API_KEY' needs to be set as an environmental variable. This token can be found on https://chain.relevanceai.com/login/sdk"
    )
if not RELEVANCE_REGION:
    raise KeyError(
        "'RELEVANCE_REGION' needs to be set as an environmental variable. This region can be found on https://chain.relevanceai.com/login/sdk"
    )
if not RELEVANCE_PROJECT:
    raise KeyError(
        "'RELEVANCE_PROJECT' needs to be set as an environmental variable. This project can be found on https://chain.relevanceai.com/login/sdk"
    )
