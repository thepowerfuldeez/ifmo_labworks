/* Глава 1. Базовая программа копирования файлов cp. Реализация, использующая библиотеку С. */ 
   /* cp файл1 файл2: Копировать файл1 в файл2. */ 
   #include <stdio.h> 
   #include <errno.h> 
   #define BUF_SIZE 256 

   int main(int argc, char *argv[]) {
    FILE *in_file, *out_file;
    char rec [BUF_SIZE];
    size_t bytes_in, bytes_out;
    if (argc != 3) {
     printf("Использование: срС файл1 файл2\n");
     return 1;
    }
    in_file = fopen(argv [1], "rb");
    if (in_file == NULL) {
     perror(argv[1]);
     return 2;
    }
    out_file = fopen(argv [2], "wb");
    if (out_file == NULL) {
     perror(argv [2]);
     return 3;
    }
    /* Обработать входной файл по одной записи за один раз. */
    while ((bytes_in = fread(rec, 1, BUF_SIZE, in_file)) > 0) {
     bytes_out = fwrite(rec, 1, bytes_in, out_file);
     if (bytes_out != bytes_in) {
      perror("Неустранимая ошибка записи.");
      return 4;
     }
    }
    fclose (in_file);
    fclose (out_file);
    return 0; 
   }
