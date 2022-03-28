#include <iostream>
#include <bits/stdc++.h>

using namespace std;
class FreqStack
{

public:
    map<int, int> freq;
    map<int, stack<int>> stacks;
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


class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int n=mat[0].size();
        for(int i=0; i<mat.size(); i++){
            mat[i].push_back(i);
        }
        sort(mat.begin(), mat.end());
        vector<int> ans(k);
        for(int i=0; i<k; i++){
            ans[i]=mat[i][n];            
        }
        return ans;
    }
};
/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */