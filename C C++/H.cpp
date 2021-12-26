#include <bits/stdc++.h>
using namespace std;
int main()
{
   long n_passengers;
   long offices;
   long passenger;

   long free_office;
   long last_office = -1;
   priority_queue<long, vector<long>, greater<long>> traffic;
   

   cin >> n_passengers;
   cin >> offices;

   for (long idx = 0; idx < offices; idx++){
      cin >> passenger;
      traffic.push(passenger);
   }
   
   for (long idx = offices; idx < n_passengers; idx++){
      cin >> passenger;
      free_office = traffic.top();
      traffic.pop();
      free_office += passenger;
      traffic.push(free_office);
   }

   while (traffic.empty() == false){
      free_office = traffic.top();
      traffic.pop();
      if (free_office > last_office) {last_office = free_office;}
   }

   cout << last_office;
   return 0;
}