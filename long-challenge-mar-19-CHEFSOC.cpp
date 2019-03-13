
/*
    Nitish S. Prajapati
    2019-03-06 14:47:45
*/
#include <bits/stdc++.h>
#include <vector>
#include <set>
#include <utility>
#include <map>
#include <cmath>
#include <iomanip>
#include <string>
#include <deque>
#include <queue>
#include <sstream>
#define fast ios_base::sync_with_stdio(false); cin.tie(NULL)
#define ull unsigned long long int
#define ll long long int
#define mod 1000000007
using namespace std;

int counter; //global

  void PassBallTo(int currentDog, vector<short> Dogs)
  {
      ::counter = ::counter+ 1;
      short skill = Dogs[currentDog];
      Dogs[currentDog] = 0;
      
      if(skill == 0){::counter = ::counter - 1; return;}
      if(skill == 1)
      {
          if(currentDog > 0)
          {
              //if previous dog still didn't get ball
              if(Dogs[currentDog-1] != 0) 
              {
                  PassBallTo(currentDog-1, Dogs);
              }
          }
          
          if(currentDog < Dogs.size()-1)
          {
              //if next dog still didn't get ball
              if(Dogs[currentDog+1] != 0)
              {
                  PassBallTo(currentDog+1, Dogs);
              }
          }
      }
      else if(skill == 2)
      {
          //check if dog can pass ball one step behind
          if(currentDog > 0)
          {
              //if previous dog still didn't get ball
              if(Dogs[currentDog-1] != 0) 
              {
                  PassBallTo(currentDog-1, Dogs);
              }
          }
          
          //check if dog can pass ball two step behind
          if(currentDog > 1)
          {
              //if dog before previous still didn't get ball
              if(Dogs[currentDog-2] != 0) 
              {
                  PassBallTo(currentDog-2, Dogs);
              }
          }
          
          //check if dog can pass ball one step forward
          if(currentDog < Dogs.size()-1)
          {
              //if next dog still didn't get ball
              if(Dogs[currentDog+1] != 0)
              {
                  PassBallTo(currentDog+1, Dogs);
              }
          }
          
          //check if dog can pass ball two step forward
          if(currentDog < Dogs.size()-2)
          {
              //if dog after next still didn't get ball
              if(Dogs[currentDog+2] != 0)
              {
                  PassBallTo(currentDog+2, Dogs);
              }
          }
      }
  }
  
  
  void tree(vector<short> dogs)
  {
      ::counter = 0;
      PassBallTo(0, dogs);
  }

int main(){
  int t;
  int n;
  short dog;
  vector<short> dogs;
  
  cin>>t;
  
  while(t--)
  {
      cin>>n;
      while(n--)
      {
          cin>>dog;
          dogs.push_back(dog);
      }
      tree(dogs);
      cout<<::counter<<endl;
      dogs.clear();
  }
  return 0;
}
