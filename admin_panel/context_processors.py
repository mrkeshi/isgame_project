from SiteModule.models import PublicSettings,SocialMediaLink

def SiteInformations(request):
	site = PublicSettings.objects.latest('-id')
	print(SocialMediaLink.objects.filter(user_id=None).first())
	return {
	'title': site.title,
	'url': site.url,
    'logoIcon':site.logoIcon,
    'logoSite':site.logoSite,
	'social':SocialMediaLink.objects.filter(user_id=None).first()
	}