#include <iostream>
#include <bitset>

int main() {
	int8_t a = 5;

	std::cout << "   a   = " << std::bitset<8*sizeof(a)>(a) << " =  " << int(a) << std::endl;
	std::cout << "~a+1   = " << std::bitset<8*sizeof(a)>(~a+1) << " = " << int(~a+1) << std::endl;
	std::cout << "bits   = " << std::bitset<8*sizeof(a)>(a^((1 << 8) - 1) + 1) << " = " << int(a^((1 << 8) - 1) + 1) << std::endl;
	int8_t b = 1 << 8;
	std::cout << "1<<8   = " << std::bitset<8*sizeof(a)>(b) << " = " << int(b) << std::endl;
	int8_t c = (1 << 8) - 1;
	std::cout << "1<<8-1 = " << std::bitset<8*sizeof(a)>(c) << " = " << int(c) << std::endl;
	std::cout << "^      = " << std::bitset<8*sizeof(a)>(a^c) << " = " << int(a^c) << std::endl;
	std::cout << "^ +1   = " << std::bitset<8*sizeof(a)>((a^c)+1) << " = " << int((a^c)+1) << std::endl;

}
