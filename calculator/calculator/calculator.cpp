
#include <iostream>

using namespace std;

int main()
{
    // I'm going to create a calculator app
    // through switch case
    float num1, num2;
    char operation;
    cout << " ganesh's calculator:) " << endl;
    cin >> num1 >> operation >> num2;
    switch (operation)

    {
    case '-': cout << num1 << operation << num2 << " = " << num1 - num2; break;
    case '+': cout << num1 << operation << num2 << " = " << num1 + num2; break;
    case '*': cout << num1 << operation << num2 << " = " << num1 * num2; break;
    case '/': cout << num1 << operation << num2 << " = " << num1 / num2; break;
    case '%':
        bool num1int, num2int;
        num1int = ((int)num1 == num1);
        num2int = ((int)num2 == num2);
        if (num1int && num2int)
        {
            cout << num1 << operation << num2 << " = " << (int)num1 % (int)num2; break;
        }

        else
        {
            cout << "invalid!";
        }
        break;

    }


}

