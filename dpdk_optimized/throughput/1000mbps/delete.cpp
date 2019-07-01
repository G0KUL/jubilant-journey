#include <iostream> 
#include <fstream> 

using namespace std; 

int main() { 
	ifstream fin1; 
	ofstream fout;
	string line; 
	int found; 

	fin1.open("netmap_udp_1000mbps.txt");
	fout.open("netmap_udp_1000mbps_delete.txt"); 
	int nl = 7;
	for(int i = 0; i < nl; i++){
		getline(fin1,line);
		//fout << line << endl; 
	}
	while(fin1) { 
		getline(fin1, line);
		found = line.find("datagrams");
		if(found == line.npos)
			fout << line << endl;
	}
	fin1.close(); 
	fout.close();
	return 0; 
} 
