import re
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.open("http://www.youtube.com")
print "We begin at %s" %br.geturl()

# Find link for "Search", this is probably wrong...
try:
    mech.follow_link(text_regex=re.compile("Search"))
except:
    #print "No link found for search"
    pass

print "What do you want to search for?"
user_in = raw_input()

# See http://wwwsearch.sourceforge.net/mechanize/forms.html on forms
search_form = None
for form in br.forms():
    #print form.click()
    #print form.name, form
    if "search" in str(form.click()):
        print "Located search bar..."
        print "Initially '%s' in search bar" %form["search_query"]
        form["search_query"] = user_in
        print "We've placed '%s' in search bar" %form["search_query"]
        search_form = form
        break
    print ''

if search_form == None:
    print "No search bar found... terminating"
    quit()

print "Sending search request..."
search_req = search_form.click()
try:
    search_res = mechanize.urlopen(search_req)
except:
    print "Request failed..."

br.open(search_res.geturl())

print "We are now at %s" %br.geturl()
for l in br.links(url_regex='/watch?'):
    print l

#print search_res.read() # body

#link1 = br.follow_link(text_regex=r"More information")
#print "We follow a link to %s" %link1.geturl()
