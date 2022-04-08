from calendar import c
from graph import Graph


def business_trip(graph, cityname_list):
    cost = 0
    next = 0
    for city in cityname_list:
        next += 1
        neighbors = graph.get_neighbor(city)
        if next > len(cityname_list) - 1:
            break
        if cityname_list[next] in neighbors:
            target = neighbors.index(cityname_list[next])
            cost += neighbors[target + 1]
        else:
            return None
    return cost


if __name__ == "__main__":

    graph = Graph()
    graph.add_node("SEA")
    graph.add_node("SLC")
    graph.add_node("PHX")
    graph.add_node("KC")
    graph.add_node("DC")
    graph.add_node("ATL")

    graph.add_edge("SEA", "SLC", 82)
    graph.add_edge("SEA", "KC", 150)
    graph.add_edge("SLC", "PHX", 37)
    graph.add_edge("PHX", "ATL", 250)
    graph.add_edge("SLC", "ATL", 26)
    graph.add_edge("SLC", "KC", 99)
    graph.add_edge("SLC", "DC", 105)
    graph.add_edge("ATL", "DC", 73)
    graph.add_edge("KC", "DC", 42)

    print(business_trip(graph, ["SEA", "SLC", "ATL"]))
    print(business_trip(graph, ["SLC", "KC", "PHX"]))
