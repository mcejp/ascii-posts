---
layout: post
render_with_liquid: false
date: 2025-05-21
title: "Pattern: Detecting key press/release/hold"
unlisted: true
---

### Polled

``` c
unsigned int keys_curr;
unsigned int keys_prev;

unsigned int key_held(int key) {
    return (keys_curr & key);
}

unsigned int key_pressed(int k) {
    return (~keys_prev & keys_curr & key);
}

unsigned int key_released(int k) {
    return (keys_prev & ~keys_curr & key);
}

void main(void) {
    for (;;) {
        keys_prev = keys_curr;
        keys_curr = READ_KEYS();

        GAME_LOGIC();
    }
}
```

### Event-driven

Suitable for low FPS: will correctly register keys pressed and released
during a single frame

``` c
unsigned int keys_curr;
unsigned int keys_pressed;
unsigned int keys_released;

unsigned int key_held(int key) {
    return (keys_curr & key);
}

unsigned int key_pressed(int k) {
    return (keys_pressed & key);
}

unsigned int key_released(int k) {
    return (keys_released & key);
}

void main(void) {
    for (;;) {
        keys_pressed = 0;
        keys_released = 0;

        int key, pressed;
        while (({key, pressed} = GET_KEY_EVENT())) {
            if (pressed) {
                keys_curr |= key;
                keys_pressed |= key;
            }
            else {
                keys_curr &= ~key;
                keys_released |= key;
            }
        }

        GAME_LOGIC();
    }
}
```

### Interrupt-driven

Push into a FIFO and use event-driven pattern.
