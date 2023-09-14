#include <stdio.h>
#include <omp.h>
#include <iostream>
#include<math.h>

using namespace std;


double func(double x)
{
    return (1.0 / sqrt(1.0 - x * x));
}


void integral(const double a, const double b, const double h, double* res) {
	int i, n;
	double sum; // локальна€ переменна€ дл€ подсчета интеграла
	double x; // координата точки сетки
	n = (int)((b - a) / h); // количество точек сетки интегрировани€

	sum = 0.0;

	#pragma omp parallel for private(x) reduction(+: sum)
	for (i = 0; i < n; i++)
	{
		x = a + i * h + h / 2.0;
		sum += func(x) * h;
	}
	*res = sum;
}

void integralSimpson(const double a, const double b, int n, double* res) {
	double integration = 0.0, k, h;
    int i;

	h = (b - a) / 2 * n;

    integration = func(a) + func(b);

    #pragma omp parallel for private(k) reduction(+: integration)
    for (i = 1; i <= n - 1; i++)
    {
        k = a + i * h;

        if (i % 2 == 0)
        {
            integration = integration + 2.0 * (func(k));
        }
        else
        {
            integration = integration + 4.0 * (func(k));
        }

    }

    integration = integration * h / 3.0;

	*res = integration;
}


double experiment(double* res)
{
	double stime, ftime; // врем€ начала и конца расчета
	double a = 0.0; // лева€ граница интегрировани€
	double b = 1.0; // права€ граница интегрировани€
	double h = 0.0001; // шаг интегрировани€
	int n = 6;
	stime = clock();
	integral(a, b, h, res); // вызов функции интегрировани€
	ftime = clock();
	return (ftime - stime) / CLOCKS_PER_SEC;
}

int main()
{
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

