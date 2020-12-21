text = input("Please select your text file: ")
title = text.removeprefix("raw/").removesuffix(".txt")

print(title)

with open(text, 'r') as fin:
    text = fin.read()

with open("pages/index.html", "a") as pout:
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
<p>
    {text}
</p>
</body>
</html>
""")
