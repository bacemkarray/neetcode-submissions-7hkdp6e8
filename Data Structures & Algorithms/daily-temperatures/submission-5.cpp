class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int,int>> stk;
        vector<int> res(temperatures.size(),0);
        for (int i=0; i<temperatures.size(); i++) {
            while (!stk.empty() && temperatures[i] > stk.top().first) {
                auto temp = stk.top();
                stk.pop();
                res[temp.second] = i-temp.second;
            }
            stk.push({temperatures[i],i});
        }
        return res;
    }
};
  