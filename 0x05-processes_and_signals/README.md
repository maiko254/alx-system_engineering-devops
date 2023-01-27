# 0x05. Processes and signals

### Task 0. What is my PID
* 0-what-is-my-pid - Write a Bash script that displays its own PID.

### Task 1. List your processes
* 1-list_your_processes - Write a Bash script that displays a list of currently running processes.
   * Must show all processes, for all users, including those which might not have a TTY
   * Display in a user-oriented format
   * Show process hierarchy

### Task 2. Show your Bash PID 
* 2-show_your_bash_pid - Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
* Requirements:
   * You cannot use `grep`
   * The third line of your script must be `# shellcheck disable=SC2009`

### Task 3. Show your Bash PID made easy
* 3-show_your_bash_pid_made_easy - Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`
* Requirements:
   * You cannot use `ps`

### Task 4. To infinity and beyond
* 4-to_infinity_and_beyond - i Bash script that displays `To infinity and beyond` indefinitely.
   * In between each iteration of the loop, add a `sleep 2`

### Task 5. Don't stop me now!
* 5-dont_stop_me_now - Write a Bash script that stops `4-to_infinity_and_beyond` process.
* Requirements:
   * You must use `kill`

### Task 6. Stop me if you can
* 6-stop_me_if_you_can - Write a Bash script that stops `4-to_infinity_and_beyond` process.
* Requirements:
   * You cannot use `kill` or `killall`

### Task 7. Highlander
* 7-highlander - Write a Bash script that displays:
   * `To infinity and beyond` indefinitely
   * With a `sleep 2` in between each iteration
   * `I am invincible!!!` when receiving a `SIGTERM` signal

### Task 8. Beheaded process
* 8-beheaded_process - Write a Bash script that kills the process `7-highlander`.