#include <bits/stdc++.h>

using namespace std;

// Complete the staircase function below.
void staircase(int n) {


    int r=1;

    for (int a=0; a<n; a++){

         for (int b=0; b<n; b++){

             if(b<(n-r)){
                 cout<<" ";
                 
             }
                else{
                 std::cout<<"#";
             }
           
        }
         r+=1;
        cout<<endl;
    }

}
int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}
