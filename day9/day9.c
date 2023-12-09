#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <string.h>
#include <ctype.h>

int datapoints1[6] = {0, 3, 6, 9, 12, 15};
int datapoints2[6] = {1, 3, 6, 10, 15, 21};
int datapoints3[6] = {10, 13, 16, 21, 30, 45};
int* datapoints[3] = {datapoints1, datapoints2, datapoints3};

const char *input = "input.txt";

int* derive_datapoints(int* input_datapoints, int array_length){
    //printf("Length of Array: %d\n", array_length);
    int* derivative = malloc(array_length*sizeof(int));
    for (int i = 1; i < array_length; i++){
        derivative[i-1] = input_datapoints[i] - input_datapoints[i-1];
    }
    return derivative;
}

int nullcheck(int* input_datapoints, int array_length) {
    int not_null = 1;
    for (int i = 0; i < array_length; i++) {
        if (input_datapoints[i] != 0) {
            not_null = 0;
            break;
        }
    }
    return not_null;
}

void is_nulled (int nulled) {
    if (nulled == 1){
        //printf("Array is nulled\n");
    }
    else {
        //printf("Array isn't nulled\n");
    }
}

//Part 1
int recursive_jank(int* input_datapoints, int array_length) {
    int* derivative = derive_datapoints(input_datapoints, array_length);
    is_nulled(nullcheck(input_datapoints, array_length));
    if(nullcheck(input_datapoints, array_length)) {
        return 0;
    }
    return (recursive_jank(derivative, array_length-1) + input_datapoints[array_length-1]);
}

//Part 2
int backwards_recursive_jank(int* input_datapoints, int array_length) {
    int* derivative = derive_datapoints(input_datapoints, array_length);
    is_nulled(nullcheck(input_datapoints, array_length));
    if(nullcheck(input_datapoints, array_length)) {
        return 0;
    }
    // this entire line was part 2 of day 9
    return (input_datapoints[0] - backwards_recursive_jank(derivative, array_length-1));
}

void janky_strtoint (char* content, int* numbers){    
    if(content){
        int position = 0;
        int number = 0;
        numbers[0] = 0;
        int numbers_position = 1;
        int negative = 1;
        while(content[position] != '\0'){
            if(content[position]){
                if(isdigit(content[position])) {
                    number = number*10 + ((int) content[position]) -48;
                }
                else{
                    if(content[position] != '-'){
                    number = number * negative;
                    numbers[numbers_position] = number;
                    number = 0;
                    numbers_position++;
                    numbers[0]++;
                    negative = 1;
                    }
                    else {
                        negative = -1;
                    }
                }
                position++;
            }
        }
    }

}

int main(int argc, char *argv[]) {
    int total_sum = 0;
    int total_sum_backwards = 0;
    FILE *input_file = fopen(input, "r");

    struct stat sb;
    stat(input, &sb);

    char *file_contents = malloc(sb.st_size);
    int numbers[50];
    while(fgets(file_contents, sb.st_size, input_file)){
        janky_strtoint(file_contents, numbers);
        total_sum += recursive_jank(&numbers[1], numbers[0]);
        total_sum_backwards += backwards_recursive_jank(&numbers[1], numbers[0]);
        //printf("\n");
        //printf("Amount of numbers: %d\n", numbers[0]);
        //printf("%s", file_contents);
    }

    fclose(input_file);

    printf("Total Sum: %d\n", total_sum);
    printf("%d :muS latoT", total_sum_backwards);  
}
