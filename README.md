# Summary

A simple audio synthesis library in Python.

An audio source is represented by the `Sample` class.

## Project structure

- `lib/`: input/output and effects.
- `src/`: the `Sample` class and a demonstration in `main`.

## Installation and dependencies

Python 3.10 or later. From the project root, using a virtual environment:

```bash
python -m pip install numpy soundfile
python -m src.main
```

In the demonstration, enter the path to the WAV file you want to process and the output filename. The result is saved in `output/`.

Feel free to create your own functions and try the demonstration with different parameters.

## Library and functions

| Function | Behavior |
| --- | --- |
| `load_wav` / `save_wav` | Reads a WAV file into a `Sample` object / saves a `Sample` object as a 16-bit PCM WAV file. |
| `simplegranular` | Extracts a single grain from the input source. |
| `gain` | Multiplies the amplitude within an interval by a given floating-point value. |
| `b2fade` / `b3fade` | Applies a linear or cubic Bezier fade; `mode="in"` or `"out"`. |
| `merge` | Mixes two input sources from the beginning; `mix` weights the first input. Preserves the first input's duration. |
| `trim` | Extracts an interval from an input source using frame indices. |
| `concat` | Concatenates two input sources into one. |
