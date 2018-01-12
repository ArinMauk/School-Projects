#include <iostream>
#include <list>

using namespace std;


int getSize(){
  int size = 0;
  cout << "How many queens? Enter: ";
  cin >> size;

  return size;
}

bool conflict(int row, int col, int *board, int n){
  int leftD = col;//left diagonal
  int rightD = col;//right diagonal
  int down = 0;

  for(int i=row; i>0; i--){
    if(board[(n*(i-1))+col] == 1){
        return true;
    }
    if(leftD > 0 && board[(n*i)+leftD-(n+1)] == 1){
        return true;
    }
    if(rightD < n-1 && board[(n*i)+rightD-(n-1)] == 1){
        return true;
    }//end if
    leftD--;
    rightD++;
    
  }//end for
  return false;
}//end conflict

void queenProblem(int rowsFilled, int N){
  list<int>queens;
  int board[N*N];
  bool keepGoing = true;
  int temp;
  int currentRow;
  
  for(int i=0; i<N*N; i++){
    board[i] = 0;
  }

  while(keepGoing){ 
    if(rowsFilled == N){
      cout << "Done, Here is the solution: " << endl; 
      for(int i=0; i<(N*N); i++){
        if(i%N == 0){
            cout << endl;
        }//end if
        cout << board[i];
       }//end for
      cout << endl;
      keepGoing = false;
      
    }else{ 
        int i=0;// always constant
        bool hitQueen = conflict(rowsFilled, i, board, N);
        while(hitQueen){
          if(i == (N-1) && queens.back() < (N-1)){
	    
            //grab your previous queen position
            int temp = queens.back();
            board[(rowsFilled-1)*N+temp] = 0;
	    
            //remove the previous queen
            queens.pop_back();
	    
            //increment the value and then check for hitQueen
            hitQueen = conflict(rowsFilled-1, temp + 1, board, N);
            rowsFilled--;
            i = temp + 1;
          }else if(i==(N-1)){
	    
            //remove current queen
            board[(rowsFilled-1)*N+queens.back()] = 0;
            queens.pop_back();
            rowsFilled--;
	    
            //grab previous queens position
            int temp = queens.back();
            board[(rowsFilled-1)*N+temp] = 0;
	    
            //remove that queen
            queens.pop_back();
	    
            //increment that value and then check for a hitQueen
            hitQueen = conflict(rowsFilled-1, temp + 1, board, N);
            rowsFilled--;
            i = temp + 1;
          }else{
            i++;
            hitQueen = conflict(rowsFilled, i, board, N);
          }//end first if in loop
         }
         queens.push_back(i);
	 

         currentRow = N*rowsFilled;
         board[currentRow+i] = 1;
         rowsFilled++;
    }//end end if statement
  }//end while

}//end queensProblem


int main(){
  int size = getSize();
  queenProblem(0, size);


}
