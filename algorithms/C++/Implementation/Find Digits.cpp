#include <bits/stdc++.h>

using namespace std;

// Complete the findDigits function below.
int findDigits(int n, int t) {

   
     int ans=0;
     int divs=1;
    int a=n;

    for(int x=0; x<t; x++){

    
    int digits=0;
    int num;
   

        while(a>0){
            a=a/10;
            digits+=1;
             
        }
        cout<<digits<<endl;
          cout<<endl;

        for(int y=0; y<digits; y++){
            
            num= n/divs %10;
            divs*=10;
            
            
            if(num!=0){
            if(n%num==0){
                ans+=1;
                
            }
            }
        }
        
        
    }
    cout<<ans<<endl;
    cout<<endl;
    return ans;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        int result = findDigits(n, t);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
