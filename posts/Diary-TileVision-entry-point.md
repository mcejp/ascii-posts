---
layout: post
render_with_liquid: false
date: 2025-09-24
title: "Diary: TileVision entry point"
unlisted: true
---

TileVision was designed to run under
[websocketd](http://websocketd.com/); this way it can simply print JSON
"frames" to stdout and WSD will take care of everything else. To launch
the user kernel, a bit of boilerplate is necessary:

    websocketd --address=localhost --port=4000 --staticdir=static \
        ./my-venv/bin/python -m my-kernel

At first, this was extremely convenient; the kernel could directly write
JSON to stdout. But now, looking at
[runner.py](https://github.com/mcejp/tilevision/blob/dddbaa5e03d2a0cc10cdf68aa0ad4ce9252c7d49/tilevision/runner.py),
it's not nearly as simple anymore -- there's a bunch of stuff provided
by the framework that you just don't want to do by hand. As we found out
early on, we always want to use the TV library in user code, even if
only to prevent code duplication. Another reason is that otherwise it
becomes impossible to track down uses of the protocol and make any
changes.

The real fun begins when we consider that commands may be sent from the
viewer to the sim -- examples are `PAUSE` and `STEP`. The `run_kernel`
function takes care of decoding and handling all that.

It is conceivable that a use-case for lower-level usage of the TV
protocol exists, but for simple simulation kernels we want to get these
conveniences for free.

This brings us to the question at hand: **How can we avoid this
boilerplate and encapsulate (hide) the WebSocket server?**

Reviewing the parameters above:

- `address`, `port`: Makes sense to be user-overridable, but good
  defaults exist (`localhost:4000`)
- `staticdir`: Already problematic today, as the static assets come from
  TV, not from the user!
- kernel name: user-provided

### Python environment

- Given what was said above about *always* using the TV API, it is not
  resonable to expect that plain Python (without installing any
  dependencies) could be used.
- The TV Python package is very light-weight. It should be OK to expect
  the user to install it in their environment.
- The tricky part is, if 1) the main entry point is a Python program,
  and 2) we need to wrap the user kernel in `websocketd`, then we will
  need to invoke a Python sub-interpreter without the user having a
  direct control over its parameters. For the most part this should be
  fine; for example, `PYTHONPATH` will be propagated. However, this
  might also be a good opportunity to switch to a native Python
  WebSocket package.

### Approach \#1: dedicated entry point, websocketd & sub-interpreter

``` sh
./my-venv/bin/python -m tilevision.run (...) my-kernel.py 1 2 3
└── websocketd --address=(...)
    ├── ./my-venv/bin/python my-kernel.py 1 2 3
    ├── ./my-venv/bin/python my-kernel.py 1 2 3
    └── ./my-venv/bin/python my-kernel.py 1 2 3
```

Smallest delta from status quo, but less self-contained: need to have
websocketd installed somewhere.

Leaves the path open for a hypothetical non-WS transport (at the cost of
complexity due to all frames going through stdio).

**Multiple connections**: will spawn multiple kernel processes.

**Installation**:: Kernel doesn't need to be an installed package.

### Approach \#2: dedicated entry point using importlib

``` sh
./my-venv/bin/python -m tilevision.run (...) \
    -k my_kernel 1 2 3
```

*flask run* seems to work like this (it defers to
`werkzeug.run_simple`). Their reasoning is that the app should not
control the main loop, because in production it would be the
responsibility of a WSGI server. For TV, I don't think we care, although
the same argument could potentially be made for deploying a TV sim in
"production".

This assumes an embedded HTTP (for static assets) + WebSocket server in
the TV Python library.

**Multiple connections**: not trivial, need to do explicit
multi-threading or async I/O

**Installation**:: Kernel doesn't need to be an installed package, but
it might be necessary to re-implement what Python does for implicit
import path when a script is launched by file name (since here we always
launch the `tilevision.run` module)

### Approach \#3: kernel is the entry point

``` sh
./my-venv/bin/python -m my_kernel \
    --tilevision-address=localhost (...) \
    1 2 3
```

Requires a little boilerplate in kernel:

``` python
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    import sys
    from tilevision.runner import run_kernel

    run_kernel(Kernel, sys.argv)
```

This, again, assumes embedded HTTP + WebSocket server in TV.

**Multiple connections**: not trivial, need to do explicit
multi-threading or async I/O

**Installation**: Kernel doesn't need to be an installed package.

### Conclusion

Approaches \#2 and \#3 look appealing from the user perspective, but the
technical challenges (embedded server, threading) are more serious than
initially estimated. We will start with approach \#1 and then see.
