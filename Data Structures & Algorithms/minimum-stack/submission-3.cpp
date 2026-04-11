class MinStack {
private:
    std::vector<int> stk;
    std::vector<int> min_stk;

public:
    MinStack() {}
    
    void push(int val) {
        stk.push_back(val);
        if (min_stk.empty()) min_stk.push_back(val);
        else min_stk.push_back(min(min_stk.back(), val));
    }
    
    void pop() {
        min_stk.pop_back();
        // if (stk.back() == min_stk.back()) min_stk.pop_back();
        stk.pop_back();

    }
    
    int top() {
        return stk.back();
    }
    
    int getMin() {
        return min_stk.back();
    }
};
