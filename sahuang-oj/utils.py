# coding=utf-8

chal1 = "a8df8f775e7c8aa780999837c885d70b"
chal2 = "18df8f775e7c8aa780999837c885d70b"
chal3 = "28df8f775e7c8aa780999837c885d70b"

flag1 = "SEKAI{59173801533e53d0e141632d9873d43fefcc80b2426bcc67d7869114b82faac46ee3ca0e85769c40f2598a55d44a7cd4}"
flag2 = "SEKAI{658f3552f59d20a184c7bd437bb1413b5c4ed4bd46a96ee48bab933d4c0245b58fb1539922d1bf327b9e2912201ed9f8}"
flag3 = "SEKAI{875c20e9fcb761e279b02644120942f508ae9efa8e7d9b4782ba100e18d472135f45067dd46add3afeba2654e68e4ab4}"

chals = [chal1, chal2, chal3]

flag_map = {
    chal1: flag1,
    chal2: flag2,
    chal3: flag3
}

c_config = {
    'language_config': {
        'run': {
            'env': ['LANG=en_US.UTF-8', 'LANGUAGE=en_US:en', 'LC_ALL=en_US.UTF-8'], 
            'command': '{exe_path}', 
            'seccomp_rule': {'File IO': 'c_cpp_file_io', 'Standard IO': 'c_cpp'}
        }, 
        'compile': {
            'exe_name': 'main', 
            'src_name': 'main.c', 
            'max_memory': 268435456, 
            'max_cpu_time': 3000, 
            'max_real_time': 10000, 
            'compile_command': '/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c11 {src_path} -lm -o {exe_path}'
        }, 
        'template': '//PREPEND BEGIN\n#include <stdio.h>\n//PREPEND END\n\n//TEMPLATE BEGIN\nint add(int a, int b) {\n  // Please fill this blank\n  return ___________;\n}\n//TEMPLATE END\n\n//APPEND BEGIN\nint main() {\n  printf("%d", add(1, 2));\n  return 0;\n}\n//APPEND END'
    }, 
    'src': '#include <stdio.h>    \nint main(){\n    int a, b;\n    scanf("%d%d", &a, &b);\n    printf("%d\\n", a+b);\n    return 0;\n}'
}

cpp_config = {
    'language_config': {
        'run': {
            'env': ['LANG=en_US.UTF-8', 'LANGUAGE=en_US:en', 'LC_ALL=en_US.UTF-8'], 
            'command': '{exe_path}', 
            'seccomp_rule': {'File IO': 'c_cpp_file_io', 'Standard IO': 'c_cpp'}
        }, 
        'compile': {
            'exe_name': 'main', 
            'src_name': 'main.cpp', 
            'max_memory': 1073741824, 
            'max_cpu_time': 10000, 
            'max_real_time': 20000, 
            'compile_command': '/usr/bin/g++ -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c++14 {src_path} -lm -o {exe_path}'
        }, 
        'template': '//PREPEND BEGIN\n#include <iostream>\n//PREPEND END\n\n//TEMPLATE BEGIN\nint add(int a, int b) {\n  // Please fill this blank\n  return ___________;\n}\n//TEMPLATE END\n\n//APPEND BEGIN\nint main() {\n  std::cout << add(1, 2);\n  return 0;\n}\n//APPEND END'
    }, 
    'src': '#include <bits/stdc++.h>\n\nusing namespace std;\n\nint main() {\n  int x, y;\n  cin >> x >> y;\n  cout << x+y << endl;\n  return 0;\n}'
}

py_config = {
    'language_config': {
        'run': {
            'env': ['LANG=en_US.UTF-8', 'LANGUAGE=en_US:en', 'LC_ALL=en_US.UTF-8', 'PYTHONIOENCODING=utf-8'], 
            'command': '/usr/bin/python3 {exe_path}', 
            'seccomp_rule': 'general'
        }, 
        'compile': {
            'exe_name': '__pycache__/solution.cpython-36.pyc', 
            'src_name': 'solution.py', 
            'max_memory': 134217728, 
            'max_cpu_time': 3000, 
            'max_real_time': 10000, 
            'compile_command': '/usr/bin/python3 -m py_compile {src_path}'
        }, 
        'template': '//PREPEND BEGIN\n//PREPEND END\n\n//TEMPLATE BEGIN\n//TEMPLATE END\n\n//APPEND BEGIN\n//APPEND END'
    }, 
    'src': 'x, y = input().strip().split(" ")\nprint(int(x)+int(y))'
}

