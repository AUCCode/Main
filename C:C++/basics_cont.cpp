/*
Written By RSimon for the AUC Code Club 
*/

#include <iostream> // This is a preprocessor statement, it tells the computer to get the file inside the <> so that it is usable

// Functions
// functions are reusable lines code that allows programmers to do certain tasks without having to type out it all over again
// In C++, every function will have a declaratory statement in which the return of the function is declared
// They follow the same convention for varialbes
/*

int/bool/float/char function_name(param1, param2, param3...){
    return something;
}

*/

int add(int x, int y){
    // This function will take in 2 integers, (x,y), and add them together. It returns an integer.
    return x + y; 
}

float area_of_circle(float radi){
    // This function will take in a radius and find the area of the circle.
    return (radi * radi) * 3.1415; 
}

bool opposite(bool val){
    // This will take in a truth value and replace it with the opposite value
    return  not val; 
}

// Main Function 
// Every C++ program will have a main function that returns an integer

int main() {
    std::cout << "Hello World\n"; 
    std::cout << "Add 2 + 3 = " << add(2,3) << "\n";
    std::cout << "Area of circle with radius 1 = " << area_of_circle(1) << "\n";
    std::cout << "Opposite of True = " << opposite(true) << "\n";
}

/* 
Output: 
    Hello World
    5
    3.1415
    0
*/
