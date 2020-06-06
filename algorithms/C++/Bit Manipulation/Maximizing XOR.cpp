#include <bits/stdc++.h>

using namespace std;

// Complete the flippingBits function below.
long flippingBits(long n) {

    int length_binary = 32;
    vector <int> binary(length_binary);
    int binary_position = length_binary-1;
    long b=0;

while(n!=0) {
    cout<<"left number is "<<n<<endl;
    binary[binary_position]= n%2;
    n/=2;
    binary_position--;
    
}
cout<<endl;
//flip bits
    for(int x=0; x<32; x++){
        cout<<binary[x];
        if(binary[x]==0){
            binary[x]=1;
        }
        else{
            binary[x]=0;
        }
    }
    cout<<endl;
    for(int y=0; y<32; y++){
        cout<<binary[y];
    }
    cout<<endl<<endl;
    //change to decimal
    for(int z=0; z<32; z++){
        b+=binary[z]*pow(2,length_binary-1);
        cout<<b<<" + "<<binary[z]<<" *2^"<<length_binary<<endl;
        length_binary--;
        
    }
cout<<b<<endl<<endl;
return b;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        long n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        long result = flippingBits(n);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
