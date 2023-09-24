// your C++ implemnetation of the programming assignment 
// note: Do only one implemention, do not implement Python if you complete the C++ code.
#include <iostream>
#include "alphabet.h"
#include <map>
using namespace std;
void program(int base, int number_of_digits,string limit)
{
    Alphabet alpha1(base);
    map<int, string> lookup_base = 
    {
        { 2, "binary" },
        { 8, "octal" },
        { 10, "decimal" },
        { 16, "hexadecimal" }
    };
    string MaxValid = alpha1.maxValid();
    cout << "alphabet for base "<< alpha1.size() << " : {'";
    for( int i = 0; i < alpha1.size(); i++)
    {

        cout <<alpha1[i];
            if(i <alpha1.size()-1)
        {
            cout << "', ";
        }
    }
    cout <<"'}"<< endl<<endl ;
    cout <<" In "<< lookup_base[base] <<" base, the first digit goes up to " << MaxValid << " then the digit is reset to 0 and 1 is carried to the next digit."<<endl;
    cout << "    If the carry is to a digit that is already " << MaxValid << " then the digit is also reset to 0 and 1 is carried to the next digit. "<< endl<< endl;
    int row = number_of_digits;
    int col = number_of_digits;
    string arr[row][col];
    
    for (int i = 0; i < number_of_digits; i++)
    {
        for (int j = 0;j < number_of_digits;  j++)
        {
            arr[i][j] = "0";
            
        }


    }
    

    for(int i = 0; i < row; i++) 
    {
        for(int j = 0; j < col; j++) 
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }

}

int main()
{
    program(2,5,"101");
    return 0;
}