#include<bits/stdc++.h>

using namespace std;
class Box{
friend std::ostream& operator << (std::ostream& out, const Box &b);

private:
    long int l,b,h;

public:  
    Box(){
        l=0;
        b=0;
        h=0;
    }
    Box(int length, int breadth, int height){
        l = length;
        b = breadth;
        h = height;
    }
    Box(const Box &other_box){
        l = other_box.l;
        h = other_box.h;
        b = other_box.b;
    }
    int getLength(){
        return l;
    }
    int getBreadth(){
        return b;
    }
    int getHeight(){
        return h;
    }
    long long CalculateVolume(){
        return l*b*h;
    }
    bool operator < (const Box &other_box){
        bool res = false;
        if (l < other_box.l)
            res = true;

        else if(b<other_box.b and l==other_box.l)
            res = true;

        else if(h<other_box.h and b==other_box.b and l==other_box.l)
            res = true;

        else
            res = false;

        return res;
    }
};
std::ostream& operator << (std::ostream& out, const Box &b){

    out<<b.l<<" "<<b.b<<" "<<b.h;

    return out;
}

void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}