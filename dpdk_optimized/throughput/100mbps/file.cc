#include <cstring>
#include <iostream> 
#include <fstream> 
#include <vector>
using namespace std; 

vector<string> split(string s){
	vector<string> v;
	int j = 0;
	for(int i = 0; i < s.size(); i++){
		if(s[i] == ' '){
			v.push_back(s.substr(j, i - j));
			while(s[i] == ' ' && i < s.size()) i++;
			j = i;
		}
	}
	return v;
}

int main() 
{ 
	ifstream fin1;
	ifstream fin2;
	ifstream fin3;
	ifstream fin4;
	ifstream fin5;
	ifstream fin6;
	ofstream fout; 
	string line, line1; 

	fin1.open("fdemu_tcp_100mbps.txt");
	fin2.open("netmap_tcp_100mbps.txt");
	fin3.open("dpdk_tcp_100mbps.txt");
	fin4.open("dpdk_udp_100mbps.txt");
	fin5.open("netmap_udp_100mbps.txt");
	fin6.open("fdemu_udp_100mbps.txt");
	
	fout.open("100mbps.txt"); 
	getline(fin1, line);
	getline(fin2, line);
	getline(fin3, line);
	getline(fin4, line);
	getline(fin5, line);
	getline(fin6, line);

	for(int i = 0; i < 940; i++) { 
		getline(fin1, line);
		vector<string> v = split(line);
		if(v.size())
			fout << v[v.size() - 3] << "\t\t"; 
		getline(fin2, line);
		v = split(line);
		if(v.size())
			fout << v[v.size() - 3] << "\t\t"; 

		getline(fin3, line);
		v = split(line);
		if(v.size())
			fout << v[v.size() - 3] << " \t\t"; 

		getline(fin4, line1);
		v = split(line1);
		if(v.size()){
			fout << v[v.size() - 10] << " \t\t";
		}
		getline(fin5, line1);
		v = split(line1);
		if(v.size())
			fout << v[v.size() - 10] << " \t\t"; 

		getline(fin6, line1);
		v = split(line1);
		if(v.size())
			fout << v[v.size() - 10] <<endl; 
	} 
	fin1.close(); 
	fin2.close(); 
	fin3.close(); 
	fin4.close(); 
	fin5.close(); 
	fin6.close(); 

	fout.close();
	return 0; 
} 