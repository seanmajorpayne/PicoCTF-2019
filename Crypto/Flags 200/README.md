# Flags 200

## Description

What do the flags mean?

## Solution

We're given a file called flags.png. Upon opening the file, we see a series of flags,
which conveniently also include two brackets { } so this is already easily identifiable
as being the flag we're looking for.

Since the format for flags is always PICOCTF{SOMETHING}, we already know the initial flags
are PICOCTF, this also reveals a few other characters.

However, I noticed that this doesn't help get closer to the solution since there is
no way to "rotate" flags like we could do with random characters.

At this point we have

```
PICOCTF{F__________FF}
```

My first inclination was to look up country flags. I was specifically searching for one
with a red diamond, since this is "F" and appears multiple times. Once I reviewed the country
flags and didn't see a red diamond I searched for "red diamond flag" which revealed that
there are "Nautical/Maritime Flags" which actually correspond to letters.

After mapping these out I ended up with

```
PICOCTF{F_AG_AND_TUFF}
```

The two Blue and Yellow flags didn't have corresponding maritime flags, but the flag for
5 is blue and yellow and that fits with the "leet speak" characters that are common in
CTF flags.

```
PICOCTF{F_AG5AND5TUFF}
```

We're now missing one character, which I assumed was 'L' however this didn't work so I tried
7 and 1, which led me to the solution.

```
PICOCTF{F1AG5AND5TUFF}
```
