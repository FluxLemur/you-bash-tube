import re
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.open("http://www.youtube.com")

user_in = raw_input()

# See http://wwwsearch.sourceforge.net/mechanize/forms.html on forms
search_form = None
for form in br.forms():
    if "search" in str(form.click()):
        form["search_query"] = user_in
        search_form = form
        break

if search_form == None:
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

print br.geturl()
