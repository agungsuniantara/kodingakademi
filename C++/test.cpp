#include <iostream> 

using namespace std;

int main(){
    float tinggi, weight, score;

    cout << "tinggi : ";
    cin >> tinggi;
    cout << "berat : ";
    cin >> weight;

    score = weight / tinggi;
    if (score < 18.5){
        cout << "kurus";
    }
    else if (score >= 18.5 && score <= 25){
        cout << "Normal";
    }
    else if (score > 25){
        cout << "Kelebihan berat badan";
    }
}