import textwrap
# NAME
#     textwrap - Text wrapping and filling.

docs = """
    docs dmas;dmssfksnlam;lml;sa
    lsmdsklmmkospk
    dsa
"""

fill = textwrap.fill(docs,width=100)
print(fill)