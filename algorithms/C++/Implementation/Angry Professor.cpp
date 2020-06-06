#include <algorithm>
#include <bits/stdc++.h>
#include <cstdio>

using namespace std;

vector<string> split_string(string);

// Complete the cutTheSticks function below.

vector<int> cutTheSticks(vector<int> arr, int n) {

    vector<int> num(n);
    int shortest=0;
    int count=0;

    for(int x=0; x<n; x++){
        cout<<"find the shortest"<<endl;
        for(int w=0; w<n; w++){
            if(arr[w]!=0){
                    shortest= arr[w];
            }
        }
        for(int y=0; y<n; y++){
            if(arr[y]!=0){
                if(arr[y]<shortest){
                    shortest= arr[y];
                   
                }
            }
        }
         cout<<"shortest is "<<shortest<<endl;

        for(int z=0; z<n; z++){
            if(arr[z]!=0){
                cout<<arr[z]<<" minus "<<shortest<<endl;
                arr[z]-=shortest;
                count+=1;

            }
        }
        cout<<endl;
        num[x]=count;
        count=0;
    }
     num.erase(std::remove(num.begin(), num.end(), 0), num.end());
    
       
    return num;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    vector<int> result = cutTheSticks(arr, n);

    for (int i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
