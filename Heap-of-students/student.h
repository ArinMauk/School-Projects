//student.h
#ifndef STUDENT_H_EXISTS
#define STUDENT_H_EXISTS

#include <iostream>
#include <string>
#include "date.h"
#include "address.h"

using namespace std;

class Student{
  private:
	string fName;
	string lName;
	Date DOB;
	Date DOC;
	Address home;
	string GPA;
	string credHrs;
	//string addressInformation[5];
	//string dateInformation[2];
  public:
	Student();
	void setFname(string firstName);
	void setLname(string lastName);
	void setGPA(string GPA);
	void setcrdHrs(string creditHours);
	void setAddressinfo(string info, int addressNum);
	void setDateinfo(string info, int dateNum);
	string getFname();
	string getLname();
	string getGPA();
	string getcrdHrs();
	string getAddressinfo();
	string getDateinfo();
	void reportStudent();
	void unsortedPrint();
	~Student();


}; //end class
#endif
