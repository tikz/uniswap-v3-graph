import graph
import os
import datetime as dt
import json

# Q64.96 https://xord.com/publications/uniswap-v3-power-to-liquidity-providers/

pools = graph.query(graph.TOP_POOLS_QUERY)

for pool in pools["data"]["pools"]:
    contract = pool["id"]
    token0, token1 = pool["token0"]["symbol"], pool["token1"]["symbol"]

    try:
        pool_query = graph.query(graph.POOL_QUERY % contract)
    except:
        continue

    date_str = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(contract, token0, token1)

    path = f"data/{token0}-{token1}/"
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

    date_str = dt.datetime.now().strftime("%Y-%m-%d-%H-%M")
    with open(path + date_str + ".json", "w") as f:
        f.write(json.dumps(pool_query))
