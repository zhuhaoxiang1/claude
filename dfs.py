"""Depth-first search example using an adjacency-list graph."""


def depth_first_search(graph, start):
    """Return nodes in the order visited by depth-first search."""
    if start not in graph:
        raise ValueError(f"Start node {start!r} does not exist in the graph.")

    visited = set()
    order = []

    def visit(node):
        visited.add(node)
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }

    print("DFS order:", " -> ".join(depth_first_search(graph, "A")))


if __name__ == "__main__":
    main()
