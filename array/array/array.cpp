#include<iostream>
using namespace std;

const int max_class_limit = 60;
int main()
{
	int array[max_class_limit];
	int arrayin;
	int number;
	int num;
	int ind;
	cout << "how many numbers to enter : \n";
	cin >> number;
	int sum, divisor;
	for ( ind = 0; ind <= number; ind++) {
		cin >> arrayin;
	  array[ind]= arrayin;
		
	}
	for ( int i = 1; i <= number; i++) {
		cout << " multiplication " << arrayin;
	}
}