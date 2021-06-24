#include <iostream>
#include <sstream>
#include <fstream>

struct Objeto {};
std::ostream &operator<<(std::ostream &o, const Objeto objeto)
{
	return o << "Mostramos el objeto " << &objeto;
}

int main()
{
	Objeto obj;
	std::ofstream archivo{"archivo.txt"};
	std::ostringstream texto;

	archivo << obj;   // Enviamos el objeto a un flujo de archivo.
	texto << obj;     // Enviamos el objeto a un flujo de texto.
	std::cout << obj; // Enviamos el objeto al búfer de consola.

	return 0;
}