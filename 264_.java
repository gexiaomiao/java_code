public class Solution {
    public int nthUglyNumber(int n) {
        PriorityQueue<Long> heap = new PriorityQueue<>();
        heap.add(1l);
        while (n>1){
            long temp = heap.poll();
            while(!heap.isEmpty()&&temp == heap.peek()) heap.poll(); // get ride of the duplicates
            heap.add(temp*2);
            heap.add(temp*3);
            heap.add(temp*5);
            n=n-1;
        }
        return heap.poll().intValue();
        
    }
}