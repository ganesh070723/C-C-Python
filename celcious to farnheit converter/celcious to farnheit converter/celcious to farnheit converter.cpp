
#include<iostream>

using namespace std;

int converter(int num)
{
	int f;
	int def = 32;
	double mul = 1.8;
	f = (double)num * mul + def;
	cout << "the \"FARENHEIT\" IS : " << f;
	return 0;
}
int main()
{
	int cel;
	cout << "\"GANESH'S CONVERTER\" \v ENTER THE CELCIOUS : ";
	cin >> cel;
	converter(cel);
}