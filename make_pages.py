text = input("Please select your text file: ")
title = text.removeprefix("raw/").removesuffix(".txt")
img = input("Please select your text image: ")

with open(text, 'r') as fin:
    text = fin.read()

with open("index.md", "a") as pout:
    pout.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
<h1>
    {title}
</h1>
<img src="{img}" width="500">
<p>
    {text}
</p>
</body>
</html>
""")
