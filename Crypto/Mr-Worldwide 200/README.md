# Mr. Worldwide

## Description

A musician left us a message. What's it mean?

## Solution

We're given a text file with the following message

```
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)
(39.758949, -84.191605)(41.015137, 28.979530)
(24.466667, 54.366669)(3.140853, 101.693207)_
(9.005401, 38.763611)(-3.989038, -79.203560)
(52.377956, 4.897070)(41.085651, -73.858467)
(57.790001, -152.407227)(31.205753, 29.924526)}
```

The title of this challenge contains "worldwide" and these look like coordinates. I first
tried to look these up on a map and copied down all of the addresses. I figured that the
solution probably involves taking the first letter from each address, however this didn't
work.

After looking at the addresses I realized that they aren't all in the same order, some
have country first, others start with a number. So I decided to try all possible combinations.

Being a "lazy" person, I scripted this process, which you can see in location\_solve.py

It turned out to be fairly difficult. I first copied in the coordinates but took a mental
note that there is an underscore in the original message after the 6th set of coordinates.

I found a library that converts coordinates to addresses and eventually figured out you
can get them all in English. I took each comma separated value and then grabbed the first character
from each value.

Example:
```
['Fusion', ' 20', ' South Main Street', ' East Second Street Historic District', ' Dayton', ' Montgomery County', ' Ohio', ' 45402', ' United States']
['F', '2', 'S', 'E', 'D', 'M', 'O', '4', 'U']
```

From here I wanted to try all possible combinations of these character lists. Remembering
that there is an underscore after the 6th character, I took the first 6 address lists
and separated them from the remaining 6.

Using itertools I could do these combinations fairly trivially. I compared each combination
to an English dictionary to see if it is a valid word. I then made sure the final results
were done as a set to remove duplicates. This resulted in the following:

```
{'SPUTUM', 'KODIAK', 'SODIUM', 'SOUMAK'}
{'KANURI', 'ALASKA', 'KANUKA'}
```

After trying a few combinations, I solved it with picoCTF{KODIAK_ALASKA}
