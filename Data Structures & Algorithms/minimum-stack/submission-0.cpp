class MinStack {
public:
    std::vector<int> s;
    int min = INT_MAX;
    std::vector<vector<int>> pairs;
    MinStack() {}
    
    void push(int val) {
        s.push_back(val);
        pairs.push_back({s.back(),min});
        min = (val < min) ? val : min;
    }
    
    void pop() {
        min = pairs.back()[1];
        pairs.pop_back();
        s.pop_back();

    }
    
    int top() {
        return s.back();
    }
    
    int getMin() {
        return min;
    }
};
