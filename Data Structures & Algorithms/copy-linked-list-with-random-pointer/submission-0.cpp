/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*,Node*> nodes;
        Node* curr = head;

        while (curr != nullptr) {
            Node* copy = new Node(curr->val);
            nodes[curr] = copy;
            curr = curr->next;
        }

        curr = head;
        while (curr != nullptr) {
            Node* copy = nodes[curr];
            copy->next = nodes[curr->next];
            copy->random = nodes[curr->random];
            curr = curr->next;
        }

        return nodes[head];
    }
};
