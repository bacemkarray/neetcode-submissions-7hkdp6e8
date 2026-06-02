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

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* curr = head;
        int v1, v2 = 0;
        int carry = 0;
        while  (l1 != nullptr || l2 != nullptr || carry != 0) {
            (l1 == nullptr) ? v1=0 : v1=l1->val;
            (l2 == nullptr) ? v2=0 : v2=l2->val;
            int sum = v1+v2+carry;
            carry = sum/10;
            curr->next = new ListNode(sum%10);
            curr = curr->next;
            (l1 == nullptr) ? l1=nullptr : l1=l1->next;
            (l2 == nullptr) ? l2=nullptr : l2=l2->next;
        }
        curr = head->next;
        delete head;
        return curr;
    }
};
