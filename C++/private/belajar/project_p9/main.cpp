#include <iostream>
#include <string>
#include "hash_table.h"
using namespace std;

// Record of the followers of one user
struct FollowersRecord {
    // The number of followers this record represents
    int n = 0;
    // The string array of those followers' usernames
    string* followers = nullptr;

    string serialise() {
        string record = "";
        for (int i = 0; i < n; i++) {
            record += followers[i];
            if (i < n - 1) {
                record += "-";
            }
        }
        return record;
    }

    void deserialise(string record) {
        // Remove any existing array on the heap
        delete[] followers;

        if (record.empty()) {
            n = 0;
            followers = nullptr;
            return;
        }

        int count = 1;
        for (int i = 0; i < (int)record.length(); i++) {
            if (record[i] == '-') {
                count++;
            }
        }

        n = count;
        followers = new string[n];

        int index = 0;
        string current = "";
        for (int i = 0; i < (int)record.length(); i++) {
            if (record[i] == '-') {
                followers[index++] = current;
                current = "";
            } else {
                current += record[i];
            }
        }
        followers[index] = current;
    }
};

struct FollowersDatabase {
    HashTable ht;

    void add_follower(string username, string follower) {
        FollowersRecord record;

        // Load existing record if the user already has followers
        try {
            record.deserialise(ht.search(username));
        } catch (string e) {
            // User not in the table yet, start with an empty record
            record.n = 0;
            record.followers = nullptr;
        }

        // Check if this follower already exists (no impact if so)
        for (int i = 0; i < record.n; i++) {
            if (record.followers[i] == follower) {
                delete[] record.followers;
                return;
            }
        }

        // Resize the dynamic array and append the new follower
        string* new_followers = new string[record.n + 1];
        for (int i = 0; i < record.n; i++) {
            new_followers[i] = record.followers[i];
        }

        new_followers[record.n] = follower;
        delete[] record.followers;
        record.n++;
        record.followers = new_followers;

        string serialised = record.serialise();
        delete[] record.followers;
        ht.insert (username, serialised);
    }

    void delete_follower (string username, string follower) {
        FollowersRecord record;

        try {
            record.deserialise (ht.search (username));
        } catch (string e) {
            // User has no followers, deleting has no effect
            return;
        }
        // Find the follower in the array
        int position = -1;
        for (int i = 0; i < record.n; i++) {
            if (record.followers[i] == follower) {
                position = i;
                break;
            }
        }

        // Follower not found, no effect
        if (position == -1) {
            delete[] record.followers;
            return;
        }

        // Shift elements left to remove the follower
        for (int i = position; i < record.n - 1; i++) {
            record.followers[i] = record.followers[i + 1];
        }
        record.n--;

        if (record.n == 0) {
            // No followers left, remove the key from the hash table
            delete[] record.followers;
            record.followers = nullptr;
            ht.del (username);
        } else {
            // Shrink the dynamic array
            string* new_followers = new string[record.n];
            for (int i = 0; i < record.n; i++) {
                new_followers[i] = record.followers[i];
            }
            delete[] record.followers;
            record.followers = new_followers;
            string serialised = record.serialise();
            delete[] record.followers;
            ht.insert (username, serialised);
        }
    }

    void print_followers (string username) {
        FollowersRecord record;

        try {
            record.deserialise (ht.search (username));
        } catch (string e) {
            cout << "User does not have any followers" << endl;
            return;
        }
        if (record.n == 0) {
            cout << "User does not have any followers" << endl;
        } else {
            for (int i = 0; i < record.n; i++) {
                cout << record.followers[i] << endl;
            }
        }
        delete[] record.followers;
    }
};

int ontrack_tests () {
    FollowersDatabase db;
    string menu = "1. Add new follower for a user\n2. Remove a follower from a user\n3. Print followers of a user\n4. Show menu\n5. Exit";
    cout << menu << endl;
    int command = 0;
    cout << "Enter command (1–5):" << endl;
    cin >> command;
    while (command != 5) {
        try {
            if (command == 1) {
                cout << "Enter the username of the user who was followed:" << endl;
                string username;
                cin >> username;
                cout << "Enter the username of the follower:" << endl;
                string follower;
                cin >> follower;
                db.add_follower (username, follower);
            } else if (command == 2) {
                cout << "Enter the username of the user who was unfollowed:" << endl;
                string username;
                cin >> username;
                cout << "Enter the username of the unfollower:" << endl;
                string unfollower;
                cin >> unfollower;
                db.delete_follower (username, unfollower);
            } else if (command == 3) {
                cout << "Enter a username to see their followers:" << endl;
                string username;
                cin >> username;
                db.print_followers (username);
            } else if (command == 4) {
                cout << menu << endl;
            } else {
                cout << "Unknown command" << endl;
            }
        } catch (const string error) {
            cout << "Error: " << error << endl;
        }
        cout << "Enter command (1–5):" << endl;
        cin >> command;
        if (!cin) {
            cerr << "ERROR: Could not read next command" << endl;
            return 1;
        }
    }

    return 0;
};

int main(int argc, char** argv) {
    if (argc == 2) {
        return ontrack_tests ();
    }
    return 0;
}