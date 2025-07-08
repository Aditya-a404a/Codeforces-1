import threading
import sys
def main():
    
    
    input = sys.stdin.readline

    n, m = map(int, input().split())
    
    # We'll build a segment tree of size = next power of two ≥ n
    size = 1
    while size < n:
        size <<= 1

    # st[node] holds the pending “add” that applies to the entire segment of that node
    st = [0] * (2 * size)

    def _update(node, node_l, node_r, ql, qr, v):
        """
        Add v to all positions in [ql, qr).
        node covers [node_l, node_r).
        """
        if ql <= node_l and node_r <= qr:
            # fully covered → accumulate lazy value here
            st[node] += v
            return
        if node_r <= ql or qr <= node_l:
            # no overlap
            return
        # partial overlap → recurse to children
        mid = (node_l + node_r) // 2
        _update(2*node,     node_l, mid, ql, qr, v)
        _update(2*node + 1, mid,    node_r, ql, qr, v)

    def _query(node, node_l, node_r, idx):
        """
        Return the total at position idx, by accumulating lazy
        tags along the path.
        """
        if node_r - node_l == 1:
            # leaf
            return st[node]
        mid = (node_l + node_r) // 2
        if idx < mid:
            return st[node] + _query(2*node,     node_l, mid, idx)
        else:
            return st[node] + _query(2*node + 1, mid,    node_r, idx)

    out = []
    for _ in range(m):
        parts = list(map(int, input().split()))
        if parts[0] == 1:
            _, l, r, v = parts
            _update(1, 0, size, l, r, v)
        else:
            _, i = parts
            out.append(str(_query(1, 0, size, i)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    threading.Thread(target=main).start()


