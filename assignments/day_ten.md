---

# Problem 1 : Finding Duration of Log file (End Time - Start Time)  

---
## Task 
* Name the script - *twiki_log_duration.py*. 
* Work on Log file - *twiki_sized.log* 
* Details of fields are: 
```
$ head -1 twiki_sized.log 
| 2017-01-01 - 07:09:07 | LyndonJohnson | view     | Main.WebHome     | 392441       | 22.169.249.196     | 
    ^^ Date     ^^ time     ^^ User      ^^ Action  ^^ Topic Name       ^^ Size in MB ^^ IP used to access 
```
* Find the duration of time for this log file.  Use datetime module. 

## Expected Output  
```
$ twiki_log_duration.py

The duration of log is: 1 day 3 hrs 20 minutes 40 seconds. a

```

---

