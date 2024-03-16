def can_make_potion(graph, ingredients, X, Y, S, visited):
    if visited[S]:
        return False
    visited[S] = True
    if S == 1:
        return True
    for ingredient in graph[S]:
        required_ingredient = ingredients[ingredient]
        new_X = X - required_ingredient[0]
        new_Y = Y - required_ingredient[1]
        if new_X >= 0 and new_Y >= 0 and can_make_potion(graph, ingredients, new_X, new_Y, ingredient, visited):
            return True
    return False

def main():
    N = int(input())
    graph = {}
    ingredients = {}
    for i in range(N - 2):
        parts = list(map(int, input().split()))
        K = parts[0]
        ingredients[i + 3] = sum([ingredients.get(parts[j], []) for j in range(1, K + 1)], [])
        for j in range(1, K + 1):
            if parts[j] not in graph:
                graph[parts[j]] = []
            graph[parts[j]].append(i + 3)

    Q = int(input())
    for _ in range(Q):
        X, Y, S = map(int, input().split())
        visited = [False] * (N + 1)
        print(1 if can_make_potion(graph, ingredients, X, Y, S, visited) else 0)

if __name__ == "__main__":
    main()
