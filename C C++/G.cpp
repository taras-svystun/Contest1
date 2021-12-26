#include <bits/stdc++.h>
using namespace std;
int main()
{
    int length;

    cin >> length;
    int array[length];

    for (int idx = 0; idx < length; idx++)
    {
        cin >> array[idx];
    }

    for (int idx = 0; idx < length - 1; idx++)
    {
        int to_print = 0;
        for (int inner = idx + 1; inner < length; inner++)
        {
            if (array[idx] < array[inner])
            {
                to_print = array[inner];
                break;
            }
        }
        cout << to_print;
        cout << ' ';
    }
    cout << 0;
    return 0;
}