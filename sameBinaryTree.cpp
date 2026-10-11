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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) { 
            return true;
        }
        if (p == nullptr || q == nullptr) {
            return false;
        }

        // first check base cases, if both are empty, return true bc theyre the same but if only one is empty, return false

        int val1 = p->val;
        int val2 = q->val;

        if (val1 != val2) {
            return false;
        }

        else {

            bool result1 = isSameTree(p->right, q->right);
            bool result2 = isSameTree(p->left, q->left);

            return result1 && result2;
        }

    }
};
