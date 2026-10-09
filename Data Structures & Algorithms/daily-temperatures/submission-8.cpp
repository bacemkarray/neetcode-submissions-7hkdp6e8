class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> result(temperatures.size(),0);
        stack<vector<int>> stk;
        for (int i=0; i<temperatures.size(); i++) {
            while (!stk.empty() && temperatures[i] > stk.top()[0]) {
                result[stk.top()[1]] = i-stk.top()[1];
                stk.pop();
            }
            stk.push({temperatures[i],i});
        }
        return result;
    }
};
