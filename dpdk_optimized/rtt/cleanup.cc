#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;


int main() { 
	ifstream fin; 
	ofstream fout;
	string line; 
	double num;
	fin.open("fdemu_100.txt");
	fout.open("fdemu_100mbps.txt");
	while(fin) { 
		getline(fin, line);
		if(line.size()){
			num = atof(line.c_str());
			if(num != 0)
				fout << num << endl;
		}
	}
	fin.close(); 
	fout.close();
	return 0; 
} 