import json
import math
from graphqlclient import GraphQLClient

client = GraphQLClient("https://data-platform.nodereal.io/graph/v1/148da1680040452aa4cf979257e760f8/projects/pancakeswap")

result = client.execute('''
query ExampleQuery($first: Int, $orderBy: Pair_orderBy, $orderDirection: OrderDirection) {
  pairs(first: $first, orderBy: $orderBy, orderDirection: $orderDirection ) {
    id
    token0 {
      id
      symbol
      decimals
    }
    token1 {
      id
      symbol
      decimals
    }
    reserve0
    reserve1
  }
}
''', variables={"first": 1000, "orderBy": "trackedReserveBNB", "orderDirection": "desc"})

json_result = json.loads(result)['data']['pairs']

pairs = []

i = 0

for pair in json_result:
    pairs.append({
        'index': i,
        'address': pair['id'],
        'token0': {
          'address': pair['token0']['id'],
          'symbol': pair['token0']['symbol'],
          'decimal': int(pair['token0']['decimals'])
         },
        'token1': {
          'address': pair['token1']['id'],
          'symbol': pair['token1']['symbol'],
          'decimal': int(pair['token1']['decimals'])
         },
        'reserve0': int(float(pair['reserve0'])),
        'reserve1': int(float(pair['reserve1']))
    })
    i += 1
    print(i)
    
    
t = open('bsc_pairs.json', 'w')

t.writelines(json.dumps(pairs))

print('done')