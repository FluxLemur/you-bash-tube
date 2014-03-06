import sys
import os
import re
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.open("http://www.youtube.com")

if len(sys.argv) < 2:
    print "Usage:\tpython %s <search query>" % sys.argv[0]
    sys.exit()

user_in = sys.argv[1]

# See http://wwwsearch.sourceforge.net/mechanize/forms.html on forms
search_form = None
for form in br.forms():
    if "search" in str(form.click()):
        form["search_query"] = user_in
        search_form = form
        break

if search_form is None:
    quit()

search_req = search_form.click()
try:
    search_res = mechanize.urlopen(search_req)
except:
    print "Request failed..."

br.open(search_res.geturl())

for l in br.links(url_regex='/watch?'):
    br.follow_link(l)
    break

print "Downloading %s..." % br.title()
os.system("youtube-dl -xq -o '%s.%%(ext)s' %s" %
          (user_in.replace(" ","_"), br.geturl()))

print "Download complete."
