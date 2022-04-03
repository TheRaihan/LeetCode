class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> heap(begin(stones), end(stones)); 
        
        while (heap.size() > 1)
        {
            auto first = heap.top(); heap.pop();
            auto second = heap.top(); heap.pop();
            if(first - second > 0) heap.push(first - second);
        }
        
        return heap.empty() ? 0 : heap.top();
    }
};