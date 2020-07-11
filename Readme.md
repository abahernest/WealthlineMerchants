WealthMerchants is an application for helping the organization reach out to its large customers to inform them of recent changes and updates in the organization and new product releases.

Basically it's a Blog.

The application contains just one django app:

home: This houses the 'blog' and the 'success stories' section of the website.

templates/home contains 6 templates

about: about page
index: homepage
moreposts: to view older blog post 
morestories: to view older stories. This basically violates DRY. but we move
stories: success stories of RAGP customers.
details: blog posts