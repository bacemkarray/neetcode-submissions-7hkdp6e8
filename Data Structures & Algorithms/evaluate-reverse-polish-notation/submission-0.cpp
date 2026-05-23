class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<string> stack;
        for (string c : tokens) {
            if (c != "+" && c != "-" && c != "*" && c != "/") stack.push(c);
            else {
                int e2 = stoi(stack.top());
                stack.pop();
                int e1 = stoi(stack.top());
                stack.pop();
                if (c=="+") stack.push(to_string(e1+e2));
                else if (c=="-") stack.push(to_string(e1-e2));
                else if (c=="*") stack.push(to_string(e1*e2));
                else if (c=="/") stack.push(to_string(e1/e2));
            }
        }
        return stoi(stack.top());
    }
};
