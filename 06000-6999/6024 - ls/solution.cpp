#include <iostream>
#include <string>

using namespace std;

string removeDuplicateStars(string str); // without this function, the solution is also accepted
bool match(string pattern, string fileName);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string pattern, fileName;
    int n;

    cin >> pattern;
    cin >> n;

    pattern = removeDuplicateStars(pattern);

    for (int i = 0; i < n; i++) {
        cin >> fileName;

        if (match(pattern, fileName)) {
            cout << fileName << "\n";
        }
    }
}

string removeDuplicateStars(string str) {
    string newStr = "";
    int strLength = str.length();

    for (int i = 0; i < strLength; i++) {
        if (i > 0 && str[i - 1] == '*' && str[i] == '*') {
            continue;
        }

        newStr += str[i];
    }

    return newStr;
}

bool match(string pattern, string fileName) {
    int patternLength = pattern.length();
    int fileNameLength = fileName.length();
    int patternIndex = 0;

    for (int i = 0; i < fileNameLength; i++) {
        if (patternIndex < patternLength && fileName[i] == pattern[patternIndex]) {
            patternIndex++;
        } else if (patternIndex < patternLength &&
                   pattern[patternIndex] == '*' &&
                   patternIndex + 1 < patternLength &&
                   fileName[i] == pattern[patternIndex + 1]) {
            patternIndex += 2;
        } else if (patternIndex < patternLength && pattern[patternIndex] == '*') {
            continue;
        } else {
            i--;

            while (patternIndex >= 0 && pattern[patternIndex] != '*') {
                patternIndex--;
            }

            if (patternIndex < 0) {
                return false;
            }
        }
    }

    return patternIndex >= patternLength - 1;
}
