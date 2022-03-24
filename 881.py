class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int cnt=0;
        sort(people.begin(),people.end());
        
        for(int i=0,j=people.size()-1; i<=j ; j--)
        {
            cnt++;
            if(i==j) break;
            if(people[i]+people[j] <= limit)
                i++;
        }
        return cnt;
    }
};