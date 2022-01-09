import penguinbullet
while True:
    text = input(">>> ")
    res, err = penguinbullet.run("<stdin>", text)
    if err: print(err.as_string())
    else: print(res)