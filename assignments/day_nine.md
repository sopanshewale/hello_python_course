---

# Problem 1 : Application Log Analysis

---
## Task 
* Name the script - *twiki_log_analysis.py*. 
* Work on Log file - *twiki_sized.log* 
* Details of fields are: 
```
$ head -1 twiki_sized.log 
| 2017-01-01 - 07:09:07 | LyndonJohnson | view     | Main.WebHome     | 392441       | 22.169.249.196     | 
    ^^ Date     ^^ time     ^^ User      ^^ Action  ^^ Topic Name       ^^ Size in MB ^^ IP used to access 
```
* Find the topics for which maximum data was transffered. 
* You need to add data for actions on a particular topic  

## Expected Output  
```
$ twiki_log_analysis.py

Maximum Size and Usage of topics:: 

1. topic_one  - xxx GB 
2. topic_two  - xxx GB 
3. topic_three  - xxx GB 
4. topic_four - xxx GB 
5. topic_five  - xxx GB 

```

topic_one, topic_two, topic_three, topic_four, topic_five will be filled with appropriate Topic Names and XXX will be filled by 
amount of data trasferred because of various actions at various times. 

---

