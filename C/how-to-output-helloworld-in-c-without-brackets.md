# 如何在c语言中不用任何括号输出hello world

# how-to-output-helloworld-in-c-without-brackets



**其实在实现这个奇怪的行为之前，你需要了解一以下几样（奇怪的）知识**

1. c语言main函数的本质
2. 汇编语言和机器码

1.main的本质初探

在平时写c语言，大多数时候都是int main()，这时候main是什么？我们不妨做个试验：

找一个**语法检查比较松**的IDE（ 比如 cfree）写入代码

```c　
int a=printf;
printf("%d",a);
```

是不是可以打印出一个奇怪的东西~.~

这里打印的其实是printf的地址。在汇编里面，调用函数是call + 地址，这里也是一样的原理。

所以在我们写的程序编译之后。某个函数call了我们的main函数，才让我们的程序得以执行。所以main本身只是一个地址。

所以如果我们写下`int main=0x2333;` 也是可以通过编译的

2.汇编&机器码

知道了一点main函数的真面目，我们就可以搞事情了~

既然是call main，只要能让main所在的地址拥有那么一段可以输出helloworld的代码不就行了？

但是如果我们直接用c语言写的话，你会发现反汇编出来的东西依旧很多，不利于我们实际的操作，所以我们这里用汇编写

（环境 kali linux x64）

```c
global main
    main:
        jmp s
        nop
    s: 
        push 0x64
        pop rdx
        push 0x1
        pop rdi
        mov rax,rdi
        push 0
        push 0x21
        push 0x64
        push 0x6C
        push 0x72
        push 0x6F
        push 0x57
        push 0x20
        push 0x2C
        push 0x6F
        push 0x6C
        push 0x6C
        push 0x65
        push 0x48
        nop
        mov rsi,rsp
        syscall
        push 0x3c
        pop rax
        push 0x1
        pop rdi
        syscall　
```

这一段就是可以输出helloworld的汇编语言，用nasm编译之后，我们开始用objdump反汇编生成的文件

![img](./public/bbb.png)

这时候再把前面对应的机器码依次用c写入

```c
const char
main=0xeb , mainl1=0x01 ,//jmp to main10
main13=0x90,//nop
main10=0x6a, main12=0x64,//push 0x64
mainl =0x5a,//pop rdx
main2 =0x6a, main3 =0x01,//push 0x1
main4 =0x5f,/ /pop rdi
main5 =0x48, main6 =0x89 , mian7=0xf8,//mov rax, rdi
main16=0x6a, main17=0x00,//push "Hello, World!"
main18=0x6a, main19=0x21
main20=0x6a, main21=0x64,
main22=0x6a, main23=0x6c ,
main24=0x6a , main25=0x72,
main26=0x6a , main27=0x6f,
main28=0x6a , main29=0x57,
main30=0x6a , main31=0x20,
main32=0x6a , main33=0x2c,
main34=0x6a , main35=0x6f,
main36=0x6a , main37=0x6c,
main38=0x6a , main39=0x6c ,
main40=0x6a , main41=0x65 ,
main42=0x6a , main43=0x48 ,
main44=0x48 , main45=0x89 , main46=0xe6,//mov rsi, rsp
main47=0x0f , main48=0x05,//syscall .
main49=0x6a , main50=0x3c,//push 0x3c
main51=0x58,//pop rax
main52=0x6a, main53=0x00,//push 0x1
main54=0x5f ,//pop rdi
main59=0x0f , main60=0x05 ;//syscall
```

（这里留个小问题：为什么用const char？ ）

做到这一步基本上就已经完成了，最后虽然可能还会有一点小问题，不过也已经不难解决了。

看上去很nb，然而这种奇怪的技巧，有什么用呢？