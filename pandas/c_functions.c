#include <stdio.h>
#include <math.h>

void c_rolling(const double *indatav, int nrows, int w_size, double *outdatav) {
    for (int i = w_size - 1; i < nrows; i++) {
        double sum = 0;
        int count = 0;
        for (int j = 0; j < w_size; j++) {
            sum += indatav[i - j];
            count++;
        }
        outdatav[i] = sum / count;
    }
}