def find_center(edges):
    a, b = edges[0]
    c, d = edges[1]
    return a if a == c or a == d else b
if __name__ == "__main__":
    # Example usage
    edges = [[1, 2], [2, 3], [4, 2]]
    center = find_center(edges)
    print("Center of the star graph:", center)