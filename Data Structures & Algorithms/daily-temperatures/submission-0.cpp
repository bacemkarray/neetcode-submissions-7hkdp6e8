class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int,int>> stk;
        vector<int> res(temperatures.size(),-1);
        for (int i=0; i<temperatures.size(); i++) {
            if (!(stk.empty()) && temperatures[i] > stk.top().first) {
                while (!(stk.empty()) && temperatures[i] > stk.top().first) {
                    auto temp = stk.top();
                    stk.pop();
                    res[temp.second] = i-temp.second;
                }
                stk.push({temperatures[i],i});
            }
            else stk.push({temperatures[i],i});
        }

        while (!(stk.empty())) {
            auto temp = stk.top();
            stk.pop();
            res[temp.second] = 0;
        }
        return res;
    }
};
  