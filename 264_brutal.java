public class Solution {
    public int nthUglyNumber(int n) {
        int i =0;
        while (n>0){
            i=i+1;
            if ( isUgly(i)) {
                n=n-1;
            }
        }
        
        return i;
    }
    
    private boolean isUgly(int num) {
        if (num <= 0) return false;
        if(num <= 5) return true; 
        else{
            if (num%5==0) return isUgly(num/5);
            else if (num%3==0) return isUgly(num/3);
            else if (num%2==0) return isUgly(num/2);
            else return false;
        }
        
    }
}