// 24 hours to 12 hours converter.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include<iostream>
using namespace std;
int main()
{
	//24 hours format to 12 hours format
	int hour24;
	int minutes24;
	int hour12;

	int minutes12;

	char dot;
	cout << "enter the 24 hours format time : \n";
	cin >> hour24 >> dot >> minutes24;
	if (hour24 >= 0 && hour24 < 11) {
		if (hour24 == 0) {
			hour24 = 12;
		}
		cout << hour24 << dot << minutes24 << " A.M " << endl;
	}
	else if (hour24 >= 12 && hour24 <= 23) {
		hour12 = hour24 - 12;
		minutes12 = minutes24;
		cout << hour12 << dot << minutes12 << " P.M ";
	}
	else
		cout << "invalid";


}