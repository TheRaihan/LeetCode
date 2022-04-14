/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    pair<bool,int> dfs(TreeNode* root){
        pair<bool,int> res,left,right;

        if(!root){
            res.first = true;
            res.second = 0;
            return res;
        }
        left = dfs(root->left);
        right = dfs(root->right);
        
        res.first = (left.first && right.first && 
                            abs(left.second - right.second) <= 1 );
            
        res.second = 1 + max(left.second,right.second);
        
        return res;
        
    }
    
    bool isBalanced(TreeNode* root) {
        return dfs(root).first;
    }
};