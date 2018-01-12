#include <string>
#include <iostream>
#include <cstdlib>
#include "address.h"
#include "date.h"
#include "student.h"
#include <fstream>
#include <sstream>

using namespace std;



int main(){
	Student *S = new Student[50];

	ifstream inFile;
	inFile.open("data.dat");

	string line;
	int i = 0;
	
	while(!inFile.eof()){
	getline(inFile, line);
	if(line != ""){
		int adrsNum = 0;
		int dateNum = 0;
		int lastCommaAt = 0;
		int currentCommaAt = 0;
		int totCommas = 0;
		//cout << line << endl;
		for(int k=0; k<line.length(); k++){
			lastCommaAt = currentCommaAt;
			if(line.at(k) == ','){
				currentCommaAt = k;
				//stringstream ss;
				//ss << "K= " << k<< " current Comma = " << currentCommaAt<< endl;
				//cout << ss.str();
				totCommas++;
			} //end if
			
			//CURRENT PROBLEM: 		
			//NOTE: An instance of student can't access it's private variables, the private variables have connections to 
			//address and date. Thus, a method must be made, in the class student, that takes in data from an instance.
			//That data can then access the private variables.
			if(lastCommaAt == currentCommaAt){
                                   
			}else{  
				if(totCommas == 1){
					string lNameinfo = line.substr(0, currentCommaAt);
					S[i].setLname(lNameinfo);
				}else if(totCommas == 2){
					string info = line.substr(lastCommaAt+1, currentCommaAt-lastCommaAt-1);
					S[i].setFname(info);
				}else if(totCommas == 3 || totCommas == 4 || totCommas == 5 || totCommas == 6 || totCommas == 7){
					string info = line.substr(lastCommaAt+1, currentCommaAt-lastCommaAt-1);
					S[i].setAddressinfo(info, adrsNum);
					adrsNum++;
				}else if(totCommas == 8 || totCommas == 9){
					string info = line.substr(lastCommaAt+1, currentCommaAt-lastCommaAt-1);
					S[i].setDateinfo(info, dateNum);
					dateNum++;
				}else if(totCommas == 10){
					string info = line.substr(lastCommaAt+1, currentCommaAt-lastCommaAt-1);
					S[i].setGPA(info);
					string crdHrsinfo = line.substr(lastCommaAt+1, line.length());
					S[i].setcrdHrs(crdHrsinfo);
				}// end if
			}//end if
			        
			}//end for
			        
		i++;            
                                
		}//end if       
		                
	}//end while
	
	inFile.close();

	for(int i=0; i<50; i++){
		cout << "STUDENT: " + S[i].getLname() + ", " + S[i].getFname() << endl;
	}

	for(int i=0; i<50; i++){
		S[i].unsortedPrint();
	}
	
	delete[] S;
	return 0;
}//end main