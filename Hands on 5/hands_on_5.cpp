#include <iostream>
#include <vector>
#include <algorithm>

template<typename T>
class MinHeap {
private:
    std::vector<T> heap;

    int parent(int i) { return (i - 1) >> 1; }  // Bit manipulation for parent
    int left(int i) { return (i << 1) + 1; }     // Bit manipulation for left child
    int right(int i) { return (i << 1) + 2; }    // Bit manipulation for right child

    void heapify(int i) {
        int l = left(i);
        int r = right(i);
        int smallest = i;
        if (l < heap.size() && heap[l] < heap[i])
            smallest = l;
        if (r < heap.size() && heap[r] < heap[smallest])
            smallest = r;
        if (smallest != i) {
            std::swap(heap[i], heap[smallest]);
            heapify(smallest);
        }
    }

public:
    MinHeap() {}

    void build_min_heap(std::vector<T>& data) {
        heap = data;
        for (int i = heap.size() / 2 - 1; i >= 0; i--) {
            heapify(i);
        }
    }

    void push(const T& value) {
        heap.push_back(value);
        int i = heap.size() - 1;
        while (i > 0 && heap[parent(i)] > value) {
            std::swap(heap[parent(i)], heap[i]);
            i = parent(i);
        }
    }

    T pop() {
        if (heap.empty()) {
            throw std::out_of_range("Heap is empty");
        }
        T root = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        heapify(0);
        return root;
    }

    void print() {
        for (const T& value : heap) {
            std::cout << value << " ";
        }
        std::cout << std::endl;
    }
};

int main() {
    MinHeap<int> heap;
    std::vector<int> data = {3, 2, 1, 5, 6, 4};

    heap.build_min_heap(data);
    heap.print();  // Output: 1 2 3 5 6 4

    heap.push(0);
    heap.print();  // Output: 0 2 1 5 6 4 3

    heap.pop();
    heap.print();  // Output: 1 2 3 5 6 4

    return 0;
}