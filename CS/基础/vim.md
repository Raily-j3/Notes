# vim

---
## 分屏：C-ws C-wv

- 分屏( window )打开多个文件：vim vim -on file1 file2 ... filen
- 移动分屏：C-wh{jkl}{HJKL}
- 关闭分屏：C-wc C-wq

---
## linux命令

- 在 vim 中执行 linux 命令：:!{command}
- VIM 执行命令，并且添加结果至操作文本光标处 :r !{command}

---
## 搜索替换

- :{作用范围}s/{目标}/{替换}/{替换的标志} 如 :%s/foo/bar/g
  - 作用范围
      - 当行：s/foo/bar/g
      - 全文：%s/foo/bar/g
      - 选区：visual模式下
      - 选行：2,5s/foo/bar/g
  - 替换的标志
      - 空：第一个 %s/foo/bar/
      - g：全局
      - 忽略和确认：gi或gc 忽略大小写或需要确认
  
---
## 光标移动 

### 跳转操作

Motion Command|Description
--|--
`%` | 括号之间跳转 
`f` | 查找当前行字符
`zz`| 将当前行移动至屏幕中央 
`zt`| 把当前行移动到当前屏幕的最上方，也就是第一行
`zb`| 把当前行移动到当前屏幕的尾部
`<leader><leader>s<char>`| easymotion
`s<char><char>` | sneak
`<C-f>/<C-u>` | 向下/向上翻屏 
`<C-i>/<C-o>` | 向前/后跳转

---
## 折叠

Motion Command|Description
--|--
`za` |  toggle )
`zR` | ( open all )
`zM` | ( close all )

---
## mark

- m{a-z...}
- `{mark point}

---
## 大小写转换

---
## 插件

---
### vim-sneak

- s\<char>\<char>
- S\<char>\<char>
- 上/下一个: __,__ __;__

---
### vim-surround

- d/c/y s\<char>
- visual 模式下选中 S \<desire char> 

---

### wildfire

vim-signiture

35min





