from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(ingredients)

        graph = defaultdict(list)
        for i in range(n):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
        
        recipes_to_index = {}
        for i in range(n):
            recipes_to_index[recipes[i]] = i

        in_degree = [0] * n
        for node in graph:
            for next_node in graph[node]:
                in_degree[recipes_to_index[next_node]] += 1

        possible_recipes = []
        queue = deque(supplies)
        while queue:
            node = queue.popleft()
            for next_node in graph[node]:
                in_degree[recipes_to_index[next_node]] -= 1
                if in_degree[recipes_to_index[next_node]] == 0:
                    possible_recipes.append(next_node)
                    queue.append(next_node)
        return possible_recipes

