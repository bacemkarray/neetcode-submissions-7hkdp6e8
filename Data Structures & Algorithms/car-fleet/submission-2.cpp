class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int,int>> cars;
        stack<double> stack;
        for (int i=0; i<position.size(); i++) {
            cars.push_back({position[i], speed[i]});
        }
        // sort(cars.begin(), cars.end(), greater<pair<int,int>>());
        sort(cars.begin(), cars.end(), [](auto& a, auto& b) {return a.first > b.first;}); //lambda function
        for (int i=0; i<cars.size(); i++) {
            double time = (double)(target - cars[i].first)/cars[i].second;
            if (stack.empty() || time > stack.top()) stack.push(time);
        }
        return stack.size();

    }
};
