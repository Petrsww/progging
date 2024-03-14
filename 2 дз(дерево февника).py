class FenwickTree:
    def __init__(self, arr):
        self.tree = [0] * (len(arr) + 1)
        self.arr = arr
        self.build()

    def build(self):
        for i in range(len(self.arr)):
            self.update(i, self.arr[i])

    def lowbit(self, x):
        return x & -x

    def update(self, index, value):
        while index < len(self.tree):
            self.tree[index] += value
            index += self.lowbit(index)

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res


arr = [2, 1, 5, 3]
fenwick_tree = FenwickTree(arr)


result = fenwick_tree.query(3)

print(f"Сумма на индексе: {result}")
