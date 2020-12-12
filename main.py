BROWSERSTACK_URL = 'https://norbertreimer1:7oHapQv97nTvbEFXTbBM@hub-cloud.browserstack.com/wd/hub'

desired_cap = {
          
  'os' : 'Windows',
  'os_version' : '10',
  'browser' : 'Chrome',
  'browser_version' : '87.0',
  'name' : "norbertreimer1's First Test"

}

driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
