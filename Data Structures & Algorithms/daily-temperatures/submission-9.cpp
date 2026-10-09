class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> result(temperatures.size(),0);
        stack<int> stk;
        for (int i=0; i<temperatures.size(); i++) {
            while (!stk.empty() && temperatures[i] > temperatures[stk.top()]) {
                result[stk.top()] = i-stk.top();
                stk.pop();
            }
            stk.push(i);
        }
        return result;
    }
};
