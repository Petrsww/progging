class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)

    def build(self, tree_index, left, right):
        if left == right:
            self.tree[tree_index] = self.arr[left]
        else:
            mid = (left + right) // 2
            self.build(2 * tree_index + 1, left, mid)
            self.build(2 * tree_index + 2, mid + 1, right)
            self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

    def update(self, index, value):
        self.update_helper(0, 0, len(self.arr) - 1, index, value)

    def update_helper(self, tree_index, left, right, index, value):
        if left == right:
            self.tree[tree_index] = value
        else:
            mid = (left + right) // 2
            if index <= mid:
                self.update_helper(2 * tree_index + 1, left, mid, index, value)
            else:
                self.update_helper(2 * tree_index + 2, mid + 1, right, index, value)
            self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

    def query(self, query_left, query_right):
        return self.query_helper(0, 0, len(self.arr) - 1, query_left, query_right)

    def query_helper(self, tree_index, left, right, query_left, query_right):
        if query_left > right or query_right < left:
            return 0
        if query_left <= left and query_right >= right:
            return self.tree[tree_index]
        
        mid = (left + right) // 2
        left_sum = self.query_helper(2 * tree_index + 1, left, mid, query_left, query_right)
        right_sum = self.query_helper(2 * tree_index + 2,mid + 1,right ,query_left ,query_right)
        
        return left_sum + right_sum


arr = [3, 5, 8, 9]
segment_tree = SegmentTree(arr)


segment_tree.update(1, 7)
result = segment_tree.query(0 ,3)

print(f"Сумма на отрезке: {result}")
