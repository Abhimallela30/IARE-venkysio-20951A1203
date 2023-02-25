using loops


import java.io.*;
import java.util.Scanner;
class main{
    public static void main(String[] args){
        String s= "geeks",nstr="";
        char ch;
        for (int i=0;i<s.length();i++){
            ch=s.charAt(i);
            nstr=ch+nstr;
        }
        System.out.println(nstr);
    }
}
