from duckduckgo_search import DDGS

results = DDGS().text("tiger news", max_results=1)
print(results[0]['href'])
for i in range( len(results)):
    print(i)
    print(results[i]['href'])