java_config = {
    'language_config': {
        'run': {
            'env': ['LANG=en_US.UTF-8', 'LANGUAGE=en_US:en', 'LC_ALL=en_US.UTF-8'], 
            'command': '/usr/bin/java -cp {exe_dir} -XX:MaxRAM={max_memory}k -Djava.security.manager -Dfile.encoding=UTF-8 -Djava.security.policy==/etc/java_policy -Djava.awt.headless=true Main', 
            'seccomp_rule': None, 
            'memory_limit_check_only': 1
        }, 
        'compile': {
            'exe_name': 'Main', 
            'src_name': 'Main.java', 
            'max_memory': -1, 
            'max_cpu_time': 5000, 
            'max_real_time': 10000, 
            'compile_command': '/usr/bin/javac {src_path} -d {exe_dir} -encoding UTF8'
        }, 
        'template': '//PREPEND BEGIN\n//PREPEND END\n\n//TEMPLATE BEGIN\n//TEMPLATE END\n\n//APPEND BEGIN\n//APPEND END'
    }, 
    'src': 'import java.util.Scanner;\npublic class Main{\n    public static void main(String[] args){\n        Scanner in=new Scanner(System.in);\n        int a=in.nextInt();\n        int b=in.nextInt();\n        System.out.println((a+b));  \n    }\n}'
}

go_config = {
    'language_config': {
        'run': {
            'env': ['GODEBUG=madvdontneed=1', 'GOMAXPROCS=1', 'LANG=en_US.UTF-8', 'LANGUAGE=en_US:en', 'LC_ALL=en_US.UTF-8'], 
            'command': '{exe_path}', 
            'seccomp_rule': 'golang', 
            'memory_limit_check_only': 1
        }, 
        'compile': {
            'env': ['GOCACHE=/tmp', 'GOPATH=/tmp', 'GOMAXPROCS=1', 'LANG=en_US.UTF-8', 'LANGUAGE=en_US:en', 'LC_ALL=en_US.UTF-8'], 
            'exe_name': 'main', 
            'src_name': 'main.go', 
            'max_memory': 1073741824, 
            'max_cpu_time': 3000, 
            'max_real_time': 5000, 
            'compile_command': '/usr/bin/go build -o {exe_path} {src_path}'
        }, 
        'template': '//PREPEND BEGIN\n//PREPEND END\n\n//TEMPLATE BEGIN\n//TEMPLATE END\n\n//APPEND BEGIN\n//APPEND END'
    }, 
    'src': 'package main\n\nimport "fmt"\n\nfunc main() {\n    var a, b int\n    fmt.Scanf("%d %d", &a, &b)\n\n    fmt.Println(a + b)\n}'
}

js_config = {
    'language_config': {
        'run': {
            'env': ['LANG=en_US.UTF-8', 'LANGUAGE=en_US:en', 'LC_ALL=en_US.UTF-8'], 
            'command': '/usr/bin/node {exe_path}',
            'seccomp_rule': 'node', 
            'memory_limit_check_only': 1
        }, 
        'compile': {
            'env': ['LANG=en_US.UTF-8', 'LANGUAGE=en_US:en', 'LC_ALL=en_US.UTF-8'],
            'exe_name': 'main.js', 
            'src_name': 'main.js', 
            'max_memory': 1073741824, 
            'max_cpu_time': 3000, 
            'max_real_time': 5000, 
            'compile_command': '/usr/bin/node --check {src_path}'
        }, 
        'template': '//PREPEND BEGIN\n//PREPEND END\n\n//TEMPLATE BEGIN\n//TEMPLATE END\n\n//APPEND BEGIN\n//APPEND END'
    }, 
    'src': "const readline = require('readline');\nconst rl = readline.createInterface({ input: process.stdin });\nrl.on('line', (input) => {\n  if (input === '') {\n    return rl.close();\n  }\n  const [a, b] = input.split(' ').map(Number)\n  console.log(a + b);\n});"
}