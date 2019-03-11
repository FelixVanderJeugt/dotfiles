from afew.filters.BaseFilter import Filter
from afew.FilterRegistry import register_filter

spammers = """
hbguirui.net
foodcongress2019.com
congresssummit.com
icmsquare.net
austinpublishinggroup.us
hindawi.com
internationalmeeting.org
openaccessusa.com
journal.aoam.email
mailpanda.com
scientificres.org
scifedconferences.com
insightmeetings.net
wgc-2019.com
intopenaccess.com
walla.co.il
innofine.in
escientificres.com
xceptdom.com
aoam.info
cambridgescholars.com
mra-journal.org
jimsindia.org
service.cyagenbio.com
oatext-alerts.net
2019ibc.com
eclinmed.org
innovationinfo.net
intechopen.com
neurologyspeakerexperts.org
conferencesinternational.org
oap-lifescience.org
synpeptide.com.cn
americaseminars.com
oatextjournals.com
connectcyagen.com
oatjournals.com
meetingsintl.com
scientglobal.org
research101.site
biochemistryjournals.org
functionalfoodcenter.com
bio-congress.com
oatext-news.org
ptzjournals.com
glazovsky.co.ua
wcfnconference2018.com
iacrlrd2019.com
scientificfederation.com
journalres.org
bangng.org
eurosciconmeetings.com
renecon.eu
kebiochem.cn
reg-med2018.com
edelweisspublications.info
ibc-congress.com
sciencescholastic.com
journals.hindawi.com
bioevents.net
clinicalopenaccess.org
easummit.net
networkwithexpert.com
cmcb2019.com
eursciconevent.com
cmedu.org
oatextjournal.info
alliedinternational.org
kingfisherbiotech.com
meettheglobalexpert.com
tonirovany.biz.ua
doveproofreading.com
clinicalcasereports.editor@protonmail.ch
scireslitoa.com
academiapublishing.org
editorialscience.org
pepcon-2019.com
oap-journals.net
klserv.com
keimra.org
oap-cancer.org
cmcb-2019.com
rebuilding-the-raindrops.ovh
gavinconferences.org
iwbbio.org
usp-pl.net
biochemjournals.com
sophia.isabella010@yahoo.com
aimspress6.com
proteinresearch.website
linkinscience.com
esciencemedicine.com
cellmech-bio2018.com
oap-journals.org
sara.wallner78@gmail.com
evajones290@gmail.com
news.caister.com
scientificfederation.info
imrjournal.email
oap-journals.com
frontiermeetings.com
submitresearch.online
editor.factor21@daum.net
"""

@register_filter
class KnownSpammers(Filter):

	def __init__(self, database, **kwargs):
		super(KnownSpammers, self).__init__(database, **kwargs)
		self.query = ' or '.join(f'from:{s}' for s in spammers.split('\n') if s)

	def handle_message(self, message):
		self.add_tags(message, 'spam')
