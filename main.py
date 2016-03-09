import obot, time, praw, re
from collections import deque
r = obot.login()
done = deque(maxlen=300)
cDone = deque(maxlen=300)

doComs = True

def main():
    stream = praw.helpers.submission_stream(r, "all", limit=None)
    cStream = praw.helpers.comment_stream(r, "all", limit=None)

    for sub, com in zip(stream, cStream):
        try:
            match = re.findall("imgur\.com\/([A-Za-z0-9]+)(?:\.gif|\.jpg)*$", sub.url)
            cMatch= re.findall("imgur\.com\/([A-Za-z0-9]+)(?:\.gif|\.jpg)*$", com.body)
            if match and sub not in done and not doComs:
                sub.add_comment("http://i.imgur.com/" + match[0] + ".gifv")
                done.append(sub)
            if cMatch and com not in cDone and doComs:
                com.reply("http://i.imgur.com/" + cMatch[0] + ".gifv")
                cDone.appen(com)
        except praw.errors.APIException:
            pass


if __name__ == "__main__":
    while True:
        main()
        time.sleep(3)

