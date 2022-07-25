#include<iostream>
#include<string>

using namespace std;

int getl();
string line;

int main()
{
	while (getline(cin, line)) {
		getl();
		cout << line<<endl;
	}

}

int getl()
{
	return 0;
}
