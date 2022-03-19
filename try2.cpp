#include <iostream>
#include <bits/stdc++.h>

using namespace std;
class FreqStack
{

public:
    unordered_map<int, int> freq;
    unordered_map<int, stack<int>> stacks;
    int mx = 0;
    
    void push(int val)
    {
        freq[val]++;
        mx = max(freq[val], mx);
        stacks[freq[val]].push(val);
    }

    int pop()
    {
        int val = stacks[mx].top();
        stacks[mx].pop();
        freq[val]--;
        if (stacks[mx].empty())
            mx--;
        return val;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */