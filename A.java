import java.io.*;
import java.util.*;

class A
{

public static void main (String[] args)
  
{
    
int i,a,fac;
  
  Scanner b=new Scanner(System.in);
   
 a=b.nextInt();
    
fac=1;
   
 for(i=1;i<=a;i++)
   
 {
      
  fac*=i;
   
 }
   
 System.out.println(fac);

}

}
