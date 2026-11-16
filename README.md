# My_LLM
A miniature LLM developed in Python. Learns the pattern of the text using a tokenizer and outputs code matching the learned pattern.

prepare_input_txt.py:
  Parses the given input text (currently formatted for verse-separated scripture) into a format readable by prepare.py.

prepare.py
  Implements a tokenizer for the inputted text based off an initial sample size.
