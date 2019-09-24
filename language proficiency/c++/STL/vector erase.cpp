#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,x,a,b;
    cin>>n;
    vector<int> v;

    for(int i=0; i<n;i++){
        cin>>x;
        v.push_back(x);
    } 
    cin>>a;
    v.erase(v.begin()+a-1);
    cin>>a>>b;
    v.erase(v.begin()+a-1,v.begin()+b-1);

    cout<<(v.size())<<endl;

    for(auto t=v.begin(); t!=v.end(); ++t)
        cout << *t <<" ";

    return 0;
}
