#!/usr/bin/env python3
import subprocess
import os
import glob
import context_analysis

def run_sqlmap(command):
    # 启动 SQLMap 进程
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # 读取 SQLMap 的输出
    stdout, stderr = process.communicate()

    # 返回输出
    return stdout, stderr

def main():
    # 欢迎信息
    print("Welcome to the Smart Injection! -- An intelligent automatic SQL Injection and database takeover tool based on SQLMap and LLM technology.\n")
    print("This tool is designed to help you to automatically detect and exploit SQL injection vulnerabilities in web applications.\n")
    

    # 打印 SQLMap 的基本用法
    sqlmap_init_command = ['sqlmap', '--help']
    stdout, stderr = run_sqlmap(sqlmap_init_command)
    print("SQLMap Basic Usage:\n")
    print(stdout)

    loop_count = 0

    # Specify the directory
    output_dir = "../session/sqlmap_out"
    os.makedirs(output_dir, exist_ok=True)

    # 主循环
    while True:
        # 读取用户输入
        print("Please input SQLMap parameters to continue. You can input 'exit' to quit the program.\n")
        user_input = input("SQLMap parameters: ")
        
        if user_input.lower() == 'exit':
            break

        loop_count += 1

        # 构建 SQLMap 命令
        sqlmap_command = ['sqlmap'] + user_input.split()

        # 运行 SQLMap
        stdout, stderr = run_sqlmap(sqlmap_command)

        # 打印输出
        print("SQLMap Output:\n")
        print("------------------------------------------\n")
        print(stdout)

        if stderr:
            print("SQLMap Errors:")
            print(stderr)
        print("------------------------------------------\n")
        # Save output to output directory
        filename = os.path.join(output_dir, f"loop_{loop_count}.txt")
        with open(filename, 'w') as file:
            file.write(f"loop_{loop_count}" + " SQLMap Output:\n")
            file.write(stdout)
            if stderr:
                file.write("\nSQLMap Errors:\n")
                file.write(stderr)
        print(f"Output saved to {filename}")
        print("\n------------------------------------------\n")
        print("Context Analysis:")
        print("\n------------------------------------------")
        context_analysis.summarize_context(loop_count)
        print("\n------------------------------------------\n")

    # Delete all saved files upon exit
    for file in glob.glob(os.path.join(output_dir, "Loop_*.txt")):
        os.remove(file)
    print("\nAll temporary session files have been cleared.\n")

if __name__ == "__main__":
    main()