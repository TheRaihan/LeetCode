class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int cnt=0;
        sort(people.begin(),people.end());
        for(int i=0,j=people.size()-1; i<=j; j--)
        {
            if(i==j){
                cnt++;
                break;
            }

            if(people[i]+people[j] <= limit){
                people[i] = 0;
                i++;
            }
            
            people[j] = 0;
            cnt++;
        }
        return cnt;
    }
};