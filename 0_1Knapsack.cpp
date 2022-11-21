
#include <iostream>

using namespace std;

int K[4][51];

int max(int a,int b){
    if(a>b)return a;
    return b;
}

int KnapSack(int *profits,int *weights,int W){
    for(int i=0;i<4;i++){
        for(int j=0;j<51;j++){
            if(i==0 || j==0)K[i][j]=0;
            else if(weights[i-1]<=j){
                K[i][j]=max(K[i-1][j],profits[i-1]+K[i-1][j-weights[i-1]]);
                
            }else{
                K[i][j]=K[i-1][j];
            }
            //cout<<K[i][j]<<" ";
        }
        //cout<<endl;
    }
    return K[3][50];
}

int main()
{
    int profits[]={60,100,120};
    int weights[]={10,20,30};
    cout<<KnapSack(profits,weights,50);

    return 0;
}

