studentdata: address.o date.o student.o main.o
	g++ address.o date.o student.o main.o -o studentdata
address.o: address.cpp address.h
	g++ -c address.cpp
date.o: date.cpp date.h
	g++ -c date.cpp
student.o: student.cpp student.h
	g++ -c student.cpp student.h
main.o: main.cpp
	g++ -c main.cpp
clean:
	rm -f *.o
	rm studentdata