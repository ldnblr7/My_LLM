# My_LLM
Mini LLM - character-level language modeling
A project to understand how LLMs process and understand text to learn next-character prediction. Developed in Python, with custom tokenization, dataset preparation, and a planned Transformer implemented with PyTorch.

Files:

prepare_input_txt.py:
  Parses the given input text (currently formatted for verse-separated scripture) into a format readable by prepare.py.

prepare.py
  Creates a tokenizer from the inputted text based off an initial sample size.
