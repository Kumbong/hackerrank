#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the permutationEquation function below.
vector<int> permutationEquation(vector<int> p, int n) {

    int count=0;
    vector<int> permutee(n);

    for(int x=0; x<n; x++){
        count+=1;
    cout<<"start number "<<count<<endl;
        for(int y=0; y<n; y++){
            cout<<"checking between count and postion"<<endl;
        cout<<"check if "<<p[y]<<"is "<<count<<endl<<endl;
            if(p[y]==count){
                cout<<"position is "<<y+1<<endl;
                    for(int z=0; z<n; z++){
                        cout<<"checking between position and vector"<<endl;
                         cout<<"check if "<<y+1<<" is "<<p[z]<<endl<<endl;
                        if(p[z]==(y+1)){
                            permutee[x]=z+1;
                        }
                    }

            }
        }

    }
    return permutee;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string p_temp_temp;
    getline(cin, p_temp_temp);

    vector<string> p_temp = split_string(p_temp_temp);

    vector<int> p(n);

    for (int i = 0; i < n; i++) {
        int p_item = stoi(p_temp[i]);

        p[i] = p_item;
    }

    vector<int> result = permutationEquation(p, n);

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
