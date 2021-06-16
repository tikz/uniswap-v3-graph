import requests


def query(q):
    request = requests.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3',
                            json={'query': q})
    if request.status_code != 200:
        raise Exception("HTTP error:", request.status_code)

    if "errors" in request.json():
        raise Exception("Query error:", request.json()["errors"][0]["message"])

    return request.json()


TOP_POOLS_QUERY = """
{
  pools(orderBy: txCount, orderDirection: desc, first: 100) {
    id
    token0 {
      symbol
    }
    token1 {
      symbol
    }
    txCount
    feeTier
  }
}
"""

POOL_QUERY = """
{
  pool(id : "%s") {
    id
    token0 {
      symbol
    }
    token1 {
      symbol
    }
    feeTier
    liquidity
    swaps (orderBy: timestamp, orderDirection: desc) {
      id
      timestamp
      amount0
      amount1
    }
    ticks (orderBy: price1, orderDirection: asc){
      price0
      price1
      liquidityNet
      liquidityGross
      tickIdx
    }
  }
}
"""
