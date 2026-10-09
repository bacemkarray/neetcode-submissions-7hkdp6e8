class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l=0;
        int r=heights.size()-1;
        int best = 0;
        while (l<r) {
            int height = min(heights[l],heights[r]);
            int width = r-l;
            best = max(best, height*width);
            heights[l] > heights[r] ? r-=1 : l+=1;
        }
        return best;
    }
};
