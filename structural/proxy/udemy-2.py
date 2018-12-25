"""
A proxy provides a surrogate or place holder to provide
access to an object.

Ex2:
    Add a wrapper and delegation to protect the real component
    from undue complexity
"""

class Blog:

    def read(self):
        print('Read the blog')

    def write(self):
        print('Write the blog')


class GenericProxy:

    def __init__(self, target):
        self.target = target

    def __getattr__(self, attr):
        return getattr(self.target, attr)


class AnonUserBlogProxy(GenericProxy):

    def __init__(self, blog):
        super().__init__(blog)

    def write(self):
        print('Only authorized users can write blog posts.')


blog = Blog()
blog.write()

proxy = AnonUserBlogProxy(blog)
proxy.write()
