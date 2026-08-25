emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("I am here")

def say(phrase):
    print(phrase + " " + emoticon)

main()   


# these is side effect of global variable, it can be changed in any function and it will affect the other functions that use it.