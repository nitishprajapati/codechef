/*
*   CODECHEF
*   LONG CHALLENGE (MAY 18)
*   RD19
*   MINIMUM DELETIONS
*   https://www.codechef.com/problems/RD19
*   -By Nitish S. Prajapati
*   date done : Sunday, February 24, 2019
*/

/*
*   Concept to know:
*   1. when finding gcd of sequence of numbers, gcd will always decrese as
*      you go on finding gcd in sequence of numbers
*      eg:
*         8 4 6 3 4 4
*         gcd(8,  4) = 4
*              ________|  
*             |    
*             v
*         gcd(4,  6) = 2
*              ________|  
*             |    
*             v
*         gcd(2,  3) = 1   <------+
*              ________|          |
*             |                   |    
*             v                   |
*         gcd(1,  4) = 1          |
*              ________|          |
*             |                   |
*             v                   |
*        gcd( 1,  4) = 1          |
*                                 |
*                                 |
            (for this question, we can stop at this point
            cause we know that gcd will be one in sequence
            definitely)
 
 
*
*   2. logically, the question asks us to find minimum number of deletions
*      required to get gcd of sequence to 1. So considering point 1, gcd will
*      become 1 if it has to, so why do we need to delete any element? 
*      we don't!! we don't need to delete any elements IF we wantto find 
*      MINIMUM deletions. simple as that! so minimum is possible = 0, else -1
*      if not possible.
*
*/


#include <bits/stdc++.h>
#include <vector>
using namespace std;

int gcd(int number1, int number2)
{
    int hcf;
    if(number2 > number1)
    {/*swap to store bigger number in number1*/
        int temp = number2;
        number2 = number1;
        number1 = temp;
    }
    
    for(int i = 1; i <= number2 ; ++i)
    {
        if(number2 % i == 0  &&  number1 % i == 0)
        {
            hcf = i;
        }
    }
    return hcf;
}

int main()
{
    int t;
    int n;
    int element;
    vector<int/*elements*/> sequence;
    vector<int>::iterator it;
    int number1;
    int number2;
    int hcf;
    
    cin>>t; // test cases
    while(t--)
    {
        cin>>n; // elements of sequence
        sequence.clear();
        for(int i = 0 ; i < n ; i++)
        {
            cin >> element;
            sequence.push_back(element);
        }
        
        it = sequence.begin();
        number1 = *it;
        it++;
        
        for( ; it != sequence.end() ; it++)
        {
            number2 = *it;
            hcf = gcd(number1, number2);
            if(hcf==1)
            {
                cout << 0; /*if hcf is one, so we have correct sequence
                          and hence minimum deletions should be zero always.
                          cause simple, if gcd has to be 1, it will be either
                          ways, so why you need to delete anything ha?
                          ¯\_(-_-)_/¯ huh? */
                break;
            }
            
            number1 = hcf;/*note: gcd of next two numbers will "always" be
                            less than the so far obtained gcd. i.e. it will
                            never increase. And for this step refer point 1
                            of description.*/
        }
        if(hcf!=1)
        {
            cout << -1; /*if we haven't got gcd 1, it means sequence is not correct*/
        }
        cout << endl;
        
    }
  return 0;
}
