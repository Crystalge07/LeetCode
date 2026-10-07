/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */


/*

firstly, checking base cases which are if 1. the list is empty 2. the list only has 1 node in which both cases are false because there can't be a cycle (or technically there can be a cycle for a single node, but we negate this by checking the value of the next node)
initializes 2 pointers, one is slow which travels 1 node at a time, and another is fast which travels 2 nodes at a time
while the fast (ahead pointer doesnt = null) slow becomes its next node, and fast goes ahead by 2 nodes. it does a check on the first node it traverses to make sure it isnt null, then goes to the second node
if the list doesnt have a cycle, fast will eventually become null, ending the while loop and if it does have a cycle, eventually fast = slow, which the if statement accounts for in every iteration of the loop
when it exits the loop, that is because it has assured it has no cycle, allowing us to return false

*/

class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode* slow = head; // intializes pointer to address of memory of head
        ListNode* fast = head;

        if (fast == nullptr) {
            return false;
        }

        if (fast->next == nullptr) {
            return false;
        }
    
        while (fast != nullptr ) {// could also just do while (fast) cus it implicity implies not null 
            slow = slow->next; // goes forward 1 at a time
            fast = fast->next; // goes forward 1 at a time 
            if (fast != nullptr) {
                fast = fast->next;
            }

            if (slow == fast) {
            return true;
            }
        }

        return false;

        }
    };

