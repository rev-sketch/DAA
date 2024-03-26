#include <iostream>
#include <cmath> 

// Doubly linked list node
struct Node {
    int key;
    int value;
    Node* next;
    Node* prev;

    Node(int k, int v) : key(k), value(v), next(nullptr), prev(nullptr) {}
};

// Hash Table class
class HashTable {
private:
    Node** table;
    int capacity;
    int size;
    const float load_factor = 0.75;
    const float shrink_factor = 0.25;

    // Hash function using multiplication method
    int hash(int key) const {
        float A = 0.6180339887; // A random real number 
        return int(capacity * fmod((key * A), 1));
    }

    // Resize the table (double or halve)
    void resize(bool grow) {
        int new_capacity = grow ? capacity * 2 : capacity / 2;
        Node** new_table = new Node*[new_capacity]();

        // Rehash all elements
        for (int i = 0; i < capacity; ++i) {
            Node* current = table[i];
            while (current != nullptr) {
                Node* next = current->next;
                int index = hash(current->key);
                
                // Insert into new table using chaining
                if (new_table[index] == nullptr) {
                    new_table[index] = current;
                    current->prev = nullptr;
                    current->next = nullptr;
                } else {
                    current->next = new_table[index];
                    new_table[index]->prev = current;
                    new_table[index] = current;
                    current->prev = nullptr;
                }
                
                current = next;
            }
        }

        delete[] table;
        table = new_table;
        capacity = new_capacity;
    }

public:
    HashTable(int initial_capacity = 16) : capacity(initial_capacity), size(0) {
        table = new Node*[capacity]();
    }

    ~HashTable() {
        for (int i = 0; i < capacity; ++i) {
            Node* current = table[i];
            while (current != nullptr) {
                Node* next = current->next;
                delete current;
                current = next;
            }
        }
        delete[] table;
    }

    // Insert key-value pair
    void insert(int key, int value) {
        int index = hash(key);
        Node* newNode = new Node(key, value);
        
        // If slot is empty
        if (table[index] == nullptr) {
            table[index] = newNode;
        } else { // Collision occurred, add to the chain
            newNode->next = table[index];
            table[index]->prev = newNode;
            table[index] = newNode;
        }
        
        size++;

        // Resize if load factor exceeds 0.75
        if ((float)size / capacity > load_factor)
            resize(true);
    }

    // Remove key-value pair
    void remove(int key) {
        int index = hash(key);
        Node* current = table[index];
        while (current != nullptr) {
            if (current->key == key) {
                if (current->prev != nullptr)
                    current->prev->next = current->next;
                else
                    table[index] = current->next;
                if (current->next != nullptr)
                    current->next->prev = current->prev;
                delete current;
                size--;

                // Resize if load factor falls below 0.25
                if ((float)size / capacity < shrink_factor)
                    resize(false);

                return;
            }
            current = current->next;
        }
    }

    // Get value for a given key
    int get(int key) const {
        int index = hash(key);
        Node* current = table[index];
        while (current != nullptr) {
            if (current->key == key)
                return current->value;
            current = current->next;
        }
        return -1; // Key not found
    }

    // Display the hash table
    void display() const {
        for (int i = 0; i < capacity; ++i) {
            std::cout << "[" << i << "]: ";
            Node* current = table[i];
            while (current != nullptr) {
                std::cout << "(" << current->key << ", " << current->value << ") ";
                current = current->next;
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    HashTable hashTable;

    // Insert some elements
    hashTable.insert(1, 10);
    hashTable.insert(2, 20);
    hashTable.insert(3, 30);
    hashTable.insert(17, 170);
    hashTable.insert(33, 330);
    hashTable.insert(65, 650);

    std::cout << "HashTable after insertions:" << std::endl;
    hashTable.display();

    // Remove an element
    hashTable.remove(2);
    std::cout << "HashTable after removal:" << std::endl;
    hashTable.display();

    // Get value for a key
    std::cout << "Value for key 3: " << hashTable.get(3) << std::endl;

    return 0;
}
