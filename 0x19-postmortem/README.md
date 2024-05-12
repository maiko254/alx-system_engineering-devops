## **Incident Postmortem: WordPress Website Outage**

### **Issue Summary**

- **Duration**: The outage occurred on May 10, 2024, from 2:00 AM to 4:30 AM (UTC-7).
- **Impact**: The WordPress website was completely down, resulting in a 500 server error for all users.
- **User Experience**: Visitors encountered blank screens and error messages, affecting 100% of site traffic.
- **Root Cause**: A mispelled file name (`class-wp-locale.phpp`) in the `wp-settings.php` file caused the issue.

### **Timeline**

1. **Detection**:
   - Our monitoring system alerted us about increased HTTP 500 errors.

2. **Misleading Paths**:
   - I suspected a misconfiguration or code issue.
   - Checked apache server logs, but no obvious errors were found.
   - I ran the command sudo apache2ctl -t to check the validity of the apache2 config file and got a Syntax OK
   - Investigated server resource utilization, but everything seemed normal.

3. **Investigation**:
   - Checked apache configuration file in sites available folder and found the content was being served from /var/www/html folder
   - Checked for apache2 processes running using ps aux | grep apache2 and found two, root and www-data.
   - Using strace on both processes, I found no errors in the root process and an error in www-data process.
   - strace on www-data returned a ENOENT (No such file or directory) error as it could not access the file /var/www/html/wp-includes/class-wp-locale.phpp.
   - I checked in the folder /var/www/html/wp-includes/ and there was a file named class-wp-locale.php, this led me to suspect a wrong file name might be used in one of the files in the root of the server.
   - I started checking each file in the /var/www/html/ for pattern matching class-wp-locale.phpp and found a match in the wp-settings.php file.
   - I deleted the extra p and on curling the server, the website was served as expected.


4. **Resolution**:
   - Identified the root cause: the mispelled file name (`class-wp-locale.phpp`).
   - Created a Puppet manifest to run a `sed` command, replacing the incorrect name with the correct one (`class-wp-locale.php`).
   - Deployed the fix to the server.

### **Root Cause and Resolution**

- **Root Cause**:
  - The `wp-settings.php` file referenced an incorrect class file (`class-wp-locale.phpp`) due to a typo.
  - This caused PHP to fail during initialization, leading to the 500 server error.

- **Resolution**:
  - I corrected the file name using a Puppet manifest.
  - Verified the fix by monitoring server logs and confirming successful requests.

### **Corrective and Preventative Measures**

1. **Code Review Process**:
   - Implement stricter code review practices to catch typos and misconfigurations.
   - Enforce linting rules to prevent similar issues.

2. **Automated Testing**:
   - Enhance automated testing to cover critical paths.
   - Include tests for file references and common configuration files.

3. **Monitoring and Alerts**:
   - Set up additional monitoring for critical files and server health.
