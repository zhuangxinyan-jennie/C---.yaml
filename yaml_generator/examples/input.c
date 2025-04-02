void example_function(int *data, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            data[i * size + j] *= 2;
        }
    }
}