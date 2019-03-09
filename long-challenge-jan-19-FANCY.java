/* 2019-01-07 01:10:23
   https://www.codechef.com/viewsolution/22266922
   Nitish S. Prajapati */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class code
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		String sentence;
    boolean flag=false;

		int T;
		T = sc.nextInt();
    sc.nextLine();

		while(T!=0){
        flag = false;
		    sentence = sc.nextLine();
        String[] words = sentence.split("\\s+");
		    for(String word : words){
          if(word.equals("not")){
            flag = true;
            break;
          }
        }
        if(flag){
          System.out.println("Real Fancy");
        }else{
          System.out.println("regularly fancy");
        }
		    T--;
		}
	}
}
