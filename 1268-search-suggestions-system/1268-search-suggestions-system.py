from typing import *


class Node:
    key = None
    result = None
    next = dict()

    def has_result(self):
        return len(self.result) > 0

    def has_next(self):
        return self.next is not None

    def __str__(self):
        return f"key: {self.key}, result:{self.result}"

    def __init__(self, key):
        self.key = key
        self.result = set()
        self.next = {}


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str):
        products = sorted(products)
        root_node = Node(key="root")

        cur = root_node
        for index, product in enumerate(products):
            self.add_product(cur, product, index)

        cur = root_node
        result = []
        empty_flag = False
        for char in searchWord:
            if empty_flag is True or char not in cur.next:
                result.append([])
                empty_flag = True
            else:
                cur = cur.next[char]
                target_index = sorted(list(cur.result))[:3]
                result.append(list(map(lambda x: products[x], target_index)))

        return result

    def add_product(self, root_node: Node, product: str, index: int):

        cur = root_node
        for char in product:
            if char not in cur.next:
                new_node = Node(key=char)
                cur.next[char] = new_node
            cur = cur.next[char]
            cur.result.add(index)