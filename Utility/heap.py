class MinHeap:
    def __init__(self, data=None):
        """
        If data is given (a list), build a heap from it.
        Otherwise start with an empty heap.
        """
        if data is None:
            self.heap = []
        else:
            self.heap = list(data)
            self.heapify()   # build the heap in-place

    # --- index helpers ---
    def _parent(self, i): 
        return (i - 1) // 2
    
    def _left(self, i):   
        return 2 * i + 1
    
    def _right(self, i):  
        return 2 * i + 2

    # --- public operations ---
    def insert(self, x):
        """Insert element x into the heap."""
        self.heap.append(x)
        self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        """Remove and return the smallest element."""
        if not self.heap:
            raise IndexError("extract_min from empty heap")
        min_val = self.heap[0]
        last = self.heap.pop()
        if self.heap:          # if not empty afterwards
            self.heap[0] = last
            self._sift_down(0)
        return min_val

    def peek(self):
        """Return the smallest element without removing it."""
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def heapify(self):
        """
        Turn the current list into a valid min-heap in-place.
        Time complexity: O(n).
        """
        n = len(self.heap)
        # start from last internal node down to root
        for i in range((n // 2) - 1, -1, -1):
            self._sift_down(i)

    def delete(self, i):
        """
        Delete the element at index i.
        Raises IndexError if i is out of range.
        """
        n = len(self.heap)
        if i < 0 or i >= n:
            raise IndexError("delete index out of range")

        # Move last element to position i and remove old last
        last = self.heap.pop()
        if i == n - 1:
            # we just removed the last element; nothing more to do
            return

        self.heap[i] = last

        # Restore heap property: depending on value, sift up or down
        # Try sift_up first; if no movement, then sift_down.
        parent = self._parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self._sift_up(i)
        else:
            self._sift_down(i)

    # --- internal helpers ---
    def _sift_up(self, i):
        """Move element at index i up to restore heap property."""
        while i > 0:
            p = self._parent(i)
            if self.heap[i] < self.heap[p]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def _sift_down(self, i):
        """Move element at index i down to restore heap property."""
        n = len(self.heap)
        while True:
            left = self._left(i)
            right = self._right(i)
            smallest = i

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest