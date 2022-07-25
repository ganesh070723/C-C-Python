// array 3.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

/*
Print Even (100 Marks)
Given a 2D array, print the even numbers of it.

You will taking two integers as input on one line separated by space representing rows and 
columns of the matrix. Following lines after that will be elements of the matrix with each element separated by space.

Constraints
1 <= n,m <= 1000

Output Format
Print the even elements of the matrix with each element separated by space.

Sample TestCase 1
Input
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16*/

int main()
{
   //I'm going to create a dynamic 2d array

	int rows, coloumns;
	cout << " ENTER THE ROWS AND COLOUMNS \n";
	cin >> rows >> coloumns;
	int** array = new int* [rows];
	for (int i = 0; i < rows; i++) {
		cin >> coloumns;
		array[i] = new int[coloumns];

	}
	for (int i = 0; i < rows; i++) {
		cout << *array[i]*[ coloumns ]; << " " << endl;
	}
}