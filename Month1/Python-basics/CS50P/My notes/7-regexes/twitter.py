import re

url = input("URL: ").strip()

# First get rid of https://twitter.com/
# replace :Find and replace
# removeprefix()could be used too
# username = url.replace("https://twitter.com/","")

#re.sub
#. needs a \
# we want both https and http to be valid, so ?
# www. is optional so we group it (www\.)? and we do the same for https, nesting the ?
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "",url)

#re.search
# (?:) is a non-capturing group
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"username= {matches.group(1)}")

