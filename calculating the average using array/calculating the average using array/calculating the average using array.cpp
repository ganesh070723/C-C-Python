#include<iostream>

using namespace std;

const int max_limit = 60;
int main()
{
	int numberofst;
	cout << "ENTER THE NUMBER OF STUDENDTS :" << endl;
	cin >> numberofst;
	int sum;
	double average;
	int marks[max_limit];
	int markfor;
	int ind;
	sum = 0;
	cout << "enter the marks :" << endl;
	for (ind = 1; ind <= numberofst; ind++) {

		cin >> markfor;
		marks[ind] = markfor;

	}
	for (ind = 1; ind <= numberofst; ind++) {
		sum += marks[ind];

	}
	average = (double)sum / (double)numberofst;
	cout << " AVERAGE OF THE ENTERED MARKS ARE : " << average << endl;
	for (ind = 1; ind <= numberofst; ind++) {
		if (marks[ind] > average) {
			cout << "the above AVERAGE MARKS ARE : " << " " << marks[ind]<<endl;

		}
	}
	cout << (int)marks[1];
	return 0;
	cout << endl;
}