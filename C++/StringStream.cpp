#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    vector<int> numbers;
    stringstream ss(str);
    
    int num;
    char ch;
    
    while(ss >> num){
        numbers.push_back(num);
        ss >> ch;
    }
    
    return numbers;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
