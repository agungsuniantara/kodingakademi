#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct ContactBook;
struct ContactBookNode;

struct User {
    string nickname;
    string display_name;
    int user_score;
};

struct ContactBookNode {
    string nickname;
    User* associated_user;
    ContactBook* recursed_book = nullptr;
    ~ContactBookNode();
};

struct ContactBook {
    const int table_size = 27;
    int depth = 0;
    int size = 0;
    ContactBookNode** table = new ContactBookNode*[table_size];

    ContactBook() : ContactBook(0) {}
    ContactBook(int start_depth) : depth(start_depth) {
        for (int i = 0; i < table_size; i++) {
            table[i] = nullptr;
        }
    }

    ~ContactBook() {
        for (int i = 0; i < table_size; i++) {
            delete table[i];
        }
        delete[] table;
    }

    int hash(const string& nickname) {
        if (depth >= (int)nickname.length()) return 26;
        return nickname[depth] - 'a';
    }

    void insert_user(const string& nickname, User* user_data) {
        int slot = hash(nickname);
        if (table[slot] == nullptr) {
            table[slot] = new ContactBookNode();
            table[slot]->nickname = nickname;
            table[slot]->associated_user = user_data;
            size++;
            return;
        }
        if (table[slot]->recursed_book == nullptr) {
            if (table[slot]->nickname == nickname) {
                return;
            }
            ContactBook* nested = new ContactBook(depth + 1);
            nested->insert_user(table[slot]->nickname, table[slot]->associated_user);
            nested->insert_user(nickname, user_data);
            delete table[slot];
            table[slot] = new ContactBookNode();
            table[slot]->recursed_book = nested;
            size++;
            return;
        }
        table[slot]->recursed_book->insert_user(nickname, user_data);
        size++;
    }

    User* retrieve_user(const string& nickname) {
        int slot = hash(nickname);
        if (table[slot] == nullptr) return nullptr;
        if (table[slot]->recursed_book == nullptr) {
            if (table[slot]->nickname == nickname) {
                return table[slot]->associated_user;
            }
            return nullptr;
        }
        return table[slot]->recursed_book->retrieve_user(nickname);
    }

    void delete_user(const string& nickname) {
        int slot = hash(nickname);
        if (table[slot] == nullptr) return;
        if (table[slot]->recursed_book == nullptr) {
            if (table[slot]->nickname == nickname) {
                delete table[slot];
                table[slot] = nullptr;
                size--;
            }
            return;
        }
        table[slot]->recursed_book->delete_user(nickname);
        size--;
        if (table[slot]->recursed_book->size == 0) {
            ContactBook* nested = table[slot]->recursed_book;
            table[slot]->recursed_book = nullptr;
            delete table[slot];
            delete nested;
            table[slot] = nullptr;
        } else if (table[slot]->recursed_book->size == 1) {
            ContactBook* nested = table[slot]->recursed_book;
            table[slot]->recursed_book = nullptr;
            User* user = nested->extract_single_user();
            delete table[slot];
            delete nested;
            table[slot] = new ContactBookNode();
            table[slot]->nickname = user->nickname;
            table[slot]->associated_user = user;
        }
    }

    User* extract_single_user() {
        for (int i = 0; i < table_size; i++) {
            if (table[i] == nullptr) continue;
            if (table[i]->recursed_book == nullptr) {
                User* user = table[i]->associated_user;
                delete table[i];
                table[i] = nullptr;
                size--;
                return user;
            }
            User* user = table[i]->recursed_book->extract_single_user();
            if (table[i]->recursed_book->size == 0) {
                ContactBook* nested = table[i]->recursed_book;
                table[i]->recursed_book = nullptr;
                delete table[i];
                delete nested;
                table[i] = nullptr;
            }
            return user;
        }
        return nullptr;
    }

