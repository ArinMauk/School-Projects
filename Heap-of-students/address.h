//address.h
#ifndef ADDRESS_H_EXISTS
#define ADDRESS_H_EXISTS

#include <iostream>
#include <string>

using namespace std;

class Address{
 private:
  string address1;
  string address2;
  string city;
  string state;
  string zip;
 public:
  Address();
  void setAddress1(string address1);
  void setAddress2(string address2);
  void setCity(string city);
  void setState(string state);
  void setZip(string zip);
  string getAddress1();
  string getAddress2();
  string getCity();
  string getState();
  string getZip();
  ~Address();

}; //end class
#endif
