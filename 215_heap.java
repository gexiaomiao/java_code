public class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue <Integer> heap = new PriorityQueue <>(k);
        for (int i=0;i<nums.length;i++){
            if (i<k){
                heap.add(nums[i]);
            }
            else{
                if (heap.peek()<nums[i]){
                    heap.poll();
                    heap.add(nums[i]);
                }
            }
        }
        return heap.peek();
    }
}