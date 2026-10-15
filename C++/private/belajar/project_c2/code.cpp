#include <iostream>
#include <string>
#include "algorithms.h"
#include "data_structures.h"

using namespace std;

// Post stores the number of likes and the name of a single post
// The comparison operators are based on likes so merge sort and binary search can use them
struct Post {
    int likes;
    string post_name;

    // Compare two posts by their like count
    bool operator<(const Post& right) const {
        return likes < right.likes;
    }
    // Check whether two posts have the same like count
    bool operator==(const Post& right) const {
        return likes == right.likes;
    }
};

// PostAnalyser keeps track of many posts split across sorted batches
// Each batch is stored inside a linked list node for easy iteration
// New batches are sorted with merge sort before being added
// Queries and deletions use binary search on the sorted arrays inside each batch
struct PostAnalyser {
    // A batch is one sorted array of posts that arrived together
    struct Batch {
        Post* posts;
        int count;
    };

    // Linked list of all batches we have received
    LinkedList<Batch*> batches;
    // Fixed number of posts per batch, set from the constructor argument
    int batch_size;

    // Remember the batch size for later use
    PostAnalyser(int n) : batch_size(n) {}

    // Delete every batch array and every Batch wrapper object
    ~PostAnalyser() {
        Node<Batch*>* current = batches.get_head();
        while (current != nullptr) {
            delete[] current->data->posts;
            delete current->data;
            current = current->next;
        }
    }

    // Receive a new batch of posts, sort it by likes, and store it
    // Time complexity: O(n log n)
    void add_batch(Post* batch_post) {
        // Copy the incoming batch into our own array so we own the memory
        Post* sorted = new Post[batch_size];
        for (int i = 0; i < batch_size; i++) {
            sorted[i] = batch_post[i];
        }
        // Sort the copy in place using generic merge sort
        merge_sort(sorted, 0, batch_size - 1);

        // Wrap the sorted array in a Batch struct
        Batch* batch = new Batch;
        batch->posts = sorted;
        batch->count = batch_size;
        // Append the new batch to the linked list
        batches.append(batch);
    }

    // Find the post with the given likes and remove it from its batch
    // Time complexity: O(b * log n) worst case
    void remove_post(Post post) {
        // Walk through every batch looking for the target likes value
        Node<Batch*>* current = batches.get_head();
        while (current != nullptr) {
            Batch* batch = current->data;
            // Use binary search because this batch array is sorted
            int index = binary_search_exact_likes(batch->posts, batch->count, post.likes);
            if (index != -1) {
                // Shift every element after the found index one position to the left
                for (int i = index; i < batch->count - 1; i++) {
                    batch->posts[i] = batch->posts[i + 1];
                }
                // The batch is now one element shorter
                batch->count--;
                return;
            }
            current = current->next;
        }
    }

    // Return the post with the smallest likes value that is still above threshold
    // If no such post exists, return nullptr
    // Time complexity: O(b * log n)
    Post* least_popular_over_threshold(int threshold) {
        // Track the best candidate found so far across all batches
        Post* best = nullptr;
        Node<Batch*>* current = batches.get_head();
        while (current != nullptr) {
            Batch* batch = current->data;
            // Use binary search to find the first post in this batch that is above the threshold
            int index = binary_search_over_threshold(batch->posts, batch->count, threshold);
            if (index != -1) {
                // If this is the first candidate, or it has fewer likes than the current best, update best
                if (best == nullptr || batch->posts[index].likes < best->likes) {
                    best = &batch->posts[index];
                }
            }
            current = current->next;
        }
        return best;
    }
};

// Interactive menu driven by the scaffold
// Run the compiled program with any command line argument to enter this menu
int ontrack_test() {
    int n;
    cout << "Enter the batch size:" << endl;
    cin >> n;
    PostAnalyser analyser(n);
    string menu = "1. Add a batch\n2. Remove a post\n3. Find least popular post over a threshold\n4. See the menu again\n5. Quit\n";
    int command = 4;
    while (command != 5) {
        if (command == 1) {
            // Allocate space for one batch of posts
            Post* batch_post = new Post[n];
            for (int i = 0; i < n; i++) {
                // Read the like count for each post from input
                cout << "Enter likes for post " << i << ":" << endl;
                int likes;
                cin >> likes;
                // Read the post name for each post from input
                cout << "Enter post name for post " << i << ":" << endl;
                string post_name;
                cin >> post_name;
                batch_post[i].likes = likes;
                batch_post[i].post_name = post_name;
            }
            // Send the filled batch to the analyser
            analyser.add_batch(batch_post);
            // Free the temporary batch array; the analyser made its own copy
            delete[] batch_post;
        } else if (command == 2) {
            // Read the like count of the post to delete
            cout << "Enter likes of the post to remove:" << endl;
            int likes;
            cin >> likes;
            // Build a dummy Post object that only uses the likes field
            Post post;
            post.likes = likes;
            post.post_name = "To be deleted";
            analyser.remove_post(post);
        } else if (command == 3) {
            // Read the threshold and ask the analyser for the result
            cout << "Enter threshold:" << endl;
            int threshold;
            cin >> threshold;
            Post* result = analyser.least_popular_over_threshold(threshold);
            if (result == nullptr) {
                cout << "No such post exists" << endl;
            } else {
                cout << "Post found with " << result->likes << " likes" << endl;
            }
        } else if (command == 4) {
            // Show the menu again
            cout << menu << endl;
        }
        // Ask for the next command
        cout << "Enter command (1-5):" << endl;
        cin >> command;
        if (!cin) {
            cout << "ERROR: could not read next command" << endl;
            return 1;
        }
    }
    return 0;
}

// If the program is run with any command line argument, start the interactive menu
// Otherwise do nothing and return 0
int main(int argc, char** argv) {
    if (argc != 1) {
        return ontrack_test();
    }
    return 0;
}
