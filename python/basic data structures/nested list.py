#include <bits/stdc++.h>

using namespace std;

// Complete the viralAdvertising function below.
int viralAdvertising(int n) {

    int constant_first=2;
    int total_like=2;
    int advertised=5;
    int liked=0;
    int next_like=total_like;
    int next_view;


    cout<<"first constant liked by "<<constant_first<<endl;

    for(int x=0; x<n-1; x++){
        next_view= next_like*3;
        cout<< "next to see "<<next_view<<endl;

        advertised+= (total_like*3);
        cout<<"seen by "<<advertised<<endl;

        total_like+= next_view/2;
        next_like= next_view/2;
        
        cout<<"next to like "<<next_view/2<<endl;
        cout<<"total liked by "<<total_like<<endl;

        
    }

    return total_like;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int result = viralAdvertising(n);

    fout << result << "\n";

    fout.close();

    return 0;
}
