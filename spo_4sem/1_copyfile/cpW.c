/* Глава 1. Базовая программа копирования файлов cp. Реализация, использующая Windows. */
   /* cpW файл1 файл2: Копировать файл1 в файл2. */ 
   #include <windows.h> 
   #include <stdio.h> 
   #define BUF_SIZE 256 

   int main (int argc, LPTSTR argv []) {
    HANDLE hIn, hOut;
    DWORD nIn, nOut;
    CHAR Buffer [BUF_SIZE];
    if (argc != 3) {
     printf ("Использование: cpW файл1 файл2\n");
     return 1;
    }
    hIn = CreateFile(argv [1], GENERIC_READ, 0, NULL, OPEN_EXISTING, 0, NULL);
    if (hIn == INVALID_HANDLE_VALUE) {
     printf("Невозможно открыть входной файл. Ошибка: %х\n", GetLastError());
     return 2;
    }
    hOut = CreateFile(argv[2], GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    if (hOut == INVALID_HANDLE_VALUE) {
     printf("Невозможно открыть выходной файл. Ошибка: %x\n", GetLastError()); 
     return 3;
    }
    while (ReadFile(hIn, Buffer, BUF_SIZE, &nIn, NULL) && nIn > 0) {
     WriteFile(hOut, Buffer, nIn, &nOut, NULL);
     if (nIn != nOut) {
      printf ("Неустранимая ошибка записи: %x\n", GetLastError());
      return 4;
     }
    }
    CloseHandle(hIn);
    CloseHandle(hOut);
    return 0; 
   }
