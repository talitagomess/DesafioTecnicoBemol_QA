from selenium.webdriver import Safari

def before_all(context):
    context.browser = Safari()
   


def after_all(context):
    context.browser.quit()