    bool search(const string& prefix) {
        if (prefix.length() <= (size_t)depth) {
            return size > 0;
        }
        int slot = hash(prefix);
        if (table[slot] == nullptr) return false;
        if (table[slot]->recursed_book == nullptr) {
            return table[slot]->nickname.length() >= prefix.length() &&
                   table[slot]->nickname.substr(0, prefix.length()) == prefix;
        }
        return table[slot]->recursed_book->search(prefix);
    }
};

ContactBookNode::~ContactBookNode() {
    delete recursed_book;
}

bool valid_nickname(const string& nickname) {
    if (nickname.empty()) {
        return false;
    }
    for (int i = 0; i < (int)nickname.length(); i++) {
        if (nickname[i] < 'a' || nickname[i] > 'z') {
            return false;
        }
    }
    return true;
}

int main() {
    ContactBook book;
    vector<User*> users;
    string menu = "1. Add a contact\n2. Retrieve a contact\n3. Remove a contact\n4. Search\n5. Book size\n6. Show menu\n7. Exit\n";
    int command = 6;
    while (command != 7) {
        if (command == 1) {
            cout << "Enter the nickname:" << endl;
            string nickname;
            cin >> nickname;
            if (!valid_nickname(nickname)) {
                cout << "Nicknames must use the lowercase letters a-z only" << endl;
            } else if (book.retrieve_user(nickname) != nullptr) {
                cout << "The nickname '" << nickname << "' is already taken" << endl;
            } else {
                cout << "Enter the display name:" << endl;
                string display_name;
                cin >> display_name;
                cout << "Enter the user score:" << endl;
                int user_score;
                cin >> user_score;
                User* user = new User;
                user->nickname = nickname;
                user->display_name = display_name;
                user->user_score = user_score;
                book.insert_user(nickname, user);
                users.push_back(user);
                cout << "Added " << display_name << " under the nickname '" << nickname << "'" << endl;
            }
        } else if (command == 2) {
            cout << "Enter the nickname to retrieve:" << endl;
            string nickname;
            cin >> nickname;
            if (!valid_nickname(nickname)) {
                cout << "Nicknames must use the lowercase letters a-z only" << endl;
            } else {
                User* user = book.retrieve_user(nickname);
                if (user == nullptr) {
                    cout << "No contact is saved under '" << nickname << "'" << endl;
                } else {
                    cout << "Nickname: " << user->nickname << " | Display name: " << user->display_name << " | Score: " << user->user_score << endl;
                }
            }
        } else if (command == 3) {
            cout << "Enter the nickname to remove:" << endl;
            string nickname;
            cin >> nickname;
            User* user = valid_nickname(nickname) ? book.retrieve_user(nickname) : nullptr;
            if (user == nullptr) {
                cout << "No contact is saved under '" << nickname << "'" << endl;
            } else {
                book.delete_user(nickname);
                for (int i = 0; i < (int)users.size(); i++) {
                    if (users[i] == user) {
                        users.erase(users.begin() + i);
                        break;
                    }
                }
                delete user;
                cout << "Removed the contact '" << nickname << "'" << endl;
            }
        } else if (command == 4) {
            cout << "Enter the prefix to search for:" << endl;
            string prefix;
            cin >> prefix;
            if (!valid_nickname(prefix)) {
                cout << "Prefixes must use the lowercase letters a-z only" << endl;
            } else if (book.search(prefix)) {
                cout << "Yes - at least one contact has the prefix '" << prefix << "'" << endl;
            } else {
                cout << "No contact has the prefix '" << prefix << "'" << endl;
            }
        } else if (command == 5) {
            cout << "The contact book holds " << book.size << " contact(s)" << endl;
        } else if (command == 6) {
            cout << menu << endl;
        }
        cout << "Enter command (1-7):" << endl;
        if (!(cin >> command)) {
            break;
        }
    }
    for (int i = 0; i < (int)users.size(); i++) {
        delete users[i];
    }
    users.clear();
    return 0;
}
