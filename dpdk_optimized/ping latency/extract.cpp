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
	ofstream fout; 
	string line;

	fin1.open("netmap_100__.txt");
	
	fout.open("100mbps.txt"); 
	
	while(fin1){
		getline(fin1, line);
		vector<string> v = split(line);
		if(v.size())
			fout << v[v.size() - 1] << endl; 
	}
	fin1.close(); 
	fout.close();
	return 0; 
} 