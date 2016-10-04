public class Solution {
    public boolean isUgly(int num) {
        if(num <= 5) return true; 
        else{
            if (num%5==0) return isUgly(num/5);
            else if (num%3==0) return isUgly(num/3);
            else if (num%2==0) return isUgly(num/2);
            else return false;
        }
        
    }
}