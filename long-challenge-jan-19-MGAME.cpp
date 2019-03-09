/*
  2019-01-08 14:29:52
  https://www.codechef.com/viewsolution/22307017
  Nitish S. Prajapati
*/

#include <map>
#include <set>
#include <vector>
#include <stdio.h>
#include <utility>
#include <bits/stdc++.h>
#define ll long long int

using namespace std;

int main(){
    ll T,N,P;
    ll MAX;
    ll res;
    ll i;
    
    scanf("%lld",&T);
    
    while(T--){
        scanf("%lld %lld",&N,&P);
        
        if(N==1ll){cout<<P*P*P;}
        else if(N==2ll){cout<<P*P*P;}
        else if(N>=3ll){
            MAX = (N%((N/2ll)+1ll));
            
            res = (P-MAX)*(P-MAX) + (P-MAX)*(P-N) + (P-N)*(P-N);
            cout<<res;
        }
        cout<<'\n';
    }
    return 0;
}
