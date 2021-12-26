// Min distance task

#include <stdio.h>
#include <math.h>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    double distance;
    double local_min = 1000000000;
    int x;
    int y;
    int other_x;
    int other_y;
    int first;
    int second;

    cin >> n;
    int dots[n][2];

    for (int idx = 0; idx < n; idx++)
    {
        cin >> dots[idx][0] >> dots[idx][1];
    }

    for (int start = 0; start < n - 1; start++)
    {
        x = dots[start][0];
        y = dots[start][1];
        for (int other = start + 1; other < n; other++)
        {
            other_x = dots[other][0];
            other_y = dots[other][1];
            distance = sqrt(pow((x - other_x), 2) + pow((y - other_y), 2));
            if (distance < local_min)
            {
                local_min = distance;
                first = start;
                second = other;
            }
        }
    }

    
    cout << dots[first][0] << ' ' << dots[first][1] << endl;
    cout << dots[second][0] << ' ' << dots[second][1] << endl;
    return 0;
}