from selenium.webdriver import Safari

def before_all(context):
    context.browser = Safari()

def after_all(context):
     context.browser.quit()

def after_step(context, step):
    if step.status == 'failed':
        print(step)
        import pdb; pdb.set_trace()
