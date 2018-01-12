#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include <map>
#include <vector>
#include "TimeInterval.h"
#include <cstring>
#include <stdlib.h>

using namespace std;
 
class Dictionary{
  
  map<char, map<char, vector<string> > > test;
  string userInput;

public: 

  Dictionary(string dictionary, int words){

  
    string line;
    //string dictionary;

    //cout << "Give me the name of the Dictionary (ie: Dictionary.txt): ";
    //cin >> dictionary;

    ifstream myfile(dictionary.c_str());
    if(myfile.is_open()){
    while(getline(myfile, line)){
      
      //cout << line << "\n";
      hashWord(line);
    }//end while
    myfile.close();
    }//end if

    //printDictionary();
    for(int i = 0; i<words; i++){
	cout << "Give me a word to find: ";
  	cin >> userInput;
    	find(userInput);
     }

    }//end constructor


   void hashWord(string word){
	//the file stream is adding a space at the end
	//of the word, causing it to NEVER be equal to 
	//the usersInput.
	
	//remove space
	string rword = word.substr(0, word.size()-1);
	
	//if the word is greater than a single character
	if(word.size() > 2){
		test[tolower(word[0])][word[1]].push_back(rword);
	}else{	
		//else create a spot for single letters with a space as the second mapping
		test[tolower(word[0])][' '].push_back(rword);
	}//end if
	
   }//end hashWord

   void find(string word){

  
	char firstChar;
	char secondChar;

	if(word.size() > 1){
		firstChar = word[0];
		secondChar = word[1];
	}else if(word.size() == 1){
		firstChar = word[0];
		secondChar = ' ';
	}//end if

	vector<string> &dictionaryWord = test[tolower(firstChar)][secondChar];
	bool found = false;
	for(vector<string>::const_iterator it = dictionaryWord.begin(); it != dictionaryWord.end(); ++it){
		string dictWord = *it;
		if(dictWord.compare(word) == 0){
			found = true;
			
		}//end if
	}// end for

	if(found == true) {
		cout << "True" << endl;
		printSimilars(tolower(firstChar), secondChar);
	}else if(found == false){
		cout << "false" << endl;
		printSimilars(tolower(firstChar), secondChar);
	}
   }//end find

   void printSimilars(char firstChar, char secondChar){

	TimeInterval time;
	time.start(); 

	cout << "Here are some similar words: " << endl;
	if(secondChar != ' '){
		for(vector<string>::const_iterator it = test[firstChar][secondChar].begin(); it != test[firstChar][secondChar].end(); ++it){
			cout << *it << endl;
		}//end for
	}else if(secondChar == ' '){
		for(map<char, vector<string> >::const_iterator it = test[firstChar].begin(); it != test[firstChar].end(); ++it){
	    	
			//loop through the second parameter of the second map, vector.
			for(vector<string>::const_iterator lit = it->second.begin(); lit != it->second.end(); ++lit){
				cout << *lit << endl;
			}//end second loop
            	}//end first for loop
	}//end if
	time.stop();

	cout << "Time: " << time.GetInterval() << " micro-seconds" << endl;

   }//end printSimilars

   void printDictionary(){
	int checkSize = 0;
	//loop through the strings first
	for(map<char, map<char, vector<string> > >::const_iterator it = test.begin(); it != test.end(); ++it){
    	    
	    //loop through the second parameter next, map.
     	    for(map<char, vector<string> >::const_iterator lit = it->second.begin(); lit != it->second.end(); ++lit){
	    	
		//loop through the second parameter of the second map, vector.
		for(vector<string>::const_iterator lite = lit->second.begin(); lite != lit->second.end(); ++lite){
			cout << "word: " << *lite << endl;
			checkSize++;
		}//end third loop
            }//end second for loop
         }//end first for loop

	cout << "Size: " << checkSize << endl;
   }//end printTwoLetters

};//end class


int main(int argc, char *argv[]){
  string dictFile = argv[1];
  int wordAmt = 0;
  long charToInt = strtol(argv[2], NULL, 10);
  wordAmt = charToInt;

  Dictionary dictionary(dictFile, wordAmt);
  
  
  return 0;
}
