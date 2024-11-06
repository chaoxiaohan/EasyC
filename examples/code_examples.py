CODE_EXAMPLES = {
    "基础示例": {
        "Hello World": {
            "code": """#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}""",
            "description": "最基本的C程序示例"
        },
        "求和计算": {
            "code": """#include <stdio.h>

int main() {
    int a, b;
    printf("请输入两个数字：\\n");
    scanf("%d %d", &a, &b);
    printf("和为：%d\\n", a + b);
    return 0;
}""",
            "description": "演示基本的输入输出和计算"
        }
    },
    "流程控制": {
        "九九乘法表": {
            "code": """#include <stdio.h>

int main() {
    for(int i = 1; i <= 9; i++) {
        for(int j = 1; j <= i; j++) {
            printf("%d×%d=%-3d ", j, i, i*j);
        }
        printf("\\n");
    }
    return 0;
}""",
            "description": "使用嵌套循环打印九九乘法表"
        },
        "猜数字游戏": {
            "code": """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(0));
    int number = rand() % 100 + 1;
    int guess, tries = 0;
    
    printf("我已经想好了一个1-100之间的数字！\\n");
    
    do {
        printf("请猜一个数字：");
        scanf("%d", &guess);
        tries++;
        
        if(guess > number)
            printf("太大了！\\n");
        else if(guess < number)
            printf("太小了！\\n");
        else
            printf("恭喜你，猜对了！你总共猜了%d次。\\n", tries);
    } while(guess != number);
    
    return 0;
}""",
            "description": "简单的猜数字游戏，练习循环和条件判断"
        }
    },
    "数组操作": {
        "冒泡排序": {
            "code": """#include <stdio.h>

void bubbleSort(int arr[], int n) {
    for(int i = 0; i < n-1; i++) {
        for(int j = 0; j < n-i-1; j++) {
            if(arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    printf("排序前：\\n");
    for(int i = 0; i < n; i++)
        printf("%d ", arr[i]);
        
    bubbleSort(arr, n);
    
    printf("\\n排序后：\\n");
    for(int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    
    return 0;
}""",
            "description": "使用冒泡排序算法对数组进行排序"
        }
    }
}