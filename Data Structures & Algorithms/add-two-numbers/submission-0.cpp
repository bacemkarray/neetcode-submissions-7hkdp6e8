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
        ListNode Dummy(0);
        ListNode* curr = &Dummy;
        int carry = 0;
        int sum = 0;
        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            int val1 = (l1 != nullptr) ? l1->val : 0;
            int val2 = (l2 != nullptr) ? l2->val : 0;

            sum = val1 + val2 + carry;
            carry = sum/10;
            sum %= 10;
            curr->next = new ListNode(sum);
            curr = curr->next;
            l1 = (l1 != nullptr) ? l1->next : nullptr;
            l2 = (l2 != nullptr) ? l2->next : nullptr;
        }

        // if (l1 == nullptr && l2 != nullptr) curr->next = l2;
        // else if (l2 == nullptr && l1 != nullptr) curr->next = l1;

        return Dummy.next;
    }
};
