results = ["Mario", "Luigi"]

results.append("Peach")
results.append("Yoshi")
results.append("Koopa")
results.append("Toad")

results.append(["Yassin", "Octave", "Carine"])
results.remove("Koopa")
results.extend(["Yassin", "Octave", "Carine"])
results.insert(0, "koopa")
results.reverse()

print(results)