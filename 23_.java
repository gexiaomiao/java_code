/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists==null||lists.length==0) return null;
        
        PriorityQueue<ListNode> heap = new  PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>(){
            @Override
            public int compare(ListNode n1, ListNode n2){
                if (n1.val<n2.val) return -1; // define the less than operator;
                if (n1.val>n2.val) return +1;// define the less than operator;
                else return 0;
                }
            });
        for (int i =0; i<lists.length;i++){
            if (lists[i]!=null)
            heap.add(lists[i]);
        }
        
        ListNode headnode = heap.peek();
        ListNode current_node =  new ListNode(0);

        
        if (headnode==null) return headnode;
        while ((!heap.isEmpty())){
            
            current_node.next = heap.poll();
            current_node = current_node.next;

            if (current_node.next!=null) heap.add(current_node.next);
        }
        return headnode;
    }
}