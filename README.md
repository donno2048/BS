# backboard

Install with:

```
pip install backboard
```

Run it with:

```
backboard
```

###### It might take a while to boot up

To change the default keyboard sound setup use:

```
backboard -k SETUP
```

## Alternative

You could do the same (only on Windows) using some of my packages like so

```py
from getkey import get_key # from my pygetkey package
from beep import beep # from my python-beep package
key_freq = {'a': 440, 's': 392, 'd': 349, 'f': 330, 'g': 294, 'h': 262, 'j': 247, 'k': 220}
while True:
    key = get_key()
    if key in key_freq: beep(key_freq[key], 500)
```

Or in C like that

```c
#include <windows.h>
char notes[8] = {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K'};
int frequencies[8] = {440, 392, 349, 330, 294, 262, 247, 220};
int main(void) {
    for (int i = 0; ; i = (i + 1) % 8) if (GetAsyncKeyState(notes[i])) Beep(frequencies[i], 200);
}
```
