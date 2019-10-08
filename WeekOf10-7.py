# More strings and text

x = "There are %d types of people" % 10
binary = "binary"
doNot = "don't"
y = "Those who know %s and those who %s" % (binary, doNot)

print(x)
print(y)

print("I said: %r.:" % x)
print("I also said: '%s'." % y)

hilarious = True
jokeEvaluation = "Isn't that joke so funny?! %r"

print(jokeEvaluation % hilarious)
# These describe what each
w = "This is the left side of..."
e = "a string with a right side."
print(w+e)


# More printing fun
print("Mary had a little lamb.")
print("Its fleece was white as %s." %'snow')
print("And everywhere that Mary went.")
print("." * 10)
# These variables describe each letter
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# These lines print the leters described above.
print(end1 + end2 + end3 + end4 + end5 + end6,)
print(end7 + end8 + end9 + end10 + end11 + end12)

# But Wait! There's more:
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, True, False))
print(formatter % (formatter, formatter, formatter, formatter))

# Why do I use %r instead of %s in the above example?
# %r is just representation of a string.
# Which should I use on a regular basis?


# Why does %r sometimes give me single quotes around things?

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
bands = "\nPink Floyd\nQueen\nRush\nMetalica"
print("Here are the days:", days)
print("Here are the months:", months)
print("Here are my favorite bands", bands)


print("""
With the three double-quotes.
We'll be able to type as much as we like.
Even 10 lines if we want, or 20, or 30.""")

print("Here are the months: %r" % months)