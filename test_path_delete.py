from test_path_objects import PageOpener

# Create an instance of PageOpener
opener = PageOpener()
# Call the open_page method
opener.open_page()

# Call the login method with the desired username and password
opener.login('xxx', 'xxx')

# Close the page and the browser
opener.close()

