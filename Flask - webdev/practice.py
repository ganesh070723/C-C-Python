class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
def is_auth(function):
    def wrapper(*args,**kwargs):
      if args[0].is_logged_in == True:
          function(args[0])
    return wrapper
@is_auth
def blog_post(user):
    print(f'this id {user.name} new blog post')
    
    
new_user=User("ganesh")
new_user.is_logged_in=True
blog_post(new_user)
