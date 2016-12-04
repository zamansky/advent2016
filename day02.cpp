#include <iostream>
#include <string>
#include <fstream>

/*
std::string board[] = {"     ",
		       " 123 ",
		       " 456 ",
		       " 789 ",
		       "     "};

*/

/* Board for part 2 */
std::string board[] = {"       ",
		       "   1   ",
		       "  234  ",
		       " 56789 ",
		       "  ABC  ",
		       "   D   ",
		       "       "
};


int main ()
{
  std::string line,code="";
  //int r=1, c=1; // start location for part 1
  int r=3, c=1;  // start location for aprt 

  int dr,dc;
  std::ifstream ifile ("day02.dat");
  if (ifile.is_open()){
    while (getline(ifile,line)){
      for (auto ch  : line){
	dr=0;
	dc=0;
	switch(ch) {
	case 'U':
          dr=-1;
	  break;
	case 'D':
	  dr=1;
	  break;
	case 'L':
	  dc=-1;
	  break;
	case 'R':
	  dc=1;
	  break;
	}
	if (board[r+dr][c+dc] != ' '){
	  r=r+dr;
	  c=c+dc;
	}
	  
        

      }
      code = code + board[r][c];
  
    }
    std::cout << code << std::endl;
  }
  
  return 0;
}

