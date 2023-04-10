import textwrap as tr

my_str = "the only function needs to call to generate prompt, text and download JPG + BMP RETURNS: downloaded picture path <String> Text Output for Display <String>"

lines = tr.fill(my_str, width=30)

print(lines)
