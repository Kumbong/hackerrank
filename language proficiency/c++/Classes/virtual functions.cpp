
class Person{
    protected:
        string name;
        int age;
        int cur_id;
    public:
         virtual void putdata(){

         }
         virtual void getdata(){

         }
};

class Professor:public Person{
    private:
        int publications;
    public:
        static int count;
        Professor(){
            cur_id=++count;
        }
        void getdata(){
            cin>>name>>age>>publications;

        }
        void putdata(){
    
                cout<<name<<" "<<age<<" "<<publications<<" "<<cur_id<<endl;


        }
};
int Professor::count = 0;
class Student:public Person{
    private:
        int marks[6];
        static int count;
    public:

        Student(){
            cur_id=++count;
        }
        void getdata(){
            cin>>name>>age;

            for(int i=0; i<6;i++)
                cin>>marks[i];

        }
        void putdata(){
            int sum =0;
            for(int i=0; i<6;i++)
                sum+=marks[i];

                cout<<name<<" "<<age<<" "<<sum<<" "<<cur_id<<endl;
        }
};
int Student::count = 0;
