#include <iostream>
#include <omp.h>
#include <cmath>


using namespace std;
#define PI 3.1415926535897932384626433832795

double func(double x, double y, const double a1, const double b1, const double a2, const double b2)
{
    return ((exp(sin(PI * x) * cos(PI * y)) + 1) / ((b1 - a1) * (b2 - a2)));
}
void trapezoidIntegral(const double a1, const double b1, const double a2, const double b2,
              const double h1, const double h2, double* res) {
    int i, j, N, M;
    double sum; // локальна€ переменна€ дл€ подсчета интеграла
    double x = a1, y = a2; // координата точки сетки
    double w = 0.0;

    N = (int)((b1 - a1) / h1); // количество точек сетки интегрировани€
    M = (int)((b2 - a2) / h2);

    sum = 0.0;
    #pragma omp parallel for private(x, y, w) reduction(+: sum)
    for (int i = 0; i <= N; i++) {
        for (int j = 0; j <= M; j++) {
            x = a1 + i * h1;
            if (i > 0 && i < N && j > 0 && j < M) {
                w = 1;
            }
            else {
                if ((i == 0 || i == N) && (j == 0 || j == M))
                    w = 0.25;
                else
                    w = 0.5;
            }

            y = a2 + j * h2;
            sum += w * (exp(sin(PI * x) * cos(PI * y)) + 1);
        }
    }

    *res = h1 * h2 * sum / ((b1 - a1) * (b2 - a2));
}

double experiment(double* res) {
    double stime, ftime; // врем€ начала и конца расчета
    double a = 0.0; // лева€ граница интегрировани€
    double b = 16.0; // права€ граница интегрировани€
    double h1 = 0.01; // шаг интегрировани€
    double h2 = 0.01; // шаг интегрировани€
    stime = clock();
    trapezoidIntegral(a, b, a, b, h1, h2, res); // вызов функции интегрировани€
    ftime = clock();
    return (ftime - stime) / CLOCKS_PER_SEC;
}

int main() {
    int i; // переменна€ цикла
    double time; // врем€ проведенного эксперимента
    double res; // значение вычисленного интеграла
    double min_time; // минимальное врем€ работы
    // реализации алгоритма
    double max_time; // максимальное врем€ работы
    // реализации алгоритма
    double avg_time; // среднее врем€ работы
    // реализации алгоритма
    int numbExp = 10; // количество запусков программы

    // первый запуск
    min_time = max_time = avg_time = experiment(&res);
    // оставшиес€ запуски
    for (i = 0; i < numbExp - 1; i++)
    {
        time = experiment(&res);
        avg_time += time;
        if (max_time < time) max_time = time;
        if (min_time > time) min_time = time;
    }
    // вывод результатов эксперимента
    cout << "execution time : " << avg_time / numbExp << "; " <<
         min_time << "; " << max_time << endl;
    cout.precision(8);
    cout << "integral value : " << res << endl;
    return 0;
}