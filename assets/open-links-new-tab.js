document.querySelectorAll('a[href]').forEach(link => {
	const href = link.getAttribute('href');
	if (href && !href.startsWith('#') && !href.startsWith('mailto:') && !href.startsWith('javascript:')) {
	  link.setAttribute('target', '_blank');
	  link.setAttribute('rel', 'noopener noreferrer');
	}
  });