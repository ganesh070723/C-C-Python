// bmi calculater.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

int main()
{
    //I'm going create my first application
    // thats bmi calculator
    //bmi = weight / (height*hight)
    // 18.5> is underweight
    //24.9< is overweight
    float weight, height, bmi;
    cout << " weight ," << " height " << endl;
    cin >> weight;
    cin>> height;
    bmi = weight / (height * height);
    if (bmi < 18.5)
        cout << "underweight" << endl;
    else if (bmi > 25)
        cout << "overweight" << endl;
    else
        cout << "normal weight" << endl;
    cout << "the bmi of you is: " << bmi;
    return 0;
}