from setuptools import setup


setup(
	name = 'Grub Wallpaper Generator',
	version = '1.0',
	py_modules = ['animewal'],
	install_requires = [
		'click',
		'requests',
		'bs4',

	],
	entry_points = '''
		[console_scripts]
		grubwallpaper = animewal:cli
	''',
)

