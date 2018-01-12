//Student.cpp
#include <string>
#include <iostream>
#include "student.h"
#include "date.h"
#include "address.h"

using namespace std;

Student::Student(){

}//end student

void Student::setFname(string firstName){
	Student::fName = firstName;
}//end setFname

void Student::setLname(string lastName){
	Student::lName = lastName;
}//end setLname

void Student::setGPA(string GPA){
	Student::GPA = GPA;
}//end setGPA

void Student::setcrdHrs(string creditHours){
	Student::credHrs = creditHours;
}//end setcrdHrs

void Student::setAddressinfo(string info, int addressNum){
	//Student::addressInformation[addressnum] = info;
	if(addressNum == 0){
		Student::home.setAddress1(info);
	}else if(addressNum == 1){
		Student::home.setAddress2(info);
	}else if(addressNum == 2){
		Student::home.setCity(info);
	}else if(addressNum == 3){
		Student::home.setState(info);
	}else if(addressNum == 4){
		Student::home.setZip(info);
	}
}//end addressInfo

void Student::setDateinfo(string info, int dateNum){
	//Student::dateInformation[dateNum] = info;
	if(dateNum == 0){
		Student::DOB.setDOB(info);
	}else if(dateNum == 1){
		Student::DOC.setDOC(info);
	}

}//end dateInfo

string Student::getFname(){
	return fName;
}//end getFname

string Student::getLname(){
	return lName;
}//end getLname

string Student::getGPA(){
	return GPA;
}//end getGPA

string Student::getcrdHrs(){
	return credHrs;
}//end getcrdHrs

string Student::getAddressinfo(){
	return home.getAddress1() + "," + home.getAddress2() + "," + home.getCity() + "," + home.getState() + "," + home.getZip();
}//end getAddressinfo

string Student::getDateinfo(){
	return DOB.getDOB() + "," + DOC.getDOC();
}//end getDateinfo
Student::~Student(){
	
}
void Student::reportStudent(){
	
}
void Student::unsortedPrint(){

cout << "====================================================================" << endl;
	cout << "STUDENT: " + lName + ", " + fName << endl;
	cout << "DATE OF BIRTH: " + DOB.getDOB() << endl;
	cout << "STUDENTS ACADEMICS: " << endl;
	cout << "GPA: " + GPA << endl;
	cout << "Credit Hours Completed: " + credHrs << endl;
	cout << "Date of Completion: " + DOC.getDOC() << endl;
	cout << "\n" << endl;
	cout << "STUDENT'S ADDRESS INFORMATION: " <<endl;
	cout << "Address 1: " + home.getAddress1() << endl;
	cout << "City: " + home.getCity() << endl;
	cout << "State: " + home.getState() << endl;
	cout << "Zip Code: " + home.getZip() << endl;
	cout << "====================================================================" << endl;

}



