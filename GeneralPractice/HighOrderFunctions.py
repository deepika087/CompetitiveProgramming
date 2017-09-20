

def logger(msg):

    def log_message():
        print "Your custome message is : ", msg

    return log_message

log_hi = logger("Hi ! !")
log_hi()


def html_tag(tags):

    def mainLine(comment):
        print "<{0}>{1}</{0}>".format(tags, comment)

    return mainLine

print_h1 = html_tag('h1')
print_h1("First blog")
print_h1("Second blog")
