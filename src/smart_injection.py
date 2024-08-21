#!/usr/bin/env python3
from re import S
import subprocess
import os
import glob
import context_analysis

def run_sqlmap(command):
    # start a new SQLMap process
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Read the standard output and error
    stdout, stderr = process.communicate()

    # Return the output
    return stdout, stderr

def main():
    # Print welcome message
    print("Welcome to the Smart Injection! -- An intelligent automatic SQL Injection and database takeover tool based on SQLMap and LLM technology.\n")
    print("This tool is designed to help you to automatically detect and exploit SQL injection vulnerabilities in web applications.\n")
    

    # Print the basic usage of SQLMap
    sqlmap_init_command = ['sqlmap', '--help']
    stdout, stderr = run_sqlmap(sqlmap_init_command)
    print("SQLMap Basic Usage:\n")
    print(stdout)

    loop_count = 0

    # Specify the directory to save the output
    output_dir = "../session/sqlmap_out"
    os.makedirs(output_dir, exist_ok=True)

    # Main loop
    while True:
        # Prompt the user to input SQLMap parameters or exit
        print("Please input SQLMap parameters to continue. You can input 'exit' to quit the program.\n")
        user_input = input("SQLMap parameters: ")
        
        if user_input.lower() == 'exit':
            break

        loop_count += 1

        # Construct the SQLMap command
        sqlmap_command = ['sqlmap'] + user_input.split()

        # Run SQLMap and get the output
        stdout, stderr = run_sqlmap(sqlmap_command)

        # Print the SQLMap output
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
        print("Injection Suggestions:")
        context_analysis.suggestion_generation(loop_count)
        print("\n------------------------------------------")


    # Delete all saved files upon exit
    for file in glob.glob(os.path.join(output_dir, "Loop_*.txt")):
        os.remove(file)
    print("\nAll temporary session files have been cleared.\n")

if __name__ == "__main__":
    main()