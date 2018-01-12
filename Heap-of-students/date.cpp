#include <string>
#include <iostream>
#include "date.h"

using namespace std;

Date::Date(){

}

void Date::setDOB(string DOB){
	Date::dateOfbirth = DOB;
}// end setDay

void Date::setDOC(string DOC){
	Date::dateOfcompl = DOC;
}// end setMonth

string Date::getDOB(){
	return dateOfbirth;
}//end getDay

string Date::getDOC(){
	return dateOfcompl;
}//end getMonth
Date::~Date(){

}