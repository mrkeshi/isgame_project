from SiteModule.models import PublicSettings

def SiteInformations(request):
	site = PublicSettings.objects.latest('-id')
	return {
	'title': site.title,
	'url': site.url,
    'logoIcon':site.logoIcon.url,
    'logoSite':site.logoSite.url
	}