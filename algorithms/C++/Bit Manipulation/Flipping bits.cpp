#include <bits/stdc++.h>

using namespace std;

// Complete the marsExploration function below.
int marsExploration(string s) {
    int count=0;
    string compare="";
    int error_number=0;
    int comp_size= (s.size())/3;
    int initial_size= s.size();

    for(int y=0; y<comp_size; y++){
        compare+="SOS";
    }
    cout<<compare<<endl;
    cout<<s<<endl;

    for(int x=0; x<initial_size; x++){
        if(s[x]!=compare[x]){
            count+=1;
        }
        
    }


    
   

    return count;
}


int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = marsExploration(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
