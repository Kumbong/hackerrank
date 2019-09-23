#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {

    int n;
    int q;

   cin>> n>> q;
  int ** Vectors = new int *[n];
   int j;
    for (int i=0;i<n;i++)
    {   
        cin>>j;
        
        Vectors[i] = new int [j];
        for (int y=0;y<j;y++)
            cin>>Vectors[i][y];
    }
    int q1,q2;
    for (int i=0;i<q;i++)
    {
        cin >>q1 >> q2;
        cout<<Vectors[q1][q2]<<endl;

     }

    return 0;
}

