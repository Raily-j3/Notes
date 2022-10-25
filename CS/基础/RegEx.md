# 正则表达式 Regular Expression

## 元字符

1. letter
2. .
3. 
| Character |               Description                           |
| :-------- | :--------------------------------------:            |
| \d \D     |               Digit or not      [0-9]               |
| \w \W     |          Word Character or not  [a-zA-Z0-9]         |
| \s \S     |            Whitespace or not.   (space, tab, newliine)   |

| Anchor    |               Description                           |
| :-------- | :--------------------------------------:            |
| \b \B     |           Word Boundary or not                      |
| ^ $       |              Start and end                          |

| Character Set   |               Description                |
| :--------       | :--------------------------------------: |
| [] [^] [0-9]    | Matches Characters in or not in brackets |
| \|              |                Either Or                 |
| ()  $1          | Group, get the information of the group  |

| Quantifiers Character |           Description            |
| --------------------- | :------------------------------: |
| *                     |            0 or More             |
| +                     |            1 or More             |
| ?                     |             0 or One             |
| {3} {3,4}             | Exact Number or Range of Numbers |

- Example: 
  - email: [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
