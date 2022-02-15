class Solution
{
public:
    int numJewelsInStones(string jewels, string stones)
    {
        bool js[150] = {0};
        int cnt = 0, sj = jewels.size(), ss = stones.size();
        sort(jewels.begin(), jewels.end());
        sort(stones.begin(), stones.end());

        for (int i = 0; i < jewels.size(); i++)
            js[jewels[i]] = 1;

        for (int i = 0; i < ss; i++)
        {
            if (js[stones[i]] == 1)
                cnt++;
        }
        return cnt;
    }
};