# shell #

```bash
#!/bin/bash

# 变量基本操作
# "$a" -> a的值  '$a' -> $a
var_name=var            # 操作符之间不允许空格
echo $var_name          # $ 引用变量
unset var_name          # 删除变量
readonly var_name       # 转换成只读变量
dir_name=`pwd`          # `cmd`

# 传参
read -p "message" a b   # a = input()
cd $1 $@ $#             # 传参 $@: 所有参数 $: 参数个数
ls / 1>a.txt            # > 覆盖,  >> 追加
asfd 2>>b.txt           # 1: 正确命令输出 2: 错误命令提示


# 分支
if [ "$a" == "$b" ]
then
    segment
elif
then
    segment
else
    segment
fi
# @@@@@@分支条件@@@@@@@
# 逻辑运算符：-a -o !
# 比较运算符：-ge: (greater equal >=) -gt; -lt(less >) -le; -eq: = -ne: !=
# 测试文件的状态：test 参数 文件名
# 字符串判断：== ,!=
# 文件判断：test -d 或者 -d  -e -f  -w -r -x .....

# in  ;;  *: 默认  [0-9]
case $var_name in
A)
    echo "";;
B)
    echo "";;
C)
    echo "";;
*)
    echo "";;
esac

#循环
# seq start size max = range()
for i in `seq 10 -1 0`
do
    segment
done

while [ 条件 ]
do
    segment
done

# 函数
read -p "m" arg1 arg2

foo() {
    s=$(($1+$2))        # $n 形参
}

foo $arg1 $arg2         # 实参
# 查看返回值 $? 默认 0 或 1

```

## 实战 自动化部署 ##

1. 判断是否为root
   1. echo $USER
2. 添加组，添加用户并修改密码，创建目录和修改文件权限。
   1. groupadd dba, useradd -g group -g group, passwd
3. cut 判断用户组是否存在
   1. -b 1-10, 2, 2-10 -b: 按字节截取( 汉字为 3 个字节 ) 会去重
   2. -c: 字符
   3. grep "xxx" | cut -d ":" -f 1    ( -d "?" -f n
4. sed -i "content" .bash.profile
