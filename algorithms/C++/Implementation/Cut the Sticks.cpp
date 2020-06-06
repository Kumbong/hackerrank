#include <bits/stdc++.h>

using namespace std;

// Complete the maximizingXor function below.
int maximizingXor(int l, int r) {
    unsigned long max=0;

    for(unsigned long x=l; x<=r; x++){
        for(unsigned long y=l; y<=r; y++){
            
            if((x^y)>max){
                max=(x^y);
            }
            
            cout<<max<<endl;
           
        }
    }
return max;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int l;
    cin >> l;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int r;
    cin >> r;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int result = maximizingXor(l, r);

    fout << result << "\n";

    fout.close();

    return 0;
}
