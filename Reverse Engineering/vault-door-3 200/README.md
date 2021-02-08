# Vault-door-3

## Description

This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java

## Solution

Opening up the Java file, we're presented with a login function. There is a series of
for loops and then a check to see if the obfuscated password is equal to the final string
shown.

This is a good example of security through obscurity and it should be relatively easy
to reverse engineer.

The series of for-loops show that the character at each position is related to the value
of i in each for-loop. 

Since I haven't used Java for a while, the only unknown aspect is the syntax for a forloop which
does not include a starting i value. To test this, I used the following code.


```
public class yoyoyo {
    public static void main(String args[]) {
        int i;
        for (i=0; i<8; i++) {
            System.out.println(i);
        }
        for (; i<16; i++) {
            System.out.println(23 - i);
        }
        for (; i<32; i+=2) {
            System.out.println(46 - i);
        }
        for (i=31; i>=17; i-=2) {
            System.out.println(i);
        }
    }
}
```

This gave me the following output. This shows me that i continues from where it left off.
For example, after i < 8, we start the next loop at i = 8.

```
0
1
2
3
4
5
6
7
15
14
13
12
11
10
9
8
30
28
26
24
22
20
18
16
31
29
27
25
23
21
19
17
```

After this, the only important thing to note is that the buffer created is using a reordered
version of the password. By mapping this out on paper, we can increment i each time and
re-assign the buffer characters to the original positions they'd be in the password. This
produces the flag.

```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}
```