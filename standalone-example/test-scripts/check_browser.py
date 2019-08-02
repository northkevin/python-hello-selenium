#!/usr/bin/env python

# Copyright 2015 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--browser", help="type of selenium browser to check", dest='browser', type=str)
parser.add_argument("--ip", help="ip of the standalone browser", dest='ip', type=str)
parser.add_argument("--port", help="port of the standalone browser", dest='port', type=str)
args = parser.parse_args()

def check_browser(browser=None, ip=None, port=None):

  driver = webdriver.Remote(
    command_executor='http://{0}:{1}/wd/hub'.format(ip, port),
    desired_capabilities=DesiredCapabilities.CHROME
  )
  
  driver.get("http://google.com")
  assert "google" in driver.page_source
  driver.quit()
  print("Browser {0} checks out for ip:port {1}:{2}!".format(browser, ip, port))

check_browser(browser=args.browser, ip=args.ip, port=args.port)
