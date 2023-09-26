#include <iostream>
#include "alphabet.h"
#include <map>
#include <string>
#include <iomanip>
using namespace std;

void program(int base, int number_of_digits, string limit) {
    Alphabet alpha1(base);
    map<int, string> lookup_base =
    {
        { 2, "binary" },
        { 8, "octal" },
        { 10, "decimal" },
        { 16, "hexadecimal" }
    };
    string MaxValid = alpha1.maxValid();

    cout << "Alphabet for base " << alpha1.size() << " : {'";
    for (int i = 0; i < alpha1.size(); i++) {
        cout << alpha1[i];
        if (i < alpha1.size() - 1) {
            cout << "', ";
        }
    }
    cout << "'}" << endl << endl;

    cout << " In " << lookup_base[base] << " base, the first digit goes up to " << MaxValid << " then the digit is reset to 0 and 1 is carried to the next digit." << endl;
    cout << "If the carry is to a digit that is already " << MaxValid << " then the digit is also reset to 0 and 1 is carried to the next digit. " << endl << endl;

    // Validate the limit
    for (char c : limit) {
        bool validChar = false;
        for (int i = 0; i < alpha1.size(); i++) {
            if (c == alpha1[i]) {
                validChar = true;
                break;
            }
        }
        if (!validChar) {
            cerr << "Invalid character in the limit: " << c << endl;
            exit(1);
        }
    }

    cout << setw(number_of_digits) << "Number" << " | Count (reset:carry)" << endl;

    // Modify the initial value of current
    string current = alpha1[0] + string(number_of_digits - 1, alpha1[0]);
    
    while (current != limit) {
        cout << setw(number_of_digits) << current << " | "   ;

        // Increment the number
        int carry = 1;
        for (int i = number_of_digits - 1; i >= 0; i--) {
            if (carry == 0) {
                break;
            }
            int index = alpha1.size() - 1;
            while (index >= 0 && current[i] != alpha1[index]) {
                index--;
            }
            if (index == alpha1.size() - 1) {
                current[i] = alpha1[0];
                carry = 1;
                cout << "(reset:carry)" ;
            } else {
                current[i] = alpha1[index + 1];
                carry = 0;
                
            }
            
        }

        if (carry) {

            current = alpha1[0] + current;
        }
        cout << endl;
    }
}

int main() {
    program(2, 3, "1000");
    return 0;
}
