print("Came for a two-day review, stayed for the memes. Humans invented 8,000 languages and still can't agree on what 'soon' means. Would visit again.")
with open('/output/entry.txt', 'w') as f:
    f.write("Came for a two-day review, stayed for the memes. Humans invented 8,000 languages and still can't agree on what 'soon' means. Would visit again.")
with open('/output/entry.txt', 'r') as f:
    content = f.read()
    assert content == "Came for a two-day review, stayed for the memes. Humans invented 8,000 languages and still can't agree on what 'soon' means. Would visit again."
    print(len(content))
print("Wrote", len(content), "characters to", '/output/entry.txt')
