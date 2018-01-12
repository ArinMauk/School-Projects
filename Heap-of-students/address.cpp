//address.cpp
#include <string>
#include <iostream>
#include "address.h"

using namespace std;

Address::Address(){

}

void Address::setAddress1(string address1){
	Address::address1 = address1;
}// end setAddress1

void Address::setAddress2(string address2){
	Address::address2 = address2;
}// end setAddress2

void Address::setCity(string city){
	Address::city = city;
}// end setCity

void Address::setState(string state){
	Address::state = state;
}// end setState

void Address::setZip(string zip){
	Address::zip = zip;
}// end setZip

string Address::getAddress1(){
	return address1;
}// end getAddress1

string Address::getAddress2(){
	return address2;
}// end getAddress2

string Address::getCity(){
	return city;
}//end getCity

string Address::getState(){
	return state;
}// end getState

string Address::getZip(){
	return zip;
}// end getZip
Address::~Address(){

}
