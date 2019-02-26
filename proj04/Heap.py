#project 04
#cse 331 
#chen,kunyu
#A54470631


class Heap:
    """
    A heap-based priority queue
    Items in the queue are ordered according to a comparison function
    """

    def __init__(self, comp):
        """
        Constructor
        :param comp: A comparison function determining the priority of the included elements
        """
        self.comp = comp
        self.h_size = 0
        self.array = []

    def __len__(self):

        return self.h_size

    def peek(self):
        """
        look at the smallest element
        return the smallest element.
        """
        if self.h_size <= 0:
            raise IndexError
        return self.array[0]

    def sift_up(self, v):
        p = (int)((v-1)/2)
        if p < 0 or v == 0: return

        if self.comp(self.array[v], self.array[p]):
            t = self.array[p]
            self.array[p] = self.array[v]
            self.array[v] = t

            self.sift_up(p)

    def insert(self, item):
        """
        Insert a element item
        """
        self.array.append(item)
        self.sift_up(self.h_size)
        self.h_size += 1

    def sift_down(self, i):
        pos = 2*i + 1
        if pos >= self.h_size: return

        if pos+1 < self.h_size and self.comp(self.array[pos+1], self.array[pos]):
            pos = pos + 1

        if self.comp(self.array[pos], self.array[i]):
            t = self.array[i]
            self.array[i] = self.array[pos]
            self.array[pos] = t

            self.sift_down(pos)

    def extract(self):
        """
        remove the smallest element
        return the smallest element which is the removed one
        """
        if self.h_size <= 0:
            raise IndexError

        t = self.array[0]
        self.h_size -= 1
        self.array[0] = self.array[self.h_size]
        self.array.pop()

        self.sift_down(0)
        return t

    def extend(self, seq):
        """
        add a list which called seq into the heap
        """
        for x in seq:
            self.insert(x)

    def clear(self):
        """
        remov all elements
        """
        for i in range(self.h_size):
            self.array.pop()
        self.h_size = 0

    def __iter__(self):
        return iter(self.array)

    # Supplied methods

    def __bool__(self):
        """
        Checks if this heap contains items
        :return: True if the heap is non-empty
        """
        return not self.is_empty()

    def is_empty(self):
        """
        Checks if this heap is empty
        :return: True if the heap is empty
        """
        return len(self) == 0

    def __repr__(self):
        """
        A string representation of this heap
        :return:
        """
        return 'Heap([{0}])'.format(','.join(str(item) for item in self))

    # Added methods


# Required Non-heap member function


def find_median(seq):
    """
    Finds the median (middle) item of the given sequence.
    Ties are broken arbitrarily.
    :param seq: an iterable sequence
    :return: the median element
    """
    if not seq:
        raise IndexError

    min_heap = Heap(lambda a, b: a <= b)
    max_heap = Heap(lambda a, b: a >= b)

    for x in seq:
        min_heap.insert(x)
        max_heap.insert(x)

    l = 0
    if len(seq)%2 == 0:
        l = len(seq)/2 - 1
    else:
        l = (int)(len(seq)/2)

    while l > 0:
        min_heap.extract()
        l -= 1

    return min_heap.peek()
