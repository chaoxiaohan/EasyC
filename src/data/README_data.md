# C语言练习题数据结构说明文档

## 整体结构

数据存储采用 JSON 格式，主要包含以下层级结构：

```
src/data/
├── exercises/
│   ├── index.json           # 章节目录索引
│   ├── chapter1/           # 第1章 - C语言基础
│   │   ├── metadata.json   # 章节元数据
│   │   └── exercises/      # 练习题
│   │       ├── ex1_1.json
│   │       └── ex1_2.json
│   ├── chapter2/           # 第2章 - 控制流程
│   │   └── ...
│   ├── chapter3/           # 第3章 - 数组与函数
│   │   └── ...
│   └── ...
└── README_data.md
```
## 文件格式说明

1. index.json
包含所有章节的基本信息：
- chapters: 章节数组
  - id: 章节唯一标识符
  - title: 章节标题
  - path: 章节路径

2. chapter{n}/metadata.json
包含具体章节的详细信息：
- id: 章节唯一标识符
- title: 章节标题
- exercises: 练习题数组
  - id: 练习题唯一标识符
  - title: 练习题标题
  - difficulty: 难度等级
  - path: 练习题路径

3. chapter{n}/exercises/ex{n}{m}.json
包含具体练习题的详细信息：
- id: 练习题唯一标识符
- title: 练习题标题
- difficulty: 难度等级（easy/medium）
- description: 题目描述
- test_cases: 测试用例数组
  - input: 输入数据
  - expected_output: 期望输出
- solution_template: 解答模板代码

## 当前内容概览

### 第1章：C语言基础
- ex1_1: Hello World (简单)
- ex1_2: 整数相加 (简单)

### 第2章：控制流程
- ex2_1: 判断奇偶数 (简单)
- ex2_2: 计算阶乘 (中等)

### 第3章：数组与函数
- ex3_1: 数组最大值 (中等)
- ex3_2: 反转数组 (中等)

## 使用说明

1. 每个练习题都包含完整的测试用例
2. 所有代码模板都提供了基本的框架结构
3. 难度分为简单(easy)和中等(medium)两级
4. 每个练习题都有明确的输入输出格式说明