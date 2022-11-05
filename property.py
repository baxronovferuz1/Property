


import urllib
from time import perf_counter
from urllib import request


class WebPage:
    def __init__(self,url):
        self.url=url
        self._page=None
        self._load_time_secs=None
        self._page_size=None


    @property
    def url(self):
        return self._url

    
    @url.setter
    def url(self,value):
        self._url=value
        self._page=None



    @property
    def page(self):
        if self._page is None:   
            self.download_page()
        return self._page


    @property
    def page_size(self):
        if self._page is None:
            self.download_page()

        return self._page_size

    @property
    def time_elapsed(self):
        if self._page is None:
            self.download_page()
        return self._load_time_secs


    
    def download_page(self):
        self._page_size=None
        self._load_time_secs=None
        start_time=perf_counter()
        with urllib.request.urlopen(self.url) as f:
            self._page=f.read()
        end_time=perf_counter()
        self._page_size=len(self._page)
        self._load_time_secs=end_time-start_time


urls =[
    "https://www.google.com",
    "https://www.python.org",
    "https://www.github.com"
]

for url in urls:
    page=WebPage(url)
    print(f'{url}\tsize={format(page.page_size, "_")}\telapsed={page.time_elapsed: .2f} secs')




#ADDITION



from numbers import Real

class Vector:
    def __init__(self, *components):
        if len(components)<1:
            raise ValueError("cannot create an empty vector")
        for component in components:
            if not isinstance(component, Real):
                raise ValueError(f"vector components must all be real numbers. {component} is invalid")

        self._components=tuple(components)


    def __len__(self):
        return len(self._components)


    @property
    def components(self):
        return self._components

    def __repr__(self):
        return f"vector ({self.components})"


    def confirm_type_and_size(self,c):
        return isinstance(c,Vector) and len(c)==len(self)

    def __add__(self,other):
        if not self.confirm_type_and_size(other):
            return NotImplemented
        components=(x+y for x,y in zip(self.components, other.components))
        return Vector(*components)

 


    def __mul__(self,other):
        if not isinstance(other,Real):
            return NotImplemented
        components=(other * x for x in self.components)
        return Vector(*components)
