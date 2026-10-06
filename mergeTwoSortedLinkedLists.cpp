/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 

 struct ListNode { // defines new type
    int val;                                                  // field 1
    ListNode *next;                                           // field 2

    ListNode() : val(0), next(nullptr) {}                     // constructor A: no args
    ListNode(int x) : val(x), next(nullptr) {}                // constructor B: one arg
    ListNode(int x, ListNode *next) : val(x), next(next) {}   // constructor C: two args
};

ListNode a;          // runs A
ListNode b(5);       // runs B
ListNode c(5, &b);   // runs C

*/


class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
       if (!list1) { // if list 1 is empty, return list 2
        return list2;
       }
       if (!list2) { // if list 2 is empty, return list 1
        return list1;
       }

       if (list1->val <= list2->val) {
        list1->next = mergeTwoLists(list1->next, list2);
        return list1;
       }
       else {
        list2->next = mergeTwoLists(list1, list2->next);
        return list2;
       }

    }
};
