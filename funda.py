from bs4 import BeautifulSoup as bs_parse
import urllib, itertools, urllib2, math, csv, unicodecsv, slugify, time, requests, collections

class Page:
	
	def __init__(self,city,pager):
		self.city = str(city)
		self.pager = int(pager)
		self.page_data = {}
		
	# update the url
	def update_page_url(self):
		self.page_url = "https://www.funda.nl/koop/%s/p%d/" % (self.city, self.pager)
		print self.page_url
		self.values = []
		self.data = urllib.urlencode(self.values)
		self.req  = urllib2.Request(self.page_url, self.data)
		self.res  = urllib2.urlopen(self.req)
		self.page = bs_parse(self.res.read())
		#print self.page
		return self.page

	def count_makelaars_on_page(self):
		self.update_page_url()
		self.makelaars_on_page_count = len(self.page('a', {'class':'realtor'}))
		return self.makelaars_on_page_count

class Makelaar:

	def __init__(self,done):
		self.count = p.count_makelaars_on_page()
		self.makelaars_on_page = range(self.count)
		self.done = done

	def makelaars(self):
		
		for makelaar in self.makelaars_on_page:
			self.page_final = page
			self.elem_find = self.page_final('a', {'class':'realtor'})[makelaar].next
			print "Makelaar element find: %s" % self.elem_find 
			self.makelaar_value = self.elem_find.string
			print "Makelaar value",self.makelaar_value
			self.makelaar_name = self.makelaar_value
			data_makelaars[self.done + makelaar] = self.makelaar_name
		print "Aantal makelaars in de dict: ", len(data_makelaars)
		return data_makelaars
	
	"""		
	def dict_makelaars(self):
		makelaars = range(int(self.count_intros()))
		self.all_intros = {}
		for intro in intros:
			self.intro_type = self.rider_html_pretty('a', {'class':'intro-title'})[intro].next.next
			self.intro_content = self.intro_type.next
			print self.intro_type, self.intro_content
			print len(self.intro_content)
			if len(self.intro_content) == 1: 
				pass
			else:
				self.all_intros[self.intro_type] = self.intro_content
		print "Print all intros"
		print self.all_intros
		return self.all_intros		
 """
 
 # TODO Removing duplicate makelaars

	def single_makelaars(self):
		duplicates = data_makelaars
		single = {}
		for key,value in duplicates.items():
			if value not in single.values():
				single[key] = value
		#print single
		return single
	
	def ordered_makelaars(self):
		duplicates = data_makelaars
		single = self.single_makelaars()
		#len(set(open(duplicates).read().split()))
		#len(set(open(single).read().split()))
		#sum(single.values())
		#print "dup",duplicates
		#print "sing",single
		
		# print "k len toestand", [(k, len(list(v))) for k, v in itertools.groupby(sorted(duplicates.values()))]
		z = collections.Counter()
		z.update(duplicates.values())
		dict(z.items())
		print "", z.items()
		print "Deze makelaars zijn in %s het beste: " %city
		count = 0
		for item in z.most_common(10):
			count = count + 1
			print "%d: %s" % (count, str(item))
		
city = raw_input("Welke gemeente?")
paginas = range(1,1000)
data_makelaars = {}

for pagina in paginas:

	time.sleep(0.1)
	print "sleeping done. "
	
	p = Page(city,pagina)
	
	
	done = pagina * 15 - 15
	print "Zoveel done: ", done
	
	count = p.count_makelaars_on_page()
	if count > 0:
		print "Er worden nog steeds makelaars gevonden."
	else:
		print "Er worden geen makelaars meer gevonden vanaf deze pagina. Bye!"
		break
	print "We zijn gekomen tot pagina: ", pagina
	
	page = p.update_page_url()
	
	m = Makelaar(done)
	m.makelaars()

print "Dit zijn dan alle makelaars in %s: " % city, data_makelaars

# m.single_makelaars()
m.ordered_makelaars()
	