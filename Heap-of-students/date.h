//date.h
#ifndef DATE_H_EXISTS
#define DATE_H_EXISTS

#include <iostream>
#include <string>

using namespace std;

class Date {
 private:
  string dateOfbirth;
  string dateOfcompl;
 public:
  Date();

  void setDOB(string DOB);
  void setDOC(string DOC);
  
  string getDOB();
  string getDOC();
  ~Date();
}; //end class
#endif
