/* Глава 1. Базовая программа копирования файлов cp. Реализация, в которой для повышения удобства использования и производительности программы используется функция Windows CopyFile. */
   /* cpCF файл1 файл2: Копировать файл1 в файл2. */
   #include <windows.h> 
   #include <stdio.h>

   int main (int argc, LPTSTR argv []) {
    if (argc != 3) {
     printf ("Использование: cpCF файл1 файл2\n");
     return 1;
    }
    if (!CopyFile(argv[1], argv[2], FALSE)) {
     printf("Ошибка при выполнении функции CopyFile: %x\n", GetLastError());
     return 2;
    }
    return 0; 
   } 
