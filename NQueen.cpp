#include <iostream>

using namespace std;

int rd[30]={0};
int ld[30]={0};
int cl[30]={0};

int board[4][4]={{0,0,0,0},
                {0,0,0,0},
                {0,0,0,0},
                {0,0,0,0}};

bool solve(int col,int x){
    
    if(col>=4)return true;
    if(col==x)return solve(col+1,x);
    for(int i=0;i<4;i++){
        if(ld[i-col+3]==0 and rd[i+col]==0 and cl[i]==0){
            ld[i-col+3]=1;
            rd[i+col]=1;
            cl[i]=1;
            board[i][col]=1;
            //cout<<i<<col<<endl;
            if(solve(col+1,x))return true;
            ld[i-col+3]=0;
            rd[i+col]=0;
            cl[i]=0;
            board[i][col]=0;
            
        }
    }
    return false;
}

int main(){
    int i,x;
    cout<<"Enter row no."<<endl;
    cin>>i;
    cout<<"Enter column no."<<endl;
    cin>>x;
    cl[i]=rd[i+x]=ld[i-x+3]=board[i][x]=1;
    //cout<<ld[2]<<endl;
    if(solve(0,x)){
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cout<<board[i][j]<<" ";
            }
            cout<<endl;
        }
}
    
    else
        cout<<"No solution is possible with this position of first queen"<<endl;
    
}
                 
                    

