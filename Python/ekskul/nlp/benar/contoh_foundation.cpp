#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Student {
    string name;
    int score;
    int projects;
    Student(string n, int s, int p) : name(n), score(s), projects(p) {}
};

bool isEligible(const Student& s) {
    return s.score >= 80 && s.projects >= 4;
}

string classifyPerformance(const vector<int>& scores) {
    int sum = 0;
    for (size_t i = 0; i < scores.size(); ++i) {
        sum += scores[i];
    }
    double avg = (double)sum / scores.size();

    if (avg >= 90) return "Outstanding";
    else if (avg >= 80) return "Excellent";
    else return "Good";
}

int main() {
    vector<Student> students;
    students.push_back(Student("Alice", 92, 5));
    students.push_back(Student("Bob", 78, 3));
    students.push_back(Student("Charlie", 85, 4));

    vector<string> eligible;
    vector<int> scores;

    for (size_t i = 0; i < students.size(); ++i) {
        scores.push_back(students[i].score);
        if (isEligible(students[i])) {
            eligible.push_back(students[i].name);
        }
    }

    string classification = classifyPerformance(scores);

    int maxGrade = *max_element(scores.begin(), scores.end());
    int minGrade = *min_element(scores.begin(), scores.end());

    cout << "Classification: " << classification << endl;
    cout << "Eligible: ";
    for (size_t i = 0; i < eligible.size(); ++i) {
        cout << eligible[i] << " ";
    }
    cout << endl;
    cout << "Max: " << maxGrade << " | Min: " << minGrade << endl;

    return 0;
}
